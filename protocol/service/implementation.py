from twisted.application import service
from zope.interface import implementer

from protocol.service.abstraction import ILighterService
from rooms.roomcache import RoomCache


@implementer(ILighterService)
class LighterService(service.Service):
    def __init__(self):
        self._room_cache = RoomCache()

    def connection_made(self):
        print('Connection made!')

    def connection_lost(self, peer):
        peer.disconnect()
        print('Connection lost!')

    def handle_request(self, data, peer):
        room = self._room_cache.try_create_room('123')
        room.join_room(peer)
        print('handling request...', data)
