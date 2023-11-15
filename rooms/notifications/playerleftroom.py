from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler

from rooms.roomcache import room_cache


class PlayerLeftRoomNotification(BaseNotification):
    def __init__(self, room):
        super().__init__()
        self._room = room

    @property
    def room(self):
        return self._room


class PlayerLeftRoomSubscriber(BaseNotificationHandler):
    async def handle(self, notification: PlayerLeftRoomNotification):
        room_cache.player_left_room(notification.room.id)
        print(f'Update in room {notification.room.id}. Player count: {notification.room.player_count}')
