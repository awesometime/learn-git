Go 是并发式语言    并发(concurrency)  goroutine channel

> 资料

https://medium.com/rungo 系列

https://medium.com/@thatisuday 系列

[GCTT 出品 | 在 Go 中实现并发性](https://mp.weixin.qq.com/s/cX9FTkBncjrwcN8y1EuGdQ) : [英文出处](https://medium.com/rungo/achieving-concurrency-in-go-3f84cbf870ca)

[Anatomy解剖 of Channels in Go - Concurrency in Go](https://medium.com/rungo/anatomy-of-channels-in-go-concurrency-in-go-1ec336086adb)

[Diving Deep Into The Golang Channels](https://codeburst.io/diving-deep-into-the-golang-channels-549fd4ed21a8)

> 代码模板

[GCTT 出品 | 图解 Go 并发编程 循序渐进 推荐先看](https://mbd.baidu.com/newspage/data/landingshare?context=%7B%22nid%22%3A%22news_10061718063488657719%22%2C%22sourceFrom%22%3A%22bjh%22%2C%22url_data%22%3A%22bjhauthor%22%7D)  : [英文出处 Learning Go’s Concurrency Through Illustrations](https://medium.com/@trevor4e/learning-gos-concurrency-through-illustrations-8c4aff603b3)

[Go Concurrency Patterns PPT  Rob Pike  Google](https://talks.golang.org/2012/concurrency.slide#1)

[Google I/O 2012 - Go Concurrency Patterns video](https://www.youtube.com/watch?v=f6kdp27TYZs)

[Google I/O 2013 - Advanced Go Concurrency Patterns video](https://www.youtube.com/watch?v=QDDwwePbDtw)

> 底层原理

[好文  Go语言通过Goroutine来支持并发编程，有关其原理可以看这篇Go并发机制](https://github.com/k2huang/blogpost/blob/master/golang/%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B/%E5%B9%B6%E5%8F%91%E6%9C%BA%E5%88%B6/Go%E5%B9%B6%E5%8F%91%E6%9C%BA%E5%88%B6.md)

[Go的CSP并发模型实现](https://www.cnblogs.com/sunsky303/p/9115530.html)

Go runtime scheduler

[Analysis of the Go runtime scheduler 论文](http://www1.cs.columbia.edu/~aho/cs6998/reports/12-12-11_DeshpandeSponslerWeiss_GO.pdf)

[goroutine调度器](https://tonybai.com/2017/06/23/an-intro-about-goroutine-scheduler/)

[理解golang调度三部曲: 操作系统调度 / Go 调度器 / 并发](https://juejin.im/post/5cdeb6cdf265da1bd605727f)

[python协程与golang协程的区别](https://segmentfault.com/a/1190000019127902?utm_campaign=studygolang.com&utm_medium=studygolang.com&utm_source=studygolang.com)

[Go vs CPython: Visual comparison of concurrency and parallelism options](https://labs.getninjas.com.br/go-vs-cpython-visual-comparison-of-concurrency-and-parallelism-d29a1ebec20a)

> 并发编程中锁

[并发编程中为什么需要锁](https://github.com/k2huang/blogpost/blob/master/golang/%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B/%E5%AE%9E%E7%94%A8%E6%95%99%E7%A8%8B/%E7%94%A8Go%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%E5%B9%B6%E5%8F%91%20-%201.%E9%94%81%E7%9A%84%E4%BD%9C%E7%94%A8.md)

> 其它

go 语言思维 价值观

[Go coding in go way](https://tonybai.com/2017/04/20/go-coding-in-go-way/?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)

[译文：Go 内存分配器可视化指南](https://www.linuxzen.com/go-memory-allocator-visual-guide.html)

#### 并发 https://mp.weixin.qq.com/s/nqoRLVYIZmzgBBTSiIqkZg 学习笔记


- 并发是指立即处理多个任务的能力。

我们可以想象一个人正在跑步。假如在他晨跑时，鞋带突然松了。于是他停下来，系一下鞋带，接下来继续跑。这个例子就是典型的并发。这个人能够一下搞定跑步和系鞋带两件事，即立即处理多个任务。

- 并行是指同时处理多个任务。       这听起来和并发差不多，但其实完全不同。

我们同样用这个跑步的例子来帮助理解。假如这个人在慢跑时，还在用他的 iPod 听着音乐。在这里，他是在跑步的同时听音乐，也就是同时处理多个任务。这称之为并行。

		       
[![concurrency parallelism](https://mmbiz.qpic.cn/mmbiz_png/UWba2ryLMqlGWzyzqqeohYZr3yic7yFBfxDxrSrcyNVA2p5oA1c0UAbpBicdXFOyh19PWA1icpcuIAs68NcRvbpqw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mmbiz.qpic.cn/mmbiz_png/UWba2ryLMqlGWzyzqqeohYZr3yic7yFBfxDxrSrcyNVA2p5oA1c0UAbpBicdXFOyh19PWA1icpcuIAs68NcRvbpqw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)		       
		       
		       
## Go 协程是什么？
			    
Go 协程是与其他函数或方法一起并发运行的函数或方法。Go 协程可以看作是轻量级线程。与线程相比，创建一个 Go 协程的成本很小。因此在 Go 应用中，常常会看到有数以千计的 Go 协程并发地运行。

什么是goroutine？ 它是一个独立执行的函数，由go语句启动。

它有自己的调用堆栈，可根据需要增长和缩小。

它很便宜。 拥有数千甚至数十万个goroutines是切实可行的。

这不是一个主题。

程序中可能只有一个线程有数千个goroutine。

相反，goroutines会根据需要动态多路复用到线程上，以保持所有goroutine运行。

但如果你认为它是一个非常便宜的线程，你就不会遥远。


|线程|	Goroutine|
|:-|:-|
|Os 线程由内核管理，并具有硬件依赖性。	|Goroutine 由 Go 运行时管理，没有硬件依赖性。|
|Os 线程通常具有 1-2 MB 的固定堆栈大小	|Goroutines 通常在较新版本的 Go 中具有 8KB 的堆栈大小|
|堆栈大小在编译期间确定，不能增长	|Go 的堆栈大小在运行时进行管理，并且可以通过分配和释放堆存储来增长到 1GB|
|线程之间没有简单的通信媒介。线程间通信之间存在巨大的延迟。	|Goroutine 使用 channel 与其他的低延迟 Goroutine 进行通信（阅读更多）。|
|线程有标识。有一个 TID 标识进程中的每个线程。	|Goroutine 没有任何标识。go 实现了这个是因为 Go 没有 TLS（线程本地存储）。|
|线程具有明显的启动和销毁成本，因为线程必须从 Os 请求大量资源并在完成后返回。	|Goroutines 由 Go 的运行时创建和释放。与线程相比，这些操作非常简便，因为运行时已经 Goroutine 维护了线程池。在这种情况下，Os 不知道 Goroutines。|
|线程被预先安排（阅读更多）。由于调度程序需要保存 / 恢复 50 个以上的寄存器和状态，因此线程之间的切换成本很高。当线程之间需要快速切换时，这可能非常重要。	|Goroutines 是合作安排的（阅读更多）。当发生 Goroutine 切换时，只需要保存或恢复 3 个寄存器就可以了。|

Go 协程相比于线程的优势
			    
- 相比线程而言，Go 协程的成本极低。堆栈大小只有若干 kb，并且可以根据应用的需求进行增减。而线程必须指定堆栈的大小，其堆栈是固定不变的。

- Go 协程会复用（Multiplex）数量更少的 OS 线程。即使程序有数以千计的 Go 协程，也可能只有一个线程。如果该线程中的某一 Go 协程发生了阻塞（比如说等待用户输入），那么系统会再创建一个 OS 线程，并把其余 Go 协程都移动到这个新的 OS 线程。所有这一切都在运行时进行，作为程序员，我们没有直接面临这些复杂的细节，而是有一个简洁的 API 来处理并发。

- Go 协程使用信道（Channel）来进行通信。信道用于防止多个协程访问共享内存时发生竞态条件（Race Condition）。信道可以看作是 Go 协程之间通信的管道。我们会在下一教程详细讨论信道。		       

			    
Go 协程的主要性质

- `启动一个新的协程时，协程的调用会立即返回。与函数不同，程序控制不会去等待 Go 协程执行完毕。`在调用 Go 协程之后，程序控制会立即返回到代码的下一行，忽略该协程的任何返回值。  

- 如果希望运行其他 Go 协程，Go 主协程必须继续运行着。如果 Go 主协程终止，则程序终止，于是其他 Go 协程也不会继续运行。  			    
			    

[![下面程序的理解图](https://golangbot.com/content/images/2017/07/Goroutines-explained.png)](https://golangbot.com/content/images/2017/07/Goroutines-explained.png)

区别于Python协程:

很多协程对应与一般是4个（4核机器的话）线程随机对应 的csp模型

```go
package main

import (  
    "fmt"
    "time"
)

func numbers() {  
    for i := 1; i <= 5; i++ {
        time.Sleep(250 * time.Millisecond)
        fmt.Printf("%d ", i)
    }
}
func alphabets() {  
    for i := 'a'; i <= 'e'; i++ {
        time.Sleep(400 * time.Millisecond)
        fmt.Printf("%c ", i)
    }
}
func main() {  
    go numbers()
    go alphabets()
    time.Sleep(3000 * time.Millisecond) 
    // 在 Go 主协程中使用休眠，以便等待其他协程执行完毕，这种方法只是用于理解 Go 协程如何工作的技巧。
    // 信道可用于在其他协程结束执行之前，阻塞 Go 主协程。
    fmt.Println("main terminated")
}
```
			    
			    
```
goroutine可能的切换点

I/O select
channel
等待锁
函数调用
runtime.Gosched()
```

```go
package goroutine

import (
"fmt"
	"runtime"
	"time"
)

//func main() {
//	for i := 0; i < 1000; i++ {
//		go func(i int) {
//			for {
//				fmt.Printf("Hello from "+    // I/O select channel 会协程切换
//					"goroutine %d\n", i)
//			}
//		}(i)
//	}
//	time.Sleep(time.Millisecond)
//
//}    4核cpu 一般最多开4个线程 也就是1000个协程映射到4个线程上

func main() {
	var a [10]int
	for i := 0; i < 10; i++ {
		// 匿名函数 anonymous
		go func(ig int) {  //拷一份传进来
			for {
				a[ig]++    // 计算任务时  不涉及协程不切换
				runtime.Gosched()
			}
		}(i)
	}
	time.Sleep(time.Millisecond)
	fmt.Println(a)
}
```
## Go并发机制学习笔记

> 1 引入协程
```
多线程(OS线程)的方式：
轻量，线程之间的通信简单但隔离性较差，任务一个线程挂掉都有可能把整个进程弄挂掉。

多进程的方式：
隔离性较好，但进程之间通信成本较大。

用户态线程/协程：
本质上是一种用户态线程(区别于OS线程，内核调度器只能看到OS线程)，协程的上下文切换不需要OS内核的参与，因此开销更小。
用协程取代OS线程，并实现自己的调度器来管理的协程的切换，并将epoll技术融入自己的网络库和运行时系统中，让用户用容易理解和使
用的传统的同步的编程思维去处理网络IO，并享受到异步网络IO带来的高性能

异步
主要用在网络IO方面，借助epoll/kqueue/iocp等技术，可以高效管理大量IO连接，是现在网络IO高并发编程中必不可少的一种手段了

```
> 2 线程实现模型

线程的实现模型主要有3种：

内核级线程模型

用户级线程模型

混合型线程模型

> 3 Go并发调度: G-P-M模型

3.1 G-P-M模型

[![pic](https://github.com/k2huang/blogpost/raw/master/golang/%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B/%E5%B9%B6%E5%8F%91%E6%9C%BA%E5%88%B6/imgs/2.png)](https://github.com/k2huang/blogpost/raw/master/golang/%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B/%E5%B9%B6%E5%8F%91%E6%9C%BA%E5%88%B6/imgs/2.png)

其图中的G, P和M都是Go语言`运行时系统`（其中包括内存分配器，并发调度器，垃圾收集器等组件，可以想象为Java中的JVM）抽象出来概念和数据结构对象：

G：

Goroutine的简称，上面用go关键字加函数调用的代码就是创建了一个G对象，是对一个要并发执行的任务的封装，也可以称作`用户态线程 go协程`。属于`用户级`资源，对OS透明，具备轻量级，可以大量创建，上下文切换成本低等特点。

M：

Machine的简称，在linux平台上是用`clone` `系统调用`创建的，其与用linux pthread库创建出来的`线程`本质上是一样的，都是利用`系统调用`创建出来的`OS线程实体`。`M的作用就是执行G中包装的并发任务`。`Go运行时系统`中的`调度器`的`主要职责`就是`将G公平合理的安排到多个M上去执行`。其属于`OS资源`，可创建的数量上也受限了OS，通常情况下G的数量都多于活跃的M的。

P：

Processor的简称，`逻辑`处理器，主要作用是`管理`G对象（每个P都有一个G队列），并为G在M上的运行提供本地化资源。

从2.3节介绍的两级线程模型来看，`似乎并不需要P的参与`，有G和M就可以了，那为什么要加入P这个东东呢？

其实Go语言运行时系统早期(Go1.0)的实现中并没有P的概念，Go中的调度器直接将G分配到合适的M上运行。

但这样带来了很多问题，例如，不同的G在不同的M上并发运行时可能都需向系统申请资源（如堆内存），由于资源是全局的，将会由于资源

竞争造成很多系统性能损耗，为了解决类似的问题，后面的Go（Go1.1）运行时系统加入了P，让P去管理G对象，M要想运行G必须先与一个P

绑定，然后才能运行该P管理的G。这样带来的好处是，我们可以在P对象中预先申请一些系统资源（本地资源），G需要的时候先向自己的本

地P申请（无需锁保护），如果不够用或没有再向全局申请，而且从全局拿的时候会多拿一部分，以供后面高效的使用。就像现在我们去政府

办事情一样，先去本地政府看能搞定不，如果搞不定再去中央，从而提供办事效率。

而且由于P解耦了G和M对象，这样即使M由于被其上正在运行的G阻塞住，其余与该M关联的G也可以随着P一起迁移到别的活跃的M上继续运行，

从而让G总能及时找到M并运行自己，从而提高系统的并发能力。

`Go运行时系统`通过构造G-P-M对象模型实现了一套`用户态的并发调度系统`，可以自己管理和调度自己的并发任务，所以可以说Go语言原

生支持并发。**自己实现的调度器**负责将并发任务分配到不同的`内核线程`上运行，然后**内核调度器**接管`内核线程`在CPU上的执行与调度。


3.2 Go运行时完整的调度过程

> 4 Goroutine与`Channel`: `锁`之外的另一种同步机制

> 5 Go语言对网络IO的优化

## Go Concurrency Patterns PPT  Rob Pike  Google学习笔记  没学完

```
1 time.Sleep()

2 channel  会等待a receiver and sender 通道既可以通信又可以同步 synchronization  不要通过共享内存进行通信，通过通信共享内存。

	当main函数执行<-c时，它将等待发送一个值。

	类似地，当钻孔函数执行c < - 值时，它等待接收器准备好。

	发送方和接收方都必须准备好在通信中发挥作用。 否则我们会等到他们。

	因此，通道既可以通信又可以同步。

3 Buffering removes synchronization. 牺牲同步了

4 在 sync 包中的 锁 的基本操作

```
```go

func main() {
    c := make(chan string)
    go boring("boring!", c)
    for i := 0; i < 5; i++ {
        fmt.Printf("You say: %q\n", <-c) // Receive expression is just a value.
    }
    fmt.Println("You're boring; I'm leaving.")
}
```
```go
func boring(msg string, c chan string) {
    for i := 0; ; i++ {
        c <- fmt.Sprintf("%s %d", msg, i) // Expression to be sent can be any suitable value.
        time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
    }
}

当main返回时，程序退出并使用它来执行boring()。

我们可以稍微闲逛一下，并且在路上显示main() 和boring()的 goroutine 都在运行通过.



func main() {
c := boring("boring!") // Function returning a channel.
    for i := 0; i < 5; i++ {
        fmt.Printf("You say: %q\n", <-c)
    }
    fmt.Println("You're boring; I'm leaving.")
}
```
```go
func boring(msg string) <-chan string { // Returns receive-only channel of strings.
    c := make(chan string)
    go func() { // We launch the goroutine from inside the function.
        for i := 0; ; i++ {
            c <- fmt.Sprintf("%s %d", msg, i)
            time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
        }
    }()
    return c // Return the channel to the caller.
}

func main() {
    joe := boring("Joe")
    ann := boring("Ann")
    for i := 0; i < 5; i++ {
        fmt.Println(<-joe)
        fmt.Println(<-ann)
    }
    fmt.Println("You're both boring; I'm leaving.")
}
```


```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func boring(msg string) <-chan string { // Returns receive-only channel of strings.
	c := make(chan string)
	go func() { // We launch the goroutine from inside the function.
		for i := 0; ; i++ {
			c <- fmt.Sprintf("%s %d", msg, i)
			time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
		}
	}()
	return c // Return the channel to the caller.
}

func fanIn(input1, input2 <-chan string) <-chan string {
	c := make(chan string)

	//go func() {
	//	for {
	//		c <- <-input1
	//	}
	//}()
	//go func() {
	//	for {
	//		c <- <-input2
	//	}
	//}()

	go func() {
		for {
			select {
			case s := <-input1:  c <- s
			case s := <-input2:  c <- s
			}
		}
	}()
	return c
}

func main() {
	c := fanIn(boring("Joe"), boring("Ann"))
	for i := 0; i < 10; i++ {
		fmt.Println(<-c)
	}
	fmt.Println("You're both boring; I'm leaving.")
}
```
```go
// Go版本的素数筛实现采用的是goroutine的并发组合。程序从2开始，依次为每个素数建立一个goroutine，用于作为筛除该素数的倍数。
// ch指向当前最新输出素数所位于的筛子goroutine的源channel，这段代码来自于Rob Pike的一次关于concurrency的分享slide。
// https://tonybai.com/2017/04/20/go-coding-in-go-way/?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io
func generate(ch chan<- int) {
    for i := 2; ; i++ {
        ch <- i // Send 'i' to channel 'ch'.
    }
}

func filter(src <-chan int, dst chan<- int, prime int) {
    for i := range src { // Loop over values received from 'src'.
        if i%prime != 0 {
            dst <- i // Send 'i' to channel 'dst'.
        }
    }
}

func sieve() {
    ch := make(chan int) // Create a new channel.
    go generate(ch)      // Start generate() as a subprocess.
    for {
        prime := <-ch
        fmt.Print(prime, "\n")
        ch1 := make(chan int)
        go filter(ch, ch1, prime)
        ch = ch1
    }
}


```
