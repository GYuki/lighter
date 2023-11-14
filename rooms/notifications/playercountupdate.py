from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler


class PlayerCountUpdateNotification(BaseNotification):
    def __init__(self, room_id, player_count):
        super().__init__()
        self._room_id = room_id
        self._player_count = player_count

    @property
    def room_id(self):
        return self._room_id

    @property
    def player_count(self):
        return self._player_count


class PlayerCountUpdateSubscriber(BaseNotificationHandler):
    async def handle(self, notification: PlayerCountUpdateNotification):
        print(f'Update in room {notification.room_id}. Player count: {notification.player_count}')
