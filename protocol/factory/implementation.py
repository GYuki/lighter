from zope.interface import implementer
from twisted.internet import protocol as _protocol
from protocol.factory.abstraction import ILighterFactory


@implementer(ILighterFactory)
class LighterFactory(_protocol.ServerFactory):
    protocol = None  # assign later

    def __init__(self, service):
        self.service = service

    def connection_made(self):
        self.service.connection_made()

    def connection_lost(self):
        self.service.connection_lost()

    def handle_request(self):
        self.service.handle_request()
