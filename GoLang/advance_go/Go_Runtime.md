go编译器、go runtime、go解释器 

[本文讲Go Runtime](https://github.com/ardanlabs/gotraining/blob/master/reading/README.md#runtimev)
```
Go Runtime主要干什么  https://www.kancloud.cn/kancloud/the-way-to-go/72443


并发调度 Go scheduler
内存分配 Go Memory Allocator
垃圾回收 Go Garbage collection
逃逸分析 Escape Analysis and Inlining  out of memory
栈处理、goroutine、channel、切片（slice）、map 和反射（reflection）
```


### 1 Go程序运行

- [Go程序是怎样跑起来的](https://mp.weixin.qq.com/s/Rewl0DKnq6CY53m5D3G2qw)

```
目录
编译链接 编译原理

golang 程序启动过程
    检查运行平台的CPU，设置好程序运行需要相关标志。
    TLS的初始化。
    runtime.args、runtime.osinit、runtime.schedinit 三个方法做好程序运行需要的各种变量与调度器。
    runtime.newproc创建新的goroutine用于绑定用户写的main方法。
    runtime.mstart开始goroutine的调度。

go命令 go build install run
```

### 2 调度

[更多 goroutine](https://github.com/awesometime/learn-git/blob/master/GoLang/advance_go/Go_goroutine.md)

Go runtime-scheduler

- [Analysis of the Go runtime scheduler 论文](http://www1.cs.columbia.edu/~aho/cs6998/reports/12-12-11_DeshpandeSponslerWeiss_GO.pdf)

- [goroutine调度器](https://tonybai.com/2017/06/23/an-intro-about-goroutine-scheduler/)

系列

- [理解golang调度之一 ：操作系统调度](https://juejin.im/post/5cdeb6cdf265da1bd605727f)

- [理解golang调度之二 ：Go调度器]()

- [理解golang调度之三 ：并发]()

系列

- [Go调度器系列（1）起源](http://lessisbetter.site/2019/03/10/golang-scheduler-1-history/)

- [Go调度器系列（2）宏观看调度器](http://lessisbetter.site/2019/03/26/golang-scheduler-2-macro-view/)

- [Go调度器系列（3）图解调度原理](http://lessisbetter.site/2019/04/04/golang-scheduler-3-principle-with-graph/)

- [Go调度器系列（4）源码阅读与探索](http://lessisbetter.site/2019/04/14/golang-scheduler-4-explore-source-code/)

其它

[弄懂goroutine调度原理](https://bingjian-zhu.github.io/2019/09/12/%E5%BC%84%E6%87%82goroutine%E8%B0%83%E5%BA%A6%E5%8E%9F%E7%90%86/)


### 3 Go内存分配

- [译文：Go 内存分配器可视化指南](https://www.linuxzen.com/go-memory-allocator-visual-guide.html)

  [fanqiang  |A visual guide to Go Memory Allocator from scratch (Golang)](https://blog.learngoprogramming.com/a-visual-guide-to-golang-memory-allocator-from-ground-up-e132258453ed)

- [3 图解 Golang的内存分配](https://mp.weixin.qq.com/s/pbwCYFEESkILGIJVqnNaLA)

[![data heap stack code](https://mmbiz.qpic.cn/mmbiz_png/W4ZicqIeQOOfQV3u8HKZuxEqEZcNdPuOiaxxPkfhjVoqq2DXc1nibqEFL0IlweHPyKic2gxHDXicibEtiaLcZFVwstKDg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mmbiz.qpic.cn/mmbiz_png/W4ZicqIeQOOfQV3u8HKZuxEqEZcNdPuOiaxxPkfhjVoqq2DXc1nibqEFL0IlweHPyKic2gxHDXicibEtiaLcZFVwstKDg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- [重点推荐 |Go内存分配那些事，就这么简单！](https://mp.weixin.qq.com/s/3gGbJaeuvx4klqcv34hmmw)

汉字 有深意 虚拟内存申请 释放 heap分配 回收
[![pic](https://mmbiz.qpic.cn/mmbiz_png/NjvicFU9uBtacnr4PU5ja25H9WlKgrgzy4ZLAdibJlINhSpzqr37GC2yVJefR80NsstMkdyfGic47kaaMQzUQHrKw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mmbiz.qpic.cn/mmbiz_png/NjvicFU9uBtacnr4PU5ja25H9WlKgrgzy4ZLAdibJlINhSpzqr37GC2yVJefR80NsstMkdyfGic47kaaMQzUQHrKw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

[![TCMalloc](https://mmbiz.qpic.cn/mmbiz_svg/lpHDr05YrIQUfyqx1PLwDx3c2qJh00ZK0XhEZJJ47QXiaopcLFHMjsJAM6RNymnbibVoFvibKqLh9lmK5NOnNNYEJR3PreYib4Zo/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mmbiz.qpic.cn/mmbiz_svg/lpHDr05YrIQUfyqx1PLwDx3c2qJh00ZK0XhEZJJ47QXiaopcLFHMjsJAM6RNymnbibVoFvibKqLh9lmK5NOnNNYEJR3PreYib4Zo/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)


- [GCTT 出品 | Go 语言的内存管理](https://mp.weixin.qq.com/s/Rm5kILm1EgDGisk-L0LDIg)

- [图解 Go语言内存分配](https://mp.weixin.qq.com/s/Hm8egXrdFr5c4-v--VFOtg)

- [图解 Go 内存分配器](https://mp.weixin.qq.com/s/3jmMexGYY4ww_urSZ36vVQ)

> 进程间通信方式
```
管道pipe
命名管道FIFO
消息队列Queue
共享内存
信号量 semphere
信号singal
socket
文件
```

> 3 图解 Golang的内存分配
```
程序的内存分配
数据段     全局变量
栈         局部变量      操作系统分配和管理          栈在高地址，从高地址向低地址增长
**堆       动态分配      程序员自己分配和释放        堆在低地址，从低地址向高地址增长
代码段   二进制代码

Go的内存分配核心思想
内置运行时的编程语言通常会抛弃传统的内存分配方式，改为自己管理。
优点
这样可以完成类似预分配、内存池等操作，以避开系统调用带来的性能问题，防止每次分配内存都需要系统调用。


```


> Go内存分配那些事，就这么简单！我是大彬  Go语言充电站
```
1 计算机的存储体系
CPU寄存器
缓存Cache
内存
硬盘

2 虚拟内存
https://zhenbianshu.github.io/2018/11/understand_virtual_memory.html
概念 
页表  换入换出swap in/out   缺页异常 
cpu寄存器  缓存  物理内存   磁盘 
虚拟内存 物理内存   磁盘




3 内存管理 内存碎片
数据段     全局变量
栈         局部变量      操作系统分配和管理          栈在高地址，从高地址向低地址增长
**堆       动态分配      程序员自己分配和释放        堆在低地址，从低地址向高地址增长
代码段   二进制代码

当我们说内存管理的时候，主要是指堆内存的管理，因为栈的内存管理不需要程序去操心，操作系统分配和管理 

栈和堆相比有这么几个好处：
    栈的内存管理简单，分配比堆上快。
    栈的内存不需要回收，而堆需要，无论是主动free，还是被动的垃圾回收，这都需要花费额外的CPU。
    栈上的内存有更好的局部性，堆上内存访问就不那么友好了，CPU访问的2块数据可能在不同的页上，CPU访问数据的时间可能就上去了
    
4 TCMalloc内存分配管理 的基本原理
Linux里的内存管理库，比如glibc的ptmalloc，FreeBSD的jemalloc，Google的tcmalloc
管理部件结构图
page span 
ThreadCache   CentralCache   PageHeap   虚拟内存   物理内存

追求更高内存管理效率
第一个层次
引入虚拟内存后，让内存的并发访问问题的粒度从多进程级别，降低到多线程级别。
第一个层次
为每个线程预分配一块缓存，线程申请小内存时，可以从缓存分配内存


5 Go自己的内存管理 内存分配 垃圾回收 内存释放
逃逸分析和垃圾回收
Go内存管理源自TCMalloc，但它比TCMalloc还多了2件东西：逃逸分析和垃圾回收
管理部件
page span
mCache    mCentral   mHeap  虚拟内存  物理内存
go/src/runtime/makesizeclass.go

内存结构图

```



### 4 Go垃圾回收

[Go垃圾回收 1：历史和原理 大彬Go语言充电站](http://lessisbetter.site/)

[垃圾回收(GC)浅谈 语言无关](https://juejin.im/post/5cf0ffa7f265da1ba56b052a)

[译 Golang 中的垃圾回收（一)](https://mp.weixin.qq.com/s/SI-_9id0XjDGA3fEGaVFiA)
```
非分代并发的三色标记和清扫回收器

1 Mark Setup - STW(Stop The World,延迟)
  开启写屏障(Write Barrier)
  回收器去检查并等待goroutine去做方法调用。方法调用确保了goroutines在安全的点停下来。
2 Marking - Concurrent
  一旦写屏障开启，回收器就会开始进入都标记阶段
  回收器第一件做的事情就是拿走25%的可用CPU给自己使用。collector使用Goroutines去进行回收工作，也就是它会从应用程序抢过来对应数量的P和M。这意味着，4个线程的go程序里，会有一个P被拿去处理回收工作。
  回收器会占用cpu资源
3 Mark Termination -STW
4 Sweeping - Concurrent

runtime中有一个配置选项叫做 GC Percentage


```

[10.8 垃圾回收和 SetFinalizer](https://www.kancloud.cn/kancloud/the-way-to-go/72518)



### 5 内存泄漏
