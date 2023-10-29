from protocol.peer.abstraction import BasePeer


class LighterWsPeer(BasePeer):
    def __init__(self, protocol):
        super().__init__(protocol)
        self._room = None

    def set_room(self, room):
        self._room = room
