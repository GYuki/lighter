from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler


class PlayerCreatedRoomNotification(BaseNotification):
    def __init__(self, room_id):
        super().__init__()
        self._room_id = room_id

    @property
    def room_id(self):
        return self._room_id


class PlayerCreatedRoomSubscriber(BaseNotificationHandler):
    async def handle(self, notification: PlayerCreatedRoomNotification):
        print(f'Room created: {notification.room_id}')


