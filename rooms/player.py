class Player(object):
    def __init__(self, peer):
        self._peer = peer

    @property
    def peer(self):
        return self._peer

    def send_message(self, data):
        self._peer.send_message(data)
