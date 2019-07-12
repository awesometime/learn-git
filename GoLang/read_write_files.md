学习接口一个比较好的方法是通过io包的例子

- [读取文件全部示例](#读取文件全部示例)
  - [1 使用ioutil直接读取](#1-使用ioutil直接读取)
  - [2 借助 os.Open 和 ioutil.ReadAll()进行读取文件](#2-借助-os.Open-和-ioutil.ReadAll()进行读取文件)
  - [3 使](#3-使)
  - [4 使](#4-使)
- [写文件全部示例](#写文件全部示例)
  - [1 使](#1-使)
  - [2 使](#2-使)
  - [3 使](#3-使)
  - [4 使](#4-使)
- [4种读写方法解读](#4种读写方法解读)
- [读取用户输入键盘控制台以及从命令行读取参数](#读取用户输入键盘控制台以及从命令行读取参数)
- [JSON 数据格式](#JSON-数据格式)
- [XML 数据格式](#XML-数据格式)
- [gob](#gob)

## 读取文件全部示例

```go
/**
 * @File Name: readfile.go
 * @Description:读取指定文件的几种方法，需要注意的是[]byte类型在转换成string类型的时候，都会在最后多一行空格，需要使用result := strings.Replace(string(contents),"\n","",1) 方式替换换行符
 */
 
package main
import (
    "fmt"
    "io/ioutil"
    "strings"
    "os"
    "strconv"
    "bufio"
)

func main() {
   Ioutil("mytestfile.txt")
   OsIoutil("mytestfile.txt")
   FileRead("mytestfile.txt")
   BufioRead("mytestfile.txt")
    }

//src
//    filename
//       filename.go
//       test.txt	
// 解决不在src下文件读取问题   https://mp.weixin.qq.com/s/oUMv8zf9OBYJ65ZZ8EMWTw
// 1 使用绝对文件路径
// 2 使用命令行标记来传递文件路径 
//    fptr := flag.String("fpath", "test.txt", "file path to read from")
//    flag.Parse()
//    data, err := ioutil.ReadFile(*fptr)
// 3 将文件绑定在二进制文件中   安装 packr 包


// ioutil.ReadFile
func Ioutil(name string) {
    if contents,err := ioutil.ReadFile(name);err == nil {
        //因为contents是[]byte类型，直接转换成string类型后会多一行空格,需要使用strings.Replace替换换行符
        result := strings.Replace(string(contents),"\n","",1)
        fmt.Println("Use ioutil.ReadFile to read a file:",result)
        }
    }

// 
func OsIoutil(name string) {
      if fileObj,err := os.Open(name);err == nil {
      //if fileObj,err := os.OpenFile(name,os.O_RDONLY,0644); err == nil {
        defer fileObj.Close()
        if contents,err := ioutil.ReadAll(fileObj); err == nil {
            result := strings.Replace(string(contents),"\n","",1)
            fmt.Println("Use os.Open family functions and ioutil.ReadAll to read a file :",result)
            }

        }
}


func FileRead(name string) {
    if fileObj,err := os.Open(name);err == nil {
        defer fileObj.Close()
        //在定义空的byte列表时尽量大一些，否则这种方式读取内容可能造成文件读取不完整
        buf := make([]byte, 1024)
        if n,err := fileObj.Read(buf);err == nil {
               fmt.Println("The number of bytes read:"+strconv.Itoa(n),"Buf length:"+strconv.Itoa(len(buf)))
               result := strings.Replace(string(buf),"\n","",1)
               fmt.Println("Use os.Open and File's Read method to read a file:",result)
            }
    }
}

//带缓冲的读取
func BufioRead(name string) {
    if fileObj,err := os.Open(name);err == nil {
        defer fileObj.Close()
        //一个文件对象本身是实现了io.Reader的 使用bufio.NewReader去初始化一个Reader对象，存在buffer中的，读取一次就会被清空
        reader := bufio.NewReader(fileObj)
        //使用ReadString(delim byte)来读取delim以及之前的数据并返回相关的字符串.
        if result,err := reader.ReadString(byte('@'));err == nil {
            fmt.Println("使用ReadSlince相关方法读取内容:",result)
        }
        //注意:上述ReadString已经将buffer中的数据读取出来了，下面将不会输出内容
        //需要注意的是，因为是将文件内容读取到[]byte中，因此需要对大小进行一定的把控
        buf := make([]byte,1024)
        //读取Reader对象中的内容到[]byte类型的buf中
        if n,err := reader.Read(buf); err == nil {
            fmt.Println("The number of bytes read:"+strconv.Itoa(n))
            //这里的buf是一个[]byte，因此如果需要只输出内容，仍然需要将文件内容的换行符替换掉
            fmt.Println("Use bufio.NewReader and os.Open read file contents to a []byte:",string(buf))
        }


    }
}
```

#### 1 使用ioutil直接读取

```go
// 需要引入io/ioutil包，该包默认拥有以下函数供用户调用。

func NopCloser(r io.Reader) io.ReadCloser
func ReadAll(r io.Reader) ([]byte, error)
func ReadDir(dirname string) ([]os.FileInfo, error)
func ReadFile(filename string) ([]byte, error)
func TempDir(dir, prefix string) (name string, err error)
func TempFile(dir, prefix string) (f *os.File, err error)
func WriteFile(filename string, data []byte, perm os.FileMode) error
//读文件，我们可以看以下三个函数:

// 从一个io.Reader类型中读取内容直到返回错误或者EOF时返回读取的数据，当err == nil时，数据成功读取到[]byte中
// ReadAll函数被定义为从源中读取数据直到EOF，它是不会去从返回数据中去判断EOF来作为读取成功的依据
func ReadAll(r io.Reader) ([]byte, error)

// 读取一个目录，并返回一个当前目录下的文件对象列表和错误信息
func ReadDir(dirname string) ([]os.FileInfo, error)

// 读取文件内容，并返回[]byte数据和错误信息。err == nil时，读取成功
func ReadFile(filename string) ([]byte, error)
```

#### 2 借助 os.Open 和 ioutil.ReadAll()进行读取文件

由于os.Open是打开一个文件并返回一个文件对象，因此其实可以结合ioutil.ReadAll(r io.Reader)来进行读取。

io.Reader其实是一个包含Read方法的接口类型，而文件对象本身是实现了了Read方法的。

我们先来看下os.Open家族的相关函数

```go
// 打开一个需要被读取的文件，如果成功读取，返回的文件对象将可用被读取，该函数默认的权限为O_RDONLY，也就是只对文件有
// 只读权限。如果有错误，将返回*PathError类型
func Open(name string) (*File, error)

// 大部分用户会选择该函数来代替Open or Create函数。该函数主要用来指定参数(os.O_APPEND|os.O_CREATE|os.O_WRONLY)
// 以及文件权限(0666)来打开文件，如果打开成功返回的文件对象将被用作I/O操作
func OpenFile(name string, flag int, perm FileMode) (*File, error)
```

使用`os.Open`家族函数和`ioutil.ReadAll()`读取文件示例:
```go
func OsIoutil(name string) {
      if fileObj,err := os.Open(name);err == nil {
      //if fileObj,err := os.OpenFile(name,os.O_RDONLY,0644); err == nil {
        defer fileObj.Close()
        if contents,err := ioutil.ReadAll(fileObj); err == nil {
            result := strings.Replace(string(contents),"\n","",1)
            fmt.Println("Use os.Open family functions and ioutil.ReadAll to read a file contents:",result)
            }

        }
}

# 在main函数中调用OsIoutil(name)函数就可以读取文件内容了
$ go run readfile.go
Use os.Open family functions and ioutil.ReadAll to read a file contents: xxbandy.github.io @by Andy_xu
```

#### 3 借助 os.Open 和 fileobj.Read() 进行读取文件

然而上述方式会比较繁琐一些，因为使用了os的同时借助了ioutil,但是在读取大文件的时候还是比较有优势的。不过读取小文件可以

直接使用文件对象的一些方法。

不论是上边说的os.Open还是os.OpenFile他们最终都返回了一个\*File文件对象，而该文件对象默认是有很多方法的，其中读取文件

的方法有如下几种:

```go
//从文件对象中读取长度为b的字节，返回当前读到的字节数以及错误信息。因此使用该方法需要先初始化一个符合内容大小的空的字节列表。读取到文件的末尾时，该方法返回0，io.EOF
func (f *File) Read(b []byte) (n int, err error)

//从文件的off偏移量开始读取长度为b的字节。返回读取到字节数以及错误信息。当读取到的字节数n小于想要读取字节的长度len(b)的时候，该方法将返回非空的error。当读到文件末尾时，err返回io.EOF
func (f *File) ReadAt(b []byte, off int64) (n int, err error)
```

使用`文件对象的Read方法`读取：

```go
func FileRead(name string) {
    if fileObj,err := os.Open(name);err == nil {
        defer fileObj.Close()
        //在定义空的byte列表时尽量大一些，否则这种方式读取内容可能造成文件读取不完整
        buf := make([]byte, 1024)
        if n,err := fileObj.Read(buf);err == nil {
               fmt.Println("The number of bytes read:"+strconv.Itoa(n),"Buf length:"+strconv.Itoa(len(buf)))
               result := strings.Replace(string(buf),"\n","",1)
               fmt.Println("Use os.Open and File's Read method to read a file:",result)
            }
    }
}
```


#### 4 使用 os.Open 和 bufio.Reader 读取文件内容  用缓冲 分块读取

bufio包实现了缓存IO,它本身包装了io.Reader和io.Writer对象，创建了另外的Reader和Writer对象，不过该种方式是带有缓存的，因此对于文本I/O来说，该包是提供了一些便利的。

先看下bufio模块下的相关的Reader函数方法：

bufio/bufio.go
```go
//首先定义了一个用来缓冲io.Reader对象的结构体，同时该结构体拥有以下相关的方法
type Reader struct {
}

//NewReader函数用来返回一个默认大小buffer的Reader对象(默认大小好像是4096) 等同于NewReaderSize(rd,4096)
func NewReader(rd io.Reader) *Reader

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

示例：
```go
func BufioRead(name string) {
    if fileObj,err := os.Open(name);err == nil {
        defer fileObj.Close()
        //一个文件对象本身是实现了io.Reader的 使用bufio.NewReader去初始化一个Reader对象，存在buffer中的，读取一次就会被清空
        reader := bufio.NewReader(fileObj)
        //使用ReadString(delim byte)来读取delim以及之前的数据并返回相关的字符串.
        if result,err := reader.ReadString(byte('@'));err == nil {
            fmt.Println("使用ReadSlince相关方法读取内容:",result)
        }
        //注意:上述ReadString已经将buffer中的数据读取出来了，下面将不会输出内容
        //需要注意的是，因为是将文件内容读取到[]byte中，因此需要对大小进行一定的把控
        buf := make([]byte,1024)
        //读取Reader对象中的内容到[]byte类型的buf中
        if n,err := reader.Read(buf); err == nil {
            fmt.Println("The number of bytes read:"+strconv.Itoa(n))
            //这里的buf是一个[]byte，因此如果需要只输出内容，仍然需要将文件内容的换行符替换掉
            fmt.Println("Use bufio.NewReader and os.Open read file contents to a []byte:",string(buf))
        }


    }
}
```
#### misc

> 逐行读取

bufio/scan.go

```go
// 在文件上新建一个 scanner 扫描文件并且逐行读取
func NewScanner(r io.Reader) *Scanner

func (s *Scanner) Scan() bool
```

> 按列读取文件中的数据
```go
// https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/12.2.md
func main() {
    file, err := os.Open("products2.txt")
    if err != nil {
        panic(err)
    }
    defer file.Close()

    var col1, col2, col3 []string
    for {
        var v1, v2, v3 string
        _, err := fmt.Fscanln(file, &v1, &v2, &v3)
        // scans until newline
        if err != nil {
            break
        }
        col1 = append(col1, v1)
        col2 = append(col2, v2)
        col3 = append(col3, v3)
    }

    fmt.Println(col1)
    fmt.Println(col2)
    fmt.Println(col3)
}

```
> compress包：读取压缩文件

```
https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/12.2.md#1222-compress%E5%8C%85%E8%AF%BB%E5%8F%96%E5%8E%8B%E7%BC%A9%E6%96%87%E4%BB%B6

```

## 写文件全部示例

```go
/**
 * @File Name: writefile.go
 * @Description:使用多种方式将数据写入文件
 */
package main
import (
    "os"
    "io"
    "fmt"
    "io/ioutil"
    "bufio"
)

func main() {
      name := "testwritefile.txt"
      content := "Hello, xxbandy.github.io!\n"
      WriteWithIoutil(name,content)
      contents := "Hello, xuxuebiao\n"
      //清空一次文件并写入两行contents
      WriteWithFileWrite(name,contents)
      WriteWithIo(name,content)
      //使用bufio包需要将数据先读到buffer中，然后在flash到磁盘中
      WriteWithBufio(name,contents)
}

//使用ioutil.WriteFile方式写入文件,是将[]byte内容写入文件,如果content字符串中没有换行符的话，默认就不会有换行符
func WriteWithIoutil(name,content string) {
    data :=  []byte(content)
    if ioutil.WriteFile(name,data,0644) == nil {
        fmt.Println("写入文件成功:",content)
        }
    }

//使用os.OpenFile()相关函数打开文件对象，并使用文件对象的相关方法进行文件写入操作
//清空一次文件
func WriteWithFileWrite(name,content string){
    fileObj,err := os.OpenFile(name,os.O_RDWR|os.O_CREATE|os.O_TRUNC,0644)
    if err != nil {
        fmt.Println("Failed to open the file",err.Error())
        os.Exit(2)
    }
    defer fileObj.Close()
    if _,err := fileObj.WriteString(content);err == nil {
        fmt.Println("Successful writing to the file with os.OpenFile and *File.WriteString method.",content)
    }
    contents := []byte(content)
    if _,err := fileObj.Write(contents);err == nil {
        fmt.Println("Successful writing to thr file with os.OpenFile and *File.Write method.",content)
    }
}


//使用io.WriteString()函数进行数据的写入
func WriteWithIo(name,content string) {
    fileObj,err := os.OpenFile(name,os.O_RDWR|os.O_CREATE|os.O_APPEND,0644)
    if err != nil {
        fmt.Println("Failed to open the file",err.Error())
        os.Exit(2)
    }
    if  _,err := io.WriteString(fileObj,content);err == nil {
        fmt.Println("Successful appending to the file with os.OpenFile and io.WriteString.",content)
    }
}

//使用bufio包中Writer对象的相关方法进行数据的写入
func WriteWithBufio(name,content string) {
    if fileObj,err := os.OpenFile(name,os.O_RDWR|os.O_CREATE|os.O_APPEND,0644);err == nil {
        defer fileObj.Close()
        writeObj := bufio.NewWriterSize(fileObj,4096)
        //
       if _,err := writeObj.WriteString(content);err == nil {
              fmt.Println("Successful appending buffer and flush to file with bufio's Writer obj WriteString method",content)
           }

        //使用Write方法,需要使用Writer对象的Flush方法将buffer中的数据刷到磁盘
        buf := []byte(content)
        if _,err := writeObj.Write(buf);err == nil {
            fmt.Println("Successful appending to the buffer with os.OpenFile and bufio's Writer obj Write method.",content)
            if  err := writeObj.Flush(); err != nil {panic(err)}
            fmt.Println("Successful flush the buffer data to file ",content)
        }
        }
}
```
#### 1 使用ioutil包进行文件写入

```go
// 写入[]byte类型的data到filename文件中，文件权限为perm
func WriteFile(filename string, data []byte, perm os.FileMode) error
```
```go
//使用ioutil.WriteFile方式写入文件,是将[]byte内容写入文件,如果content字符串中没有换行符的话，默认就不会有换行符
func WriteWithIoutil(name,content string) {
    data :=  []byte(content)
    if ioutil.WriteFile(name,data,0644) == nil {
        fmt.Println("写入文件成功:",content)
        }
    }
 
# 会有换行符    
$ go run writefile.go
写入文件成功: Hello, xxbandy.github.io!
```
#### 2 使用os.Open相关函数进行文件写入

因为os.Open系列的函数会打开文件，并返回一个文件对象指针，而该文件对象是一个定义的结构体，拥有一些相关写入的方法。

文件对象结构体以及相关写入文件的方法:
```go
//写入长度为b字节切片到文件f中，返回写入字节号和错误信息。当n不等于len(b)时，将返回非空的err
func (f *File) Write(b []byte) (n int, err error)
//在off偏移量出向文件f写入长度为b的字节
func (f *File) WriteAt(b []byte, off int64) (n int, err error)
//类似于Write方法，但是写入内容是字符串而不是字节切片
func (f *File) WriteString(s string) (n int, err error)
```
注意：使用WriteString()j进行文件写入发现经常新内容写入时无法正常覆盖全部新内容。(是因为字符串长度不一样)

示例：
```go
//使用os.OpenFile()相关函数打开文件对象，并使用文件对象的相关方法进行文件写入操作
func WriteWithFileWrite(name,content string){
    fileObj,err := os.OpenFile(name,os.O_RDWR|os.O_CREATE|os.O_TRUNC,0644)
    if err != nil {
        fmt.Println("Failed to open the file",err.Error())
        os.Exit(2)
    }
    defer fileObj.Close()
    if _,err := fileObj.WriteString(content);err == nil {
        fmt.Println("Successful writing to the file with os.OpenFile and *File.WriteString method.",content)
    }
    contents := []byte(content)
    if _,err := fileObj.Write(contents);err == nil {
        fmt.Println("Successful writing to thr file with os.OpenFile and *File.Write method.",content)
    }
}
```
注意:使用os.OpenFile(name string, flag int, perm FileMode)打开文件并进行文件内容更改，需要注意flag相关的参数以及含义。
```go
const (
        O_RDONLY int = syscall.O_RDONLY // 只读打开文件和os.Open()同义
        O_WRONLY int = syscall.O_WRONLY // 只写打开文件
        O_RDWR   int = syscall.O_RDWR   // 读写方式打开文件
        O_APPEND int = syscall.O_APPEND // 当写的时候使用追加模式到文件末尾
        O_CREATE int = syscall.O_CREAT  // 如果文件不存在，此案创建
        O_EXCL   int = syscall.O_EXCL   // 和O_CREATE一起使用, 只有当文件不存在时才创建
        O_SYNC   int = syscall.O_SYNC   // 以同步I/O方式打开文件，直接写入硬盘.
        O_TRUNC  int = syscall.O_TRUNC  // 如果可以的话，当打开文件时先清空文件
)
```
#### 3 使用io包中的相关函数写入文件

在io包中有一个WriteString()函数，用来将字符串写入一个Writer对象中。

```go
//将字符串s写入w(可以是一个[]byte)，如果w实现了一个WriteString方法，它可以被直接调用。否则w.Write会再一次被调用
func WriteString(w Writer, s string) (n int, err error)

//Writer对象的定义
type Writer interface {
        Write(p []byte) (n int, err error)
}
```

示例:
```go
//使用io.WriteString()函数进行数据的写入
func WriteWithIo(name,content string) {
    fileObj,err := os.OpenFile(name,os.O_RDWR|os.O_CREATE|os.O_APPEND,0644)
    if err != nil {
        fmt.Println("Failed to open the file",err.Error())
        os.Exit(2)
    }
    if  _,err := io.WriteString(fileObj,content);err == nil {
        fmt.Println("Successful appending to the file with os.OpenFile and io.WriteString.",content)
    }
}
```
#### 4 使用bufio包中的相关函数写入文件

bufio和io包中很多操作都是相似的，唯一不同的地方是bufio提供了一些缓冲的操作，如果对文件I/O操作比较频繁的，使用bufio还是能增加一些性能的。

在bufio包中，有一个Writer结构体，而其相关的方法也支持一些写入操作。
```go
//Writer是一个空的结构体，一般需要使用NewWriter或者NewWriterSize来初始化一个结构体对象
type Writer struct {
        // contains filtered or unexported fields
}

//NewWriterSize和NewWriter函数
//返回默认缓冲大小的Writer对象(默认是4096)
func NewWriter(w io.Writer) *Writer

//指定缓冲大小创建一个Writer对象
func NewWriterSize(w io.Writer, size int) *Writer

//Writer对象相关的写入数据的方法

//把p中的内容写入buffer,返回写入的字节数和错误信息。如果nn<len(p),返回错误信息中会包含为什么写入的数据比较短
func (b *Writer) Write(p []byte) (nn int, err error)
//将buffer中的数据写入 io.Writer
func (b *Writer) Flush() error

//以下三个方法可以直接写入到文件中
//写入单个字节
func (b *Writer) WriteByte(c byte) error
//写入单个Unicode指针返回写入字节数错误信息
func (b *Writer) WriteRune(r rune) (size int, err error)
//写入字符串并返回写入字节数和错误信息
func (b *Writer) WriteString(s string) (int, error)
```
注意：如果需要再写入文件时利用缓冲的话只能使用bufio包中的Write方法

示例:
```go
//使用bufio包中Writer对象的相关方法进行数据的写入
func WriteWithBufio(name,content string) {
    if fileObj,err := os.OpenFile(name,os.O_RDWR|os.O_CREATE|os.O_APPEND,0644);err == nil {
        defer fileObj.Close()
        writeObj := bufio.NewWriterSize(fileObj,4096)
        //
       if _,err := writeObj.WriteString(content);err == nil {
              fmt.Println("Successful appending buffer and flush to file with bufio's Writer obj WriteString method",content)
           }

        //使用Write方法,需要使用Writer对象的Flush方法将buffer中的数据刷到磁盘
        buf := []byte(content)
        if _,err := writeObj.Write(buf);err == nil {
            fmt.Println("Successful appending to the buffer with os.OpenFile and bufio's Writer obj Write method.",content)
            if  err := writeObj.Flush(); err != nil {panic(err)}
            fmt.Println("Successful flush the buffer data to file ",content)
        }
        }
}
```
#### misc

> 文件拷贝

```go
func main() {
	CopyFile("target.txt", "source.txt")
	fmt.Println("Copy done!")
}

func CopyFile(dstName, srcName string) (written int64, err error) {
	src, err := os.Open(srcName)
	if err != nil {
		return
	}
	defer src.Close()

	dst, err := os.Create(dstName)
	if err != nil {
		return
	}
	defer dst.Close()

	return io.Copy(dst, src)
}
```


## 4种读写方法解读

[完美 Golang读写文件的方式 总览](https://www.jianshu.com/p/7790ca1bc8f6):https://xxbandy.github.io/2017/12/17/Golang%E8%AF%BB%E5%86%99%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C/

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
## 读取用户输入键盘控制台以及从命令行读取参数

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	firstName, lastName, s string
	firstAge, lastAge      int
	i                      int
	f                      float32
	input                  = "56.12 / 5212 / Go"
	format                 = "%f / %d / %s"
	inputReader            *bufio.Reader
	input2                 string
	err                    error
)

func main() {
	// 1 从标准输入读取  Scanln   Scanf
	fmt.Println("Please enter your full name: ")
	// Scanln 扫描来自标准输入的文本，将空格分隔的值依次存放到后续的参数内，直到碰到换行
	fmt.Scanln(&firstName, &lastName)
	// fmt.Scanf("%s %s", &firstName, &lastName)
	fmt.Printf("Hi %s %s!\n", firstName, lastName) // Hi

	fmt.Println("Please enter your full age: ")
	// Scanf 的第一个参数用作格式字符串，用来决定如何读取
	fmt.Scanf("%d %d", &firstAge, &lastAge)
	fmt.Printf("i am %d %d!\n", firstAge, lastAge) //

	// 2 从字符串读取 Sscanf
	// 将input 按format格式读取
	fmt.Sscanf(input, format, &f, &i, &s)
	fmt.Println("From the string we read: ", f, i, s)
	// 输出结果: From the string we read: 56.12 5212 Go
        
	
	// 3 bufio      bufio.NewReader(os.Stdin)
	inputReader = bufio.NewReader(os.Stdin)
	fmt.Println("Please enter your name:")

	// 从输入中读取内容，直到碰到 delim 指定的字符，然后将读取到的内容连同 delim 字符
	// 一起放到缓冲区
	input2, err = inputReader.ReadString('\n')
	if err != nil {
		fmt.Println("There were errors reading, exiting program.")
		return
	}

	fmt.Printf("Your name is %s", input2)
	// For Unix: test with delimiter "\n", for Windows: test with "\r\n"
	switch input2 {
	case "Philip\r\n":
		fmt.Println("Welcome Philip!")
	case "Chris\r\n":
		fmt.Println("Welcome Chris!")
	case "Ivo\r\n":
		fmt.Println("Welcome Ivo!")
	default:
		fmt.Printf("You are not welcome here! Goodbye!")
	}

	// version 2:
	switch input2 {
	case "Philip\r\n":
		fallthrough
	case "Ivo\r\n":
		fallthrough
	case "Chris\r\n":
		fmt.Printf("Welcome %s\n", input2)
	default:
		fmt.Printf("You are not welcome here! Goodbye!\n")
	}

	// version 3:
	switch input2 {
	case "Philip\r\n", "Ivo\r\n":
		fmt.Printf("Welcome %s\n", input2)
	default:
		fmt.Printf("You are not welcome here! Goodbye!\n")
	}
}

```
从命令行读取参数`io包`和 `flag包`

io
```go
func main() {
	who := "Alice "
	if len(os.Args) > 1 {
		who += strings.Join(os.Args[1:], " ")
	}
	fmt.Println("Good Morning", who)
}
```
flag
```go

package main

import (
	"flag" // command line option parser
	"os"
)

var NewLine = flag.Bool("n", false, "print newline") // echo -n flag, of type *bool

const (
	Space   = " "
	Newline = "\n"
)

func main() {
	flag.PrintDefaults()
	flag.Parse() // Scans the arg list and sets up flags
	var s string = ""
	for i := 0; i < flag.NArg(); i++ {
		if i > 0 {
			s += " "
			if *NewLine { // -n is parsed, flag becomes true
				s += Newline
			}
		}
		s += flag.Arg(i)
	}
	os.Stdout.WriteString(s)
}
```

> 命令行用切片读写文件

```go
package main

import (
	"flag"
	"fmt"
	"os"
)

func cat(f *os.File) {
	const NBUF = 512
	var buf [NBUF]byte
	for {
		switch nr, err := f.Read(buf[:]); true {
		case nr < 0:
			fmt.Fprintf(os.Stderr, "cat: error reading: %s\n", err.Error())
			os.Exit(1)
		case nr == 0: // EOF
			return
		case nr > 0:
			if nw, ew := os.Stdout.Write(buf[0:nr]); nw != nr {
				fmt.Fprintf(os.Stderr, "cat: error writing: %s\n", ew.Error())
			}
		}
	}
}

func main() {
	flag.Parse() // Scans the arg list and sets up flags
	if flag.NArg() == 0 {
		cat(os.Stdin)
	}
	for i := 0; i < flag.NArg(); i++ {
		f, err := os.Open(flag.Arg(i))
		if err != nil {
			fmt.Fprintf(os.Stderr, "cat: can't open %s: error %s\n", flag.Arg(i), err)
			os.Exit(1)
		}
		cat(f)
		f.Close()
	}
}

```

## JSON 数据格式

json.Marshal()

json.UnMarshal() 的函数签名是 
```go
func Marshal(v interface{}) ([]byte, error)
func Unmarshal(data []byte, v interface{}) error
https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/12.9.md
```

## XML 数据格式

## gob
```go
package main

import (
	"bytes"
	"encoding/gob"
	"fmt"
	"log"
)

type P struct {
	X, Y, Z int
	Name    string
}

type Q struct {
	X, Y *int32
	Name string
}

func main() {
	// Initialize the encoder and decoder.  Normally enc and dec would be
	// bound to network connections and the encoder and decoder would
	// run in different processes.
	var network bytes.Buffer
	// bytes.Buffer is a struct which implements io.Reader and io.Writer,
	// Stand-in for a network connection

	enc := gob.NewEncoder(&network) // Will write to network.
	// NewEncoder returns a new encoder that will transmit on the io.Writer.
	//func NewEncoder(w io.Writer) *Encoder {
	//	enc := new(Encoder)
	//	enc.w = []io.Writer{w}
	//	enc.sent = make(map[reflect.Type]typeId)
	//	enc.countState = enc.newEncoderState(new(encBuffer))
	//	return enc
	//}


	dec := gob.NewDecoder(&network) // Will read from network.
	// Encode (send) the value.
	err := enc.Encode(P{3, 4, 5, "Pythagoras"})
	if err != nil {
		log.Fatal("encode error:", err)
	}
	// Decode (receive) the value.
	var q Q
	err = dec.Decode(&q)
	if err != nil {
		log.Fatal("decode error:", err)
	}
	fmt.Printf("%q: {%d,%d}\n", q.Name, *q.X, *q.Y)
}
```
