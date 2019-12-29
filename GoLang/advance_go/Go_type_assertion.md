Go语言类型转换和类型断言

https://studygolang.com/articles/9335

https://www.jianshu.com/p/bd2acab2a8e9

[![总结](https://upload-images.jianshu.io/upload_images/10797606-16168e32621d3a89.png?imageMogr2/auto-orient/strip|imageView2/2/w/425/format/webp)](https://upload-images.jianshu.io/upload_images/10797606-16168e32621d3a89.png?imageMogr2/auto-orient/strip|imageView2/2/w/425/format/webp)

**Go语言的类型转换和类型断言:**

**类型转换在编译期完成，包括强制转换【typeA(变量)】和 隐式转换 如普通类型向接口转换【interface=type】**

**类型断言在运行时确定，包括安全类型断言和非安全类型断言【xxx.(yyy)】**

Go语言要求不同类型之间必须做显式的类型转换。但似乎涉及到接口类型时，就会有所不同。

```
//两种类型断言
//不安全的类型断言，如果系统检测到不匹配，会在运行时调用内置的panic，抛出异常
s := "abc"
i := s.(int)
//安全的类型断言。 其中ok为一个bool值， 表征类型转换是否成功; s为返回的int变量，如果失败返回该类型的零值
i, ok := s.(int)
```

### 1. 类型之间转换   typeA(typeB变量)

下面是部分例子：
```
*Point(p)        // same as *(Point(p))
(*Point)(p)      // p is converted to *Point
<-chan int(c)    // same as <-(chan int(c))
(<-chan int)(c)  // c is converted to <-chan int
func()(x)        // function signature func() x
(func())(x)      // x is converted to func()
(func() int)(x)  // x is converted to func() int
func() int(x)    // x is converted to func() int (unambiguous)
```
如果不确定符号的优先级，可以用括号来约束。

### 2. 接口之间的转换

接口之间在编译期间可以确定的情况下可以使用隐式类型转换，当然也可以用强制类型转换（不常用），

所有情况下都可以使用类型断言。

```
type A interface {}
type B interface {Foo()}
// 编译时无法确定能不能转换，因此用断言  type_assertion   interfaceA.(interfaceB)
var a A
var b = a.(B)
// 编译时，可以确定  显式类型转换  typeA(变量)
var c B
var d = A(c)    
// or var d = c
// or d = c.(A)
```

### 3. 接口和类型之间的转换

**普通类型向接口转换，可以使用隐式类型转换**
```
type A interface {}
var s = "abc"
var a A
a = s
```
**接口向普通类型转换，只能使用类型断言，因为编译器无法确定**
```
type A interface {}
var s string
var a A
s = a.(string)
```



补充一个例子：
```
package main

import (
    "fmt"
)
func main() {
    var e error
    defer func() {
        if err := recover(); err != nil {
            e = err
        fmt.Println(e)
    }
    }()
}
会报错

# command-line-arguments
./recover.go:12:15: cannot use err (type interface {}) as type error in assignment:
    interface {} does not implement error (missing Error method)
为什么呢？我们可以看一下recover函数的原型：

func recover() interface{}
原来recover返回的不是error类型，而是空接口，所以编译时无法确定能否类型转换。当然，类型断言是可以的。类似的还有panic。
这就告诉我们：名字是err的不一定是error类型，不能以貌取人~
```

### golang中指针类型的转换

```
package main

func main() {
    var a int = 10
    var p *int =&a
    var c *int64 
    c= (*int64)(p)
}
```
这样的代码是错误的,编译器会提示cannot convert p (type *int) to type *int64
指针的强制类型转换需要用到unsafe包中的函数实现

```
package main

import "unsafe"
import "fmt"

func main() {
    var a int =10
    var b *int =&a
    var c *int64 = (*int64)(unsafe.Pointer(b))
    fmt.Println(*c)
}
```
