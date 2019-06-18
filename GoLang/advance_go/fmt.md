[go  中文官方文档](http://zh-golang.appspot.com/)

[fmt 中文官方文档](http://zh-golang.appspot.com/pkg/fmt/)


```
写数据 print
   写入到标准输出   print
   写入到文件对象   Fprint
   写入成字符串形式返回给变量  Sprint
读数据 scan
   从标准输入中读取  Scan 
   从文件对象中读取  Fscan
   从字符串中读取    Sscan 
```


```go
func Errorf(format string, a ...interface{}) error


// 1 任意对象读写

// 将 参数列表 a 中的各个参数 按默认格式 写入 w 对象
func Fprint(w io.Writer, a ...interface{}) (n int, err error)
// 将 参数列表 a 中的各个参数 填写到格式字符串 format 的占位符中
func Fprintf(w io.Writer, format string, a ...interface{}) (n int, err error)
func Fprintln(w io.Writer, a ...interface{}) (n int, err error)
// 从r对象读入
func Fscan(r io.Reader, a ...interface{}) (n int, err error)
func Fscanf(r io.Reader, format string, a ...interface{}) (n int, err error)
func Fscanln(r io.Reader, a ...interface{}) (n int, err error)


// 2 标准输入输出读写

// 将`a ...interface{}`按格式 format 写入 `标准输出std.out`
func Print(a ...interface{}) (n int, err error)
func Printf(format string, a ...interface{}) (n int, err error)
func Println(a ...interface{}) (n int, err error)
// 从 标准输入std.in 读入
func Scan(a ...interface{}) (n int, err error)
func Scanf(format string, a ...interface{}) (n int, err error)
func Scanln(a ...interface{}) (n int, err error)


// 3 将转换结果以字符串形式返回(写) /或者从字符串中读入

func Sprint(a ...interface{}) string
func Sprintf(format string, a ...interface{}) string
func Sprintln(a ...interface{}) string
// Scanf 扫描实参 string，并将连续由空格分隔的值存储为连续的实参， 其格式由 format 决定。它返回成功解析的条目数。
func Sscan(str string, a ...interface{}) (n int, err error)
func Sscanf(str string, format string, a ...interface{}) (n int, err error)
func Sscanln(str string, a ...interface{}) (n int, err error)


type Formatter
type GoStringer
type ScanState
type Scanner
type State
type Stringer
```

例子
```go
func main() {
	count := 1
	v := fmt.Sprint("这是我的第%d个程序", count)
	fmt.Print(v)
}
// 这是我的第%d个程序1
```

函数签名
```go
func Errorf
func Errorf(format string, a ...interface{}) error
Errorf 根据于格式说明符进行格式化并将字符串a ...interface{}作为满足 error 的值返回。
```

```go
func Fprint
func Fprint(w io.Writer, a ...interface{}) (n int, err error)
// Fprint 使用 `默认格式`将`a ...interface{}`进行格式化并写入到 `w 对象(struct)`中。 当两个连续的操作数均不为字符串时，它们之间就会添加空格。 它返回写入的字节数以及任何遇到的错误。

func Fprintf
func Fprintf(w io.Writer, format string, a ...interface{}) (n int, err error)
//Fprintf 根据格式说明符`format`将`a ...interface{}`进行格式化并写入到 `w`。 它返回写入的字节数以及任何遇到的写入错误。

func Fprintln
func Fprintln(w io.Writer, a ...interface{}) (n int, err error)
//Fprintln 使用其操作数的默认格式进行格式化并写入到 w。 其操作数之间总是添加空格，且总在最后`追加一个换行符`。 它返回写入的字节数以及任何遇到的错误。

func Fscan
func Fscan(r io.Reader, a ...interface{}) (n int, err error)
//Fscan 扫描从 r 中读取的文本，并将连续由空格分隔的值存储为连续的实参。 换行符计为空格。它返回成功扫描的条目数。若它少于实参数，err 就会报告原因。

func Fscanf
func Fscanf(r io.Reader, format string, a ...interface{}) (n int, err error)
//Fscanf 扫描从 r 中读取的文本，并将连续由空格分隔的值存储为连续的实参， 其格式由 format 决定。它返回成功解析的条目数。

func Fscanln
func Fscanln(r io.Reader, a ...interface{}) (n int, err error)
//Fscanln 类似于 Sscan，但它在换行符处停止扫描，且最后的条目之后必须为换行符或 EOF。
```

```go
func Print
func Print(a ...interface{}) (n int, err error)
Print 使用其操作数的默认格式进行格式化并写入到标准输出。 当两个连续的操作数均不为字符串时，它们之间就会添加空格。 它返回写入的字节数以及任何遇到的错误。

func Printf
func Printf(format string, a ...interface{}) (n int, err error)
Printf 根据于格式说明符进行格式化并写入到标准输出。 它返回写入的字节数以及任何遇到的写入错误。

func Println
func Println(a ...interface{}) (n int, err error)
Fprintln 使用其操作数的默认格式进行格式化并写入到标准输出。 其操作数之间总是添加空格，且总在最后追加一个换行符。 它返回写入的字节数以及任何遇到的错误。

func Scan
func Scan(a ...interface{}) (n int, err error)
Scan 扫描从标准输入中读取的文本，并将连续由空格分隔的值存储为连续的实参。 换行符计为空格。它返回成功扫描的条目数。若它少于实参数，err 就会报告原因。

func Scanf
func Scanf(format string, a ...interface{}) (n int, err error)
Scanf 扫描从标准输入中读取的文本，并将连续由空格分隔的值存储为连续的实参， 其格式由 format 决定。它返回成功扫描的条目数。

func Scanln
func Scanln(a ...interface{}) (n int, err error)
Scanln 类似于 Scan，但它在换行符处停止扫描，且最后的条目之后必须为换行符或 EOF。
```

```go
func Sprint
func Sprint(a ...interface{}) string
Sprint 使用其操作数的默认格式进行格式化并返回其结果字符串。 当两个连续的操作数均不为字符串时，它们之间就会添加空格。

func Sprintf
func Sprintf(format string, a ...interface{}) string
Fprintf 根据于格式说明符进行格式化并返回其结果字符串。

func Sprintln
func Sprintln(a ...interface{}) string
Fprintln 使用其操作数的默认格式进行格式化并写返回其结果字符串。 其操作数之间总是添加空格，且总在最后追加一个换行符。

func Sscan
func Sscan(str string, a ...interface{}) (n int, err error)
Sscan 扫描实参 string，并将连续由空格分隔的值存储为连续的实参。 换行符计为空格。它返回成功扫描的条目数。若它少于实参数，err 就会报告原因。

func Sscanf
func Sscanf(str string, format string, a ...interface{}) (n int, err error)
Scanf 扫描实参 string，并将连续由空格分隔的值存储为连续的实参， 其格式由 format 决定。它返回成功解析的条目数。

func Sscanln
func Sscanln(str string, a ...interface{}) (n int, err error)
Sscanln 类似于 Sscan，但它在换行符处停止扫描，且最后的条目之后必须为换行符或 EOF。
```

```go
type Formatter
type Formatter interface {
        Format(f State, c rune)
}
Formatter 接口由带有定制的格式化器的值所实现。 Format 的实现可调用 Sprintf 或 Fprintf(f) 等函数来生成其输出。

type GoStringer
type GoStringer interface {
        GoString() string
}
GoStringer 接口由任何拥有 GoString 方法的值所实现，该方法定义了该值的Go语法格式。 GoString 方法用于打印作为操作数传至 %#v 进行格式化的值。

type ScanState
type ScanState interface {
        // ReadRune reads the next rune (Unicode code point) from the input.
        // If invoked during Scanln, Fscanln, or Sscanln, ReadRune() will
        // return EOF after returning the first '\n' or when reading beyond
        // the specified width.
        //
        // ReadRune 从输入中读取下一个符文（Unicode码点）。若它在 Scanln、Fscanln 或
        // Sscanln 中被调用，ReadRune() 就会在返回第一个“\n”或读取至指定宽度后返回 EOF。
        ReadRune() (r rune, size int, err error)
        // UnreadRune causes the next call to ReadRune to return the same rune.
        // UnreadRune 会使 ReadRune 的下一次调用返回相同的符文。
        UnreadRune() error
        // SkipSpace skips space in the input. Newlines are treated as space
        // unless the scan operation is Scanln, Fscanln or Sscanln, in which case
        // a newline is treated as EOF.
        //
        // SkipSpace 跳过输入中的空格。换行符会被视作空格，除非该扫描操作为 Scanln、
        // Fscanln 或 Sscanln，在这种情况下，换行符会被视作 EOF。
        SkipSpace()
        // Token skips space in the input if skipSpace is true, then returns the
        // run of Unicode code points c satisfying f(c).  If f is nil,
        // !unicode.IsSpace(c) is used; that is, the token will hold non-space
        // characters.  Newlines are treated as space unless the scan operation
        // is Scanln, Fscanln or Sscanln, in which case a newline is treated as
        // EOF.  The returned slice points to shared data that may be overwritten
        // by the next call to Token, a call to a Scan function using the ScanState
        // as input, or when the calling Scan method returns.
        //
        // Token 会在 skipSpace 为 true 时从输入中跳过空格，然后返回一系列满足 f(c)
        // 的Unicode码点 c。若 f 为 nil，就会使用 !unicode.IsSpace(c)；
        // 即，该标记会保留非空格字符。换行符会被视作空格，除非该扫描操作为 Scanln、
        // Fscanln 或 Sscanln，否则在这种情况下，换行符会被视作 EOF。
        // 所返回的指向共享数据的切片可能会在下次调用 Token 时被覆盖，Scan 函数的调用
        // 会将 ScanState 用作输入，或当调用 Scan 方法返回时也会。
        Token(skipSpace bool, f func(rune) bool) (token []byte, err error)
        // Width returns the value of the width option and whether it has been set.
        // The unit is Unicode code points.
        // Width 返回宽度选项的值，并判断它是否被设置。其单元为Unicode码点。
        Width() (wid int, ok bool)
        // Because ReadRune is implemented by the interface, Read should never be
        // called by the scanning routines and a valid implementation of
        // ScanState may choose always to return an error from Read.
        //
        // 由于 ReadRune 被此接口实现，因此 Read 不应当被扫描功能调用，而 ScanState
        // 的有效实现可选择总是从 Read 中返回错误。
        Read(buf []byte) (n int, err error)
}
ScanState 表示传递给定制扫描器的扫描状态。扫瞄器可一次扫描一个附文或请求 ScanState 发现下一个以空格分隔的标记。

type Scanner
type Scanner interface {
        Scan(state ScanState, verb rune) error
}
Scanner 由任何拥有 Scan 方法的值实现，它将输入扫描成值的表示，并将其结果存储到接收者中， 该接收者必须为可用的指针。Scan 方法会被 Scan、Scanf 或 Scanln 的任何实现了它的实参所调用。

type State
type State interface {

        // Write 函数用于打印出已格式化的输出。
        Write(b []byte) (ret int, err error)

        // Width 返回宽度选项的值以及它是否已被设置。
        Width() (wid int, ok bool)

        // Precision 返回精度选项的值以及它是否已被设置。
        Precision() (prec int, ok bool)

        // Flag 返回标记 c（一个字符）是否已被设置。
        Flag(c int) bool
}
State 表示传递给格式化器的打印器的状态。 它提供了访问 io.Writer 接口及关于标记的信息，以及操作数的格式说明符选项。

type Stringer
type Stringer interface {
        String() string
}
Stringer 接口由任何拥有 String 方法的值所实现，该方法定义了该值的“原生”格式。 String 方法用于打印值，该值可作为操作数传至任何接受字符串的格式，或像 Print 这样的未格式化打印器。
```
