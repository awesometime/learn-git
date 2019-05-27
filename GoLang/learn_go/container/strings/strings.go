package main

import (
	"fmt"
	"os"
	"unicode/utf8"
)

func m1() {

	str := "hello, 世界"
	n := len(str)

	for i := 0; i < n; i++ {
		fmt.Fprintf(os.Stdout, "%d  %v  %c\n", i, str[i], str[i])
	}

	fmt.Fprintf(os.Stdout, "---------------\n")

	for i, v := range str {
		fmt.Fprintf(os.Stdout, "%d  %v  %c\n", i, v, v)
	}

	fmt.Fprintf(os.Stdout, "---------------\n")

	rs := []rune(str)
	n = len(rs)
	for i := 0; i < n; i++ {
		fmt.Fprintf(os.Stdout, "%d  %v  %c\n", i, rs[i], rs[i])
	}

}

func main() {
	m1()
	fmt.Println()

	s := "Yes我爱你慕课网!" // UTF-8
	fmt.Println(s)

	fmt.Printf("%s\n", []byte(s))
	fmt.Printf("%X\n", []byte(s))
	fmt.Println()

	// 1--- for i := 0; i < length; i++    s[i]
	// []byte获得每个字节
	fmt.Println("1--- for i := 0; i < length; i++    s[i] 或者[]byte(s)")
	fmt.Println("len(s): ", len(s)) // 22  UTF-8字节数
	// python len 不同
	// s = "Yes我爱你慕课网!"
	// print(len(s))    # 10
	length := len(s)
	for i := 0; i < length; i++ {
		fmt.Printf("(%X %c) ", s[i], s[i])
	}
	fmt.Println()

	for i := 0; i < length; i++ {
		fmt.Printf("(%v %c) ", s[i], s[i])
	}
	fmt.Println()

	fmt.Println("[]byte(s) 按字节遍历 获得每个字节: ")
	for _, b := range []byte(s) {
		fmt.Printf("%X ", b)
	}
	fmt.Println("\n")

	// 2--- for i, ch := range s
	// utf8 英文1字节 中文3字节
	// utf8.decode成 unicode(2字节)
	fmt.Println("2--- for i, ch := range s ")
	fmt.Println("utf8.decode 成 unicode(2字节): ")
	fmt.Println("按字节遍历 并且中文会跳 (注意 不是我们常见的应用场景 我们通常是按字符遍历) ")
	for i, ch := range s { // ch is a rune
		fmt.Printf("(%d %X) ", i, ch)
	}
	fmt.Println("\n")

	// 补充---utf8.DecodeRune(bytes)
	fmt.Println("补充---utf8.DecodeRune(bytes)")
	bytes := []byte(s)
	for len(bytes) > 0 {
		ch, size := utf8.DecodeRune(bytes)
		fmt.Printf("(%d %c) ", size, ch)
		bytes = bytes[size:]
		// fmt.Printf("%c ", ch)
	}
	fmt.Println("\n")

	// 3--- for i, ch := range []rune(s)
	// 使用 utf8.RuneCountInString 获得字符数量
	fmt.Println("3--- for i, ch := range []rune(s)")
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
0  104  h
1  101  e
2  108  l
3  108  l
4  111  o
5  44  ,
6  32
7  228  ä
8  184  ¸
9  150  
10  231  ç
11  149  
12  140  
---------------
0  104  h
1  101  e
2  108  l
3  108  l
4  111  o
5  44  ,
6  32
7  19990  世
10  30028  界
---------------
0  104  h
1  101  e
2  108  l
3  108  l
4  111  o
5  44  ,
6  32
7  19990  世
8  30028  界

Yes我爱你慕课网!
Yes我爱你慕课网!
596573E68891E788B1E4BDA0E68595E8AFBEE7BD9121

1--- for i := 0; i < length; i++    s[i] 或者[]byte(s)
len(s):  22
(59 Y) (65 e) (73 s) (E6 æ) (88 ) (91 ) (E7 ç) (88 ) (B1 ±) (E4 ä) (BD ½) (A0  ) (E6 æ) (85 ) (95 ) (E8 è) (AF ¯) (BE ¾) (E7 ç) (BD ½) (91 ) (21 !)
(89 Y) (101 e) (115 s) (230 æ) (136 ) (145 ) (231 ç) (136 ) (177 ±) (228 ä) (189 ½) (160  ) (230 æ) (133 ) (149 ) (232 è) (175 ¯) (190 ¾) (231 ç) (189 ½) (145 ) (33 !)
[]byte(s) 按字节遍历 获得每个字节:
59 65 73 E6 88 91 E7 88 B1 E4 BD A0 E6 85 95 E8 AF BE E7 BD 91 21

2--- for i, ch := range s
utf8.decode 成 unicode(2字节):
按字节遍历 并且中文会跳 (注意 不是我们常见的应用场景 我们通常是按字符遍历)
(0 59) (1 65) (2 73) (3 6211) (6 7231) (9 4F60) (12 6155) (15 8BFE) (18 7F51) (21 21)

补充---utf8.DecodeRune(bytes)
(1 Y) (1 e) (1 s) (3 我) (3 爱) (3 你) (3 慕) (3 课) (3 网) (1 !)

3--- for i, ch := range []rune(s)
字符数量 Rune count: 10
[]rune(s) 按字符遍历:
(0 Y) (1 e) (2 s) (3 我) (4 爱) (5 你) (6 慕) (7 课) (8 网) (9 !)
*/

/*
bool string
(u)int,(u)int8,(u)int16,(u)int32,(u)int64,uintptr    int不指明时在32位机器是32位,在64位机器是64位
byte(uint8) rune(uint32)=int32
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
