# Copyright 2015 Cha Dong-Hwi

import webob
from baryon.core import middleware
import routes



class Index():
    def __init__(self):
        pass

    @webob.dec.wsgify
    def __call__(self, req):
        return webob.Response('ver1')


class RestAPIRouter(middleware.Router):

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls(**local_config)

    def __init__(self, **local_config):
        mapper = routes.Mapper()
        mapper.connect('index', '/', controller=Index())
        # self._map_basic_resource(mapper)
        super(RestAPIRouter, self).__init__(mapper)
    #
    # def _map_basic_resource(self, mapper):
    #     for resource in self._get_resource_list():
    #         with mapper.submapper(path_prefix="/" % resource, controller=resource) as m:
    #
    #             mapper_kwargs = dict(collection_name=resource,
    #                                  controller=resource,
    #
    #                                  )
    #             m.connect()
    #
    #
    # def _get_resource_list(self):
    #     return {
    #         'lxc'
    #     }

