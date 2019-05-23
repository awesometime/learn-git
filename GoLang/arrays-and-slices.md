- 原文 https://golangbot.com/arrays-and-slices/

- 源码 https://github.com/golangbot/arraysandslices/blob/master/arrayslice.go


# arrays

数组是**同一类型**元素的集合。例如，整数集合 5,8,9,79,76 形成一个数组。

**Go 语言中不允许混合不同类型的元素**，例如包含字符串和整数的数组。

当然：如果是 interface{} 类型数组，可以包含任意类型

数组的大小是类型的一部分。因此 [5]int 和 [25]int 是不同类型。

数组不能调整大小，不要担心这个限制，因为 slices 的存在能解决这个问题。


> 数组是值类型

Go 中的数组是值类型而不是引用类型。

**这意味着当数组赋值给一个新的变量时，该变量会得到一个原始数组的一个副本。如果对新变量进行更改，则不会影响原始数组。**

同样，当数组作为参数传递给函数时，它们是按值传递，而原始数组保持不变

> 数组声明

var a [3]int

简略声明

a := [3]int{12, 78, 50}

a := [3]int{12}             只提供了一个值剩下的 2 个元素自动赋值为 0

a := [...]int{12, 78, 50}   编译器为你自动计算长度

> 使用 range 迭代数组

```go
for i, v := range a 

for _, v := range a { // ignores index  }
```

> 多维数组

```go
a := [3][2]string{
        {"lion", "tiger"},
        {"cat", "dog"},
        {"pigeon", "peacock"}, // this comma is necessary. The compiler will complain if you omit this comma
    }

var b [3][2]string
b[0][0] = "apple"
b[0][1] = "samsung"
```

# slices

切片是由数组建立的一种方便、灵活且功能强大的包装（Wrapper）。切片本身不拥有任何数据。它们只是对现有数组的引用。

**创建一个切片总是先创建一个数组，并返回引用该数组的切片**

**切片包含长度、容量和指向数组第零个元素的指针**

切片自己不拥有任何数据。它只是底层数组的一种表示。对切片所做的任何修改都会反映在底层数组中。

当多个切片共用相同的底层数组时，每个切片所做的更改将反映在数组中


> 创建一个切片

切片类型的零值为 nil。一个 nil 切片的长度和容量为 0。可以使用 append 函数将值追加到 nil 切片

方法一

c := []int{6, 7, 8}  创建一个有 3 个整型元素的**数组**，并**返回一个存储在 c 中的切片引用**。

方法二

```go
a := [5]int{76, 77, 78, 79, 80}  // creates an array
var b []int = a[1:4]    // creates a slice from array a[1] to a[3]
```

方法三

使用 make 创建一个切片

func make（[]T，len，cap）[]T 通过传递类型，长度和容量来创建切片。容量是可选参数, 默认值为切片长度。

**make 函数创建一个数组，并返回引用该数组的切片**

> 切片长度 容量

```go
fruitarray := [...]string{"apple", "orange", "grape", "mango", "water melon", "pine apple", "chikoo"}
fruitslice := fruitarray[1:3]
fmt.Printf("length of slice %d capacity %d", len(fruitslice), cap(fruitslice)) // length of is 2 and capacity is 6
```

> append

func append（s[]T，x ... T）[]T   ... 表示参数 x 的个数是可变的

如果切片由数组支持，并且数组本身的长度是固定的，那么切片如何具有动态长度，以及内部发生了什么？

当新的元素被添加到切片时，会创建一个新的数组。现有数组的元素被复制到这个新数组中，并返回这个新数组的新切片引用

```go
cars: [Ferrari Honda Ford] has old length 3 and capacity 3  
cars: [Ferrari Honda Ford Toyota] has new length 4 and capacity 6

veggies := []string{"potatoes", "tomatoes", "brinjal"}
fruits := []string{"oranges", "apples"}
food := append(veggies, fruits...)
fmt.Println("food:",food)  //food: [potatoes tomatoes brinjal oranges apples]
```
> 切片的函数传递

切片包含长度、容量和指向数组第零个元素的指针。

当切片传递给函数时，即使它通过值传递，指针变量也将引用相同的底层数组。

因此，当切片作为参数传递给函数时，函数内所做的更改也会在函数外可见

> 多维切片

```go
 pls := [][]string {
            {"C", "C++"},
            {"JavaScript"},
            {"Go", "Rust"},
     }
```     
> 内存优化

切片持有对底层数组的引用。**只要切片在内存中，数组就不能被垃圾回收。**

在内存管理方面，这是需要注意的。让我们假设我们有一个非常大的数组，我们只想处理它的一小部分。

然后，我们由这个数组创建一个切片，并开始处理切片。

这里需要重点注意的是，在切片引用时数组仍然存在内存中。

一种**解决方法**是使用 copy 函数 func copy(dst，src[]T)int 来生成一个切片的副本。

这样我们可以使用新的切片，原始数组可以被垃圾回收。



