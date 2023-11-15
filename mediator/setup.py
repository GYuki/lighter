from pydiator_core.mediatr import pydiator
from pydiator_core.mediatr_container import MediatrContainer

from rooms.commands.authcommand import AuthCommandRequest, AuthCommandHandler
from rooms.commands.createcommand import CreateCommandRequest, CreateCommandHandler
from rooms.commands.joincommand import JoinCommandRequest, JoinCommandHandler
from rooms.commands.leavecommand import LeaveRoomCommandRequest, LeaveRoomCommandHandler
from rooms.commands.raiseeventcommand import RaiseEventCommandRequest, RaiseEventCommandHandler
from rooms.notifications.playerjoinedroom import PlayerJoinedRoomNotification, PlayerJoinedRoomSubscriber
from rooms.notifications.playerleftroom import PlayerLeftRoomSubscriber, PlayerLeftRoomNotification
from rooms.notifications.roomdeleted import RoomDeletedNotification, RoomDeletedSubscriber


def mediator_set_up():
    container = MediatrContainer()
    container.register_request(CreateCommandRequest, CreateCommandHandler())
    container.register_request(JoinCommandRequest, JoinCommandHandler())
    container.register_request(RaiseEventCommandRequest, RaiseEventCommandHandler())
    container.register_request(AuthCommandRequest, AuthCommandHandler())
    container.register_request(LeaveRoomCommandRequest, LeaveRoomCommandHandler())

    container.register_notification(PlayerJoinedRoomNotification, [PlayerJoinedRoomSubscriber()])
    container.register_notification(RoomDeletedNotification, [RoomDeletedSubscriber()])
    container.register_notification(PlayerLeftRoomNotification, [PlayerLeftRoomSubscriber()])

    pydiator.ready(container=container)
