from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler


class PlayerJoinedRoomNotification(BaseNotification):
    def __init__(self, room):
        super().__init__()
        self._room = room

    @property
    def room(self):
        return self._room


class PlayerJoinedRoomSubscriber(BaseNotificationHandler):
    async def handle(self, notification: PlayerJoinedRoomNotification):
        print(f'Update in room {notification.room.id}. Player count: {notification.room.player_count}')
