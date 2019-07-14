[Go语言interface底层实现](https://i6448038.github.io/2018/10/01/Golang-interface/)

### a example of interface
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

用接口来实现多态

接口的组合实现继承

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
### 空接口 interface{}

空接口里面没有方法，所以它也不具有任何能力，其作用相当于 Java 的 Object 类型，可以容纳任意对象，它是一个万能容器。

比如一个字典的 key 是字符串，但是希望 value 可以容纳任意类型的对象，类似于 Java 语言的 Map 类型，这时候就可以使用空接口类型 interface{}。
```go
package main

import (
	"fmt"
)

// fmt.Printf("v1 type:%T\n", v1)
// fmt.Println("v1 type:", reflect.TypeOf(v1))

func main() {
	var user = map[string]interface{}{
		"age":     30,
		"address": "Beijing Tongzhou",
		"married": true,
	}
	fmt.Println(user)


	//var age = user["age"]
	//fmt.Println("age type:", reflect.TypeOf(age))  // int
	//var address = user["address"]
	//var married = user["married"]
	//fmt.Printf("age %T; address %T; married %T" ,age, address, married)
	//fmt.Println()
	//fmt.Printf("age %v; address %v; married %v" ,age, address, married)


	// 类型转换 将interface{}转成对应类型 貌似并不需要
	var age = user["age"].(int)
	var address = user["address"].(string)
	var married = user["married"].(bool)
	fmt.Printf("age %T; address %T; married %T", age, address, married) // 两个参数
	fmt.Println()                                                       // 一个参数
	fmt.Printf("age %v; address %v; married %v", age, address, married)
	//map[address:Beijing Tongzhou age:30 married:true]
	//age int; address string; married bool
	//age 30; address Beijing Tongzhou; married true

}
```
user 字典变量的类型是 map[string]interface{}，从这个字典中直接读取得到的 value 类型是interface{}，需要通过类型转换才能得到期望的变量，但我自己验证了一下貌似不需要这样

> 接口变量:  指向指针  指向值

变量赋值本质上是一次内存浅拷贝，切片的赋值是拷贝了切片头，字符串的赋值是拷贝了字符串的头部，而数组的赋值呢是直接拷贝整个数组。

接口变量的赋值也是浅拷贝

### 深浅拷贝

```
b:= a  深拷贝 会生成两个内存地址，

b:= &a 浅拷贝a，b公用a的内存地址，b就是指针类型

new(struct) 关键字之后,使用 b：=a是浅拷贝，b是拷贝了a的内存,可以这样理解 全程只有new时候申请了一次内存地址

function(struct)  对象传到函数里面也是深拷贝
```

```go
// 深拷贝 内存地址不同
package main

import "fmt"

type Rect struct {
	Width  int
	Height int
}

func main() {
	var a interface{}
	var r = Rect{50, 50}
	a = r

	var rx = a.(Rect)
	r.Width = 100
	r.Height = 100
	fmt.Printf("%T %v %p\n", r, r, &r)    // 得取地址& 才能打印地址
	fmt.Printf("%T %v %p", rx, rx, &rx)

}

//main.Rect {100 100} 0xc000086000
//main.Rect {50 50} 0xc000086010
```

```go
// 浅拷贝  a = &b 指向同一地址
package main

import "fmt"

type Rect struct {
	Width  int
	Height int
}

func main() {
	var a interface{}
	var r = Rect{50, 50}
	a = &r

	var rx = a.(*Rect)
	r.Width = 100
	r.Height = 100
	fmt.Printf("%T %v %p\n", r, r, &r)    // 得 取地址 & 才能打印地址
	fmt.Printf("%T %v %p", rx, rx, rx)    // rx 本身是一个指针类型 

}

//main.Rect {100 100} 0xc000092000
//*main.Rect &{100 100} 0xc000092000
```
