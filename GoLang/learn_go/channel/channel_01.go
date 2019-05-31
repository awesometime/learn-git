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
	// 此处没用close 但是time.Millisecond之后
	// 主函数main退出 发送方退出  接收方也收不到了
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
	fmt.Println("Channel as first-class citizen")
	chanDemo()
	fmt.Println("Buffered channel")
	bufferedChannel()
	fmt.Println("Channel close and range")
	channelClose()
}

/*
var c chan int   // c == nil
c := make(chan int)  // c == 0
  <-ch 在箭头的右边  收数据
ch<-   在箭头的左边  发数据
deadlock
in go function and channel  is first-class citizen
*/
