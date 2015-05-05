# Copyright 2015 Cha Dong-Hwi

from webob import Response
from webob.dec import wsgify
from baryon.core import middleware


class BaseAPIRouter(middleware.Router):

    def __init__(self, **local_config):
        pass

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls().application

    @wsgify
    def application(self, request):
        return Response('hello')

