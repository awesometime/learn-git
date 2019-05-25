/*
 函数式编程 闭包
*/

package main

import "fmt"

/*
python 闭包
def adder():
	sum := 0
	def func(value):
		nonlocal sum
        sum += value
		return sum
    return func
*/

// 更好理解
func adder() func(int) int {
	sum := 0
	return func(v int) int {
		sum += v
		return sum
	}
}

// 严格的正统 函数式编程
type iAdder func(int) (int, iAdder)

func adder2(base int) iAdder {
	return func(v int) (int, iAdder) {
		return base + v, adder2(base + v)
	}
}

func main() {
	a0 := adder() // a0 == func(v int) int { sum += v return sum}  没名字函数
	for i := 0; i < 10; i++ {
		fmt.Printf("0 + 1 + ... + %d = %d\n", i, a0(i))
	}
	// a0() == func()

	// 和上面不一样
	for i := 0; i < 10; i++ {
		fmt.Printf("0 + 1 + ... + %d = %d\n",
			i, adder()(i))
	}

	// 正统的 函数式编程 但不好理解 没必要这样用
	// a := adder() is trivial and also works.
	a := adder2(0)
	for i := 0; i < 10; i++ {
		var s int
		s, a = a(i)
		fmt.Printf("0 + 1 + ... + %d = %d\n", i, s)
	}
}
