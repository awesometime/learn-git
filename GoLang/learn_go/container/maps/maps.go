/*
解剖Go语言map底层实现
https://i6448038.github.io/2018/08/26/map-secret/
*/


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
