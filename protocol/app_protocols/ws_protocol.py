from typing import Union, Optional, Tuple, Dict

from autobahn.twisted.websocket import WebSocketServerProtocol
from autobahn.websocket import ConnectionRequest
from autobahn.websocket.protocol import WebSocketProtocol
from twisted.internet.protocol import connectionDone
from twisted.python.failure import Failure

from protocol.peer.ws_peer import LighterWsPeer


class WsAppProtocol(WebSocketServerProtocol):
    def __init__(self):
        super().__init__()
        self._peer = None

    def onConnect(self, request: ConnectionRequest) -> Union[Optional[str], Tuple[Optional[str], Dict[str, str]]]:
        self._peer = LighterWsPeer(self)
        self.factory.connection_made()
        return super().onConnect(request)

    def onMessage(self, payload, isBinary):
        self.factory.handle_request(payload, self._peer)
        super().onMessage(payload, isBinary)

    def connectionLost(self, reason: Failure = connectionDone):
        self.factory.connection_lost(self._peer)
        super().connectionLost(reason)
