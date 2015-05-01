# Copyright 2015 Cha Dong-Hwi

import eventlet
import eventlet.wsgi
import socket

from paste import deploy
from baryon.openstack.common import log as logging
from oslo.config import cfg
from baryon.common import exception

LOG = logging.getLogger(__name__)

wsgi_opts = [
    cfg.StrOpt('wsgi_log_format',
                default='%(client_ip)s "%(request_line)s" status: %(status_code)s'
                        ' len: %(body_length)s time: %(wall_seconds).7f',
                help='A python format string that is used as the template to '
                     'generate log lines. The following values can be formatted '
                     'into it: client_ip, date_time, request_line, status_code, '
                     'body_length, wall_seconds.'),
    cfg.IntOpt('client_socket_timeout',
                default=0,
                help="Timeout for client connections' socket operations. "
                    "If an incoming connection is idle for this number of "
                    "seconds it will be closed. A value of '0' means "
                    "wait forever."),
    cfg.BoolOpt('wsgi_keep_alive',
                default=True,
                help="If False, closes the client socket connection "
                     "explicitly.")
]

CONF = cfg.CONF
CONF.register_opts(wsgi_opts)


class EventletProvider(object):
    """ Create Server process with Eventlet """

    def __init__(self, name, app):
        self._name = name
        self._app = app
        self._server = None
        self._protocol = eventlet.wsgi.HttpProtocol
        self._pool = eventlet.GreenPool()
        self._pool_size = 1000
        self._logger = logging.getLogger("nova.%s.wsgi.server" % self._name)
        self._wsgi_logger = logging.WritableLogger(self._logger)

        self._client_socket_timeout = CONF.client_socket_timeout
        self._wsgi_log_format = CONF.wsgi_log_format
        self._wsgi_keep_alive = CONF.wsgi_keep_alive

        self._bind_ip = CONF.bind_host
        self._port = CONF.bind_port

        self._set_server()

    def _set_server(self):
        host = self._bind_ip
        port = self._port
        bind_addr = (host, port)

        info = socket.getaddrinfo(bind_addr[0], bind_addr[1], socket.AF_UNSPEC, socket.SOCK_STREAM)[0]

        family = info[0]
        self._socket = eventlet.listen(bind_addr, family, backlog=128)

    def start(self):
        dup_socket = self._socket.dup()
        wsgi_kwargs = {
            'func': eventlet.wsgi.server,
            'sock': dup_socket,
            'site': self._app,
            'protocol': self._protocol,
            'custom_pool': self._pool,
            'log': self._wsgi_logger,
            'log_format': self._wsgi_log_format,
            'debug': False,
            'keepalive': self._wsgi_keep_alive,
            'socket_timeout': self._client_socket_timeout
        }

        self._server = eventlet.spawn(**wsgi_kwargs)

    def reset(self):

        self._pool.resize(self._pool_size)

    def wait(self):
        self._pool.waitall()
        self._server.wait()

    def stop(self):
        self._pool.resize(0)
        self._server.kill()


class Server(object):
    """ Provides Server class. At this time eventlet is used as default. """

    def __init__(self, app_name):
        self.name = app_name
        self._worker = None

        self._load_eventlet_with_paste()

    def start(self):
       self._worker.start()

    def stop(self):
        self._worker.stop()

    def wait(self):
        self._worker.wait()

    def _load_eventlet_with_paste(self):
        app = PasteProvider.load_paste_app(self.name)
        self._worker = EventletProvider(self.name, app)


class PasteProvider(object):

    def __init__(self, name):
        config_path = cfg.CONF.find_file(cfg.CONF.api_paste_config)
        if not config_path:
            raise exception.ConfigNotFound()
        self._config_path = config_path
        self._name = name

    def load(self):
        # TODO: exception handling with "try catch"
        return deploy.loadapp("config:%s" % self._config_path, name=self._name)

    @classmethod
    def load_paste_app(cls, app_name):
        paste = cls(app_name)
        return paste.load()