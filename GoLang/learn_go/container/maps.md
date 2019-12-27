/*
解剖Go语言map底层实现
https://i6448038.github.io/2018/08/26/map-secret/
*/


### map的初始化
```go
func main(){
	// 先声明map
	var mapping map[string]string
	// 再使用make函数创建一个非nil的map，nil map不能赋值
	mapping = make(map[string]string)
	mapping["a"] = "aa"
	mapping["b"] = "bb"
	
	
	// 直接创建
	mapping2 := make(map[string]string)
	mapping2["a"] = "aa"
	mapping2["b"] = "bb"
	
	// 初始化 + 赋值一体化
	m3 := map[string]string{
	    "a": "aa",
	    "b": "bb",
	}

}
```

main 函数外边
```go
var (
	mu      sync.Mutex // guards mapping
	mapping = make(map[string]string)
)

func main(){
}
```
### 使用
```go
// 查找键值是否存在
if v, ok := m1["a"]; ok {
    fmt.Println(v)
} else {
    fmt.Println("Key Not Found")
}

// 遍历map
for k, v := range m1 {
    fmt.Println(k, v)
}
```


```go
/*
除slice map function之外的内建类型都可以作为key
*/
package main

import "fmt"

func main() {
	m := map[string]string{
		"name":    "ccmouse",
		"course":  "golang",
		"site":    "imooc",
		"quality": "notbad",
	}

	m2 := make(map[string]int) // m2 == empty map

	var m3 map[string]int // m3 == nil

	fmt.Println("m, m2, m3:")
	fmt.Println(m, m2, m3)

	// 遍历
	// 注意 map 是无序的 每次打印结果不同
	fmt.Println("Traversing map m")
	for k, v := range m {
		fmt.Println(k, v)
	}

	fmt.Println("Getting values")
	courseName := m["course"]
	fmt.Println(`m["course"] =`, courseName)
	
	// map中key不存在时 打印value相应类型的初始值
	// 判断key是否存在
	if causeName, ok := m["cause"]; ok {
		fmt.Println(causeName)
	} else {
		fmt.Println("key 'cause' does not exist")
	}

	// 删除
	fmt.Println("Deleting values")
	name, ok := m["name"]    //   :=
	fmt.Printf("m[%q] before delete: %q, %v\n",
		"name", name, ok)

	delete(m, "name")
	name, ok = m["name"]     // ok 有了需要用  =
	fmt.Printf("m[%q] after delete: %q, %v\n",
		"name", name, ok)
}
```

```
1 map数据类型初始化：

两种方式：map[string]string{}或make(map[string]string)

2 未初始化的map是nil：

未初始化的map是nil，它与一个空map基本等价，只是nil的map不允许往里面添加值。（A nil map
is equivalent to an empty map except that no elements may be added）
因此，map是nil时，取值是不会报错的（取不到而已），但增加值会报错。
其实，还有一个区别，delete一个nil map会panic，但是delete 空map是一个空操作（并不会panic）
（这个区别在最新的Go tips中已经没有了，即：delete一个nil map也不会panic）

3 通过fmt打印map时，空map和nil map结果是一样的：

通过fmt打印map时，空map和nil map结果是一样的，都为map[]。所以，这个时候别断定map是空还是
nil，而应该通过map == nil来判断。
Request中的Form字段就是如此，在没有直接或间接调用ParseForm()时，Form其实是nil，但是，
你如果println出来，却是map[]，可能有些困惑。通过跟踪源码可以发现，Form根本没有初始化。
而在FormValue()方法中会判断Form是否为nil，然后决定是否调用ParseForm()方法，
当然，你也可以手动调用ParseForm()方法。
```
