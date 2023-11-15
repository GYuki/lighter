import asyncio

from pydiator_core.mediatr import pydiator
from twisted.internet import reactor

from rooms.notifications.roomdeleted import RoomDeletedNotification
from rooms.room import Room


class RoomCache(object):
    def __init__(self, room_timeout=3):
        self._rooms = {}
        self._room_deletion_timers = {}
        self._room_timeout = room_timeout

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
        return self._rooms[_id]

    def player_left_room(self, room_id):
        if room_id not in self._rooms:
            print(f'No such room to delete: {room_id}')
            return
        if room_id in self._room_deletion_timers:
            print('Room already in order to be deleted')
            return

        if self._rooms[room_id].player_count == 0:
            self._room_deletion_timers[room_id] = reactor.callLater(
                self._room_timeout,
                self._delete_room_by_timeout,
                room_id
            )

    def _delete_room_by_timeout(self, room_id):
        if room_id in self._rooms:
            del self._rooms[room_id]
            del self._room_deletion_timers[room_id]
            loop = asyncio.new_event_loop()
            loop.run_until_complete(
                pydiator.publish(RoomDeletedNotification(
                    room_id=room_id
                ))
            )
            loop.close()


room_cache = RoomCache()
