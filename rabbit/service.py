from twisted.application import service, internet
from twisted.internet import ssl

from rabbit.factory import PikaFactory


class PikaService(service.MultiService):
    name = 'amqp'

    def __init__(self, parameter):
        service.MultiService.__init__(self)
        self.parameters = parameter

    def startService(self):
        self.connect()
        service.MultiService.startService(self)

    def getFactory(self):
        return self.services[0].factory

    def connect(self):
        f = PikaFactory(self.parameters)
        if self.parameters.ssl_options:
            s = ssl.ClientContextFactory()
            serv = internet.SSLClient( # pylint: disable=E1101
                host=self.parameters.host,
                port=self.parameters.port,
                factory=f,
                contextFactory=s)
        else:
            serv = internet.TCPClient( # pylint: disable=E1101
                host=self.parameters.host,
                port=self.parameters.port,
                factory=f)
        serv.factory = f
        f.service = serv # pylint: disable=W0201
        name = '%s%s:%d' % ('ssl:' if self.parameters.ssl_options else '',
                            self.parameters.host, self.parameters.port)
        serv.__repr__ = lambda: '<AMQP Connection to %s>' % name
        serv.setName(name)
        serv.setServiceParent(self)
