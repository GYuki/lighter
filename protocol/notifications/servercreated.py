import json
import os

from pydiator_core.interfaces import BaseNotification, BaseNotificationHandler

# global rps


class ServerCreatedNotification(BaseNotification):
    def __init__(self):
        super().__init__()


class ServerCreatedSubscriber(BaseNotificationHandler):
    def __init__(self, rps):
        super().__init__()
        self._rps = rps

    async def handle(self, notification: ServerCreatedNotification):
        # global rps
        address = f'{os.environ.get("ip")}:{os.environ.get("port")}'
        domain = os.environ.get("domain")
        self._rps.send_message('server_create', json.dumps({
            "address": address,
            "domain": domain
        }))
