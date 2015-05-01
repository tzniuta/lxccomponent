from webob import Response
from webob.dec import wsgify

class APIRouter():

    def __init__(self, **local_config):
        pass

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls().appliation

    @wsgify
    def appliation(self, request):
        return Response('hello')

