from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler

from rooms.roomcache import room_cache


class PlayerLeftRoomNotification(BaseNotification):
    def __init__(self, room_id):
        super().__init__()
        self._room_id = room_id

    @property
    def room_id(self):
        return self._room_id


class PlayerLeftRoomSubscriber(BaseNotificationHandler):
    async def handle(self, notification: PlayerLeftRoomNotification):
        room_cache.player_left_room(notification.room_id)
