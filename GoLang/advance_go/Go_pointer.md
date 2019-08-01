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
