from rooms.playercontainer import PlayerContainer


class Room(object):
    def __init__(self, _id):
        self._id = _id
        self._container = PlayerContainer()

    @property
    def id(self):
        return self._id

    def join_room(self, peer, join_mode):
        self._container.try_add_peer_to_game(peer, join_mode)
        peer.set_room(self)

    def leave_room(self, peer):
        self._container.remove_player(peer)

    def broadcast_data_to_all_players(self, data):
        self._container.broadcast_to_all(data)
