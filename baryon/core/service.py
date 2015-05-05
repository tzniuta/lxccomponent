# Copyright 2015 Cha Dong-Hwi

from baryon.openstack.common import service
from baryon.core import wsgi
from nova.openstack.common import log as logging

LOG = logging.getLogger(__name__)

class WSGIService(object):

    def __init__(self, app_name):
        #fixme: logging isn't working: check option are needed to enable logging
        print "logging isn't working!"
        LOG.info("Logging enabled!")
        LOG.info(_("Logging enabled!"))

        self.app_name = app_name
        self.server = wsgi.Server(self.app_name)

    def start(self):
        self.server.start()

    def wait(self):
        self.server.wait()

    def stop(self):
        self.server.stop()


class WSGIServiceFactory(WSGIService):

    @classmethod
    def get_instance(cls, app_name):
        return cls(app_name)


def process_launcher():
    return service.ProcessLauncher()

