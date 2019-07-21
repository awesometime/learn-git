[模板用法](https://gobyexample.com/)

[图解Go的channel底层原理](https://mp.weixin.qq.com/s/w9_ycAYD6SRhaxy-4BnvwA)

https://zhuanlan.zhihu.com/p/27917262

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
