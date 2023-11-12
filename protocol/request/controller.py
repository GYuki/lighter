import json

from pydiator_core.mediatr import pydiator

from protocol.request.codes import RequestCode
from rooms.commands.createcommand import CreateCommandRequest
from rooms.commands.joincommand import JoinCommandRequest
from rooms.commands.raiseeventcommand import RaiseEventCommandRequest
from rooms.resultcode import DebugMessage


class RequestController(object):
    async def handle(self, raw_request, peer):
        request = json.loads(raw_request)
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
        elif request['cmd'] == RequestCode.JoinRoom:
            result = await pydiator.send(
                JoinCommandRequest(
                    peer=peer,
                    room_id=request['data']['room_name']
                )
            )

            data = {
                    'room_name': result.room_name
                }

        elif request['cmd'] == RequestCode.RaiseEvent:
            result = await pydiator.send(
                RaiseEventCommandRequest(
                    peer=peer,
                    data=request['data']
                )
            )

            data = {}
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
