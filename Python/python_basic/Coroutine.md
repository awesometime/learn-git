协程，又称作Coroutine。
从字面上来理解，即协同运行的例程，它是比是线程（thread）更细量级的用户态线程，特点是允许用户的主动调用和主动退出，
挂起当前的例程然后返回值或去执行其他任务，接着返回原来停下的点继续执行。

做到这样主要因为
python有yield语句
操作系统（OS）具有getcontext和swapcontext特性，通过系统调用，我们可以把上下文和状态保存起来，切换到其他的上下文，
这些特性为coroutine的实现提供了底层的基础。










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
上面这个例子是典型的生产者－消费者问题，我们用协程的方式来实现它。首先从主程序中开始看，第一句c = consumer()，因为consumer函数中存在yield语句，python会把它当成一个generator（生成器，注意：生成器和协程的概念区别很大，千万别混淆了两者），因此在运行这条语句后，python并不会像执行函数一样，而是返回了一个generator object。

再看第二条语句c.send(None)，这条语句的作用是将consumer（即变量c，它是一个generator）中的语句推进到第一个yield语句出现的位置，那么在例子中，consumer中的status = True和while True:都已经被执行了，程序停留在n = yield status的位置（注意：此时这条语句还没有被执行），上面说的send(None)语句十分重要，如果漏写这一句，那么程序直接报错，这个send()方法看上去似乎挺神奇，等下再讲它的作用。

下面第三句p = producer(c)，这里则像上面一样定义了producer的生成器，注意的是这里我们传入了消费者的生成器，来让producer跟consumer通信。

第四句for status in p:，这条语句会循环地运行producer和获取它yield回来的状态。

好了，进入正题，现在我们要让生产者发送1,2,3,4,5给消费者，消费者接受数字，返回状态给生产者，而我们的消费者只需要3,4,5就行了，当数字等于3时，会返回一个错误的状态。最终我们需要由主程序来监控生产者－消费者的过程状态，调度结束程序。

现在程序流进入了producer里面，我们直接看yield consumer.send(n)，生产者调用了消费者的send()方法，把n发送给consumer（即c），在consumer中的n = yield status，n拿到的是消费者发送的数字，同时，consumer用yield的方式把状态（status）返回给消费者，注意：这时producer（即消费者）的consumer.send()调用返回的就是consumer中yield的status！消费者马上将status返回给调度它的主程序，主程序获取状态，判断是否错误，若错误，则终止循环，结束程序。上面看起来有点绕，其实这里面generator.send(n)的作用是：把n发送generator(生成器)中yield的赋值语句中，同时返回generator中yield的变量（结果）。


于是程序便一直运作，直至consumer中获取的n的值变为3！此时consumer把status变为False，最后返回到主程序，主程序中断循环，程序结束。
 ```
