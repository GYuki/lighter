from autobahn.twisted import WebSocketServerFactory
from zope.interface import implementer

from protocol.app_protocols.ws_protocol import WsAppProtocol
from protocol.factory.abstraction import ILighterFactory


@implementer(ILighterFactory)
class LighterFactory(WebSocketServerFactory):
    protocol = WsAppProtocol

    def __init__(self, service):
        self.service = service
        super().__init__()

    def connection_made(self):
        self.service.connection_made()

    def connection_lost(self):
        self.service.connection_lost()

    def handle_request(self, data):
        self.service.handle_request(data)
