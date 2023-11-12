from twisted.application import service
from twisted.internet import endpoints, reactor

from mediator.setup import mediator_set_up
from protocol.factory.implementation import LighterFactory
from protocol.service.implementation import LighterService


application = service.Application("Lighter")
ls = LighterService()

ls.setServiceParent(application)
ws_factory = LighterFactory("ws://127.0.0.1:8000")
ws_factory.service = ls

ws_endpoint = endpoints.serverFromString(reactor, 'tcp:8000')
ws_endpoint.listen(ws_factory)

mediator_set_up()
reactor.run()
