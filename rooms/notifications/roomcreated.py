import os

from pydiator_core.interfaces import BaseNotification

from rooms.notifications.rpsnotifications import RpsNotificationHandler


class RoomCreatedNotification(BaseNotification):
    def __init__(self, room_id):
        super().__init__()
        self._room_id = room_id

    @property
    def room_id(self):
        return self._room_id


class RoomCreatedSubscriber(RpsNotificationHandler):
    async def handle(self, notification: RoomCreatedNotification):
        domain = os.environ.get("domain", "")
        self._send_message(
            'room_create',
            {
                'room_id': notification.room_id,
                'address': domain if domain else f'{os.environ.get("ip")}:{os.environ.get("port")}'
            }
        )
