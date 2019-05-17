> :=为一个新的变量完成声明以及初始化的工作

https://nanxiao.me/golang-short-variable-declarations-analysis/

i := 1等价于：var i = 1  要注意语句中没有变量类型，不是var i int = 1。
“:=”只能用在函数体中。它的一个重要用途是用在“if”，“for”和“switch”语句的初始化，使变量成为一个“临时变量”，也就是变量的作用域仅限于这条语句。
“:=”不能重新声明一个已经声明过的变量，如下例所示：

```go
package main

import "fmt"

func main() {
    var i = 1

    i := 2

    fmt.Println(i)
}
```
