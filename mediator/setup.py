from pydiator_core.mediatr import pydiator
from pydiator_core.mediatr_container import MediatrContainer

from protocol.notifications.servercreated import ServerCreatedNotification, ServerCreatedSubscriber
from rooms.commands.authcommand import AuthCommandRequest, AuthCommandHandler
from rooms.commands.createcommand import CreateCommandRequest, CreateCommandHandler
from rooms.commands.joincommand import JoinCommandRequest, JoinCommandHandler
from rooms.commands.leavecommand import LeaveRoomCommandRequest, LeaveRoomCommandHandler
from rooms.commands.raiseeventcommand import RaiseEventCommandRequest, RaiseEventCommandHandler
from rooms.notifications.playerjoinedroom import PlayerJoinedRoomNotification, PlayerJoinedRoomSubscriber
from rooms.notifications.playerleftroom import PlayerLeftRoomSubscriber, PlayerLeftRoomNotification
from rooms.notifications.roomcreated import RoomCreatedNotification, RoomCreatedSubscriber
from rooms.notifications.roomdeleted import RoomDeletedNotification, RoomDeletedSubscriber


def mediator_set_up(rps):
    container = MediatrContainer()
    container.register_request(CreateCommandRequest, CreateCommandHandler())
    container.register_request(JoinCommandRequest, JoinCommandHandler())
    container.register_request(RaiseEventCommandRequest, RaiseEventCommandHandler())
    container.register_request(AuthCommandRequest, AuthCommandHandler())
    container.register_request(LeaveRoomCommandRequest, LeaveRoomCommandHandler())

    container.register_notification(PlayerJoinedRoomNotification, [PlayerJoinedRoomSubscriber(rps)])
    container.register_notification(RoomDeletedNotification, [RoomDeletedSubscriber(rps)])
    container.register_notification(PlayerLeftRoomNotification, [PlayerLeftRoomSubscriber(rps)])
    container.register_notification(ServerCreatedNotification, [ServerCreatedSubscriber(rps)])
    container.register_notification(RoomCreatedNotification, [RoomCreatedSubscriber(rps)])

    pydiator.ready(container=container)
