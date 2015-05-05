from oslo.config import cfg

CONF = cfg.CONF

# TODO: Implement filters: request_id, catch_errors, noauth ..

def pipline_factory(loader, global_conf, **local_conf):
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