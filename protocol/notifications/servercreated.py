import json
import os

from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler

from rooms.notifications.rpsnotifications import RpsNotificationHandler


# global rps


class ServerCreatedNotification(BaseNotification):
    def __init__(self):
        super().__init__()


class ServerCreatedSubscriber(RpsNotificationHandler):

    async def handle(self, notification: ServerCreatedNotification):
        # global rps
        address = f'{os.environ.get("ip")}:{os.environ.get("port")}'
        domain = os.environ.get("domain")
        self._send_message('server_create', {
            "address": address,
            "domain": domain
        })
