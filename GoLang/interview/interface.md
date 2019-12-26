https://blog.csdn.net/weixin_33874713/article/details/94165890

**interface 由两部分组成， type 和 value**

调用 func f 的时候，out 的 type 设置为 \*bytes.Buffer， value 设置为 nil。

此时 out != nil，因为虽然 out 的 value == nil， 但是 type !=nil

**也就是interface 赋值 nil Pointer 之后，变成 non-nil**


在写代码时如果不注意这里，很容易导致运行时的 panic

```go
package main

import (
	"bytes"
	"fmt"
	"io"
)

var (
	a *bytes.Buffer = nil
	b io.Writer
)

func set(v *bytes.Buffer) {
	if v == nil {
		fmt.Printf("v is nil;")
	}
	b = v
	fmt.Println(b)
}

func get() {
	if b == nil {
		fmt.Printf("b is nil")
	} else {
		fmt.Printf("b is not nil")
	}
}

func main() {
	set(nil)
	get()
}

// v is nil; <nil>
// b is not nil


func main() {
	var w io.Writer
	w = os.Stdout

	rw, ok := w.(*os.File)       // 可以正常执行
	// rw := w.(*os.File)        // 也可以正常执行
	fmt.Println(rw, ok)
}
```
