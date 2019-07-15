[go defer,panic,recover详解 go 的异常处理](https://www.jianshu.com/p/63e3d57f285f)

[go使用Defer的几个场景](https://studygolang.com/articles/5932)

```
[go defer,panic,recover详解 go 的异常处理](https://www.jianshu.com/p/63e3d57f285f)

2 3 6 条比较重要

defer后边会接一个函数，但该函数不会立刻被执行，而是等到包含它的程序返回时(包含它的函数执行了return语句、运行到函数结尾自动返回、对应的goroutine panic）defer函数才会被执行。通常用于资源释放、打印日志、异常捕获等

2. F中出现panic时，F函数会立刻终止，不会执行F函数内panic后面的内容，但不会立刻return，而是调用F的defer，如果F的defer中有recover捕获，则F在执行完defer后正常返回，调用函数F的函数G继续正常执行
   执行顺序 panic -> defer -> recover 捕获异常

3. 向上传递   

6. func panic(v interface{})
   func recover() interface{}
   recover 返回接口类型 不同于 error类型 
```
