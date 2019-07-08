```
Go Runtime 
调度
内存
垃圾回收
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
### 2 Go内存分配

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
