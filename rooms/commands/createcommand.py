from pydiator_core.interfaces import BaseRequest, BaseResponse, BaseHandler
from twisted.internet import defer
from twisted.internet.defer import inlineCallbacks

from rooms.joinmodes import JoinModes
from rooms.resultcode import ResultCode
from rooms.roomcache import room_cache


class CreateCommandRequest(BaseRequest):
    def __init__(self, peer, room_id):
        super().__init__()
        self._peer = peer
        self._room_id = room_id

    @property
    def peer(self):
        return self._peer

    @property
    def room_id(self):
        return self._room_id


class CreateCommandResponse(BaseResponse):
    def __init__(self, status, room_name):
        super().__init__()
        self._status = status
        self._room_name = room_name

    @property
    def status(self):
        return self._status

    @property
    def room_name(self):
        return self._room_name


class CreateCommandHandler(BaseHandler):
    async def handle(self, req: CreateCommandRequest):
        room = self._get_room_from_room_cache(req.room_id)

        if room is None:
            response = self._generate_failed_response()

        else:
            result = await room.join_room(req.peer, JoinModes.Create)
            response = self._generate_success_response(result, room.id)

            if result == ResultCode.OK:
                req.peer.set_room(room)

        return response

    def _get_room_from_room_cache(self, _id):
        return room_cache.try_create_room(_id)

    def _generate_failed_response(self):
        return CreateCommandResponse(
                status=ResultCode.RoomCreationError,
                room_name=""
            )

    def _generate_success_response(self, status, _id):
        return CreateCommandResponse(
                status=status,
                room_name=_id
            )
