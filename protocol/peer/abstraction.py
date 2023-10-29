from zope.interface import Interface, implementer


class IPeer(Interface):
    def send_message(self):
        """
        call to send messages from server to client
        @return:
        """

    def disconnect(self):
        """
        call to disconnect client from server
        @return:
        """


@implementer(IPeer)
class BasePeer(object):
    def __init__(self, protocol):
        self._protocol = protocol

    def _prepare_data(self, data):
        return data

    def send_message(self, data):
        self._protocol.send_message(self._prepare_data(data))

    def disconnect(self):
        pass
