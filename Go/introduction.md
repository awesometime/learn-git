> 在哪里写代码？

如果你只是跑一下 demo ，写一个 main 方法，那么你可以在任意路径编写 main.go 文件，然后执行 go run main.go 就可以运行代码了。如果你要自己编写一个 package，那么就必须在 GOPATH 里面的指定路径来编写代码。

在基础学习阶段，大部分代码都是一个简单的 main 函数，所以对于源码路径没有限制。到了高级阶段，我们免不了要自己编写 package，这时候就必须在 GOPATH 目录下面工作了。

读者请尝试在任意目录下创建 main.go 文件，将代码贴进去。执行 go run main.go 命令观察输出结果是否是期望的 hello world!。

> := 为一个新的变量完成声明以及初始化的工作

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
