```
Go Runtime 
调度
内存
垃圾回收
```


### 1 Go程序运行

- [Go程序是怎样跑起来的](https://mp.weixin.qq.com/s/Rewl0DKnq6CY53m5D3G2qw)

```
目录
编译链接 编译原理

golang 程序启动过程
    检查运行平台的CPU，设置好程序运行需要相关标志。
    TLS的初始化。
    runtime.args、runtime.osinit、runtime.schedinit 三个方法做好程序运行需要的各种变量与调度器。
    runtime.newproc创建新的goroutine用于绑定用户写的main方法。
    runtime.mstart开始goroutine的调度。

go命令 go build install run
```
### 2 Go内存分配

- [Go内存分配那些事，就这么简单！](https://mp.weixin.qq.com/s/3gGbJaeuvx4klqcv34hmmw)

- [GCTT 出品 | Go 语言的内存管理](https://mp.weixin.qq.com/s/Rm5kILm1EgDGisk-L0LDIg)

- [图解Golang的内存分配](https://mp.weixin.qq.com/s/pbwCYFEESkILGIJVqnNaLA)

- [图解Go语言内存分配](https://mp.weixin.qq.com/s/Hm8egXrdFr5c4-v--VFOtg)

- [图解 Go 内存分配器](https://mp.weixin.qq.com/s/3jmMexGYY4ww_urSZ36vVQ)
