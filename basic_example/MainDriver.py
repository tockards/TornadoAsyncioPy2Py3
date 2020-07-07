"""Basic Example to demonstrate Python 2 and Python 3 compatibility with
tornado and asyncio.

This aims to show how you can use the tornado ioloop to run both
tornado coroutines and asyncio coroutines
"""

import future
from future.standard_library import install_aliases
install_aliases()

from tornado.ioloop import IOLoop
from compat import BasicExampleClass

if future.utils.PY2:
    io_loop = IOLoop()
else:
    from tornado.platform.asyncio import AsyncIOMainLoop
    io_loop = AsyncIOMainLoop()

example = BasicExampleClass(1)

io_loop.add_callback(example.show_version)
io_loop.start()