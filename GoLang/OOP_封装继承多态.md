Object Oriented Programming
 - Structs Instead of Classes 
 - Encapsulation with uppercase/Lowercase letters
 - Composition Instead of Inheritance 
 - Polymorphism using interface

# 总结：Go 中的面向对象

我们总结一下前面看到的：Go 没有类，而是松耦合的类型、方法对接口的实现。

OO 语言最重要的三个方面分别是：封装，继承和多态，在 Go 中它们是怎样表现的呢？

- 封装（数据隐藏）：和别的 OO 语言有 4 个或更多的访问层次相比，Go 把它简化为了 2 层（参见 4.2 节的可见性规则）:

	1）包范围内的：通过标识符首字母小写，`对象` 只在它所在的包内可见

	2）可导出的：通过标识符首字母大写，`对象` 对所在包以外也可见

类型只拥有自己所在包中定义的方法。

- 继承：用组合实现：内嵌一个（或多个）包含想要的行为（字段和方法）的类型；多重继承可以通过内嵌多个类型实现
- 多态：用接口实现：某个类型的实例可以赋给它所实现的任意接口类型的变量。类型和接口是松耦合的，并且多重继承可以通过实现多个接口实现。Go 接口不是 Java 和 C# 接口的变体，而且接口间是不相关的，并且是大规模编程和可适应的演进型设计的关键。



# 1 OOP Structs Instead of Classes 

[ 结构体+方法  取代类](https://mp.weixin.qq.com/s/My1sXXRZS4vxCZPCmbmqPA)

employee.go

```go
package employee

import (  
    "fmt"
)

type employee struct {  
    firstName   string
    lastName    string
    totalLeaves int
    leavesTaken int
}

// New() function instead of constructors(Java)
func New(firstName string, lastName string, totalLeave int, leavesTaken int) employee {  
    e := employee {firstName, lastName, totalLeave, leavesTaken}
    return e
}

func (e employee) LeavesRemaining() {  
    fmt.Printf("%s %s has %d leaves remaining", e.firstName, e.lastName, (e.totalLeaves - e.leavesTaken))
}
```

main.go
```go
package main  

import "oop/employee"

func main() {  
    // 1
    e := employee.Employee {
            FirstName: "Sam",
            LastName: "Adolf",
            TotalLeaves: 30,
            LeavesTaken: 20,
        }
    
    // 2 New() function instead of constructors
    e := employee.New("Sam", "Adolf", 30, 20)
    
    e.LeavesRemaining()
}
```
```
为了新建一个合法的对象 使用New()

Go 并不支持构造器。如果某类型的零值不可用，需要程序员来隐藏该类型，避免从其他包直接访问。程序员应该提供一种
名为 NewT(parameters) 的 函数，按照要求来初始化 T 类型的变量。按照 Go 的惯例，应该把创建 T 类型变量的函数
命名为 NewT(parameters)。这就类似于构造器了。如果一个包只含有一种类型，按照 Go 的惯例，应该把函数命名为
New(parameters)， 而不是 NewT(parameters)。
```

# 2 OOP_Encapsulation with uppercase/Lowercase letters


# 3 OOP_Composition Instead of Inheritance

OOP_Composition_Instead_of_Inheritance.md

Composition by embedding structs 

Composition Instead of Inheritance - OOP in Go

[通过嵌套结构体进行组合  取代继承](https://mp.weixin.qq.com/s?__biz=MzAxMTA4Njc0OQ==&mid=2651435370&idx=1&sn=3cfb0b8a318c411e2a1b76066ce7aba8&chksm=80bb6f98b7cce68e5f24cb715de71b6455bf3871e41a59a773b75954d37ba74edbe35795392c&mpshare=1&scene=1&srcid=0529Y1iJ7aMjhlvW8BO6psjR&from=singlemessage&ascene=1&devicetype=android-28&version=2700043b&nettype=WIFI&abtest_cookie=BAABAAoACwASABMABgAjlx4AVpkeAL%2BZHgDcmR4A9ZkeAAOaHgAAAA%3D%3D&lang=zh_CN&pass_ticket=6NFrC%2BvqM1C%2Bzqy8DJVTshi3ylnKB54NSQOWmYt8atUz7rO%2BMkZjXfrQn6%2FoUc%2Be&wx_header=1)

```go
package main

import (  
    "fmt"
)

type author struct {  
    firstName string
    lastName  string
    bio       string
}

func (a author) fullName() string {  
    return fmt.Sprintf("%s %s", a.firstName, a.lastName)
}

type post struct {  
    title   string
    content string
    author
}

func (p post) details() {  
    fmt.Println("Title: ", p.title)
    fmt.Println("Content: ", p.content)
    fmt.Println("Author: ", p.fullName())
    fmt.Println("Bio: ", p.bio)
}

// Embedding slice of structs   结构体切片的嵌套
type website struct {  
 posts []post
}

func (w website) contents() {  
    fmt.Println("Contents of Website\n")
    for _, v := range w.posts {
        v.details()
        fmt.Println()
    }
}

func main() {  
    author1 := author{
        "Naveen",
        "Ramanathan",
        "Golang Enthusiast",
    }
    
    post1 := post{
        "Inheritance in Go",
        "Go supports composition instead of inheritance",
        author1,
    }
    
    post2 := post{
        "Struct instead of Classes in Go",
        "Go does not support classes but methods can be added to structs",
        author1,
    }
    
    post3 := post{
        "Concurrency",
        "Go is a concurrent language and not a parallel one",
        author1,
    }
    
    w := website{
        posts: []post{post1, post2, post3},
    }
    
    w.contents()
}
```


# 4 OOP_Polymorphism_using_interface

> 使用接口实现多态

一个`类型struct`如果定义了`接口`的**所有**方法，那它就**隐式**地实现了该`接口`。

所有实现了接口的`类型struct`，都可以把它的值保存在一个`接口类型的变量`中。在 Go 中，我们使用接口的这种特性来实现`多态`。

> 多态

接口是一种契约，实现类型必须满足它，它描述了类型的行为，规定类型可以做什么。

接口彻底将类型能做什么，以及如何做分离开来，使得相同接口的变量在不同的时刻表现出不同的行为，这就是多态的本质。 

摘自 the-way-to-go_ZH_CN/eBook/11.5.md

根据当前的类型选择正确的方法，或者说：同一种类型在不同的实例上似乎表现出不同的行为。摘自 the-way-to-go_ZH_CN/eBook/11.1.md


#### 例子：新增收益流

**编写参数是接口变量的函数，这使得它们更具有一般性。使用接口使代码更具有普适性。**

假设前面的组织通过广告业务，建立了一个新的收益流（Income Stream）。我们可以看到添加它非常简单，

并且计算总收益也很容易，我们无需对 calculateNetIncome 函数进行任何修改。这就是多态的好处。

```go
package main

import (
    "fmt"
)

type Income interface {
    calculate() int
    source() string
}

type FixedBilling struct {
    projectName  string
    biddedAmount int
}

type TimeAndMaterial struct {
    projectName string
    noOfHours   int
    hourlyRate  int
}

type Advertisement struct {
    adName     string
    CPC        int
    noOfClicks int
}

func (fb FixedBilling) calculate() int {
    return fb.biddedAmount
}

func (fb FixedBilling) source() string {
    return fb.projectName
}

func (tm TimeAndMaterial) calculate() int {
    return tm.noOfHours * tm.hourlyRate
}

func (tm TimeAndMaterial) source() string {
    return tm.projectName
}

func (a Advertisement) calculate() int {
    return a.CPC * a.noOfClicks
}

func (a Advertisement) source() string {
    return a.adName
}

// 编写参数是接口变量的函数，这使得它们更具有一般性。
// 使用接口使代码更具有普适性。
func calculateNetIncome(ic []Income) {
    var netincome int = 0
    for _, income := range ic {
        fmt.Printf("Income From %s = $%d\n", income.source(), income.calculate())
        netincome += income.calculate()
    }
    fmt.Printf("Net income of organisation = $%d", netincome)
}

func main() {
    project1 := FixedBilling{projectName: "Project 1", biddedAmount: 5000}
    project2 := FixedBilling{projectName: "Project 2", biddedAmount: 10000}
    project3 := TimeAndMaterial{projectName: "Project 3", noOfHours: 160, hourlyRate: 25}
    bannerAd := Advertisement{adName: "Banner Ad", CPC: 2, noOfClicks: 500}
    popupAd := Advertisement{adName: "Popup Ad", CPC: 5, noOfClicks: 750}
    
    // 编写参数是接口变量的函数，这使得它们更具有一般性。
    incomeStreams := []Income{project1, project2, project3, bannerAd, popupAd}
    calculateNetIncome(incomeStreams)
}
```
