from twisted.application import service


class RabbitPublisherService(service.Service):
    def __init__(self):
        super().__init__()
        self._amqp = None

    def startService(self):
        amqp_service = self.parent.getServiceNamed("amqp")
        self._amqp = amqp_service.getFactory()
        self._amqp.buildProtocol('')
