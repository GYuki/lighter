import json

from protocol.peer.abstraction import BasePeer


class LighterWsPeer(BasePeer):
    def __init__(self, protocol):
        super().__init__(protocol)
        self._room = None
        self._id = 0

    def _prepare_data(self, data):
        return json.dumps(data).encode('utf8')

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
        self.leave_room()

    def set_room(self, room):
        self._room = room

    def leave_room(self):
        self._room.leave_room(self)
        self._room = None
