#requests -> urlib -> socket
import socket
from urllib.parse import urlparse

# 通过阻塞式io实现http请求
def get_url(url):
    """socket 实现http请求"""
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    #建立socket连接  三次握手耗时
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.setblocking(False)  # 非阻塞式I/O
    client.connect((host, 80)) # 等待网络时间 阻塞式I/O 不会消耗cpu

    ### 非阻塞式I/O
    # 如果后面代码前提必须是建立连接,需要在send连接请求前不停的询问连接
    # 是否建立好， 需要while循环不停的去检查状态,会消耗cpu,所以并不一定非阻塞式I/O就有优势

    # 如果后面代码本前边没有关系,可以先去执行一些计算等等
    # 做计算任务或者再次发起其他的连接请求

    ### I/O复用 select
    # 用select可以同时去监听多个socket/文件句柄请求
    # select功能: 返回可读的或准备好的socket/文件句柄

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)  # 此处有较长的等待网络时间
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    import time
    start_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        get_url(url)
    print(time.time()-start_time)
