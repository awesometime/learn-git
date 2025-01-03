# AdvancePython
慕课网课程-python高级编程和异步io并发编程

[Python高级编程和异步IO并发编程 学习笔记](https://www.cnblogs.com/crazymagic/category/1355733.html)

[Python高级编程和异步IO并发编程 目录](https://www.cnblogs.com/BuildtoWin/p/10290096.html)

```
第1章 课程简介
介绍如何配置系统的开发环境以及如何加入github私人仓库获取最新源码。

1-1 导学 试看
1-2 开发环境配置
1-3 资源获取方式
第2章 python中一切皆对象
本章节首先对比静态语言以及动态语言，然后介绍 python 中最底层也是面向对象最重要的几个概念-object、type和class之间的关系，以此来引出在python如何做到一切皆对象、随后列举python中的常见对象。

2-1 python中一切皆对象 试看
2-2 type、object和class之间的关系 试看
2-3 python中的内置类型
2-4 本章小结
第3章 魔法函数
本章将会介绍python语言简介语法背后的基石-魔法函数，会通过例子来演示魔法函数对python的影响、最后整体呈现python中的魔法函数来对python做一个概览。

3-1 什么是魔法函数
3-2 python数据模型对python的影响
3-3 python魔法函数一览
3-4 len函数的特殊性
3-5 本章小结
第4章 深入类和对象
本章节是python面向对象的进阶知识，通过本章的学习会掌握 python 鸭子类型以及鸭子类型对 python 的影响，随后讲解 python 中的抽象基类的运用、python 的 mro 属性查找算法和 super 函数、类变量和对象变量以及数据封装、本章节会讲解对象的自省机制能让大家对对象内部有更进一步的了解、最后是上下文管理协议...

4-1 鸭子类型和多态
4-2 抽象基类(abc模块) - 1
4-3 抽象基类(abc模块) - 2
4-4 isinstance和type的区别
4-5 类变量和实例变量
4-6 类和实例属性的查找顺序—mro查找
4-7 类方法、静态方法和实例方法
4-8 数据封装和私有属性
4-9 python对象的自省机制
4-10 super真的是调用父类吗？
4-11 mixin继承案例-django rest framework
4-12 python中的with语句
4-13 contextlib简化上下文管理器
4-14 本章小结
第5章 自定义序列类
本章节在讲解 python 的序列协议后进一步讲解 python 中序列的类型以及序列协议中的魔法函数，之后实现了自己的可以切片的序列、在本章中我们也会接触 bisect 和列表推导式、生成器表达式和字典推导式等，经过本章的学习之后大家会知道如何去定义可以像list一样使用方便的类以及明白 django 中的 queryset 的核心...

5-1 python中的序列分类
5-2 python中序列类型的abc继承关系
5-3 list中extend方法区别
5-4 实现可切片的对象
5-5 bisect维护已排序序列
5-6 什么时候我们不该使用列表
5-7 列表推导式、生成器表达式、字典推导式
5-8 本章小结
第6章 深入python的set和dict
因为 dict 的高性能，dict 在 python 内部被大量应用。本章节我们会首先通过例子演示dict 和 list 之间的性能差异，以及讲解 dict 高性能背后的原理，我们也将接触到散列表以及可散列类型，最后我们我们会知道 set 和 frozenset 的区别。...

6-1 dict的abc继承关系
6-2 dict的常用方法
6-3 dict的子类
6-4 set和frozenset
6-5 dict和set的实现原理
6-6 本章小结
第7章 对象引用、可变性和垃圾回收
本章节是偏理论的章节，却是我们进一步理解 pytho n以及排查各种隐含的 bug 最重要的章节，本章的对象引用、可变性和垃圾回收会让我们对 python 的变量本质有更进一步的加深，本章节会让我们在编码的过程中尽量避免各种坑以及出错后有排错的经验。...

7-1 python中的变量是什么
7-2 ==和is的区别
7-3 del语句和垃圾回收
7-4 一个经典的参数错误
7-5 本章小结
第8章 元类编程
元类在 python 高级工程师面试中会被经常问到、元类作为 python 中一个高级特性，熟练使用元类能不仅让我们写出更加优雅和可控性更好的代码还能进一步加深我们对python 的理解、本章节我们将会理解更多的 python 面向对象的高级特性比如property 以及属性描述符、__getattr__和__getattribute__等等，这些让我们可...

8-1 property动态属性
8-2 __getattr__、__getattribute__魔法函数
8-3 属性描述符和属性查找过程
8-4 __new__和__init__的区别
8-5 自定义元类
8-6 通过元类实现orm-1
8-7 通过元类实现orm-2
8-8 本章小结
第9章 迭代器和生成器
深刻理解生成器是理解协程的基础、迭代器和生成器作为 python 难以理解的功能，很多人对其区别以及使用都是模棱两可，本章节我们会全面理解迭代器协议以及生成器和迭代器之间的关系，我们会重点讲解生成器的原理，让我们更清楚我们在什么时候应该使用生成器，本章节我会通过几个例子加深大家对生成器的理解和使用。...

9-1 python中的迭代协议
9-2 什么是迭代器和可迭代对象
9-3 生成器函数的使用
9-4 python是如何实现生成器的
9-5 生成器在UserList中的应用
9-6 生成器如何读取大文件
9-7 本章小结
第10章 python socket编程
本章节我会从 http、socket、tcp 协议开始讲起，通过 socket 方式实现客户端和服务端让大家名明白聊天类软件的核心、要想深刻理解 web 编程、我们必须知道 socket 编程，本章节我们将通过多线程+ socket 的方式实现支持并发的服务端、最后通过 socket 模拟 http 的请求来实现为后续的异步 IO 打下并发的基...

10-1 弄懂 HTTP、Socket、TCP 这几个概念
10-2 socket 和 server 实现通信
10-3 socket 实现聊天和多用户连接
10-4 socket 模拟 http请求
10-5 本章小结
第11章 多线程、多进程和线程池编程
多线程、多进程编程一直是面试中被问到的高频问题，本章节我们将从 GIL 开始讲解多线程以及多进程的应用场景、之后详细的介绍多线程的编码、线程间通信以及线程的同步- Lock\Rlock\Condition，通过对 condition 的源码分析加深大家对条件变量的理解，接着通过线程池 ThreadPoolExecutor 的使用和源码分析加深大家对...

11-1 python 中的 GIL
11-2 多线程编程 - threading
11-3 线程间通信 - 共享变量和 Queue
11-4 线程同步 - Lock、RLock
11-5 线程同步 - condition 使用以及源码分析
11-6 线程同步 - Semaphore 使用以及源码分析
11-7 ThreadPoolExecutor线程池
11-8 ThreadPoolExecutor源码分析
11-9 多线程和多进程对比
11-10 multiprocessing 多进程编程
11-11 进程间通信 - Queue、Pipe，Manager
11-12 本章小结
第12章 协程和异步io
本章节是一个过渡章节，也是从生成器过渡到协程的最重要的章节，本章节我们将从阻塞和非阻塞等概念开始一直到引出多线程和多进程编程在并发编程中的不足、IO多路复用，然后我们会通过事件循环+回调的方式完成高并发的请求，之后我们会讲解回调之痛以及生成器进阶中的 send、close 和 yield from 等功能，最后通过这...

12-1 并发、并行、同步、异步、阻塞、非阻塞
12-2 IO 多路复用 (select、poll 和 epoll)
12-3 select+回调+事件循环获取html-1
12-4 select+回调+事件循环获取html-2
12-5 回调之痛
12-6 协程是什么
12-7 生成器进阶-send、close和throw方法
12-8 生成器进阶-yield from-1
12-9 生成器进阶-yield from-2
12-10 生成器实现协程
12-11 async和await
12-12 本章小节
第13章 asyncio并发编程
asyncio 作为 python 未来最有野心也是最有前景的模块，是我们学习 python 高并发编程的必学模块。有了12章的基础，我们直接使用 asyncio 来进行并发编程就会变得容易理解，我们从 asyncio 的基本功能开始讲解、如何将任务提交到asyncio、如何将 ThreadPoolExecutor 和 asyncio 集成，明白 asyncio 内部是如...

13-1 事件循环-1
13-2 事件循环-2
13-3 task取消和子协程调用原理
13-4 call_soon、call_at、call_later、call_soon_threadsafe
13-5 ThreadPollExecutor 和 asycio 完成阻塞 IO 请求
13-6 asyncio 模拟 http 请求
13-7 future 和 task
13-8 asyncio同步和通信
13-9 aiohttp实现高并发爬虫 - 1
13-10 aiohttp实现高并发爬虫 - 2
13-11 aiohttp实现高并发爬虫 - 3
13-12 本章小节
第14章 课程总结
本章节我们会对课程的内容做一个整体的总结，加深大家对所学知识点的整体理解。

14-1 课程总结
```
