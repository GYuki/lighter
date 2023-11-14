from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler

from rooms.resultcode import ResultCode


class LeaveRoomCommandRequest(BaseRequest):
    def __init__(self, peer):
        super().__init__()
        self._peer = peer

    @property
    def peer(self):
        return self._peer


class LeaveRoomCommandResponse(BaseResponse):
    def __init__(self, status):
        super().__init__()
        self._status = status

    @property
    def status(self):
        return self._status


class LeaveRoomCommandHandler(BaseHandler):
    async def handle(self, req: LeaveRoomCommandRequest):
        req.peer.leave_room()
        return LeaveRoomCommandResponse(ResultCode.OK)
