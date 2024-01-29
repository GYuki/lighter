from pydiator_core.mediatr import pydiator
from twisted.application import service
from twisted.internet.defer import ensureDeferred
from zope.interface import implementer

from protocol.notifications.servercreated import ServerCreatedNotification
from protocol.request.controller import RequestController
from protocol.service.abstraction import ILighterService


@implementer(ILighterService)
class LighterService(service.Service):
    def __init__(self):
        self.request_controller = RequestController()

    def service_created(self):
        d = ensureDeferred(self._service_created())
        d.addCallback(print)

    async def _service_created(self):
        await pydiator.publish(
            ServerCreatedNotification()
        )

    def connection_made(self, peer):
        print('Connection made!')

    def connection_lost(self, peer):
        peer.disconnect()
        print('Connection lost!')

    def handle_request(self, data, peer):
        d = ensureDeferred(self.request_controller.handle(data, peer))
        d.addCallback(print)
        # peer.room.broadcast_data_to_all_players(data)
        print('handling request...', data)
