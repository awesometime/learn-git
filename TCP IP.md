ISO-OSI的七层协议经典架构   按照层次由上到下
```
应用层       http，ftp                                                               常用应用编程接口有socket和TLI
表示层       ssh,pop,html,mime,smtp                                                 将数据从主机特有的格式转换为网络标准传输格式
会话层                                                                           采用何种连接发送
传输层       TCP，UDP ，UDP-Lite，SCTP，DCCP                                     确立连接与断开连接，重发
网络层       [IPv4，IPv6，(唯一性，层次性)],ARP,ICMP,IPsec，loopback协议               它负责对数据加上IP地址和其他的数据（后面会讲到）以确定传输的目标。
数据链路层      ppp,   以太网协议,无线LAN                                        这个层次为待传送的数据加入一个以太网协议头，并进行CRC编码，为最后的数据传输做准备。
物理层       MAC地址(唯一性)                                                        负责网络的传输，这个层次的定义包括网线的制式，网卡的定义等等.
```
```
应用层       
表示层                           
会话层                            
传输层                    
网络层        (三层)路由器，功能比交换机更强大从家用的角度来说：
                 路由器本质上就是一种交换机   利用IP地址来确定数据转发的地址   用于WAN-WAN之间的连接
数据链路层    (二层)交换机(网桥)   利用物理地址或者说MAC地址来确定转发数据的目的地址  用于LAN-WAN的连接，多用于局域网互连
物理层        中继器
```
路由器和交换机的区别
http://www.pc811.com/1/25478.html
http://www.meilele.com/article_cat-1/article-6630.html



### 网络编程之Socket

端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

Web服务是80端口。

SMTP服务是25端口。

FTP服务是21端口。

**客户端**

`import socket`    导入socket库

`s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`    创建一个socket

AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议.

`s.connect(('www.sina.com.cn', 80))`     建立连接,一般address的格式为元组（hostname,port）

建立TCP连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容(此时用到http协议)：

TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。

例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。

`s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')`  发送请求数据,要求返回首页的内容

`s.close()`  关闭连接

**服务端**

```
# 导入 socket 模块
import socket

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname()
# print(host) = linuix
port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      

    print("连接地址: %s" % str(addr))
    
    msg='欢迎访问菜鸟教程！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
```
