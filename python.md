总结自菜鸟教程

### 2 Python
**标准库**

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

处理图像的Pillow，

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
### 5
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
### Python3 模块

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
 
### 11 Python3   多进程 multiprocessing    多线程 threading

多进程和多线程最大的不同在于，

`多进程`中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响.

`多线程`中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改.

因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。



#### 多进程multiprocessing

**启动一个子进程并等待其结束**   `os.getpid()  p.start()  p.join()`

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
    
**Pool  批量创建子进程**   `p.apply_async` 

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
 **进程Process间通信**
 
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

#### 多线程   

Python的标准库提供了两个模块：`_thread 和 threading`，_thread是低级模块，threading是高级模块，对_thread进行了封装。

绝大多数情况下，我们只需要使用threading这个高级模块。

**启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：** 


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
**Lock**
lock = threading.Lock()                # 创建一个锁
def run_thread(n):
    for i in range(100000):        
        lock.acquire()                 # 先要获取锁
        try:           
            change_it(n)               # 执行一段代码
        finally:            
            lock.release()             # 执行代码完了一定要释放锁
    
