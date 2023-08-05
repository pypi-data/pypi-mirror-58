from .service import ManagedService
from dialog_api import peers_pb2, users_pb2, messaging_pb2, search_pb2, sequence_and_updates_pb2


class Users(ManagedService):
    """Class for handling users
    """
    def find_user_outpeer_by_nick(self, nick):
        """Return OutPeer by shortname
        :param nick: nick (str)
        :return: OutPeer object
        """
        request = search_pb2.RequestResolvePeer(
                shortname=nick
            )
        result = self._resolve_peer(request)
        if hasattr(result, "peer"):
            return result.peer

    def get_user_outpeer_by_id(self, uid):
        request = messaging_pb2.RequestLoadDialogs(
            min_date=0,
            limit=1,
            peers_to_load=[peers_pb2.Peer(type=peers_pb2.PEERTYPE_PRIVATE, id=uid)]
        )
        result = self._load_dialogs(request)

        for outpeer in result.user_peers:
            if outpeer.uid == uid:
                return peers_pb2.OutPeer(
                    type=peers_pb2.PEERTYPE_PRIVATE,
                    id=outpeer.uid,
                    access_hash=outpeer.access_hash
                )

    def get_user_by_id(self, uid):
        req = messaging_pb2.RequestLoadDialogs(
            min_date=0,
            limit=1,
            peers_to_load=[peers_pb2.Peer(type=peers_pb2.PEERTYPE_PRIVATE, id=uid)]
        )
        result = self.internal.messaging.LoadDialogs(req)
        users_list = self.internal.updates.GetReferencedEntitites(
            sequence_and_updates_pb2.RequestGetReferencedEntitites(
                users=list(result.user_peers)
            )
        )

        for user in users_list.users:
            if hasattr(user, "id") and user.id == uid:
                return user
        return None

    @staticmethod
    def get_user_peer_by_id(uid):
        return peers_pb2.Peer(type=peers_pb2.PEERTYPE_PRIVATE, id=uid)

    def get_user_by_nick(self, nick):
        """Returns User object by nickname
        :param nick: user's nickname
        :return: User object
        """
        outpeer = self.find_user_outpeer_by_nick(nick)
        if not (outpeer.id and outpeer.access_hash):
            return

        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                users=[
                    peers_pb2.UserOutPeer(uid=outpeer.id, access_hash=outpeer.access_hash)
                ]
            )
        result = self._get_reference_entities(request)
        for user in result.users:
            if hasattr(user.data, "nick") and user.data.nick.value == nick:
                return user

    def get_user_full_profile_by_nick(self, nick):
        """Returns FullUser object by nickname
        :param nick: user's nickname
        :return: FullUser object
        """
        user = self.find_user_outpeer_by_nick(nick)
        request = users_pb2.RequestLoadFullUsers(
                user_peers=[
                    peers_pb2.UserOutPeer(
                        uid=user.id,
                        access_hash=user.access_hash
                    )
                ]
            )
        full_profile = self._load_full_users(request)

        if full_profile:
            if hasattr(full_profile, 'full_users'):
                if len(full_profile.full_users) > 0:
                    return full_profile.full_users[0]

    def get_user_custom_profile_by_nick(self, nick):
        """Returns custom_profile field of FullUser object by nickname
        :param nick: user's nickname
        :return: user's custom profile string
        """
        full_profile = self.get_user_full_profile_by_nick(nick)

        if hasattr(full_profile, 'custom_profile'):
            return str(full_profile.custom_profile)

    def get_user_custom_profile_by_peer(self, peer):
        """Returns custom_profile field of FullUser object by Peer object
        :param peer: user's Peer object
        :return: user's custom profile string
        """
        outpeer = self.manager.get_outpeer(peer)

        request = users_pb2.RequestLoadFullUsers(
                user_peers=[
                    peers_pb2.UserOutPeer(
                        uid=outpeer.id,
                        access_hash=outpeer.access_hash
                    )
                ]
            )
        full_profile = self._load_full_users(request)

        if full_profile:
            if hasattr(full_profile, 'full_users'):
                if len(full_profile.full_users) > 0:
                    if hasattr(full_profile.full_users[0], 'custom_profile'):
                        return str(full_profile.full_users[0].custom_profile)

    def search_users_by_nick_substring(self, query):
        """Returns list of User objects by substring of nickname (not complete coincidence!)
        :param query: user's nickname
        :return: list User objects
        """
        request = search_pb2.RequestPeerSearch(
                query=[
                    search_pb2.SearchCondition(
                        searchPeerTypeCondition=search_pb2.SearchPeerTypeCondition(
                            peer_type=search_pb2.SEARCHPEERTYPE_CONTACTS)
                    ),
                    search_pb2.SearchCondition(
                        searchPieceText=search_pb2.SearchPieceText(query=query)
                    )
                ]
            )
        user_peers = self._peer_search(request).user_peers
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                users=list(user_peers)
            )
        users_list = self._get_reference_entities(request)
        result = []

        for user in users_list.users:
            if hasattr(user.data, "nick") and query in user.data.nick.value:
                result.append(user)
        return result

    def _load_dialogs(self, request):
        return self.internal.messaging.LoadDialogs(request)

    def _resolve_peer(self, request):
        return self.internal.search.ResolvePeer(request)

    def _get_reference_entities(self, request):
        return self.internal.updates.GetReferencedEntitites(request)

    def _load_full_users(self, request):
        return self.internal.users.LoadFullUsers(request)

    def _peer_search(self, request):
        return self.internal.search.PeerSearch(request)
