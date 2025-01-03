#### 操作系统from清华大学向勇，陈渝 笔记（一）绪论

```
https://blog.csdn.net/github_36487770/article/details/54924928

https://www.bilibili.com/video/av6538245/?p=15
```

#### b站王道考研

[计算机操作系统书 目录结构](https://github.com/SSHeRun/CS-Xmind-Note/tree/master/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F)

#### 深入分析Linux内核源码 知识结构
```
前言

第一章 走进linux
      1.1 GNU与Linux的成长
      1.2 Linux的开发模式和运作机制
      1.3 走进Linux内核
          1.3.1 Linux内核的特征
          1.3.2 Linux内核版本的变化
      1.4 分析Linux内核的意义
          1.4.1 开发适合自己的操作系统
          1.4.2 开发高水平软件
          1.4.3 有助于计算机科学的教学和科研
      1.5 Linux内核结构
          1.5.1  Linux内核在整个操系统中的位置
          1.5.2 Linux内核的作用
          1.5.3 Linux内核的抽象结构
      1.6 Linux内核源代码
          1.6.1 多版本的内核源代码
          1.6.2  Linux内核源代码的结构 
          1.6.3 从何处开始阅读源代码
      1.7 Linux内核源代码分析工具
          1.7.1 Linux超文本交叉代码检索工具 
          1.7.2 Windows平台下的源代码阅读工具Source Insight

第二章 Linux运行的硬件基础
      2.1  i386的寄存器 
           2.1.1通用寄存器
           2.1.2段寄存器       
           2.1.3状态和控制寄存器
           2.1.4 系统地址寄存器
           2.1.5 调试寄存器和测试寄存器
      2.2 内存地址
      2.3 段机制和描述符
          2.3.1 段机制
          2.3.2  描述符的概念
          2.3.3系统段描述符
          2.3.4 描述符表
          2.3.5 选择符与描述符表寄存器
          2.3.6 描述符投影寄存器
          2.3.7 Linux中的段
      2.4 分页机制
          2.4.1 分页机构
          2.4.2页面高速缓存
      2.5 Linux中的分页机制  
          2.5.1 与页相关的数据结构及宏的定义
          2.5.2 对页目录及页表的处理
      2.6 Linux中的汇编语言
          2.6.1 AT&T与Intel汇编语言的比较
          2.6.2 AT&T汇编语言的相关知识
          2.6.3 Gcc嵌入式汇编
          2.6.4 Intel386汇编指令摘要
 
第三章 中断机制
      3.1 中断基本知识
          3.1.1 中断向量
          3.1.2 外设可屏蔽中断
          3.1.3 异常及非屏蔽中断
          3.1.4 中断描述符表
          3.1.5 相关汇编指令
      3.2中断描述符表的初始化
          3.2.1 外部中断向量的设置
          3.2.2 中断描述符表IDT的预初始化
          3.2.3 中断向量表的最终初始化
      3.3异常处理
          3.3.1 在内核栈中保存寄存器的值
          3.3.2 中断请求队列的初始化
          3.3.3中断请求队列的数据结构
      3.4 中断处理
          3.4.1中断和异常处理的硬件处理
          3.4.2 Linux对异常和中断的处理
          3.4.3 与堆栈有关的常量、数据结构及宏
          3.4.4 中断处理程序的执行
          3.4.5 从中断返回
      3.5中断的后半部分处理机制
          3.5.1 为什么把中断分为两部分来处理
          3.5.2 实现机制
          3.5.3数据结构的定义
          3.5.4 软中断、bh及tasklet的初始化
          3.5.5后半部分的执行
          3.5.6 把bh移植到tasklet
 
第四章 进程描述
      4.1 进程和程序（Process and Program）
      4.2 Linux中的进程概述
      4.3 task_struct结构描述
      4.4 task_struct结构在内存中的存放
          4.4.1 进程内核栈
          4.4.2 当前进程（current宏）
      4.5 进程组织的方式
          4.5.1哈希表
          4.5.2双向循环链表
          4.5.3 运行队列
          4.5.4 等待队列
      4.6 内核线程
      4.7 进程的权能
      4.8 内核同步
          4.8.1信号量
          4.8.2原子操作
          4.8.3 自旋锁、读写自旋锁和大读者自旋锁
      4.9 本章小节
 
第五章 进程调度
      5.1 Linux时间系统
          5.1.1 时钟硬件
          5.1.2 时钟运作机制
          5.1.3  Linux时间基准
          5.1.4 Linux的时间系统
      5.2 时钟中断
          5.2.1 时钟中断的产生
          5.2.2.Linux实现时钟中断的全过程
      5.3 Linux的调度程序－Schedule( )
          5.3.1 基本原理
          5.3.2 Linux进程调度时机
          5.3.3 进程调度的依据
          5.3.4 进程可运行程度的衡量
          5.3.5 进程调度的实现 
      5.4 进程切换
          5.4.1 硬件支持
          5.4.2 进程切换
          
第六章 Linux内存管理
      6.1 Linux的内存管理概述
          6.1.1 Linux虚拟内存的实现结构
          6.1.2 内核空间和用户空间
          6.1.3 虚拟内存实现机制间的关系
      6.2 Linux内存管理的初始化
          6.2.1 启用分页机制
          6.2.2  物理内存的探测
          6.2.3 物理内存的描述
          6.2.4 页面管理机制的初步建立
          6.2.5页表的建立
          6.2.6内存管理区
      6.3 内存的分配和回收
          6.3.1 伙伴算法
          6.3.2 物理页面的分配和释放
          6.3.3 Slab分配机制
      6.4 地址映射机制
          6.4.1 描述虚拟空间的数据结构
          6.4.2 进程的虚拟空间
          6.4.3 内存映射
      6.5 请页机制
          6.5.1  页故障的产生
          6.5.2 页错误的定位
          6.5.3 进程地址空间中的缺页异常处理
          6.5.4 请求调页
          6.5.5 写时复制
      6.6 交换机制
          6.6.1 交换的基本原理
          6.6.2 页面交换守护进程kswapd
          6.6.3 交换空间的数据结构
          6.6.4 交换空间的应用
      6.7 缓存和刷新机制
          6.7.1 Linux使用的缓存
          6.7.2 缓冲区高速缓存
          6.7.3 翻译后援存储器(TLB)
          6.7.4 刷新机制
      6.8 进程的创建和执行
          6.8.1 进程的创建
          6.8.2 程序执行
          6.8.3 执行函数
 
第七章 进程间通信
      7.1 管道
          7.1.1 Linux管道的实现机制
          7.1.2 管道的应用
          7.1.3 命名管道(FIFO)
      7.2  信号(signal)
          7.2.1 信号种类
          7.2.2 信号掩码
          7.2.3 系统调用
          7.2.4 典型系统调用的实现
          7.2.5 进程与信号的关系
          7.2.6 信号举例
      7.3 System V 的IPC机制
          7.3.1 信号量
          7.3.2 消息队列
          7.3.3 共享内存

第八章 虚拟文件系统
      8.1  概述
      8.2 VFS中的数据结构
          8.2.1 超级块
          8.2.2 VFS的索引节点
          8.2.3 目录项对象
          8.2.4 与进程相关的文件结构
          8.2.5 主要数据结构间的关系
          8.2.6 有关操作的数据结构
      8.3 高速缓存
          8.3.1 块高速缓存
          8.3.2 索引节点高速缓存
          8.3.3 目录高速缓存
      8.4 文件系统的注册、安装与拆卸
          8.4.1 文件系统的注册
          8.4.2  文件系统的安装
          8.4.3  文件系统的卸载
      8.5 限额机制
      8.6 具体文件系统举例
          8.6.1 管道文件系统pipefs
          8.6.2 磁盘文件系统BFS
      8.7 文件系统的系统调用
          8.7.1  open 系统调用
          8.7.2  read 系统调用
          8.7.3  fcntl 系统调用
      8.8 Linux2.4文件系统的移植问题 
 
第九章 Ext2文件系统
      9.1 基本概念
      9.2 Ext2的磁盘布局和数据结构
          9.2.1 Ext2的磁盘布局
          9.2.2 Ext2的超级块
          9.2.3 Ext2的索引节点
          9.2.4 组描述符
          9.2.5 位图
          9.2.6 索引节点表及实例分析
          9.2.7 Ext2的目录项及文件的定位
      9.3 文件的访问权限和安全
      9.4 链接文件
      9.5 分配策略
          9.5.1 数据块寻址
          9.5.2 文件的洞
          9.5.3 分配一个数据块
          
第十章 模块机制
      10.1 概述
          10.1.1 什么是模块
          10.1.2 为什么要使用模块?
      10.2 实现机制
          10.2.1 数据结构
          10.2.2 实现机制的分析
      10.3 模块的装入和卸载
          10.3.1 实现机制
          10.3.2 如何插入和卸载模块
      10.4 内核版本
          10.4.1 内核版本与模块版本的兼容性
          10.4.2 从版本2.0到2.2内核API的变化
          10.4.3 把内核2.2移植到内核2.4
      10.5 编写内核模块
          10.5.1 简单内核模块的编写
          10.5.2 内核模块的Makefiles文件
          10.5.3  内核模块的多个文件
 
第十一章  设备驱动程序
      11.1 概述
          11.1.1 I/O软件
          11.1.2 设备驱动程序
      11.2 设备驱动基础
          11.2.1 I/O端口
          11.2.2 I/O接口及设备控制器
          11.2.3 设备文件
          11.2.4 VFS对设备文件的处理
          11.2.5 中断处理
          11.2.6 驱动DMA工作
          11.2.7 I/O 空间的映射
          11.2.8 设备驱动程序框架
      11.3 块设备驱动程序
          11.3.1 块设备驱动程序的注册
          11.3.2 块设备基于缓冲区的数据交换
          11.3.3 块设备驱动程序的几个函数
          11.3.4 RAM 盘驱动程序的实现
          11.3.5 硬盘驱动程序的实现
      11.4 字符设备驱动程序
          11.4.1 简单字符设备驱动程序
          11.4.2 字符设备驱动程序的注册
          11.4.3 一个字符设备驱动程序的实例
          11.4.4 驱动程序的编译与装载

第十二章 网络
      12.1 概述 
      12.2 网络协议
          12.2.1 网络参考模型
          12.2.2 TCP/IP 协议工作原理及数据流
          12.2.3 Internet 协议
          12.2.4 TCP协议 
      12.3 套接字(socket)
          12.3.1 套接字在网络中的地位和作用
          12.3.2 套接字接口的种类
          12.3.3 套接字的工作原理
          12.3.4 socket 的通信过程
          12.3.5 socket为用户提供的系统调用
      12.4 套接字缓冲区(sk_buff)
          12.4.1 套接字缓冲区的特点
          12.4.2 套接字缓冲区操作基本原理
          12.4.3  sk_buff数据结构的核心内容
          12.4.4 套接字缓冲区提供的函数
          12.4.5 套接字缓冲区的上层支持例程
      12.5 网络设备接口
          12.5.1 基本结构 
          12.5.2 命名规则
          12.5.3 设备注册
          12.5.4 网络设备数据结构
          12.5.5 支持函数
          
第十三章 启动系统
        13.1 初始化流程     
            13.1.1 系统加电或复位
            13.1.2 BIOS启动
            13.1.3 Boot Loader
            13.1.4 操作系统的初始化
        13.2 初始化的任务
            13.2.1 处理器对初始化的影响
            13.2.2 其他硬件设备对处理器的影响
        13.3 Linux 的Boot Loarder
            13.3.1 软盘的结构
            13.3.2 硬盘的结构
            13.3.3 Boot Loader
            13.3.4 LILO
            13.3.5 LILO的运行分析
        13.4 进入操作系统
            13.4.1 Setup.S
            13.4.2 Head.S
        13.5 main.c中的初始化
        13.6 建立init进程
            13.6.1 init进程的建立
            13.6.2 启动所需的Shell脚本文件

附录：
1     Linux 2.4内核API
2.1   驱动程序的基本函数
2.2   双向循环链表的操作
2.3   基本C库函数
2.4   Linux内存管理中Slab缓冲区
2.5   Linux中的VFS
2.6   Linux的连网
2.7   网络设备支持
2.8   模块支持
2.9   硬件接口
2.10  块设备
2.11  USB 设备
2  参考文献
```
