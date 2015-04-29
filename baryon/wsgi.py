from paste import deploy

class WSGILoader(object):

    def load_app(self, name):
        return deploy.loadapp("config:")



class ServerProcessor(object):

    def __init__(self):
        print 'setup server config'
        print 'eventlet listen'

    def start(self):
        print 'eventlet start'
