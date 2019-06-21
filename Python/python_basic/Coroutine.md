[awesometime/learn-git/python_advance/协程异步编程](https://github.com/awesometime/learn-git/blob/master/Python/python_advance/README.md)

[进程、线程、协程 比较（多角度对比)](https://blog.csdn.net/weixin_42767581/article/details/86030143)

[小灰 什么是协程](https://mp.weixin.qq.com/s/57IERpGIlvRwYCh6vSbMDA)

[A Curious Course on Coroutines and Concurrency](http://dabeaz.com/coroutines/): [PDF](http://dabeaz.com/coroutines/Coroutines.pdf)

[In practice, what are the main uses for the new “yield from” syntax in Python 3.3?
](https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-new-yield-from-syntax-in-python-3)

> 疑问  

**yield from 语句 如何实现 send 发消息**

### 1 谈谈Python协程技术的演进

[谈谈Python协程技术的演进](http://zhuanlan.51cto.com/art/201709/552465.htm#topx)

EventLoop与协程的发展史

就不同语言中面向并发设计的协程实现而言，Scala 与 Erlang 的 Actor 模型、Golang 中的 goroutine 都较 Python 更为成熟，

不同的协程使用通信来共享内存，优化了竞态、冲突、不一致性等问题。然而，根本的理念没有区别，都是在用户态通过**事件循环**

`驱动`实现调度。

生成器的进化

yield 关键字被加入到语法中，下一次从生成器中取值可以恢复到生成器上次 yield 执行的位置。

在 Python2.5 中生成器还加入了 send 方法，与 yield 搭配使用。

生成器不仅仅可以 yield 暂停到一个状态，还可以往它停止的位置通过 send 方法传入一个值改变其状态。

yield from 实现了在生成器内调用另外生成器的功能  在生成器中从其他生成器 yield 一个值，这样不同的**生成器之间可以互相通信**

每个协程都有独立的栈空间，即使它们是都工作在同一个线程中的

短暂的asynico.coroutine 与yield from

async/await

await 的行为类似 yield from，但是它们异步等待的对象并不一致，yield from 等待的是一个生成器对象，而await接收的是定义了__await__

方法的 awaitable 对象。

### Python3.5 协程原理


[可迭代、迭代器、生成器](https://juejin.im/post/5b3391a0518825748b56b42c#heading-4)

[yield from语法 引入协程](https://juejin.im/post/5b3af9fb51882507d4487144)

[Python3.5 协程原理](https://github.com/xitu/gold-miner/blob/master/TODO/how-the-heck-does-async-await-work-in-python-3-5.md)
```
https://juejin.im/post/5b3391a0518825748b56b42c

Iterable   __iter__
Iterator   __next__
Generator  yield

如何创建一个生成器，主要有如下两种方法

使用列表生成式

# 使用列表生成式，注意不是[]，而是()
L = (x * x for x in range(10))
print(isinstance(L, Generator))  # True
复制代码

实现yield的函数

# 实现了yield的函数
def mygen(n):
    now = 0
    while now < n:
        yield now
        now += 1

if __name__ == '__main__':
    gen = mygen(10)
    print(isinstance(gen, Generator))  # True
```
```
进程：
每个人（cpu）都领一套工具（环境，上下文）去干活，人多（核多）就可以做的更快。
一个cpu 一套环境就可以干活了

线程：
单线程 有一组 "计算 io 计算 io ..." 类似这样的任务 如果只有一个线程 碰到io耗时操作只能等io完成再去执行计算
多线程 的话就可以在一个线程执行io耗时任务的时候 另一个线程拿到上下文相关环境信息去执行计算 但是线程切换会消耗较多资源

协程：
一个线程内由用户的主动调用  省去线程切换消耗的资源




```








协程，又称作Coroutine。

从字面上来理解，即协同运行的例程，它是比是线程（thread）更细量级的用户态线程，特点是允许用户的主动调用和

主动退出，挂起当前的例程然后返回值或去执行其他任务，接着返回原来停下的点继续执行。

做到这样主要因为

1) python有yield语句

2) 操作系统（OS）具有getcontext和swapcontext特性，通过系统调用，我们可以把上下文和状态保存起来，切换到其

   他的上下文，这些特性为coroutine的实现提供了底层的基础。

# 第一部分

> 普通函数

```python3
def consumer():           
    print('good')
    return 2

b = consumer()            # 实例化方法时会执行print('good')
print(b)
# good
# 2
```


> yield 函数

```python3
def consumer():           
    print('good')   
    yield 5               # 只能迭代一次

a = consumer()            # 实例化方法时不会执行print('good')
print(a)


# <generator object fun at 0x0000000002433BF8>
```
a = consumer()，因为consumer函数中存在yield语句，python会把它当成一个generator（生成器），

因此在运行这条语句后，python并不会像执行函数一样全部执行完返回一个值，而是返回了一个generator object

想要启动函数consumer需要给他发送一个类似驱动指令的东西如  a.send(None)   a.__next__()   next(a)

去激活它

参考 (https://zhuanlan.zhihu.com/p/25228075)

> 生产者－消费者的协程

```python3
def consumer():
    status = True
    while True:
        nr = yield status
        # 1  nr = yield status = send("");
        # 2  yield status语句 = return status
        #    consumer().__next__()    consumer().send("") 的返回就是 status
        print("我拿到了{}!".format(nr))
        if nr == 3:
            status = False


def producer(consumer):
    n = 5
    while n > 0:
        # yield给主程序返回消费者的状态
        
        yield consumer.send(n)             # 让生产者发送1,2,3,4,5给消费者
        
        # generator.send(n)的作用是：把n发送到consumer()的yield赋值语句中，同时返回consumer中yield的变量（status）。
        
        n -= 1


if __name__ == '__main__':
    c = consumer()              # 有yield的话实例化时候不会执行到函数内
    c.send(None)                # 通过send(None)或__next__()初始化到第一个值的位置
    
    # c.send(None)，这条语句的作用是将consumer（即变量c，它是一个generator）中的语句推进到第一个
    # yield语句出现的位置，那么在例子中，consumer中的status = True和while True:
    # 都已经被执行了，程序停留在n = yield status的位置（【注意】：此时这条语句还没有被执行）
    # 可以理解为yield status 执行了 因为它相当于return status 但是n = yield status这个没执行
    # 这句执行需要send 发送过来东西
    
    p = producer(c)             # 有yield的话实例化时候不会执行到函数内
    for status in p:            # for in 应该是底层调用了__next__()初始化到第一个值的位置.然后依次遍历
        if status == False:
            print("我只要3,4,5就行啦")
            break
    print("程序结束")
 

# 我拿到了5!
# 我拿到了4!
# 我拿到了3!
# 我只要3,4,5就行啦
# 程序结束
```
 
```
上面这个例子是典型的生产者－消费者问题，我们用协程的方式来实现它。首先从主程序中开始看，
第一句c = consumer()，因为consumer函数中存在yield语句，python会把它当成一个generator
（生成器，注意：生成器和协程的概念区别很大，千万别混淆了两者），因此在运行这条语句后，
python并不会像执行函数一样，而是返回了一个generator object。

再看第二条语句c.send(None)，这条语句的作用是将consumer（即变量c，它是一个generator）
中的语句推进到第一个yield语句出现的位置，那么在例子中，consumer中的status = True和
while True:都已经被执行了，程序停留在n = yield status的位置（注意：此时这条语句还没
有被执行），上面说的send(None)语句十分重要，如果漏写这一句，那么程序直接报错，这个send()
方法看上去似乎挺神奇，等下再讲它的作用。

下面第三句p = producer(c)，这里则像上面一样定义了producer的生成器，注意的是这里我们
传入了消费者的生成器，来让producer跟consumer通信。

第四句for status in p:，这条语句会循环地运行producer和获取它yield回来的状态。

好了，进入正题，现在我们要让生产者发送1,2,3,4,5给消费者，消费者接受数字，返回状态给生产者，
而我们的消费者只需要3,4,5就行了，当数字等于3时，会返回一个错误的状态。最终我们需要由主程序
来监控生产者－消费者的过程状态，调度结束程序。

现在程序流进入了producer里面，我们直接看yield consumer.send(n)，生产者调用了消费者的
send()方法，把n发送给consumer（即c），在consumer中的n = yield status，n拿到的是消费者
发送的数字，同时，consumer用yield的方式把状态（status）返回给消费者，注意：这时producer
（即消费者）的consumer.send()调用返回的就是consumer中yield的status！消费者马上将status
返回给调度它的主程序，主程序获取状态，判断是否错误，若错误，则终止循环，结束程序。上面看起
来有点绕，其实这里面generator.send(n)的作用是：把n发送generator(生成器)中yield的赋值语
句中，同时返回generator中yield的变量（结果）。

于是程序便一直运作，直至consumer中获取的n的值变为3！此时consumer把status变为False，
最后返回到主程序，主程序中断循环，程序结束。
```

# 第二部分

> Python Async/Await入门指南

[Python Async/Await入门指南](https://www.cnblogs.com/dhcn/p/9032461.html)

[A Web Crawler With asyncio Coroutines](http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html)


看下Python中常见的几种函数形式：

1. 普通函数
```python3
def function():
    return 1
```
2. 生成器函数
```python3
def generator():
    yield 1
```
在3.5过后，我们可以使用async修饰将普通函数和生成器函数包装成异步函数和异步生成器。

3. 异步函数（即协程）
```python3
async def async_function():
    return 1

async def await_coroutine():
    result = await async_function()
    print(result)

def run(coroutine):
    # 生成器函数、协程/异步函数async_function 在正常返回退出时(遇到return语句返回时)会抛出一个StopIteration异常，
    # 而原来的返回值,会存放在StopIteration对象的value属性中，通过以下捕获可以获取协程真正的返回值
    try: 
        coroutine.send(None)
    except StopIteration as e:
        return e.value   

run(await_coroutine())

1
``` 

4. 异步生成器

> 先介绍同步生成器
```python3
import time
import asyncio
import random
class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos

all_potatos = Potato.make(5)

def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            time.sleep(.1)              # ==0 以后只能够死等，而且在上面例子中等多长时间都不会有结果（因为一切都是同步的）
        else:
            potato = all_potatos.pop()
            yield potato
            count += 1
            if count == num:
                break

def buy_potatos():
    bucket = []
    for p in take_potatos(50):
        bucket.append(p)

buy_potatos()
```

> 异步生成器
```python3
import time
import asyncio
import random
class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos


all_potatos = Potato.make(5)


async def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0: 
            await ask_for_potato()               # 
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break


async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))


async def buy_potatos():
    bucket = []
    async for p in take_potatos(50):
        bucket.append(p)
        print(f'Got potato {id(p)}...')


def main():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(buy_potatos())
    loop.close()
    

main()
```


```python3
import time
import asyncio
import random
class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos


all_potatos = Potato.make(2)


async def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break


async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 3)))


async def buy_potatos():
    global bucket
    async for p in take_potatos(10):
        bucket.append(p)
        print(f'Got potato {id(p)}...')


async def buy_tomatos():
    global bucket
    async for p in take_potatos(10):
        bucket.append(p)
        print(f'Got tomato {id(p)}...')


def main():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(asyncio.wait([buy_potatos(), buy_tomatos()]))
    loop.close()

bucket = []
main()
```


```
Python 3.5
import types

@types.coroutine
def function():


-------------
import asyncio

async def function():
    await asyncio.sleep(1)
    
异步推导表达式  async for p in ...
bucket = [p async for p in take_potatos(50)]

上下文管理器
async with lock:
    ...
```


``` 
Python 3.4 新增asyncio库 刚开始使用yield from 
import asyncio
@asyncio.coroutine
def function():
    yield from
    
with (yield from lock):
...
```

完成异步的代码不一定要用async/await，使用了async/await的代码也不一定能做到异步，

async/await是协程的语法糖，使协程之间的调用变得更加清晰，使用async修饰的函数调用时会返回

一个协程对象，await只能放在async修饰的函数里面使用，await后面必须要跟着一个协程对象或Awaitable，

await的目的是等待协程控制流的返回，而实现暂停并挂起函数的操作是yield。

asyncio是使用async/await语法开发的协程库，而不是有asyncio才能用async/await

> 再来一例

三个主要概念 EventLoop future对象 Task对象

```python3
import asyncio

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([print_sum(1, 2), print_sum(11, 12),print_sum(111, 112)]))
loop.close()


Compute 11 + 12 ...
Compute 111 + 112 ...
Compute 1 + 2 ...
11 + 12 = 23
111 + 112 = 223
1 + 2 = 3
```


```
当事件循环开始运行时，它会在Task中寻找coroutine来执行调度，因为事件循环注册了print_sum()，
因此print_sum()被调用，执行result = await compute(x, y)这条语句
（等同于result = yield from compute(x, y)），因为compute()自身就是一个coroutine，
因此print_sum()这个协程就会暂时被挂起，compute()被加入到事件循环中，程序流执行compute()
中的print语句，打印”Compute %s + %s …”，然后执行了await asyncio.sleep(1.0)，因为
asyncio.sleep()也是一个coroutine，接着compute()就会被挂起，等待计时器读秒，在这1秒的过程中，
事件循环会在队列中查询可以被调度的coroutine，而因为此前print_sum()与compute()都被挂起了，
因此事件循环会停下来等待协程的调度，当计时器读秒结束后，程序流便会返回到compute()中执行
return语句，结果会返回到print_sum()中的result中，最后打印result，事件队列中没有可以调度
的任务了，此时loop.close()把事件队列关闭，程序结束。
```

> asyncio 中 Future

```py
# https://juejin.im/post/5c13245ee51d455fa5451f33#heading-3
import asyncio

future = asyncio.Future()


async def coro1():
    print("wait 1 second")
    await asyncio.sleep(1)
    print("set_result")
    future.set_result('data')


async def coro2():
    result = await future
    print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([
    coro1()
    coro2()
]))
loop.close()
```
