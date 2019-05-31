/*
使用done channel等待多个goroutine结束
使用sync.WaitGroup等待多个goroutine结束
wg.Add()
wg.Done()
wg.Wait()
*/

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

/*
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
*/
