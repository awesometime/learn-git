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


```
目录
创建 HTTP 服务 
func ListenAndServe(addr string, handler Handler) error

添加 http.Handler 
type HandlerFunc func(ResponseWriter, *Request)  HandlerFunc是一个结构体对象
// ServeHTTP calls f(w, r).
func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request) {
	f(w, r)
}

http.ServeMux 路由

Request  上传问价 表单 细节
http.ResponseWriter 接口

Context包  传递数据和做超时、取消等处理
Hijack 将 HTTP 对应的 TCP 取出
http.Server 的使用细节
HTTPS的数据传输是加密的。实际使用中，HTTPS利用的是对称与非对称加密算法结合的方式，需要加密用的公私密钥对进行加密，
也就是 server.crt 和 server.key 文件，可以被理解为运行在SSL（Secure Sockets Layer）或TLS(Transport Layer Security)
协议所构建的安全层之上的HTTP协议，协议的传输安全性以及内容完整性实际上是由SSL或TLS保证的。
```

[Go和HTTPS](https://tonybai.com/2015/04/30/go-and-https/)

常见的陷阱与错误
