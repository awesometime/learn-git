/*
goroutine可能的切换点
I/O select
channel
等待锁
函数调用
runtime.Gosched()
*/


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
				a[ig]++    // 协程不切换
				runtime.Gosched()
			}
		}(i)
	}
	time.Sleep(time.Millisecond)
	fmt.Println(a)
}


