from pydiator_core.mediatr import pydiator
from pydiator_core.mediatr_container import MediatrContainer

from rooms.commands.authcommand import AuthCommandRequest, AuthCommandHandler
from rooms.commands.createcommand import CreateCommandRequest, CreateCommandHandler
from rooms.commands.joincommand import JoinCommandRequest, JoinCommandHandler
from rooms.commands.raiseeventcommand import RaiseEventCommandRequest, RaiseEventCommandHandler


def mediator_set_up():
    container = MediatrContainer()
    container.register_request(CreateCommandRequest, CreateCommandHandler())
    container.register_request(JoinCommandRequest, JoinCommandHandler())
    container.register_request(RaiseEventCommandRequest, RaiseEventCommandHandler())
    container.register_request(AuthCommandRequest, AuthCommandHandler())
    pydiator.ready(container=container)
