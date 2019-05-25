package main

import "fmt"

func updateSlice(s []int) {
	s[0] = 100
}

func main() {
	arr := [...]int{0, 1, 2, 3, 4, 5, 6, 7}

	fmt.Println("arr[2:6] =", arr[2:6])
	fmt.Println("arr[:6] =", arr[:6])
	s1 := arr[2:]
	fmt.Println("s1 =", s1)
	s2 := arr[:]
	fmt.Println("s2 =", s2)

	fmt.Println("After updateSlice(s1)")
	updateSlice(s1)
	fmt.Println(s1)
	fmt.Println(arr)

	fmt.Println("After updateSlice(s2)")
	updateSlice(s2)
	fmt.Println(s2)
	fmt.Println(arr)

	fmt.Println("Reslice")
	fmt.Println(s2)
	s2 = s2[:5]
	fmt.Println(s2)
	s2 = s2[2:]
	fmt.Println(s2)

	fmt.Println("Extending slice")
	arr[0], arr[2] = 0, 2
	fmt.Println("arr =", arr)
	s1 = arr[2:6]
	s2 = s1[3:5] // [s1[3], s1[4]]
	fmt.Printf("s1=%v, len(s1)=%d, cap(s1)=%d\n",
		s1, len(s1), cap(s1))
	fmt.Printf("s2=%v, len(s2)=%d, cap(s2)=%d\n",
		s2, len(s2), cap(s2))

	s3 := append(s2, 10)
	s4 := append(s3, 11)
	s5 := append(s4, 12)
	fmt.Println("s3, s4, s5 =", s3, s4, s5)
	// s4 and s5 no longer view arr.
	fmt.Println("arr =", arr)

	// Uncomment to run sliceOps demo.
	// If we see undefined: sliceOps
	// please try go run slices.go sliceops.go
	fmt.Println("Uncomment to see sliceOps demo")
	// sliceOps()
}



/*
[理解Go数组和切片的内部实现原理](https://i6448038.github.io/2018/08/11/array-and-slice-principle/)


// 关于数组扩容
// 两条规则：
// 1
// 如果切片的容量小于1024个元素，那么扩容的时候slice的cap就翻番，乘以2；
// 一旦元素个数超过1024个元素，增长因子就变成1.25，即每次增加原来容量的四分之一。
// 2
// 如果扩容之后，还没有触及原数组的容量，那么，切片中的指针指向的位置，就还是原数组，
// 如果扩容之后，超过了原数组的容量，那么，Go就会开辟一块新的内存，
// 把原来的值拷贝过来，这种情况丝毫不会影响到原数组

package main

import (
	"fmt"
)

func main() {
	array := [4]int{10, 20, 30, 40}
	slice := array[0:2]
	fmt.Println(slice, len(slice),cap(slice))

	newSlice := append(slice, 50)
	newSlice[1] += 100
	fmt.Println(newSlice, len(newSlice),cap(newSlice))

	newSlice1 := append(newSlice, 100)
	fmt.Println(newSlice1, len(newSlice1),cap(newSlice1))

	newSlice2 := append(newSlice1, 150)
	fmt.Println(newSlice2, len(newSlice2),cap(newSlice2))

	newSlice2[1] += 1
	fmt.Println(newSlice2, len(newSlice2),cap(newSlice2))

	fmt.Println(slice, len(slice),cap(slice))
	fmt.Println(array, len(array),cap(array))
}


//[10 20] 2 4
//[10 120 50] 3 4
//[10 120 50 100] 4 4
//[10 120 50 100 150] 5 8
//[10 121 50 100 150] 5 8
//[10 120] 2 4
//[10 120 50 100] 4 4

*/
