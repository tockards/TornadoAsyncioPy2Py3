from future.standard_library import install_aliases
install_aliases()
from sys import version
import asyncio

from basic_example import BasicExampleBaseClass

class BasicExampleClass(BasicExampleBaseClass):

    async def say_hello(self):
        print("Hello from %s", version)
        await asyncio.sleep(self._wait_secs)
        print("Goodbye from %s", version)
        self._ioloop.stop()