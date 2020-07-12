from future.standard_library import install_aliases
install_aliases()
from tornado import gen

from basic_example import BasicExampleBaseClass


class BasicExampleClass(BasicExampleBaseClass):

    @gen.coroutine
    def say_hello(self):
        print("Hello from %s", self._pyversion)
        yield gen.sleep(self._wait_secs)
        print("Goodbye from %s", self._pyversion)
        self._ioloop.stop()
