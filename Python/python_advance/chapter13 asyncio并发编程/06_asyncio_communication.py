# asyncio同步和通信communication
# 1
# 在多少线程中考虑安全性，需要加锁，在协程中是不需要的
import asyncio
 
total = 0
 
 
async def add():
    global total
    for _ in range(1000000):
        total += 1
 
 
async def desc():
    global total, lock
    for _ in range(1000000):
        total -= 1
 
 
if __name__ == '__main__':
    tasks = [add(), desc()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(total)
    
# 2
#在有些情况在对协程中我们还是需要类似锁的机制

#parse_stuff和use_stuff有共同调用的代码
 
#get_stuff parse_stuff去请求的时候 如果get_stuff也去请求， 会触发网站的反爬虫机制.
 
#这就需要我们像上诉代码那样加lock



#
#get_stuff 和 use_stuff  中都调用了parse_stuff我们想在get_stuff中只请求一次，下次用缓存，所以要用到锁


import asyncio
import aiohttp
from asyncio import Lock
 
cache = {}
lock = Lock()
 
 
async def get_stuff(url):
    async with lock:  # 等价于 with await lock:   还有async for 。。。类似的用法
        # 这里可以使用async with 是因为 Lock中有__await__ 和 __aenter__两个魔法方法
        # 和线程一样， 这里也可以用 await lock.acquire() 并在结束时 lock.release
        if url in cache:
            return cache[url]
        print("第一次请求")
        stuff =  aiohttp.request('GET', url)
 
        cache[url] = stuff
        return stuff
 
 
async def parse_stuff(url):
    stuff = await get_stuff(url)
    print('parse_stuff',stuff)
    # do some parse
 
 
async def use_stuff(url):
    stuff = await get_stuff(url)
    print('use_stuff',stuff)
 
    # use stuff to do something interesting
 
 
if __name__ == '__main__':
    tasks = [parse_stuff('baidu'), use_stuff('baidu')]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))




# 3  
#asyncio 通信 queue

#协程是单线程的，所以协程中完全可以使用全局变量实现queue来相互通信，但是如果想要 在queue中定义存放有限的最大数目。 我们需要使用 :

#put 和get 的前面都要加 await 

from asyncio import Queue
 
queue = Queue(maxsize=3) 
 
await queue.get()
 
await queue.put()
