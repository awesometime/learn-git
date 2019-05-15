# python3.5 以前通过生成器实现协程
# python3.5 为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协程

"""1 协程是单线程模式"""
import threading
import asyncio


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(3)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# Hello world! (<_MainThread(MainThread, started 37128)>)
# Hello world! (<_MainThread(MainThread, started 37128)>)
# Hello again! (<_MainThread(MainThread, started 37128)>)
# Hello again! (<_MainThread(MainThread, started 37128)>)



# --------------------
# async def downloader(url):
#     return "bobby"
import types


@types.coroutine
def downloader(url):
    yield "bobby"


async def download_url(url):
    # dosomethings
    html = await downloader(url)  # await == yield from
    return html


if __name__ == "__main__":
    coro = download_url("http://www.imooc.com")
    # next(None)
    coro.send(None)
