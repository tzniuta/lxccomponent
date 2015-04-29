from baryon.openstack.common import service
from baryon import wsgi

class WSGIService(object):

    def __init__(self,app_name):
        self.app_name = app_name
        self.wsgi_app = None

    def start(self):
        self.app = wsgi.WSGILoader().load_app(self.app_name)
        self.host = "0.0.0.0"
        self.port = "20000"
        self.server = wsgi.Server()
        self.server.start(app,)

    def wait(self):
        self.wsgi_app.wait()


class WSGIServiceFactory(WSGIService):

    @classmethod
    def create(cls, app_name):
        return cls(app_name)







def process_launcher():
    return service.ProcessLauncher()