from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler
from twisted.internet import defer
from twisted.internet.defer import inlineCallbacks

from rooms.resultcode import ResultCode


class RaiseEventCommandRequest(BaseRequest):
    def __init__(self, peer, data):
        super().__init__()
        self._peer = peer
        self._data = data

    @property
    def peer(self):
        return self._peer

    @property
    def data(self):
        return self._data


class RaiseEventCommandResponse(BaseResponse):
    def __init__(self, status):
        super().__init__()
        self._status = status

    @property
    def status(self):
        return self._status


class RaiseEventCommandHandler(BaseHandler):
    async def handle(self, req: RaiseEventCommandRequest):
        req.peer.room.broadcast_data_to_all_players(req.data)
        return RaiseEventCommandResponse(ResultCode.OK)
