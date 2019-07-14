反射和接口的关系

[Go Blog的一篇文章《The law of reflection》](https://blog.golang.org/laws-of-reflection)

[大彬LIB  Go高级实践：反射3定律](http://lessisbetter.site/2019/02/24/go-law-of-reflect/)

[掘金 图解反射](https://juejin.im/post/5d27f572e51d4550bf1ae900)

[![pic](https://user-gold-cdn.xitu.io/2019/7/12/16be416ecd20d1ef?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)](https://user-gold-cdn.xitu.io/2019/7/12/16be416ecd20d1ef?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

```go
package main

import (
	"fmt"
	"reflect"
)

func main() {

	x := 10
	v1 := reflect.ValueOf(x)
	fmt.Println("setable:", v1.CanSet())
	fmt.Println("v1:", v1)

	p := reflect.ValueOf(&x)
	fmt.Println(p)
	fmt.Println("p:", p)
	fmt.Printf("p: %T", p)
	fmt.Println("setable:", p.CanSet())

	v2 := p.Elem()
	fmt.Println(v2)
	fmt.Println("setable:", v2.CanSet())

}

setable: false
v1: 10
0xc000080000
p: 0xc000080000
p: reflect.Valuesetable: false
10
setable: true


```
反射三定律
```go
1  Reflection goes from interface value to reflection object.
// 获取某个变量的值，但值是通过reflect.Value对象描述的。
reflect.ValueOf({}interface) reflect.Value

// 获取某个变量的静态类型，但值是通过reflect.Type对象描述的，是可以直接使用Println打印的
reflect.TypeOf({}interface) reflect.Type

// 获取变量值的底层类型（类别），注意不是类型，是Int、Float，还是Struct，还是Slice
reflect.Value.Kind() Kind

// 获取变量值的类型，效果等同于reflect.TypeOf
reflect.Value.Type() reflect.Type



2  Reflection goes from reflection object to interface value.
func (v Value) Interface() (i interface{})



3  To modify a reflection object, the value must be settable.

```

reflct 包函数 

Elem

Value
