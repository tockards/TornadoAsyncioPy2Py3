"""Basic Example to demonstrate Python 2 and Python 3 compatibility with
tornado and asyncio.

This aims to show how you can use the tornado ioloop to run both
tornado coroutines and asyncio coroutines
"""

import future
from future.standard_library import install_aliases
install_aliases()

from tornado.ioloop import IOLoop
from message_bus_adapter import Adapter

if future.utils.PY2:
    io_loop = IOLoop()
    from message_bus_broker_adaptee_py2 import BasicExampleClass
else:
    from tornado.platform.asyncio import AsyncIOMainLoop
    io_loop = AsyncIOMainLoop()
    from message_bus_broker_adaptee_py2 import BasicExampleClass

base_example = BasicExampleClass(2)
adapt = Adapter(base_example, dict(say_hello=base_example.say_hello))

io_loop.add_callback(adapt.say_hello)
io_loop.start()