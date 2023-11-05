from protocol.peer.abstraction import BasePeer


class LighterWsPeer(BasePeer):
    def __init__(self, protocol):
        super().__init__(protocol)
        self._room = None
        self._id = 0

    @property
    def room(self):
        return self._room

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def disconnect(self):
        super().disconnect()
        self._room.leave_room(self)
        self._room = None

    def set_room(self, room):
        self._room = room
