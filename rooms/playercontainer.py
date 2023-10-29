from rooms.player import Player


class PlayerContainer(object):
    def __init__(self):
        self._players = []

# Peers in add_player and remove_player later will be substituted to user_id and PlayerContainer won't know about
# peers at all.

    def add_player(self, peer):
        player = Player(peer)
        print('Add player with peer:', player.peer)
        self._players.append(player)

    def remove_player(self, peer):
        player_index = next((i for i, p in enumerate(self._players) if p.peer == peer), -1)
        if 0 < player_index < len(self._players):
            print('Remove player with peer:', self._players[player_index].peer)
            del self._players[player_index]

    def broadcast_to_all(self, data):
        [player.send_message(data) for player in self._players]
