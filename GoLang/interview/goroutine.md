goroutine 主协程要等待
```go
package main

import (
	"fmt"
	"sync"
	"time"
)


func main() {
	a:=1
	m:=sync.Mutex{}
	for i:=0;i<3;i++{
		go func() {
			m.Lock()
			a+=a
			m.Unlock()
			fmt.Print(a)
		}()
	}
	time.Sleep(time.Second)

}
// 248
```
empty map 
```go
package main

import (
	"fmt"
	"sync"
)

var (
	mu      sync.Mutex // guards mapping
	mapping = make(map[string]string)   // empty map
)

func Lookup(key string) string {
	mu.Lock()
	v := mapping[key]
	mu.Unlock()
	return v
}

func main() {
	if mapping == nil {
		fmt.Println("map is nil")
	} else {
		fmt.Println("map is empty")
	}
	mapping["a"] = "aaa"
	mapping["b"] = "bbb"
	fmt.Println(Lookup("a"))
	fmt.Println(Lookup("b"))
}

// map is empty
// aaa
// bbb

```

匿名函数

```go
func main() {
	i := 1
	test := func() {
		i += 1
		fmt.Print(i)
	}
	test()
	i = 10
	test()
}

// 211
```
