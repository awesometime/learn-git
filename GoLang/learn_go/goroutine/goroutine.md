Go 是并发式语言    并发(concurrency)  goroutine channel

> 资料

[「GCTT 出品」图解 Go 并发编程](https://mbd.baidu.com/newspage/data/landingshare?context=%7B%22nid%22%3A%22news_10061718063488657719%22%2C%22sourceFrom%22%3A%22bjh%22%2C%22url_data%22%3A%22bjhauthor%22%7D)

[英文出处 Learning Go’s Concurrency Through Illustrations](https://medium.com/@trevor4e/learning-gos-concurrency-through-illustrations-8c4aff603b3)

[Go Concurrency Patterns   Rob Pike  Google](https://talks.golang.org/2012/concurrency.slide#1)

[Go的CSP并发模型实现](https://www.cnblogs.com/sunsky303/p/9115530.html)

[python协程与golang协程的区别](https://segmentfault.com/a/1190000019127902?utm_campaign=studygolang.com&utm_medium=studygolang.com&utm_source=studygolang.com)


> 并发

https://mp.weixin.qq.com/s/nqoRLVYIZmzgBBTSiIqkZg

- 并发是指立即处理多个任务的能力。

我们可以想象一个人正在跑步。假如在他晨跑时，鞋带突然松了。于是他停下来，系一下鞋带，接下来继续跑。这个例子就是典型的并发。这个人能够一下搞定跑步和系鞋带两件事，即立即处理多个任务。

- 并行是指同时处理多个任务。       这听起来和并发差不多，但其实完全不同。

我们同样用这个跑步的例子来帮助理解。假如这个人在慢跑时，还在用他的 iPod 听着音乐。在这里，他是在跑步的同时听音乐，也就是同时处理多个任务。这称之为并行。

		       
[![concurrency parallelism](https://mmbiz.qpic.cn/mmbiz_png/UWba2ryLMqlGWzyzqqeohYZr3yic7yFBfxDxrSrcyNVA2p5oA1c0UAbpBicdXFOyh19PWA1icpcuIAs68NcRvbpqw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mmbiz.qpic.cn/mmbiz_png/UWba2ryLMqlGWzyzqqeohYZr3yic7yFBfxDxrSrcyNVA2p5oA1c0UAbpBicdXFOyh19PWA1icpcuIAs68NcRvbpqw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)		       
		       
		       
### Go 协程是什么？
			    
Go 协程是与其他函数或方法一起并发运行的函数或方法。Go 协程可以看作是轻量级线程。与线程相比，创建一个 Go 协程的成本很小。因此在 Go 应用中，常常会看到有数以千计的 Go 协程并发地运行。

Go 协程相比于线程的优势
			    
- 相比线程而言，Go 协程的成本极低。堆栈大小只有若干 kb，并且可以根据应用的需求进行增减。而线程必须指定堆栈的大小，其堆栈是固定不变的。

- Go 协程会复用（Multiplex）数量更少的 OS 线程。即使程序有数以千计的 Go 协程，也可能只有一个线程。如果该线程中的某一 Go 协程发生了阻塞（比如说等待用户输入），那么系统会再创建一个 OS 线程，并把其余 Go 协程都移动到这个新的 OS 线程。所有这一切都在运行时进行，作为程序员，我们没有直接面临这些复杂的细节，而是有一个简洁的 API 来处理并发。

- Go 协程使用信道（Channel）来进行通信。信道用于防止多个协程访问共享内存时发生竞态条件（Race Condition）。信道可以看作是 Go 协程之间通信的管道。我们会在下一教程详细讨论信道。		       

			    
Go 协程的主要性质

- 启动一个新的协程时，协程的调用会立即返回。与函数不同，程序控制不会去等待 Go 协程执行完毕。在调用 Go 协程之后，程序控制会立即返回到代码的下一行，忽略该协程的任何返回值。  

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

