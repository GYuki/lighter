class Player(object):
    def __init__(self, peer):
        self._peer = peer
        self._id = peer.id

    @property
    def id(self):
        return self._id

    @property
    def peer(self):
        return self._peer

    @property
    def is_active(self):
        return self._peer is not None

    def deactivate(self):
        self._peer = None

    def reactivate(self, peer):
        self._peer = peer

    def send_message(self, data):
        self._peer.send_message(data)
