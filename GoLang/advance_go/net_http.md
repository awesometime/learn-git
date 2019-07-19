https://studygolang.com/articles/9467

https://juejin.im/entry/5a4a124d51882506bd042d07

[the-way-to-go](https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/15.1.md)

[net/http的大概流程](https://www.haohongfan.com/post/2019-02-17-gin-01/)

```
这基本是整个过程的代码了. 基本上是:

ln, err := net.Listen("tcp", addr)做了初试化了socket, bind, listen的操作.
rw, e := l.Accept()进行accept, 等待客户端进行连接
go c.serve(ctx) 启动新的goroutine来处理本次请求. 同时主goroutine继续等待客户端连接, 进行高并发操作
h, _ := mux.Handler(r) 获取注册的路由, 然后拿到这个路由的handler, 然后将处理结果返回给客户端

```

[Go 开发 HTTP](http://fuxiaohei.me/2016/9/20/go-and-http-server.html)

[Go和HTTPS](https://tonybai.com/2015/04/30/go-and-https/)

常见的陷阱与错误
