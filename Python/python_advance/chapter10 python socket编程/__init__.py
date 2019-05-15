"""
client 从上往下拆包  server 从下往上组包

http 是单向连接的 a发请求b响应 然后就断开
socket 双向的, a可以给b发, b也可以给a发
socket 不属于任何一个层, 直接对接TCP层 操作系统提供
http建立在socket基础上   http->socket->tcp->ip
requests第三方库 -> urllib标准库 -> socket -> tcp -> ip





















"""
