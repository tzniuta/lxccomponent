# Copyright 2015 Cha Dong-Hwi

import sys
from oslo.config import cfg
from baryon import service
from baryon.common import config

CONF = cfg.CONF


def main():
    config.init(sys.argv)

    launcher = service.process_launcher()
    server = service.WSGIServiceFactory.get_instance('api')
    launcher.launch_service(server, 1)
    launcher.wait()