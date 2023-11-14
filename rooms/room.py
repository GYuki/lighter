import asyncio

from pydiator_core.mediatr import pydiator

from rooms.notifications.playercountupdate import PlayerCountUpdateNotification
from rooms.playercontainer import PlayerContainer
from rooms.resultcode import ResultCode


class Room(object):
    def __init__(self, _id):
        self._id = _id
        self._container = PlayerContainer()

    @property
    def id(self):
        return self._id

    def join_room(self, peer, join_mode):
        result = self._container.try_add_peer_to_game(peer, join_mode)
        if result == ResultCode.OK:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(pydiator.publish(PlayerCountUpdateNotification(
                self._id,
                self._container.player_count
            )))
            loop.close()
        return result

    def leave_room(self, peer):
        self._container.remove_player(peer)

    def broadcast_data_to_all_players(self, data):
        self._container.broadcast_to_all(data)
