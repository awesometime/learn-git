协程，又称作Coroutine。

从字面上来理解，即协同运行的例程，它是比是线程（thread）更细量级的用户态线程，特点是允许用户的主动调用和

主动退出，挂起当前的例程然后返回值或去执行其他任务，接着返回原来停下的点继续执行。

做到这样主要因为

1) python有yield语句

2) 操作系统（OS）具有getcontext和swapcontext特性，通过系统调用，我们可以把上下文和状态保存起来，切换到其

   他的上下文，这些特性为coroutine的实现提供了底层的基础。


> 普通函数

```python3
def consumer():           # 只能迭代一次
    print('good')
    return 2

b = consumer()            # 实例化方法时会执行print('good')
print(b)
# good
# 2
```


> yield 函数

```python3
def consumer():           # 只能迭代一次
    print('good')   
    yield 5

a = consumer()            # 实例化方法时不会执行print('good')
print(a)


# <generator object fun at 0x0000000002433BF8>
# a = consumer()，因为consumer函数中存在yield语句，python会把它当成一个generator（生成器），
# 因此在运行这条语句后，python并不会像执行函数一样全部执行完返回一个值，而是返回了一个generator object
# 想要启动函数consumer需要给他发送一个类似驱动指令的东西如  a.send(None)   a.__next__()   next(a)
# 去激活它
```

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
        
        yield consumer.send(n)  # 让生产者发送1,2,3,4,5给消费者
        
        # generator.send(n)的作用是：把n发送到consumer()的yield赋值语句中，同时返回consumer中yield的变量（status）。
        
        n -= 1


if __name__ == '__main__':
    c = consumer()  # 有yield的话实例化时候不会执行到函数内
    c.send(None)  # 通过send(None)或__next__()初始化到第一个值的位置
    
    # c.send(None)，这条语句的作用是将consumer（即变量c，它是一个generator）中的语句推进到第一个
    # yield语句出现的位置，那么在例子中，consumer中的status = True和while
    # True: 都已经被执行了，程序停留在n = yield status的位置（注意：此时这条语句还没有被执行）
    
    p = producer(c)  # 有yield的话实例化时候不会执行到函数内
    for status in p:  # for in 应该是底层调用了__next__()初始化到第一个值的位置.然后依次遍历
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
而我们的消费者只需要3,4,5就行了，
当数字等于3时，会返回一个错误的状态。最终我们需要由主程序来监控生产者－消费者的过程状态，
调度结束程序。

现在程序流进入了producer里面，我们直接看yield consumer.send(n)，生产者调用了消费者的
send()方法，把n发送给consumer（即c），在consumer中的n = yield status，n拿到的是消费者发送的数字，
同时，consumer用yield的方式把状态（status）返回给消费者，注意：
这时producer（即消费者）的consumer.send()调用返回的就是consumer中yield的status！
消费者马上将status返回给调度它的主程序，
主程序获取状态，判断是否错误，若错误，则终止循环，结束程序。上面看起来有点绕，其实这里面
generator.send(n)的作用是：把n发送
generator(生成器)中yield的赋值语句中，同时返回generator中yield的变量（结果）。

于是程序便一直运作，直至consumer中获取的n的值变为3！此时consumer把status变为False，
最后返回到主程序，主程序中断循环，程序结束。
```


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
            time.sleep(.1)
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
            await ask_for_potato()
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
    res = loop.run_until_complete(asyncio.wait([buy_potatos(), buy_tomatos()]))
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
async def function():
    await asyncio.sleep(1)
```


``` 
Python 3.4 新增asyncio库 刚开始使用yield from 
@types.coroutine 
def function():
    yield from
```

完成异步的代码不一定要用async/await，使用了async/await的代码也不一定能做到异步，

async/await是协程的语法糖，使协程之间的调用变得更加清晰，使用async修饰的函数调用时会返回

一个协程对象，await只能放在async修饰的函数里面使用，await后面必须要跟着一个协程对象或Awaitable，

await的目的是等待协程控制流的返回，而实现暂停并挂起函数的操作是yield。

> 再来一例

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
loop.run_until_complete(print_sum(1, 2))
loop.close()


# Compute 1 + 2 ...
# 1 + 2 = 3
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
