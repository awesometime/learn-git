
- [清华大学 李金老师 Python笔记 《自学Python——编程基础、科学计算及数据分析》](https://github.com/lijin-THU/notes-python)
  [李金老师github.io](http://lijin-thu.github.io/)
- [人工智能 机器学习 深度学习 入门及进阶资料](Python入门网络爬虫之精华版)
- [Python入门网络爬虫之精华版](https://github.com/lining0806/PythonSpiderNotes)


### pip相关
pip安装时指定清华源速度快,比如安装lxml  `pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/  lxml`
```
python pip 安装模块
C:\Users\li>  python -m pip install pygal
Collecting pygal
  Downloading https://files.pythonhosted.org/packages/5f/b7/201c9254ac0d2b8ffa3bb2d528d23a4130876d9ba90bc28e99633f323f17/pygal-2.4.0-py2.py3-none-any.whl (127kB)
    100% |████████████████████████████████| 133kB 15kB/s
Installing collected packages: pygal
Successfully installed pygal-2.4.0

查看安装路径
C:\Users\li> pip install pygal
Requirement already satisfied: pygal in g:\python\python-3.6.5\lib\site-packages (2.4.0)
```




以下总结自菜鸟教程

### 2 Python
**标准库**

[The Python Standard Library](https://docs.python.org/3/library/index.html)

**sy**s调用命令行参数 argv 变量，sys 还有 stdin，stdout 和 stderr 属性，另外大多脚本的定向终止都使用 "sys.exit()"。

**os**模块提供与操作系统接口相关联的函数，

mod 、shutil 模块提供了一个易于日常的文件和目录管理的高级接口，

glob模块提供了一个函数用于从 目录通配符搜索 生成文件列表，

**re**模块为高级字符串处理提供了 Perl 风格的正则表达式模式，re.match 与 re.search  , re.sub用于替换字符串中的匹配项 ， re.compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

math模块为浮点运算提供了对底层C函数库的访问，

random提供了生成随机数的工具，

urllib.request 处理从 urls 接收的数据的；  smtplib 用于发送电子邮件的；(用于访问互联网以及处理网络通信协议)

datetime模块为日期和时间处理同时提供了简单和复杂的方法。

以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。

度量解决同一问题的不同方法之间的性能：timeit 细粒度； :mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

doctest ， unittest模块提供了一个用于测试代码的工具，扫描模块并根据程序中内嵌的文档字符串执行测试

**第三方模块安装**

处理图像的[Pillow](https://pillow.readthedocs.io/en/latest/index.html)，

SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。
MySQL是Web世界中使用最广泛的数据库服务器。MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。

**MySQL驱动程序，MySQLdb 和 mysql-connector-python**  
MySQLdb（即MySQL-Python）: 封装了MySQL C驱动的Python驱动器，python 3.x不再支持
PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库。
MySQL官方提供了mysql-connector-python驱动，以支持Python连接到MySQL服务器。

Web框架Flask，科学计算Numpy等。

matplotlib_venn  文氏图的绘制

用pip一个一个安装费时费力，还需要考虑兼容性。

我们推荐直接使用**Anaconda，这是一个基于Python的数据处理和科学计算平台**，它已经内置了许多非常有用的第三方库，

我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。

### 3 Python3 中有六个标准的数据类型：
```
Number（数字）           整型(Int) 浮点型（Float）复数（Complex）
                        数字类型转换int(x)   float(x)   complex(x)   complex(x,y)
String（字符串）         **var[1:5]取变量的第二到五位(4个)，不包括第六位           转义字符串  字符串运算 格式化字符串
List（列表）             有序  列表写在方括号[]之间，用逗号分隔开的元素列表
Tuple（元组）                  元组写在小括号 () 里，元素之间用逗号隔开
Sets（集合）             无序,**不重复**用大括号 { } 或者 set() 函数创建集合,创建一个空集合必须用 set() 而不是 { }。基本功能包括关系测试和消除重复元素
Dictionary（字典）       无序,{ } 是用来创建一个空字典,键(key) : 值(value)对集合,键(key)必须使用不可变类型。 
```
Python3 的六个标准数据类型中：
```
不可变数据（四个）：Number（数字）、String（字符串）、Tuple（元组）、Sets（集合）；
可变数据（两个）：List（列表）、Dictionary（字典）。
```


tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
    构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
    tup1 = ()    # 空元组
    tup2 = (20,) # 一个元素，需要在元素后添加逗号

### 4 Python3 解释器
### 5  if判断

if isinstane(object, classinfo) 如果参数 object 是参数 classinfo 的实例，返回真，否则假；

参数 classinfo 可以是一个包含若干 type 对象的元祖，如果参数 object 是其中任意一个类型的实例，返回真，否则假

```
def __init__(self, path_or_image):
    # 若 path_or_image 为 Image.Image 类型的实例，直接赋值
    if isinstance(path_or_image, Image.Image):
        self.image = path_or_image
    # 若 path_or_image 为 str 类型的实例，打开图片
    elif isinstance(path_or_image, str):
        self.image = Image.open(path_or_image)
```
### 6 Python3 运算符
Python语言支持以下类型的运算符:
```
算术运算符            + - * / % ** // (得到的并一定是整数类型的数，它与分母分子的数据类型有关系。 7.0 // 2= 3.0)
比较（关系）运算符     ==  !=  >  <  >=  <=
赋值运算符            += -= *= /= %= **= //=
逻辑运算符            and布尔与   or布尔或       not布尔非 
位运算符              &两个都为1,则结果为1   |有一个为1，结果为1   ^二位不相同时，结果为1   ~按位取反  >>右移  <<n左移n位，高位丢弃，低位补0。
成员运算符            in    not in
身份运算符            is    is not                 id() 函数用于获取对象内存地址。
运算符优先级
```
```
两个集合的操作
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # a 中唯一的字母
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # 在 a 中的字母，但不在 b 中
{'r', 'd', 'b'}
>>> a | b                              # 在 a 或 b 中的字母
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # 在 a 和 b 中都有的字母
{'a', 'c'}
>>> a ^ b                              # 在 a 或 b 中的字母，但不同时在 a 和 b 中
{'r', 'd', 'b', 'm', 'z', 'l'}
```
```
Python中变量在使用前都必须赋值,但不需要声明。

不区分单双引号

o八进制 x十六进制

在 python 中，类型属于对象，变量是没有类型的：a=[1,2,3]           a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，
她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

is 与 == 区别：   ???
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。 _ 变量应被用户视为只读变量。

round(float， n) 方法返回浮点数 float 的 n 位四舍五入值。    详见Python3 数字

list(range(2,2))  返回[]        list(range(0, 1))返回[0]          list(range(1, 0))返回[],默认步长+1，所以到不了0
```
```
运算符优先级      	描述
**	                  指数 (最高优先级)
~ + -	                按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	           乘，除，取模和取整除
+ -	                 加法减法
>> <<	               右移，左移运算符
&	                   位 'AND'
^ |	                 位运算符
<= < > >=	           比较运算符
<> == !=	           等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	           身份运算符
in not in	           成员运算符
and or not	         逻辑运算符
```
### 7 Python3 数字(Number)
数学函数
随机数函数
三角函数
常量 π e
### 8 Python3 字符串
print("12" , "34")
12 34   会自动产生一个空格

字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。

还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。

另一个方法 zfill(), 它会在数字的左边填充 0

str.format() 的基本使用如下:
```
>>> print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
菜鸟教程网址： "www.runoob.com!"
```
```
在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：

>>> print('{0} 和 {1}'.format('Google', 'Runoob'))
Google 和 Runoob
>>> print('{1} 和 {0}'.format('Google', 'Runoob'))
Runoob 和 Google
```
### 9 Python3 列表

### 10 Python3 循环语句

break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value:
```   
   for k, v in d.items():
        print(k, '=', v)
```
### 11 Python3 模块

每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块只在本程序内部运行，其他程序中导入该模块并不会执行。

内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
```
>>> import  sys

>>> dir(sys)  

['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',等等]
```


import sound.effects.echo  必须使用全名去访问:

sound.effects.echo.echofilter

from sound.effects import echo   这同样会导入子模块: echo，但他不需要那些冗长的前缀，可以这样使用:

echo.echofilter

包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
 
### 12 Python3   多进程 multiprocessing    多线程 threading     (参考廖雪峰)


多进程和多线程最大的不同在于，

`多进程`中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响.

`多线程`中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改.

因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。



#### 12.1 多进程multiprocessing

**12.1.1 启动一个子进程并等待其结束**   `os.getpid()  p.start()  p.join()`

multiprocessing模块（具有跨平台特性）提供了一个Process类来代表一个进程对象

```
from multiprocessing import Process
import time,os

def run_proc(name):                           # 定义一个执行函数run_proc和函数的参数name
    print('Run child process %s (%s)...' % (name, os.getpid()))      #os.getpid()获取当前进程id , os.getppid()获取父进程id 

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())      # 打印当前进程(父进程)id
    p=Process(target=run_proc, args=('test',))     # 传入参数，创建一个Process实例，即创建一个子进程
    p.start()                                      # 开启一个进程
    p.join()                                       # 等待该进程运行结束
```    

另一种方法：创建一个类继承Process类，并重写run方法。[参考](https://www.cnblogs.com/hypnus-ly/p/8129205.html)
    
**12.1.2 Pool  批量创建子进程**   `p.apply_async` 

```
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))   # 用time.sleep结合随机函数来指定每个进程执行多长时间

if __name__=='__main__':
    
    p = Pool(4)                   # 同时跑4个进程，默认大小是CPU的核数
    for i in range(6):            # 总共6个进程，由于只能同时跑4个进程，需要等前边4个中某个结束才能加入一个新的进程
        p.apply_async(long_time_task, args=(i,))
    
    p.close()
    p.join()
    
```
 **12.1.3 进程Process间通信**
 
Python的multiprocessing模块包装了底层的机制，提供了`Queue、Pipes`等多种方式来交换数据。我们以``Queue``为例  
```
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)                                  # 将xxx写入到Queue
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)           # 从Queue读出xxx

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))             # 创建子进程pw，pr
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
 ```

#### 12.2 多线程 Threading 

Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，

然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，

多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了

Python简单易用的特点。不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。

多个Python进程有各自独立的GIL锁，互不影响。


Python的标准库提供了两个模块：`_thread 和 threading`，_thread是低级模块，threading是高级模块，对_thread进行了封装。

绝大多数情况下，我们只需要使用threading这个高级模块。

**12.2.1 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：** 


由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，

Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，

子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，

如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
```
import time, threading

# 新线程执行的代码:
def loop():                                                              # 新线程的代码
    print('thread %s is running...' % threading.current_thread().name)   # print(threading.current_thread().name)=MainThread
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)   # MainThread 正在运行
t = threading.Thread(target=loop, name='LoopThread')                 # Thread中传入loop函数，及参数，创建Thread实例
t.start()                                                            # 新线程开始执行
t.join()
print('thread %s ended.' % threading.current_thread().name)          # MainThread 执行完毕
```
**12.2.2 Lock**
lock = threading.Lock()                # 创建一个锁
def run_thread(n):
    for i in range(100000):        
        lock.acquire()                 # 先要获取锁
        try:           
            change_it(n)               # 执行一段代码
        finally:            
            lock.release()             # 执行代码完了一定要释放锁
    
**12.3 ThreadLocal**

一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
```
import threading
   
local_school = threading.local()                      # 创建全局ThreadLocal对象

def process_student():    
    std = local_school.student                        # 获取当前线程关联的student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(std_name):    
    local_school.student = std_name                   # 绑定ThreadLocal的student
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')  # 此处args传给std_name,  name传给threading.current_thread().name，不传则为Thread-1， Thread-2
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-A')
t1.start()
t2.start()
t1.join()
t2.join()
```
**12.4 分布式进程**

可以在多台机子上跑

##### task_master.py
```
import random, time, queue                                                                    右侧为模块化的东西
from multiprocessing.managers import BaseManager                                              managers为multiprocessing的子模块

# 发送  任务task_queue  的队列:
task_queue = queue.Queue()                                                                    queue.Queue()
# 接收  结果result_queue 的队列:
result_queue = queue.Queue()                                                                  queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)                            QueueManager.register
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')                                      绑定 QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()                                                                                 QueueManager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()                                                                 QueueManager.get_task_queue()
result = manager.get_result_queue()                                                             QueueManager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)                                                   QueueManager.get_task_queue().put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)                                    QueueManager.get_result_queue().get(timeout=10) 
    print('Result: %s' % r)
# 关闭:
manager.shutdown()                                                manager.shutdown()
print('master exit.')
```
##### task_worker.py
```
import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')                                           QueueManager.register
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')                      绑定QueueManager
# 从网络连接:
m.connect()                                                                          QueueManager.connect()
# 获取Queue的对象:
task = m.get_task_queue()                                                            QueueManager.get_task_queue()
result = m.get_result_queue()                                                        QueueManager.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)                                                 QueueManager.get_task_queue().get()
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)                                                           QeueManager.get_result_queue().put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')
```
Queue 之所以能通过网络访问，就是通过 QueueManager 实现的。也就是 QueueManager 管理着众多的 Queue，参考廖雪峰的图更好理解
