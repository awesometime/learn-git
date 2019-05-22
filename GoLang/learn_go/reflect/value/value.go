package main

import "reflect"
import "fmt"

type asd interface{}
func main() {
	type SomeInt int
	var s SomeInt = 42
	var t = reflect.TypeOf(s)
	var v = reflect.ValueOf(s)
	// reflect.ValueOf(s).Type() 等价于 reflect.TypeOf(s)
	fmt.Println(t == v.Type())
	fmt.Println(v.Kind() == reflect.Int) // 元类型
	// 将 Value 还原成原来的变量
	var is = v.Interface()
	fmt.Println(is.(SomeInt))

}

// Value 结构体的 Type() 方法也可以返回变量的类型信息，它可以作为 reflect.TypeOf() 函数的替代品，没有区别。
// 通过 Value 结构体提供的 Interface() 方法可以将 Value 还原成原来的变量值。


/*
https://zhuanlan.zhihu.com/p/53114706  精炼 详细讲解再看一遍这个文章


理解 Go 语言官方的反射三大定律
Reflection goes from interface value to reflection object.
Reflection goes from reflection object to interface value.
To modify a reflection object, the value must be settable.

第一个定律
的意思是反射将接口变量转换成反射对象 Type 和 Value，这个很好理解，就是下面这两个方法的功能
反射是通过检查一个接口的值，变量首先被转换成空接口。返回结构体
变量 ---> 空接口interface{} --->返回Type 、Value结构体

	func TypeOf(v interface{}) Type
	func ValueOf(v interface{}) Value

	type Value struct { } 结构体类型
	type Type interface { } 接口类型

第二个定律
的意思是反射可以通过反射对象 Value 还原成原先的接口变量，
这个指的就是 Value 结构体提供的 Interface() 方法。
注意它得到的是一个接口变量，如果要换成成原先的变量还需要经过一次类型转换。
Value ---> interface{} --->  原先的变量
	func (v Value) Interface() interface{}
    var is = v.Interface()
	fmt.Println(is.(SomeInt))
Type没有这条

第三个定律是用反射功能来修改一个变量的值，前提是这个值可以被修改。
	var s int = 42
    // 反射指针类型
    var v = reflect.ValueOf(&s)
    // 要拿出指针指向的元素进行修改
    v.Elem().SetInt(43)
    fmt.Println(s)
*/
