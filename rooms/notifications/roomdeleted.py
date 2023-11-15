from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler


class RoomDeletedNotification(BaseNotification):
    def __init__(self, room_id):
        super().__init__()
        self._room_id = room_id

    @property
    def room_id(self):
        return self._room_id


class RoomDeletedSubscriber(BaseNotificationHandler):
    async def handle(self, notification: RoomDeletedNotification):
        print(f'Room with id {notification.room_id} deleted')
