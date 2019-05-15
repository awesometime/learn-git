import socket
import threading

# AF_INET tcp的ipv4网络    SOCK_STREAM tcp协议
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))  # 元组
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        re_data = input()
        sock.send(re_data.encode("utf8"))

#获取从客户端发送的数据
#一次获取1k的数据
while True:
    sock, addr = server.accept()

    #用线程去处理新接收的连接(用户) 模拟实现多用户聊天连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # data = sock.recv(1024)
    # print(data.decode("utf8"))
    # re_data = input()
    # sock.send(re_data.encode("utf8"))
    # server.close()
    # sock.close()
