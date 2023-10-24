from twisted.application import service
from zope.interface import implementer

from protocol.service.abstraction import ILighterService


@implementer(ILighterService)
class LighterService(service.Service):
    def connection_made(self):
        print('Connection made!')

    def connection_lost(self):
        print('Connection lost!')

    def handle_request(self, data):
        print('handling request...', data)
