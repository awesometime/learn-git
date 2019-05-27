package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	s := "Yes我爱你慕课网!" // UTF-8
	fmt.Println(s)

	fmt.Printf("%s\n", []byte(s))
	fmt.Printf("%X\n", []byte(s))
	fmt.Println("\n")

	// []byte获得每个字节
	fmt.Println("len(s): ", len(s)) // 22  UTF-8字节数
	// python len 不同
	// s = "Yes我爱你慕课网!"
	// print(len(s))    # 10
	fmt.Println("[]byte(s) 按字节遍历 获得每个字节: ")
	for _, b := range []byte(s) {
		fmt.Printf("%X ", b)
	}
	fmt.Println("\n")

	// utf8 英文1字节 中文3字节
	// utf8.decode成 unicode(2字节)
	fmt.Println("utf8.decode 成 unicode(2字节): ")
	fmt.Println("这样遍历是按字节遍历 (注意 不是我们常见的应用场景 我们通常是按字符遍历) ")
	for i, ch := range s { // ch is a rune
		fmt.Printf("(%d %X) ", i, ch)
	}
	fmt.Println("\n")

	// utf8.DecodeRune(bytes)
	bytes := []byte(s)
	for len(bytes) > 0 {
		ch, size := utf8.DecodeRune(bytes)
		fmt.Printf("(%d %c) ", size, ch)
		bytes = bytes[size:]
		// fmt.Printf("%c ", ch)
	}
	fmt.Println("\n")

	// 使用 utf8.RuneCountInString 获得字符数量
	fmt.Println("字符数量 Rune count:",
		utf8.RuneCountInString(s))
	// 按字符个数打印 遍历的正确用法 按字符遍历
	fmt.Println("[]rune(s) 按字符遍历:")
	for i, ch := range []rune(s) {
		fmt.Printf("(%d %c) ", i, ch)
	}
	fmt.Println()

}

/*
Yes我爱你慕课网!
Yes我爱你慕课网!
596573E68891E788B1E4BDA0E68595E8AFBEE7BD9121


len(s):  22
[]byte(s) 按字节遍历 获得每个字节:
59 65 73 E6 88 91 E7 88 B1 E4 BD A0 E6 85 95 E8 AF BE E7 BD 91 21

utf8.decode 成 unicode(2字节):
这样遍历是按字节遍历 (注意 不是我们常见的应用场景 我们通常是按字符遍历)
(0 59) (1 65) (2 73) (3 6211) (6 7231) (9 4F60) (12 6155) (15 8BFE) (18 7F51) (21 21)

(1 Y) (1 e) (1 s) (3 我) (3 爱) (3 你) (3 慕) (3 课) (3 网) (1 !)

字符数量 Rune count: 10
[]rune(s) 按字符遍历:
(0 Y) (1 e) (2 s) (3 我) (4 爱) (5 你) (6 慕) (7 课) (8 网) (9 !)
*/

/*
bool string
(u)int,(u)int8,(u)int16,(u)int32,(u)int64,uintptr    int不指明时在32位机器是32位,在64位机器是64位
byte(8) rune(32)=int32
float32 float64 complex64 complex128

// unicode是一个标准   2字节
// utf8               可变长 英文1字节 中文3字节


[]byte(s)  获得每个字节
[]rune(s)  获得每个字符


strings.Fields()
strings.Split()
strings.Join()
strings.Contains()
strings.Index()
strings.ToLower()
strings.ToUpper()
strings.Trim()
strings.TrimLeft()
strings.TrimRight()
*/
