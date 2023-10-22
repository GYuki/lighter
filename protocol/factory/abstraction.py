from zope.interface import Interface


class ILighterFactory(Interface):
    def connection_made(self):
        """
        called when client connects to server. calls service's connection_made
        @return:
        """

    def connection_lost(self):
        """
        called when client disconnects. calls service's connection_lost
        @return:
        """

    def handle_request(self):
        """
        handle incoming request. calls service's handle_request
        @return:
        """
