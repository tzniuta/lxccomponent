from paste import deploy


class WorkerProvider(object):

    def __init__(self,app,service):
        self._service = service
        self._app = app
        self._server = None

    def start(self):
        print "get socket"
        print "launch process (eventlet.wsgi.server,spawn)..."

    def wait(self):
        print "_service wait"

    def stop(self):
        print "kill service"


class Server(object):

    def __init__(self, name,app):
        self.name = name
        self.service = None
        self.app = app

    def start(self):
       service = WorkerProvider(self, self.app)
