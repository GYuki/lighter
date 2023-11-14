import asyncio

from pydiator_core.mediatr import pydiator

from rooms.notifications.playercreatedroom import PlayerCreatedRoomNotification
from rooms.room import Room


class RoomCache(object):
    def __init__(self):
        self._rooms = {}

    def get_room_by_id(self, _id):
        if _id in self._rooms:
            print('Return room with id', _id)
            return self._rooms[_id]
        return None

    def try_create_room(self, _id):
        if _id in self._rooms:
            print('Cant create room with existing id')
            return None
        self._rooms[_id] = Room(_id)
        # ???
        loop = asyncio.new_event_loop()
        loop.run_until_complete(pydiator.publish(PlayerCreatedRoomNotification(_id)))
        loop.close()
        # ???
        return self._rooms[_id]


room_cache = RoomCache()
