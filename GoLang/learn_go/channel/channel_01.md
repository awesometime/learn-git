```
Concurrency
20 - Introduction to Concurrency 
21 - Goroutines 
22 - Channels                                    https://mp.weixin.qq.com/s/NW9zCVRG-CKslNZd9L4RnQ
23 - Buffered Channels and Worker Pools 
24 - Select 
25 - Mutex
```


> Channel as first-class citizen
```go
package main

import (
	"fmt"
	"time"
)

func worker(id int, c chan int) {
	// 发送方close关闭之后 接收方需要判断一下 没有数据了 然后停止

	// method one
	//for {
	//	n, ok := <-c
	//	if !ok {
	//		break
	//	}
	//	fmt.Printf("Worker %d received %c\n", id, n) // %c字符
	//}

	// method two
	for n := range c {
		fmt.Printf("Worker %d received %c\n", id, n) // %c字符
	}
}

func createWorker(id int) chan<- int {
	c := make(chan int)
	go worker(id, c)
	return c
}

func chanDemo() {
	var channels [10]chan<- int
	for i := 0; i < 10; i++ {
		channels[i] = createWorker(i)
	}

	for i := 0; i < 10; i++ {
		channels[i] <- 'a' + i
	}

	for i := 0; i < 10; i++ {
		channels[i] <- 'A' + i
	}

	time.Sleep(time.Millisecond)    
	// 此处没用close 但是time.Millisecond 之后
	// 主函数main退出 发送方退出  接收方也收不到了
}

func main() {
	chanDemo()
}
```
> buffered Channel
```go
package main

import (
	"fmt"
	"time"
)

func worker(id int, c chan int) {
	// 发送方close关闭之后 接收方需要判断一下 没有数据了 然后停止

	// method one
	//for {
	//	n, ok := <-c
	//	if !ok {
	//		break
	//	}
	//	fmt.Printf("Worker %d received %c\n", id, n) // %c字符
	//}

	// method two
	for n := range c {
		fmt.Printf("Worker %d received %c\n", id, n) // %c字符
	}
}

func bufferedChannel() {
	c := make(chan int, 3)
	go worker(0, c)
	c <- 'a'
	c <- 'b'
	c <- 'c'
	c <- 'd'
	time.Sleep(time.Millisecond)
}

func main() {
	bufferedChannel()
}
```
> Channel close and range
```go
package main

import (
	"fmt"
	"time"
)

func worker(id int, c chan int) {
	// 发送方close关闭之后 接收方需要判断一下 没有数据了 然后停止

	// method one
	//for {
	//	n, ok := <-c
	//	if !ok {
	//		break
	//	}
	//	fmt.Printf("Worker %d received %c\n", id, n) // %c字符
	//}

	// method two
	for n := range c {
		fmt.Printf("Worker %d received %c\n", id, n) // %c字符
	}
}

func channelClose() {
	c := make(chan int)
	go worker(0, c)
	c <- 'a'
	c <- 'b'
	c <- 'c'
	c <- 'd'
	close(c)                     //
	time.Sleep(time.Millisecond) // deadlock
}

func main() {
	channelClose()
}
```

```
var c chan int   // c == nil
c := make(chan int)  // c == 0
  <-ch 在箭头的右边  收数据
ch<-   在箭头的左边  发数据
deadlock
in go function and channel  is first-class citizen
```

### 4 channel的作用之一： 使用 done channel 等待任务结束 

```go
package main

import (
	"fmt"
)

func doWork(id int, c chan int, done chan bool) {
	for n := range c {
		fmt.Printf("Worker %d received %c\n",
			id, n)
		done <- true   // 不是go程  以为着阻塞 done没有接收方
	}
}

type worker struct {
	in   chan int
	done chan bool
}

func createWorker(id int) worker {
	w := worker{
		in:   make(chan int),
		done: make(chan bool),
	}
	go doWork(id, w.in, w.done) //程序执行到这里先执行return w 这句go routine 并发的,之后执行
	return w
}

// 不带缓冲的 chan 是阻塞的
func chanDemo() {
	var workers [5]worker
	for i := 0; i < 5; i++ {
		workers[i] = createWorker(i)
	}
        // 发一个收一个 回一个done收到done 只是这样打出来是按顺序的 没什么卵意义
	for i := 0; i < 5; i++ {
		workers[i].in <- 'a' + i
		<-workers[i].done
	}
	for i := 0; i < 5; i++ {
		workers[i].in <- 'A' + i
		<-workers[i].done
	}
}

func main() {
	chanDemo()
}
```

"接收方(不是go 程) <-ch 之前要有发送方go程"
```go
go func(){ ch <- "string" }()
<- ch
```
"发送方(不是go 程) ch<- 之前要有接收方go程"
```go
go func(){ <-ch }()
ch <- "string"
```

```go
package main

import (
	"fmt"
)

func doWork(id int, c chan int, done chan bool) {
	for n := range c {
		fmt.Printf("Worker %d received %c\n",
			id, n)
		go func() {
			done <- true   // 注意此处如果done 不放在go func 里边会deadlock
		}()     // 这样的话 满足了 "接受方(不是go 程) <-worker.done 之前要有发送方go程"
	}
}

type worker struct {
	in   chan int
	done chan bool
}

func createWorker(id int) worker {
	w := worker{
		in:   make(chan int),
		done: make(chan bool),
	}
	go doWork(id, w.in, w.done) //程序执行到这里先执行return w 这句go routine 并发的,之后执行
	return w
}

func chanDemo() {
	var workers [5]worker
	for i := 0; i < 5; i++ {
		workers[i] = createWorker(i)
	}

	for i, worker := range workers {
		worker.in <- 'a' + i
	}

	for i, worker := range workers {
		worker.in <- 'A' + i
	}

	// wait for all of them done
	// 并发打印 乱序 达到了并发目的
	for _, worker := range workers {
		<-worker.done        // done true
		<-worker.done
	}
}

func main() {
	chanDemo()
}
```
```go
package main

import (
	"fmt"
)

func doWork(id int, c chan int, done chan bool) {
	for n := range c {
		fmt.Printf("Worker %d received %c\n",
			id, n)
		done <- true
	}
}

type worker struct {
	in   chan int
	done chan bool
}

func createWorker(id int) worker {
	w := worker{
		in:   make(chan int),
		done: make(chan bool),
	}
	go doWork(id, w.in, w.done) //程序执行到这里先执行return w 这句go routine 并发的,之后执行
	return w
}

func chanDemo() {
	var workers [10]worker  // 10 和 i<10 要想等 注意如果一个10长度的channel和 i<2 则输出结果deadlock不对 
	for i := 0; i < 10; i++ {
		workers[i] = createWorker(i)
	}

	for i, worker := range workers {
		worker.in <- 'a' + i
	}

	// wait for all of them done
	for _, worker := range workers {
		<-worker.done
	}

	for i, worker := range workers {
		worker.in <- 'A' + i
	}

	// wait for all of them done
	for _, worker := range workers {
		<-worker.done
	}

}

func main() {
	chanDemo()

}
```
### 5 使用sync.WaitGroup等待多个goroutine结束
```go
wg.Add()
wg.Done()
wg.Wait()

// 没用函数式编程
package main
import (
	"fmt"
	"sync"
)
func doWork(id int, c chan int, wg *sync.WaitGroup) {
	for n := range c {
		fmt.Printf("Worker %d received %c\n",
			id, n)
		wg.Done()
	}
}
type worker struct {
	in chan int
	wtyg *sync.WaitGroup
}
func createWorker(id int, wog *sync.WaitGroup) worker {
	w := worker{
		in: make(chan int),
		wtyg: wog,
	}
	go doWork(id, w.in, w.wtyg)
	return w
}
func chanDemo() {
	var wg sync.WaitGroup //相当于全局的 loop 所以要在最外边创建并传地址
	var workers [10]worker
	for i := 0; i < 10; i++ {
		workers[i] = createWorker(i, &wg)
	}
	wg.Add(20)
	for i, worker := range workers {
		worker.in <- 'a' + i
	}
	for i, worker := range workers {
		worker.in <- 'A' + i
	}
	wg.Wait()
}
func main() {
	chanDemo()
}
```
函数式编程 抽象程度更高
```go
package main

import (
	"fmt"
	"sync"
)

func doWork(id int, w worker) {
	for n := range w.in {
		fmt.Printf("Worker %d received %c\n",
			id, n)
		w.done()
	}
}

type worker struct {
	in   chan int
	done func() //函数式编程
}

func createWorker(id int, wg *sync.WaitGroup) worker {
	w := worker{
		in: make(chan int),
		done: func() {
			wg.Done()
		},
	}
	go doWork(id, w)
	return w
}

func chanDemo() {
	var wg sync.WaitGroup //相当于全局的 loop 所以要在最外边创建并传地址

	var workers [10]worker
	for i := 0; i < 10; i++ {
		workers[i] = createWorker(i, &wg)
	}

	wg.Add(20)
	for i, worker := range workers {
		worker.in <- 'a' + i
	}
	for i, worker := range workers {
		worker.in <- 'A' + i
	}

	wg.Wait()
}

func main() {
	chanDemo()
}
```
