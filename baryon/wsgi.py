from paste import deploy
import eventlet
import eventlet.wsgi
import socket

class WorkerProvider(object):

    def __init__(self, app, service, host='0.0.0.0', port=0):
        self._service = service
        self._app = app
        self._server = None
        self._pool = eventlet.GreenPool(2)
        info = socket.getaddrinfo(host,
                                  port,
                                  socket.AF_UNSPEC,
                                  socket.SOCK_STREAM)[0]
        bind_addr = (host, port)
        self._socket = eventlet.listen(bind_addr, family=host, backlog=128)

    def start(self):
        dup_socket = self._socket
        self._server = eventlet.spawn(
            eventlet.wsgi.server,
            dup_socket,
            self._app
        )
        print "get socket"
        print "launch process (eventlet.wsgi.server,spawn)..."

    def wait(self):
        print "_service wait"

    def stop(self):
        print "kill service"


class Server(object):

    def __init__(self, name, app):

        self._worker = WorkerProvider(self, self.app)

    def start(self):
       self._worker.start()

    def stop(self):
        self._worker.stop()

    def wait(self):
        self._worker.wait()
