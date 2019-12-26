package main

import "fmt"

func bit(v uint32) uint32 {
	v--

	//fmt.Println(1785>>2)   // 446
	//fmt.Println(2047>>4)   // 127
	//fmt.Println(2047>>8)   // 7
	//fmt.Println(2047>>16)  // 0
	//fmt.Println(1233|616)  // 1785
	//fmt.Println(1785|446)  // 2047
	//fmt.Println(2047|127)  // 2047
	//fmt.Println(2047|7)    // 2047
	//fmt.Println(2047|0)    // 2047

	fmt.Println(v)  // 1233
	v |= (v >> 1)  // v = 1233|616   或
	fmt.Println(v) // 1785
	v |= v >> 2    // v = 1785|446
	fmt.Println(v) // 2047
	v |= v >> 4    // v = 2047|
	fmt.Println(v) // 2047
	v |= v >> 8
	fmt.Println(v) // 2047
	v |= v >> 16
	fmt.Println(v) // 2047
	v++
	fmt.Println(v) // 2048
	return v
}

func main() {
	a:=bit(1234)
	fmt.Println()
	fmt.Println(a)
}
