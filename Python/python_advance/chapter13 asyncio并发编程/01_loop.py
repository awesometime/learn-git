# 事件循环+回调（协程驱动）+epoll(IO多路复用)
# asyncio是python用于解决异步io编程的一整套解决方案
# tornado、gevent、twisted（scrapy， django channels）
# django+flask(uwsgi, gunicorn+nginx)本身不提供web服务器也就是不完成socket编码
# torando(实现web服务器)
# tornado可以直接部署， nginx+tornado


"""
# 使用asyncio
import asyncio
import time
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)   # 这个sleep是异步的 不能用time.sleep
    print("end get url")

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    #loop.run_until_complete(get_html("http://www.imooc.com"))
    print(time.time()-start_time)
"""

# 获取协程的返回值
import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "bobby"


def callback(future):
    print("send email to bobby")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 方法一 ensure_future
    # get_future = asyncio.ensure_future(get_html("http://www.imooc.com"))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    # 方法二 create_task
    task = loop.create_task(get_html("http://www.imooc.com"))
    task.add_done_callback(callback)  # callback的参数就是task
    loop.run_until_complete(task)
    print(task.result())

# -------------------
import asyncio
import time
from functools import partial  # 给callback传参数


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "bobby"


def callback(url, future):  # url只能是第一个参数
    print(url)
    print("send email to bobby")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html("http://www.imooc.com"))
    # callback有参数时  用partial
    task.add_done_callback(partial(callback, "http://www.imooc.com"))
    loop.run_until_complete(task)
    print(task.result())

# ------------------------------
# asyncio.wait 和 asyncio.gather
import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10)]
    # *tasks将list解析成参数
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(time.time()-start_time)

    # gather和wait的区别
    # gather更加high-level
    group1 = [get_html("http://projectsedu.com") for i in range(2)]
    group2 = [get_html("http://www.imooc.com") for i in range(2)]
    # loop.run_until_complete(asyncio.gather(*group1, *group2))
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    group2.cancel()
    loop.run_until_complete(asyncio.gather(group1, group2))
    print(time.time() - start_time)
