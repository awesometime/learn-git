// 思维
// go 代码不是普通函数
// 不是顺序执行

/*
使用done channel等待多个goroutine结束   done 是自己定义的channel 并不是什么库包
*/


/*
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
	var workers [10]worker
	for i := 0; i < 2; i++ {
		workers[i] = createWorker(i)
	}

	for i := 0; i < 2; i++ {
		workers[i].in <- 'a' + i
		<-workers[i].done
	}

	for i := 0; i < 2; i++ {
		workers[i].in <- 'A' + i
		<-workers[i].done
	}

    // 下面写法 deadlock
	//for i, worker := range workers {
	//	worker.in <- 'a' + i
	//	<-worker.done
	//
	//}
	//
	//for i, worker := range workers {
	//	worker.in <- 'A' + i
	//	<-worker.done
	//
	//}

	// wait for all of them done
	//for _, worker := range workers {
	//	<-worker.done
	//	<-worker.done
	//}

}

func main() {
	chanDemo()
}

//Worker 0 received a
//Worker 1 received b
//Worker 0 received A
//Worker 1 received B
*/


// 以下deadlock
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
	var workers [10]worker
	for i := 0; i < 2; i++ {
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
// deadlock
