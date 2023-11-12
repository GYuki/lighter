from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from rooms.resultcode import ResultCode


class AuthCommandRequest(BaseRequest):
    def __init__(self, peer, peer_id):
        super().__init__()
        self._peer = peer
        self._peer_id = peer_id

    @property
    def peer(self):
        return self._peer

    @property
    def peer_id(self):
        return self._peer_id


class AuthCommandResponse(BaseResponse):
    def __init__(self, status):
        super().__init__()
        self._status = status

    @property
    def status(self):
        return self._status


class AuthCommandHandler(BaseHandler):
    async def handle(self, req: AuthCommandRequest):
        req.peer.id = req.peer_id
        return AuthCommandResponse(status=ResultCode.OK)
