> 在哪里写代码？

如果你只是跑一下 demo ，写一个 main 方法，那么你可以在任意路径编写 main.go 文件，然后执行 go run main.go 就可以运行代码了。如果你要自己编写一个 package，那么就必须在 GOPATH 里面的指定路径来编写代码。

在基础学习阶段，大部分代码都是一个简单的 main 函数，所以对于源码路径没有限制。到了高级阶段，我们免不了要自己编写 package，这时候就必须在 GOPATH 目录下面工作了。

读者请尝试在任意目录下创建 main.go 文件，将代码贴进去。执行 go run main.go 命令观察输出结果是否是期望的 hello world!。

同一目录里变量名不能相同

> Type assertion 类型断言问题

```
Type assertion 【r.(*mock.Retriever)】
测试一个struct的值mock.Retriever  是否实现了某个接口r Retriever
mockRetriever, ok := r.(*mock.Retriever);
// https://github.com/awesometime/learn-git/blob/c36ca039a5/GoLang/learn_go/interface/main.go

err, ok := r.(error);
a.(b Type) 判断a是否是b所属的Type
// GoLang/learn_go/errhandling/recover/recover.go
userErr, ok := err.(userError)
```

> []byte(s) 类型转换问题

```
for _, b := range []byte(s) {
		fmt.Printf("%X ", b)
```


> 为什么 Go 标准库中有些函数只有签名，没有函数体

[为什么 Go 标准库中有些函数只有签名，没有函数体？](https://mp.weixin.qq.com/s?__biz=MzAxMTA4Njc0OQ==&mid=2651436552&idx=1&sn=6f038e546bdf0fcace133631b0247bc2&chksm=80bb68fab7cce1ecb0a60bfed973649cf0952476ca982fa07ba6293feb78c1d8ce4f7ddef7b9&mpshare=1&scene=1&srcid=&from=singlemessage&ascene=1&devicetype=android-28&version=2700043b&nettype=WIFI&abtest_cookie=BAABAAoACwASABMABgAjlx4AVpkeAL%2BZHgDcmR4A9ZkeAAOaHgAAAA%3D%3D&lang=zh_CN&pass_ticket=6NFrC%2BvqM1C%2Bzqy8DJVTshi3ylnKB54NSQOWmYt8atUz7rO%2BMkZjXfrQn6%2FoUc%2Be&wx_header=1)


# 变量

> := 为一个新的变量完成声明以及初始化的工作

```go
var s int = 42
var s = 42
s := 42  // 自动类型推导 + 赋值
```

https://nanxiao.me/golang-short-variable-declarations-analysis/

i := 1等价于：var i = 1  要注意语句中没有变量类型，不是var i int = 1。
“:=”只能用在函数体中。它的一个重要用途是用在“if”，“for”和“switch”语句的初始化，使变量成为一个“临时变量”，也就是变量的作用域仅限于这条语句。
“:=”不能重新声明一个已经声明过的变量，如下例所示：

```go
package main

import "fmt"

func main() {
    var i = 1

    i := 2   // 错误

    fmt.Println(i)
}
```

> 指针类型

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
指针符号 * 和取地址符 &
* 操作符存在两次内存读写，第一次获取指针变量的值，也就是内存地址，然后再去拿这个内存地址所在的变量内容。

> Go 语言基础类型大全
```go
package main

import "fmt"

func main() {
    // 有符号整数，可以表示正负
    var a int8 = 1 // 1 字节
    var b int16 = 2 // 2 字节
    var c int32 = 3 // 4 字节
    var d int64 = 4 // 8 字节
    fmt.Println(a, b, c, d)

    // 无符号整数，只能表示非负数
    var ua uint8 = 1
    var ub uint16 = 2
    var uc uint32 = 3
    var ud uint64 = 4
    fmt.Println(ua, ub, uc, ud)

    // int 类型，在32位机器上占4个字节，在64位机器上占8个字节
    var e int = 5
    var ue uint = 5
    fmt.Println(e, ue)

    // bool 类型
    var f bool = true
    fmt.Println(f)

    // 字节类型
    var j byte = 'a'
    fmt.Println(j)

    // 字符串类型
    var g string = "abcdefg"
    fmt.Println(g)

    // 浮点数
    var h float32 = 3.14
    var i float64 = 3.141592653
    fmt.Println(h, i)
}


// 复数类型 complex64 和 complex128
// unicode字符类型 rune
// uintptr 指针类型
```
# 运算符
https://www.runoob.com/go/go-operators.html

# 函数

> max函数有两个参数，它们的类型都是int，那么第一个变量的类型可以省略（即 a,b int,而非 a int, b int)，默认为离它最近的类型，同理多于2个同类型的变量或者返回值。同时我们注意到它的返回值就是一个类型，这个就是省略写法。
```go
package main

import "fmt"

// 返回a、b中最大值.
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```



# struct

[Go Struct超详细讲解  掘金](https://juejin.im/post/5ca2f37ce51d4502a27f0539#heading-14)

> struct的匿名字段

```go
package main

import "fmt"

type Skills []string

type Human struct {
	name string
	age int
	weight int
}

type Student struct {
	Human  // 匿名字段，struct
	Skills // 匿名字段，自定义的类型string slice
	int    // 内置类型作为匿名字段
	speciality string
}

func main() {
	// 初始化学生Jane
	jane := Student{Human:Human{"Jane", 35, 100}, speciality:"Biology"}
	// 现在我们来访问相应的字段
	fmt.Println("Her name is ", jane.name)
	fmt.Println("Her age is ", jane.age)
	fmt.Println("Her weight is ", jane.weight)
	fmt.Println("Her speciality is ", jane.speciality)
	// 我们来修改他的skill技能字段
	jane.Skills = []string{"anatomy"}
	fmt.Println("Her skills are ", jane.Skills)
	fmt.Println("She acquired two new ones ")
	jane.Skills = append(jane.Skills, "physics", "golang")
	fmt.Println("Her skills now are ", jane.Skills)
	// 修改匿名内置类型字段
	jane.int = 3
	fmt.Println("Her preferred number is", jane.int)
}
```

> 声明一个struct 并初始化
```go
type person struct {
	name string
	age int
}
// 赋值初始化
var P person  // P现在就是person类型的变量了
P.name = "Astaxie"  // 赋值"Astaxie"给P的name属性.
P.age = 25  // 赋值"25"给变量P的age属性
fmt.Printf("The person's name is %s", P.name)  // 访问P的name属性.

// 两个字段都写清楚的初始化
bob := person{age:25, name:"Bob"}

// 按照struct定义顺序初始化值
paul := person{"Paul", 43}

//也可以通过new函数分配一个指针，此处P的类型为*person
//P := new(person)
```




# 方法 面向对象

#### 方法声明
https://docs.hacknode.org/gopl-zh/ch6/ch6-01.html

能够给任意自定义类型定义方法 只要这个自定义类型的底层类型不是指针或者interface

go中type:

是用来定义类型的。首先定义一个自定义的类型，这类型不能是go内置的类型。然后将类型与函数绑定

go中的对象:

对象是你要处理的数据，与处理这个数据所需要的函数封装在一起
```go
package main

import (
	"fmt"
	"math"
)

type Point struct{ X, Y float64 }

// traditional function
func Distance(p, q Point) float64 {
	return math.Hypot(q.X-p.X, q.Y-p.Y)
}

// same thing, but as a method of the Point type
func (p Point) Distance(q Point) float64 {
	return math.Hypot(q.X-p.X, q.Y-p.Y)
}

func main() {
	p := Point{1, 2}
	q := Point{4, 6}
	fmt.Println(Distance(p, q)) // "5", function call
	fmt.Println(p.Distance(q))  // "5", method call
}
```
上面的代码里那个附加的参数p，叫做方法的接收器(receiver)，早期的面向对象语言留下的遗产将调用一个方法称为“向一个对象发送消息”。

在Go语言中，我们并不会像其它语言那样用this或者self作为接收器

可以看到，上面的两个函数调用都是Distance，但是却没有发生冲突。

第一个Distance的调用实际上用的是包级别的函数geometry.Distance，而第二个则是使用刚刚声明的Point，

调用的是Point类下声明的Point.Distance方法。

```go
package main

import (
	"fmt"
	"math"
)

type Point struct{ X, Y float64 }

type Path []Point   //a slice of boxes

func (p Point) Distance(q Point) float64 {
	return math.Hypot(q.X-p.X, q.Y-p.Y)
}

func (path Path) Distance() float64 {
	sum := 0.0
	for i := range path {
		if i > 0 {
			sum += path[i-1].Distance(path[i])
		}
	}
	return sum
}
func main() {
	perim := Path{
		{1, 1},
		{5, 1},
		{5, 4},
		{1, 1},
	}
	fmt.Println(perim.Distance()) // "12"
}
```
```go
package main

import "fmt"

const (
	WHITE = iota
	BLACK
	BLUE
	RED
	YELLOW
)

type Color byte

type Box struct {
	width, height, depth float64
	boxPropertyColor     Color
}

type BoxList []Box //a slice of boxes

func (b Box) Volume() float64 {
	return b.width * b.height * b.depth
}

func (b *Box) SetColor(c Color) {     //指针作为receiver
	//b.boxPropertyColor = c
	(*b).boxPropertyColor = c
}

func (bl BoxList) BiggestColor() Color {
	v := 0.00
	k := Color(WHITE)
	for _, b := range bl {
		if bv := b.Volume(); bv > v {
			v = bv
			k = b.boxPropertyColor
		}
	}
	return k
}

func (bl BoxList) PaintItBlack() {
	for i := range bl {
		// bl[i].SetColor(BLACK)
		(&bl[i]).SetColor(BLACK)
	}
}

func (c Color) String() string {
	       strings := []string{"WHITE", "BLACK", "BLUE", "RED", "YELLOW"}
	return strings[c]
}

func main() {
	boxes := BoxList{
		Box{4, 4, 4, RED},
		Box{10, 10, 1, YELLOW},
		Box{1, 1, 20, BLACK},
		Box{10, 10, 1, BLUE},
		Box{10, 30, 1, WHITE},
		Box{20, 20, 20, YELLOW},
	}
        // Printf 不换行
	fmt.Printf("We have %d boxes in our set", len(boxes))
	fmt.Println("The volume of the first one is", boxes[0].Volume(), "cm³")
	// fmt.Println("The color of the last one is",boxes[len(boxes)-1].boxPropertyColor)    byte
	fmt.Println("The color of the last one is", boxes[len(boxes)-1].boxPropertyColor.String()) //string
	fmt.Println("The biggest one is", boxes.BiggestColor().String())

	fmt.Println("Let's paint them all black")
	boxes.PaintItBlack()
	fmt.Println("The color of the second one is", boxes[1].boxPropertyColor.String())

	fmt.Println("Obviously, now, the biggest one is", boxes.BiggestColor().String())

	// 格式化输出
	fmt.Println(fmt.Sprintf("%d°C", 55))
}

```
#### 封装

Go里面的面向对象是如此的简单，没有任何的私有、公有关键字，通过大小写来实现(大写开头的为公有，小写开头的为私有)


#### method 重写
```go
package main

import "fmt"

type Human struct {
	name string
	age int
	phone string
}

type Student struct {
	Human //匿名字段
	school string
}

type Employee struct {
	Human //匿名字段
	company string
}

//Human定义method
func (h *Human) SayHi() {
	fmt.Printf("Hi, I am %s you can call me on %s\n", h.name, h.phone)
}

//Employee的method重写Human的method
func (e *Employee) SayHi() {
	fmt.Printf("Hi, I am %s, I work at %s. Call me on %s\n", e.name,
		e.company, e.phone) //Yes you can split into 2 lines here.
}

func main() {
	mark := Student{Human{"Mark", 25, "222-222-YYYY"}, "MIT"}
	sam := Employee{Human{"Sam", 45, "111-888-XXXX"}, "Golang Inc"}

	mark.SayHi()
	sam.SayHi()
}
```

[6.3. 通过嵌入结构体来扩展类型](https://docs.hacknode.org/gopl-zh/ch6/ch6-03.html)
```go
/*
   方法重写
*/
package main

import (
	"fmt"
	"image/color"
	"math"
)



type Point struct{ X, Y float64 }

type ColoredPoint struct {
	Point
	Color color.RGBA
}


func (p Point) Distance(q Point) float64 {
	dX := q.X - p.X
	dY := q.Y - p.Y
	return math.Sqrt(dX*dX + dY*dY)
}

func (p *Point) ScaleBy(factor float64) { // p是一个地址  p.ScaleBy()     *p取到地址里的Point对象,该对象有.X属性
	p.X *= factor // 相乘后再赋值
	// (*p).X *= factor
	p.Y *= factor
}

// var value int = 42
// var p1 *int = &value   *int   p1是一个int型地址
// p1=0xc4200160a0   *p1=42

func main() {
	red := color.RGBA{255, 0, 0, 255}
	blue := color.RGBA{0, 0, 255, 255}
	var p = ColoredPoint{Point{1, 1}, red}
	var q = ColoredPoint{Point{5, 4}, blue}
	fmt.Println(p.Distance(q.Point)) // "5"
	p.ScaleBy(2)
	//(&p).ScaleBy(2)
	//(&(p.Point)).ScaleBy(2)
	q.ScaleBy(2)
	fmt.Println(p.Distance(q.Point)) // "10"
}

/*
//!+error
	p.Distance(q) // compile error: cannot use q (ColoredPoint) as Point
    一个ColoredPoint  not "is a Point", 但他"has a Point"
//!-error
*/

func init() {
	//!+methodexpr
	p := Point{1, 2}
	q := Point{4, 6}

	distance := Point.Distance   // method expression
	fmt.Println(distance(p, q))  // "5"
	fmt.Printf("%T\n", distance) // "func(main.Point, main.Point) float64"  "func(接收者, 参数) 返回值类型"

	scale := (*Point).ScaleBy    //*Point  标明 接收者 是一个Point型的地址
	scale(&p, 2)   // &p 取p地址
	fmt.Println(p)            // "{2 4}"
	fmt.Printf("%T\n", scale) // "func(*main.Point, float64)"
	//!-methodexpr
}

func init() {
	red := color.RGBA{255, 0, 0, 255}
	blue := color.RGBA{0, 0, 255, 255}

	//!+indirect
	type ColoredPoint struct {
		*Point   //一个Point型的地址
		Color color.RGBA
	}

	p := ColoredPoint{&Point{1, 1}, red}
	q := ColoredPoint{&Point{5, 4}, blue}
	fmt.Println(q.Point) // &{5 4}         // q.Point 【 ？？？？？】 q.*Point
	fmt.Println(*q.Point) // {5 4}

	fmt.Println(p.Distance(*q.Point)) // "5"
	q.Point = p.Point                 // p and q now share the same Point
	p.ScaleBy(2)
	fmt.Println(*p.Point, *q.Point) // "{2 2} {2 2}"
	//!-indirect
}

```


#### 基于指针对象的方法

```go

```

# interface

[浅析Go语言Interface类型的语法行为及用法](https://studygolang.com/articles/2652)


# reflect

[![reflect](https://pic4.zhimg.com/80/v2-5641dae0a8b8d4059e3782d8e92c204f_hd.jpg)](https://pic4.zhimg.com/80/v2-5641dae0a8b8d4059e3782d8e92c204f_hd.jpg)



# misc

> Go语言fmt.Sprintf（格式化输出）http://c.biancheng.net/view/41.html

|动  词|	功  能|
|-|-|
|%v	|按值的本来值输出|
|%+v	|在 %v 基础上，对结构体字段名和值进行展开|
|%#v	|输出 Go 语言语法格式的值|
|%T	|输出 Go 语言语法格式的类型和值|
|%%	|输出 % 本体|
|%b	|整型以二进制方式显示|
|%o	|整型以八进制方式显示|
|%d	|整型以十进制方式显示|
|%x	|整型以十六进制方式显示||
|%X	|整型以十六进制、字母大写方式显示|
|%U	|Unicode 字符|
|%f	|浮点数|
|%p	|指针，十六进制方式显示|
