from pydiator_core.mediatr import pydiator

from protocol.request.codes import RequestCode
from rooms.commands.createcommand import CreateCommandRequest
from rooms.resultcode import DebugMessage


class RequestController(object):
    async def handle(self, request, peer):
        if request['cmd'] == RequestCode.CreateRoom:
            result = await pydiator.send(
                CreateCommandRequest(
                    peer=peer,
                    room_id=request['data']['room_name']
                )
            )
            data = {
                    'room_name': result.room_name
                }
        else:
            print('could not parse request')
            return

        peer.send_message(
            {
                'cmd': request['cmd'],
                'data': data,
                'status': result.status,
                'msg': DebugMessage[result.status]
            }
        )
