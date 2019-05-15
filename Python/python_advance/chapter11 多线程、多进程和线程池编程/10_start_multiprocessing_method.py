# import os
# #fork代码只能运行于linux/unix系统中
# fork是完全拷贝一份数据从父进程，然后运行，也就是新fork出来一个进程
# 线程通过全局变量实现线程间通信
# pid = os.fork()
# print("bobby")
# if pid == 0:
#   print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
# else:
#   print('我是父进程：{}.'.format(pid))

# time.sleep(2) 父进程运行完等2秒保证子进程运行完再退出父进程，否则子进程没办法退出

from concurrent.futures import ProcessPoolExecutor # 多进程编程推荐使用这个
import multiprocessing # 更加底层


#多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n

# windows下ProcessPoolExecutor multiprocessing.Process 必须放在
# if __name__ == "__main__":里,linux不需要
if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    #使用线程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))
    #
    # #等待所有任务完成
    # pool.close()
    # pool.join()
    #
    # print(result.get())

    #imap
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))




