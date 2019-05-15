"""
几个主要问题
1 启动线程方法
2 线程间通信
3 线程同步

"""


#对于io操作来说，多线程和多进程性能差别不大


#1.通过Thread类实例化启动一个线程

import time
import threading

def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


#2. 通过继承Thread来启动多线程,重写run方法,类里可以写更多方法


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")

if  __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    # thread1.setDaemon(True)  主线程退出 子线程立马退出
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()

    # 此时实际有3个线程 MainThread thread1 thread2
    # join将thread1,thread2加到MainThread 这样主线程才会等子线程先执行完
    # 如果不加join则主线程会一路执行完 打印last time: 0
    thread1.join()
    thread2.join()

    #当主线程退出的时候， 子线程kill掉
    print ("last time: {}".format(time.time()-start_time))