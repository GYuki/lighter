from pydiator_core.interfaces import BaseNotification

from rooms.notifications.rpsnotifications import RpsNotificationHandler


class PlayerJoinedRoomNotification(BaseNotification):
    def __init__(self, room):
        super().__init__()
        self._room = room

    @property
    def room(self):
        return self._room


class PlayerJoinedRoomSubscriber(RpsNotificationHandler):
    async def handle(self, notification: PlayerJoinedRoomNotification):
        self._send_message('room_players_update', {
            'players': notification.room.player_count,
            'room_id': notification.room.id
        })
