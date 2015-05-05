# Copyright 2015 Cha Dong-Hwi

import sys

from baryon.core import service
from baryon.common import config


def main():
    config.init(sys.argv)

    launcher = service.process_launcher()
    server = service.WSGIServiceFactory.get_instance('baryon')
    launcher.launch_service(server, 1)
    launcher.wait()