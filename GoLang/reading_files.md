https://mp.weixin.qq.com/s/oUMv8zf9OBYJ65ZZ8EMWTw

### 1

将整个文件读取到内存

分块读取文件

逐行读取文件

### 2

使用绝对文件路径

使用命令行标记来传递文件路径

将文件绑定在二进制文件中

### 4种读写方法

[完美 Golang读写文件的方式 总览](https://www.jianshu.com/p/7790ca1bc8f6)

[和上边一样  Golang简单写文件操作的四种方法](https://studygolang.com/articles/2073)

由于os.Open是打开一个文件并返回一个文件对象file struct，因此其实可以结合ioutil.ReadAll(r io.Reader)来进行读取。

io.Reader其实是一个包含Read方法的接口类型，而文件对象本身是实现了了Read方法的。

文件对象 `file struct` 实现了 `io.Reader接口` 里的 `Read方法` 就可以在一个需要 `io.Reader接口类型变量`做参数的

函数 (比如ioutil.ReadAll) 中作为参数使用

[参考](https://gobyexample.com/interfaces)

```go
//io.Reader 是一个接口
//src/io/io.go
type Reader interface {
	Read(p []byte) (n int, err error)
}

//os.Open() 返回一个文件对象 struct
//src/os/file.go
func Open(name string) (*File, error) {
	return OpenFile(name, O_RDONLY, 0)
}

type File struct {
	*file // os specific
}

type file struct {
	pfd     poll.FD
	name    string
	dirinfo *dirInfo // nil unless directory being read
}

//文件对象实现了Read Write Close 等方法
func (f *File) pread(b []byte, off int64) (n int, err error) {
	n, err = f.pfd.Pread(b, off)
	runtime.KeepAlive(f)
	return n, err
}
```

src/bufio/bufio.go
```go
//首先定义了一个用来缓冲io.Reader对象的结构体，同时该结构体拥有以下相关的方法
// Reader 是一个struct
type Reader struct {
	buf          []byte
	rd           io.Reader // reader provided by the client
	r, w         int       // buf read and write positions
	err          error
	lastByte     int // last byte read for UnreadByte; -1 means invalid
	lastRuneSize int // size of last rune read for UnreadRune; -1 means invalid
}

//NewReader函数用来返回一个默认大小buffer的Reader对象(默认大小好像是4096) 等同于NewReaderSize(rd,4096)
func NewReader(rd io.Reader) *Reader         // Reader 是一个struct



//该函数返回一个指定大小buffer(size最小为16)的Reader对象，如果 io.Reader参数已经是一个足够大的Reader，它将返回该Reader
func NewReaderSize(rd io.Reader, size int) *Reader


//该方法返回从当前buffer中能被读到的字节数
func (b *Reader) Buffered() int

//Discard方法跳过后续的 n 个字节的数据，返回跳过的字节数。如果0 <= n <= b.Buffered(),该方法将不会从io.Reader中成功读取数据。
func (b *Reader) Discard(n int) (discarded int, err error)

//Peekf方法返回缓存的一个切片，该切片只包含缓存中的前n个字节的数据
func (b *Reader) Peek(n int) ([]byte, error)

//把Reader缓存对象中的数据读入到[]byte类型的p中，并返回读取的字节数。读取成功，err将返回空值
func (b *Reader) Read(p []byte) (n int, err error)

//返回单个字节，如果没有数据返回err
func (b *Reader) ReadByte() (byte, error)

//该方法在b中读取delimz之前的所有数据，返回的切片是已读出的数据的引用，切片中的数据在下一次的读取操作之前是有效的。如果未找到delim，将返回查找结果并返回nil空值。因为缓存的数据可能被下一次的读写操作修改，因此一般使用ReadBytes或者ReadString，他们返回的都是数据拷贝
func (b *Reader) ReadSlice(delim byte) (line []byte, err error)

//功能同ReadSlice，返回数据的拷贝
func (b *Reader) ReadBytes(delim byte) ([]byte, error)

//功能同ReadBytes,返回字符串
func (b *Reader) ReadString(delim byte) (string, error)

//该方法是一个低水平的读取方式，一般建议使用ReadBytes('\n') 或 ReadString('\n')，或者使用一个 Scanner来代替。ReadLine 通过调用 ReadSlice 方法实现，返回的也是缓存的切片，用于读取一行数据，不包括行尾标记（\n 或 \r\n）
func (b *Reader) ReadLine() (line []byte, isPrefix bool, err error)

//读取单个UTF-8字符并返回一个rune和字节大小
func (b *Reader) ReadRune() (r rune, size int, err error)
```
