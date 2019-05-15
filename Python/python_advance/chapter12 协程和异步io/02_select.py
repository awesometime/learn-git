# epoll并不代表一定比select好
# 在并发高的情况下，连接活跃度不是很高， epoll比select
# 并发性不高，同时连接很活跃， select比epoll好

# -----------------
# select + 回调 + 事件循环
# 并发性高
# 使用单线程 省去线程切换开销
# 回调函数比线程切换内存损耗小
#
# 回调之痛
# 1 可读性差
# 2 共享状态管理困难
# 3 异常处理困难

#-------------------
# UNIX I/O模型
# 1  阻塞式I/O
# 2  非阻塞式I/O                  不用select只能实现监听一个socket/文件句柄，可以简单理解为只能为一个任务服务
# 3  I/O复用（使用最多成熟）       select、poll(windows)、epoll(linux)  可以同时服务多个任务
# 4  信号驱动式I/O（不用看）
# 5  异步I/O （不如I/O复用成熟）   posix的aio_系列函数

"""
本代码使用 I/O多路复用 中的select完成http请求 单线程
*事件循环使用场景
    tornado
    twisted  (scrapy、django channels)
    gevent
    asyncio
"""
import socket
from urllib.parse import urlparse
# selectors是对select库的进一步封装
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# import select
# select.select()


selector = DefaultSelector() # win用poll ,linux用epoll
urls = []
stop = False


class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)  # fd == self.client.fileno()
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        # 注册一个事件: 先监听等待，当当前socket变为可写EVENT_READ时候，调用self.readable方法
        # (里边有recv data方法)里边的逻辑
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd) # 一次请求读完将一个socket unregister
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        # 注册事件
        # 三个参数
        # socket的文件描述符,注意不是socket;
        # 事件 EVENT_READ, EVENT_WRITE;
        # 回调函数
        # 注册一个事件: 先监听等待，当当前socket变为可写EVENT_WRITE时候，调用self.connected方法
        # (里边有send request方法)里边的逻辑  send请求是一个可写事件
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)
        # 等待事件循环loop()去调用


def loop():
    """事件循环，不停的请求socket的状态并调用对应的回调函数"""
    # 1. select本身是不支持register模式 所以使用封装好的selector库
    # 2. socket状态变化以后的回调是由程序员完成的
    #    也就是socket变为可读可写状态之后操作系统并不会自动去读写,需要我们自己去编写逻辑
    while not stop:
        # ready=(key,events) tuple
        # key(fileno,fd,events,data) 是一个namedtuple(SelectorKey,[fileno,fd,events,data])
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data  # 当时注册的回调函数,即本例中的self.connected, self.readable
            call_back(key)  # self.connected(key), self.readable(key)
    # 回调+事件循环+select(poll\epoll)


if __name__ == "__main__":
    import time

    start_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()  # socket注册完以后, 状态变化以后的回调是由程序员完成的 不是操作系统
    print(time.time() - start_time)




# def get_url(url):
#     #通过socket请求html
#     url = urlparse(url)
#     host = url.netloc
#     path = url.path
#     if path == "":
#         path = "/"
# 
#     #建立socket连接
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.setblocking(False)
#     try:
#         client.connect((host, 80)) #阻塞不会消耗cpu
#     except BlockingIOError as e:
#         pass
# 
#     #不停的询问连接是否建立好， 需要while循环不停的去检查状态
#     #做计算任务或者再次发起其他的连接请求
# 
#     while True:
#         try:
#             client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
#             break
#         except OSError as e:
#             pass
# 
# 
#     data = b""
#     while True:
#         try:
#             d = client.recv(1024)
#         except BlockingIOError as e:
#             continue
#         if d:
#             data += d
#         else:
#             break
# 
#     data = data.decode("utf8")
#     html_data = data.split("\r\n\r\n")[1]
#     print(html_data)
#     client.close()
