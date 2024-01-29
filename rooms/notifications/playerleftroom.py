from pydiator_core.interfaces import BaseNotification

from rooms.notifications.rpsnotifications import RpsNotificationHandler
from rooms.roomcache import room_cache


class PlayerLeftRoomNotification(BaseNotification):
    def __init__(self, room):
        super().__init__()
        self._room = room

    @property
    def room(self):
        return self._room


class PlayerLeftRoomSubscriber(RpsNotificationHandler):
    async def handle(self, notification: PlayerLeftRoomNotification):
        room_cache.player_left_room(notification.room.id)
        self._send_message('room_players_update', {
            'players': notification.room.player_count,
            'room_id': notification.room.id
        })
