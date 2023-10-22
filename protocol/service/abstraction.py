from zope.interface import Interface


class ILighterService(Interface):
    def connection_made(self):
        """
        called when client connects to server
        @return:
        """

    def connection_lost(self):
        """
        called when client disconnects
        @return:
        """

    def handle_request(self):
        """
        handle incoming request
        @return:
        """
