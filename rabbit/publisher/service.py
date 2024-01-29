from twisted.application import service


class RabbitPublisherService(service.Service):
    def __init__(self):
        super().__init__()
        self._amqp = None

    def startService(self):
        amqp_service = self.parent.getServiceNamed("amqp")
        self._amqp = amqp_service.getFactory()
        self._amqp.buildProtocol('')

    def send_message(self, event_name, event):
        self._amqp.send_message('lighter', event_name, event)
