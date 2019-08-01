指针

\*var 是值

&var是地址

Golang是值传递，复制一份 ;Python引用传递

除map slice 等
```go
package main

import "fmt"

func DF(a *int) {
	*a += 1
}

func DFer(a *int) {
	*a += 100
	fmt.Println(*a)
}
func main() {
	a := 1
	DF(&a)
	//fmt.Println(&a)
	fmt.Println(a)
	DFer(&a)
	fmt.Println(a)
}

//2
//102
//102
```

```go
package main

import "fmt"

func main() {
    var value int = 42
    var p1 *int = &value
    var p2 **int = &p1
    var p3 ***int = &p2
    fmt.Println(p1, p2, p3)
    fmt.Println(*p1, **p2, ***p3)
}

----------
0xc4200160a0 0xc42000c028 0xc42000c030
42 42 42
```
