from rooms.commands.createcommand import CreateCommandRequest, CreateCommandResponse, CreateCommandHandler
from rooms.resultcode import ResultCode
from rooms.roomcache import room_cache


class JoinCommandRequest(CreateCommandRequest):
    pass


class JoinCommandResponse(CreateCommandResponse):
    pass


class JoinCommandHandler(CreateCommandHandler):
    def _get_room_from_room_cache(self, _id):
        return room_cache.get_room_by_id(_id)

    def _generate_failed_response(self):
        return JoinCommandResponse(
            status=ResultCode.GetRoomFromRoomCacheError,
            room_name=""
        )

    def _generate_success_response(self, status, _id):
        return JoinCommandResponse(
                status=status,
                room_name=_id
            )
