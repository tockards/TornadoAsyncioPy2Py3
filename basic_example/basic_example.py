import tornado
from future.standard_library import install_aliases
install_aliases()
from sys import version


class BasicExampleBaseClass(object):
    def __init__(self, wait_secs):
        self._ioloop = tornado.ioloop.IOLoop.current()
        self._wait_secs = wait_secs
        self._pyversion = version