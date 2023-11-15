import json

from pydiator_core.mediatr import pydiator

from protocol.request.codes import RequestCode
from rooms.commands.authcommand import AuthCommandRequest
from rooms.commands.createcommand import CreateCommandRequest
from rooms.commands.joincommand import JoinCommandRequest
from rooms.commands.leavecommand import LeaveRoomCommandRequest
from rooms.commands.raiseeventcommand import RaiseEventCommandRequest
from rooms.notifications.playerjoinedroom import PlayerJoinedRoomNotification
from rooms.notifications.playerleftroom import PlayerLeftRoomNotification
from rooms.resultcode import DebugMessage, ResultCode


class RequestController(object):
    async def handle(self, raw_request, peer):
        request = json.loads(raw_request)
        data = {}

        if request['cmd'] == RequestCode.CreateRoom:
            result = await pydiator.send(
                CreateCommandRequest(
                    peer=peer,
                    room_id=request['data']['room_name']
                )
            )

            if result.status == ResultCode.OK:
                await pydiator.publish(PlayerJoinedRoomNotification(
                    peer.room
                ))

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

            if result.status == ResultCode.OK:
                await pydiator.publish(PlayerJoinedRoomNotification(
                    peer.room
                ))

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
        elif request['cmd'] == RequestCode.Auth:
            result = await pydiator.send(
                AuthCommandRequest(
                    peer=peer,
                    peer_id=request['data']['id']
                )
            )
        elif request['cmd'] == RequestCode.LeaveRoom:
            room = peer.room
            result = await pydiator.send(
                LeaveRoomCommandRequest(
                    peer=peer
                )
            )
            if result.status == ResultCode.OK:
                await pydiator.publish(
                    PlayerLeftRoomNotification(
                        room
                    )
                )
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
