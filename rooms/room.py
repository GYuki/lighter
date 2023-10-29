from rooms.playercontainer import PlayerContainer


class Room(object):
    def __init__(self):
        self._container = PlayerContainer()

    def join_room(self, peer):
        self._container.add_player(peer)
        peer.set_room(self)

    def leave_room(self, peer):
        self._container.remove_player(peer)

    def broadcast_data_to_all_players(self, data):
        self._container.broadcast_to_all(data)
