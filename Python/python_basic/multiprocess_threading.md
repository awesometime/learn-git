[Python多进程与多线程](https://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247484084&idx=1&sn=573989b9526aef01a3d515ab09afe86a&chksm=a73c628c904beb9a39adef9b95a1ce6560245b7f4e2a39207a55abc1a293935be203a35bcb13&mpshare=1&scene=1&srcid=&pass_ticket=0QnHRl6v1Xkew4C5DrpSerNBri6BPOinWKKfydIySHIIQ%2BKJhsjSdnkU2wZYGdie#rd)

[看了廖雪峰自己总结的](https://github.com/awesometime/learn-git/blob/master/Python/python_basic/Basic_knowledge.md#12-python3---%E5%A4%9A%E8%BF%9B%E7%A8%8B-multiprocessing----%E5%A4%9A%E7%BA%BF%E7%A8%8B-threading-----%E5%8F%82%E8%80%83%E5%BB%96%E9%9B%AA%E5%B3%B0)

Python的线程是真正的Posix Thread，而不是模拟出来的线程  怎么理解

> Python的多进程编程与multiprocess模块

join()方法就是为了让母进程阻塞，等待子进程都完成后

> 利用multiprocess模块的Pool类创建多进程

下面介绍一下multiprocessing 模块下的Pool类的几个方法：

1.apply_async

函数原型：apply_async(func[, args=()[, kwds={}[, callback=None]]])

其作用是向进程池提交需要执行的函数及参数， 各个进程采用非阻塞（异步）的调用方式，即每个子进程只管运行自己的，不管其它进程是否已经完成。

2.map()

函数原型：map(func, iterable[, chunksize=None])

Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到结果返回。 注意：虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。

3.map_async()

函数原型：map_async(func, iterable[, chunksize[, callback]])
与map用法一致，但是它是非阻塞的。其有关事项见apply_async。

4.close()

关闭进程池（pool），使其不在接受新的任务。

5. terminate()

结束工作进程，不在处理未处理的任务。

6.join()

主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。

> python解释器中GIL(全局解释器锁)   

> 作用就是保证同一时刻只有一个**线程**可以执行代码

python解释器中存在GIL(全局解释器锁), 它的作用就是保证同一时刻只有一个`线程`可以执行代码。由于GIL的存在，很多人认为

python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程。

然而这并意味着python多线程编程没有意义哦，请继续阅读下文。

> 恩
>> 恩
>>> 恩
