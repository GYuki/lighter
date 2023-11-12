from rooms.joinmodes import JoinModes
from rooms.player import Player
from rooms.resultcode import ResultCode, DebugMessage


class PlayerContainer(object):
    def __init__(self, max_actors=32):
        self._players = []
        self._max_actors = max_actors
        self._number_stack = []
        for i in range(self._max_actors, 0, -1):
            self._number_stack.append(i)

    def _pop_number_stack(self):
        return self._number_stack.pop()

    def _push_number_stack(self, item):
        self._number_stack.append(item)

    def _add_player(self, peer):
        player = Player(peer)
        player.player_nr = self._pop_number_stack()
        print('Add player with peer:', player.peer)
        self._players.append(player)

    def remove_player(self, peer):
        player_index = next((i for i, p in enumerate(self._players) if p.peer == peer), -1)
        if 0 <= player_index < len(self._players):
            print('Remove player with peer:', self._players[player_index].peer)
            del self._players[player_index]

    def broadcast_to_all(self, data):
        [player.send_message(data) for player in self._players]

    def get_player_by_id(self, _id):
        return next((player for player in self._players if player.id == _id), None)

    def get_player_by_peer(self, peer):
        return next((player for player in self._players if player.peer == peer), None)

    def _verify_can_join(self, peer, join_mode):
        player = self.get_player_by_peer(peer)
        if player is not None:
            return ResultCode.PeerAlreadyJoined, player

        if peer.id < 1:
            return ResultCode.PeerIdIsNull, player

        player = self.get_player_by_id(peer.id)
        if player is not None:
            if player.is_active:
                # check this moment later
                return ResultCode.ActiveJoiner, player

            if join_mode != JoinModes.RejoinOnly and join_mode != JoinModes.RejoinOrJoin:
                return ResultCode.InactiveJoiner, player

            return ResultCode.OK, player

        if join_mode == JoinModes.RejoinOnly:
            return ResultCode.RejoinerNotFound, player

        return ResultCode.OK, player

    def try_add_peer_to_game(self, peer, join_mode):
        result_code, player = self._verify_can_join(peer, join_mode)
        if result_code == ResultCode.OK:
            if player is None:
                self._add_player(peer)
            else:
                player.reactivate(peer)

        print(DebugMessage[result_code])
        return result_code
