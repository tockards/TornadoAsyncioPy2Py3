"""Simple example to demonstrate how a async def coroutine
can be added/used with tornado.ioloop.PeriodicCallback

It works out of the box as the PeriodicCallback requires a Callable.

"""
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado import gen
from tornado.ioloop import PeriodicCallback
import asyncio
import tornado

@gen.coroutine
def hello_delay(wait=1):
    print("Hello...")
    yield gen.sleep(wait)
    print("...World")

async def hello_aiodelay(wait=1):
    print("Hello ...")
    await asyncio.sleep(wait)
    print("...World")


async def hello_tornadoaiodelay(wait=1):
    print("Hello ...")
    await asyncio.sleep(wait)
    print("...World")

async def stop_at(runtime=10):
    io_loop =

if __name__ == '__main__':
    io_loop = AsyncIOMainLoop()
    pc = PeriodicCallback(hello_delay, 3*1000)
    aiopc = PeriodicCallback(hello_aiodelay, 4*1000)
    pc = PeriodicCallback(hello_delay, 3 * 1000)


    aiopc.start()
    pc.start()
    io_loop.start()