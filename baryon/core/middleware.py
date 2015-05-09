from oslo.config import cfg
import webob.dec
import webob.exc
import routes.middleware

CONF = cfg.CONF


class Router(object):

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls()

    def __init__(self, mapper):
        self.map = mapper
        self._router = routes.middleware.RoutesMiddleware(self._dispatch, self.map)

    @webob.dec.wsgify
    def __call__(self, request):
        return self._router

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(request):
        match = request.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound
        app = match['controller']
        return app