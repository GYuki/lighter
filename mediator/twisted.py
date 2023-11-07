from pydiator_core.interfaces import BaseRequest
from pydiator_core.mediatr import Mediatr
from twisted.internet.defer import inlineCallbacks


class TwistedMediator(Mediatr):
    @inlineCallbacks
    def deferred_send(self, req: BaseRequest, **kwargs):
        if self.__container is None:
            raise Exception("Twisted container is None")

        pipelines = self.__container.get_pipelines()
        if len(pipelines) == 0:
            raise Exception("Twisted container doesn't have any pipeline")

        result = yield pipelines[0].handle(req=req, **kwargs)
        return result


twidiator = TwistedMediator()
