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

### 3 Go内存分配

- [译文：Go 内存分配器可视化指南](https://www.linuxzen.com/go-memory-allocator-visual-guide.html)

  [fanqiang  |A visual guide to Go Memory Allocator from scratch (Golang)](https://blog.learngoprogramming.com/a-visual-guide-to-golang-memory-allocator-from-ground-up-e132258453ed)

- [图解 Golang的内存分配](https://mp.weixin.qq.com/s/pbwCYFEESkILGIJVqnNaLA)

- [Go内存分配那些事，就这么简单！](https://mp.weixin.qq.com/s/3gGbJaeuvx4klqcv34hmmw)

- [GCTT 出品 | Go 语言的内存管理](https://mp.weixin.qq.com/s/Rm5kILm1EgDGisk-L0LDIg)

- [图解 Go语言内存分配](https://mp.weixin.qq.com/s/Hm8egXrdFr5c4-v--VFOtg)

- [图解 Go 内存分配器](https://mp.weixin.qq.com/s/3jmMexGYY4ww_urSZ36vVQ)

```
0 进程间通信方式
管道   命名管道FIFO
消息队列
共享内存
信号量
socket

# Go内存分配那些事，就这么简单！
1 计算机的存储体系
CPU寄存器
缓存Cache
内存
硬盘

2 虚拟内存

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
    
4 TCMalloc基本原理
page span ThreadCache CentralCache PageHeap

5 Go内存管理 内存分配 垃圾回收 内存释放
逃逸分析和垃圾回收
```
### 4 垃圾回收

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
