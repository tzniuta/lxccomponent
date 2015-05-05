# Copyright 2015 Cha Dong-Hwi

from oslo.config import cfg
from baryon.common import exception
import routes.middleware
import webob.dec
import webob.exc
import webob

CONF = cfg.CONF

# TODO: Implement filters: request_id, noauth ..

def pipline_factory(loader, global_conf, **local_conf):
    if CONF.auth_strategy not in ['noauth', 'keystone']:
        raise exception.ConfigWrongValue()
    pipline = local_conf[CONF.auth_strategy]
    pipline = pipline.split()
    filters = [loader.get_filter(n) for n in pipline[:-1]]
    app = loader.get_app(pipline[-1])
    filters.reverse()
    for filter in filters:
        app = filter(app)
    return app


class Middleware(object):
    pass

class Request(webob.Request):
    pass

class Router(object):

    def __init__(self, mapper):
        self.map = mapper

    def __call__(self, req):
        pass

    @staticmethod
    @webob.dec.wsgify(RequestClass=Request)
    def _dispath(req):
        match =req.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound
        app = match['controller']
        return app

