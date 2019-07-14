[Go语言interface底层实现](https://i6448038.github.io/2018/10/01/Golang-interface/)

```go
package main
import "fmt"
import "math"
// Here’s a basic interface for geometric shapes.

type geometry interface {
    area() float64
    perim() float64
}
// For our example we’ll implement this interface on rect and circle types.

type rect struct {
    width, height float64
}
type circle struct {
    radius float64
}
// To implement an interface in Go, we just need to implement all the methods in the interface.
// Here we implement geometry on rects.

func (r rect) area() float64 {
    return r.width * r.height
}
func (r rect) perim() float64 {
    return 2*r.width + 2*r.height
}
// The implementation for circles.

func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
    return 2 * math.Pi * c.radius
}
// If a variable has an interface type, then we can call methods that are in the named interface. 
// Here’s a generic measure function taking advantage of this to work on any geometry.

func measure(g geometry) {
    fmt.Println(g)
    fmt.Println(g.area())
    fmt.Println(g.perim())
}
func main() {
    r := rect{width: 3, height: 4}
    c := circle{radius: 5}
// The circle and rect struct types both implement the geometry interface so we can use instances
// of these structs as arguments to measure.

    measure(r)
    measure(c)
}

```

Go只有封装

> 用接口来实现多态
```go
type Fruitable interface {
    eat()
}

type Fruit struct {
    Name string  // 属性变量
    Fruitable  // 匿名内嵌接口变量
}

// 通过组合属性变量（Name）和接口变量（Fruitable）来模拟多态，
// 属性变量是对象的数据，而接口变量是对象的功能，将它们组合到一块就形成了一个完整的多态性的结构体。
```

> 接口的组合实现继承

```go
type Smellable interface {
  smell()
}

type Eatable interface {
  eat()
}

type Fruitable interface {
  Smellable
  Eatable
}
```
> interface{}

空接口里面没有方法，所以它也不具有任何能力，其作用相当于 Java 的 Object 类型，可以容纳任意对象，它是一个万能容器。

比如一个字典的 key 是字符串，但是希望 value 可以容纳任意类型的对象，

类似于 Java 语言的 Map 类型，这时候就可以使用空接口类型 interface{}。
```go
package main
import "fmt"
func main() {
    // 连续两个大括号，是不是看起来很别扭
    var user = map[string]interface{}{
        "age": 30,
        "address": "Beijing Tongzhou",
        "married": true,
    }
    fmt.Println(user)
    // 类型转换语法来了   【】
    var age = user["age"].(int)
    var address = user["address"].(string)
    var married = user["married"].(bool)
    fmt.Println(age, address, married)
}


//map[age:30 address:Beijing Tongzhou married:true]
//30 Beijing Tongzhou true
```
user 字典变量的类型是 map[string]interface{}，从这个字典中直接读取得到的 value 类型是

interface{}，需要通过类型转换才能得到期望的变量

> 接口变量:  指向指针  指向值

变量赋值本质上是一次内存浅拷贝，切片的赋值是拷贝了切片头，字符串的赋值是拷贝了字符串的头部，而数组的赋值呢是直接拷贝整个数组。

接口变量的赋值也是浅拷贝
```go

package main

import "fmt"

type Rect struct {
    Width int
    Height int
}

func main() {
    var a interface {}
    var r = Rect{50, 50}
    a = r

    var rx = a.(Rect)
    r.Width = 100
    r.Height = 100
    fmt.Println(rx)
}

// {50 50}
```

```go
package main

import "fmt"

type Rect struct {
    Width int
    Height int
}

func main() {
    var a interface {}
    var r = Rect{50, 50}
    a = &r // 指向了结构体指针

    var rx = a.(*Rect) // 转换成指针类型
    r.Width = 100
    r.Height = 100
    fmt.Println(rx)
}

// &{100 100}
```
