from threading import Lock, RLock, Condition #可重入的锁
"""锁是加在线程上的"""
total = 0
# RLock()使得在同一个线程里面，可以连续调用多次acquire， 一定要注意acquire的次数要和release的次数相等
lock = RLock()  # 可重入的锁
def add():
    #1. dosomething1
    #2. io操作
    # 1. dosomething3
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()


#
thread1.join()
thread2.join()
print(total)

#1. 用锁会影响性能
#2. 锁会引起死锁
#死锁的几种情况
# 1 A（a，b）
"""
A(a、b)
acquire (a)
acquire (b)

B(a、b)
acquire (a)
acquire (b)
"""
lock = Lock()  # 死锁 2
def add():
    #1. dosomething1
    #2. io操作
    # 1. dosomething3
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        lock.release()


lock = Lock()  # 死锁 3
def add():
    #1. dosomething1
    #2. io操作
    # 1. dosomething3
    global lock
    for i in range(1000000):
        lock.acquire()
        dosomething()
        lock.release()

def dosomething():
    lock.acquire()
    lock.release()