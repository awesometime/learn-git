# 注意
# 该文件有多个if __name__ == "__main__": 每个需要单独拎出来去运行
import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe


# 问题一:
# 多进程能不能通过共享全局变量global通信?
# 共享全局变量不适用于多进程编程,只适用于多线程


def producer(a):
    a += 100
    time.sleep(2)


def consumer(a):  # 不能更改producer中的a 输出a还是1
    time.sleep(2)
    print(a)


if __name__ == "__main__":
    a = 1
    my_producer = Process(target=producer, args=(a,))
    my_consumer = Process(target=consumer, args=(a,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()


# 问题二:
# 多进程编程用于进程间通信的是multiprocessing.Queue模块
# from multiprocessing import Queue

def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == "__main__":
    queue = Queue(10)
    my_producer = Process(target=producer, args=(queue,))
    my_consumer = Process(target=consumer, args=(queue,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()


# 问题三:
# 进程池
# multiprocessing.Queue不能用于进程池multiprocessing pool方式创建的多进程中
# multiprocessing pool方式创建的多进程间通信需要使用multiprocessing.Manager().Queue

# 注意区分这三个Queue
# 1 multiprocessing 进程间通信不可用queue.Queue
#   from queue import Queue

# 2 进程中实现通信使用的是自己包下的Queue multiprocessing.Queue
#   from multiprocessing import Queue

# 3 multiprocessing.pool进程池中的进程间通信需要使用manager中的queue,不能用from multiprocessing import Queue
#   from multiprocessing import Manager
#   Manager().Queue

def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == "__main__":
    queue = Manager().Queue(10)
    pool = Pool(2)

    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))

    pool.close()
    pool.join()


# 问题四:
# 通过pipe实现进程间通信 pipe是简化版的Manager().Queue
# pipe的性能高于Manager().Queue

def producer(pipe):
    pipe.send("bobby")


def consumer(pipe):
    print(pipe.recv())


if __name__ == "__main__":
    recevie_pipe, send_pipe = Pipe()
    # pipe只能适用于两个进程, Manager().Queue可以用于多个进程间通信
    my_producer = Process(target=producer, args=(send_pipe,))
    my_consumer = Process(target=consumer, args=(recevie_pipe,))

    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()


# 问题五:
# 进程间共享内存/变量方法
# dict array list lock semaphore等
def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":
    progress_dict = Manager().dict()

    first_progress = Process(target=add_data, args=(progress_dict, "bobby1", 22))
    second_progress = Process(target=add_data, args=(progress_dict, "bobby2", 23))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()

    print(progress_dict)
