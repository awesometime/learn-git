[模板用法](https://gobyexample.com/)

[图解Go的channel底层原理](https://mp.weixin.qq.com/s/w9_ycAYD6SRhaxy-4BnvwA)

https://zhuanlan.zhihu.com/p/27917262



```go
1 chan 变量申明
不带缓冲区的就是同步的信道
 带缓冲区是异步的
var ch chan int // ch == nil
ch := make(chan string, 1)

  一般要带缓冲的协程
  
2 slect  原理 为啥可以 监听
  工厂函数
3 WaitGroups
4 Timeouts
  close
5 for elem := range queue
Timers  适用于您希望将来做某事的时间
Tickers 适用于您希望定期重复执行某些操作的情况 
Mutexes

//msg := <-pings
//pongs <- msg
pongs <- <-pings
	
```
use `select` with a `default` clause to implement _non-blocking_ sends, receives, and even non-blocking multi-way `select`s.
```go
// use `select` with a `default` clause to
// implement _non-blocking_ sends, receives, and even
// non-blocking multi-way `select`s.

package main

import "fmt"

func main() {
    messages := make(chan string)
    signals := make(chan bool)

    select {
    case msg := <-messages:
        fmt.Println("received message", msg)
    default:
        fmt.Println("no message received")
    }

    // A non-blocking send . Here `msg`
    // cannot be sent to the `messages` channel, because
    // the channel has no buffer and there is no receiver.
    // Therefore the `default` case is selected.
    msg := "hi"
    select {
    case messages <- msg:
        fmt.Println("sent message", msg)
    default:
        fmt.Println("no message sent")
    }

    // implement a multi-way non-blocking select. 
    select {
    case msg := <-messages:
        fmt.Println("received message", msg)
    case sig := <-signals:
        fmt.Println("received signal", sig)
    default:
        fmt.Println("no activity")
    }
}
```
close
```go
package main

import "fmt"

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)             // close
	fmt.Println("sent all jobs")

	<-done
}

sent job 1
sent job 2
sent job 3
sent all jobs
received job 1
received job 2
received job 3
received all jobs
```
一个Bug
```go
package main

const MaxOutstanding = 3

var sem = make(chan int, MaxOutstanding)

func Serve(queue chan *Request) {
	for req := range queue {
		sem <- 1
		go func() {
			process(req) // 这儿有 Bug，解释见下。 go 函数会继续循环，无需等当前go程结束，所以会导致req共享，因为req指向的地址是一块内存
			<-sem
		}()
	}
}
```
在 Go 的 for 循环中，该循环变量在每次迭代时会被重用，因此 req 变量会在所有的goroutine 间共享，这不是我们想要的。我们需要确保 req 对于每个 goroutine 来说都是唯一的。

方法一 ：能够做到，就是将 req 的值作为实参传入到该 goroutine 的闭包中：
```go
package main

const MaxOutstanding = 3

var sem = make(chan int, MaxOutstanding)

func Serve(queue chan *Request) {
	for req := range queue {
		sem <- 1
		go func(req *Request) {
			process(req)
			<-sem
		}(req)
	}
}
```

方法二 ：或者以相同的名字创建新的变量

用相同的名字获得了该变量的一个新的版本,以此来局部地刻意屏蔽循环变量，使它对每个 goroutine 保持唯一。
```go
package main

const MaxOutstanding = 3

var sem = make(chan int, MaxOutstanding)

func Serve(queue chan *Request) {
	for req := range queue {
		req := req // 为该 Go 程创建 req 的新实例。
		sem <- 1
		go func() {
			process(req)
			<-sem
		}()
	}
}

```

### channel能干吗

```
通过阻塞 保证同步
Channel Synchronization
Here’s an example of using a blocking receive to wait for a send goroutine to finish.
https://gobyexample.com/channel-synchronization
```

### deadlock

[deadlock的几种情况](https://wumansgy.github.io/2018/09/09/go%E7%9A%84%E5%87%A0%E7%A7%8D%E6%AD%BB%E9%94%81%E6%83%85%E5%86%B5%E5%88%86%E6%9E%90/)

> 1
```go
package main

func main(){
    ch:=make(chan int)  //这就是在main程里面发生的死锁情况
    ch<-6   //  这里会发生一直阻塞的情况，执行不到下面一句
    <-ch
}
```
改为
```go
package main

import "fmt"

func main() {
	ch := make(chan int, 1) //
	ch <- 6                 //  
	fmt.Println(<-ch)
}
```

> 2 
```go
package main

import "fmt"

func f1(in chan int) {
	fmt.Println(<-in)
}

func main() {
	out := make(chan int)
	out <- 2
	go f1(out)
}
```
改为
```go
package main

import "fmt"

func f1(in chan int) {
	fmt.Println(<-in)
}

func main() {
	out := make(chan int)
	go f1(out)
	out <- 2      // 发送方先要有接收方go程准备好，发送方阻塞等待， 接收方go程好了以后开始发送
}
```
这样也对 总之不要让go 程位于 mian函数最后边
```go
package main

import "fmt"

func main() {
	messages := make(chan string)
	go func() { messages <- "ping" }()
	fmt.Println(<-messages)  // 接收方阻塞等待 发送方go程
}

```

> 3
```go
package main
func main()  {
    ch1 := make(chan int)
    ch2 := make(chan int)
    go func() {    //匿名子go程
        for {
            select {    //这里互相等对方造成死锁
            case <-ch1:   //这里ch1有数据读出才会执行下一句
                ch2 <- 777
            }
        }
    }()
    for {         //主go程
        select {
        case <-ch2 : //这里ch2有数据读出才会执行下一句
            ch1 <- 999
        }
    }
}
```
> 4 channel 和 读写锁、互斥锁 尽量避免交叉混用 用channel就不用锁
