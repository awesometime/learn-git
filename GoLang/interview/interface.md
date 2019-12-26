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

// https://blog.csdn.net/weixin_33874713/article/details/94165890
// v is nil; <nil>
// b is not nil
```
