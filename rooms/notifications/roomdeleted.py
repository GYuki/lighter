from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler

from rooms.notifications.rpsnotifications import RpsNotificationHandler


class RoomDeletedNotification(BaseNotification):
    def __init__(self, room_id):
        super().__init__()
        self._room_id = room_id

    @property
    def room_id(self):
        return self._room_id


class RoomDeletedSubscriber(RpsNotificationHandler):
    async def handle(self, notification: RoomDeletedNotification):
        self._send_message('room_delete', {
            'room_id': notification.room_id
        })
