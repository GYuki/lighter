import json

from pydiator_core.interfaces import BaseNotificationHandler


class RpsNotificationHandler(BaseNotificationHandler):
    def __init__(self, rps):
        super().__init__()
        self._rps = rps

    def _send_message(self, event, data):
        self._rps.send_message(event, json.dumps(data))
