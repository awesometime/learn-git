 
- [Python-100-Days](https://github.com/jackfrued/Python-100-Days)

- [李金老师 Python笔记 《自学Python——编程基础、科学计算及数据分析》github.io](http://lijin-thu.github.io/)
  
  [李金老师 Python笔记 《自学Python——编程基础、科学计算及数据分析》Jupyter Notebook Viewer](http://nbviewer.jupyter.org/github/lijin-THU/notes-python/blob/master/index.ipynb)
  
  [清华大学 李金老师 Python笔记 《自学Python——编程基础、科学计算及数据分析》](https://github.com/lijin-THU/notes-python)
- [人工智能 机器学习 深度学习 入门及进阶资料](Python入门网络爬虫之精华版)
- [Python入门网络爬虫之精华版](https://github.com/lining0806/PythonSpiderNotes)

### python36 python37共存

```
将python36目录下的python.exe的名字改成python36.exe   python37目录下的python.exe仍然不变
pyhton36 python37 都添加path  假设python37在path的靠前位置，则默认先识别到是python37
cmd 中 输入python打开的是python37 python36打开的是python36
cmd 中 输入pip3.6则下载到python36目录下pip则下载到python37下

tensorflow 在jupyter notebook中的使用：由于tensorflow目前支持到python36：
先将python37从path中删除，打开就是用的python36解释器
使用结束需要用python37的话,比如Django的Xadmin，再将python37添加到path（在python36前）
```
### python源码pass
```
python定义函数，必须有函数体，否则编译就会报错。函数体用一句pass占位是防止报错，并且不会有任何动作。
这种只有pass的函数一般有以下几种可能：

1 父类中声明函数，但不声明实现，由继承的子类进行实现，也就是说这就是一个空方法；
        
2 python是C语言实现的，尽管有很多标准库是由python代码实现，但是涉及到底层支撑架构的功能还是C代码。
  一些IDE为了对这些进行友好代码提示，会弄和底层一样的访问接口，而其实现直接写 pass 略过。
  源码在https://github.com/python/cpython
```
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

- [Python 3.8.0a0 documentation](https://docs.python.org/3.8/)
- [The Python Standard Library](https://docs.python.org/3.8/library/index.html)
- [Python 3.5.2中文文档](https://yiyibooks.cn/xx/python_352/index.html)


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
- [内置的原子数据类型](https://github.com/facert/python-data-structure-cn/blob/master/1.%E4%BB%8B%E7%BB%8D/1.8.%E6%95%B0%E6%8D%AE%E5%85%A5%E9%97%A8/README.md)
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

| |1 |2 |3 |4|
|-|-|-|-|-|
|🐍不可变数据（四个）|Number（数字）|String（字符串）|Tuple（元组）|Sets（集合）|
|🐼 可变数据（两个）  |List（列表）  |Dictionary（字典）|||
|🌳有序 |            List（列表）|String（字符串）|Tuple（元组）||
|🎯无序|             Dictionary（字典）|Sets（集合）|||



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

[multiprocessing  threading](https://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247484084&idx=1&sn=573989b9526aef01a3d515ab09afe86a&chksm=a73c628c904beb9a39adef9b95a1ce6560245b7f4e2a39207a55abc1a293935be203a35bcb13&mpshare=1&scene=1&srcid=&pass_ticket=0QnHRl6v1Xkew4C5DrpSerNBri6BPOinWKKfydIySHIIQ%2BKJhsjSdnkU2wZYGdie#rd)

```
进程 优先级于 线程  一个进程至少有一个线程

线程是最小的调度执行单元。如何调度进程和线程，完全由操作系统决定。

多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。

总结一句话是“进程是操作系统分配资源的最小单元，线程是操作系统调度的最小单元”。

- 进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单位.

- 线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上不拥有
系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),但是它可与同属一个进程的其他的线程共
享进程所拥有的全部资源.一个线程可以创建和撤销另一个线程;同一个进程中的多个线程之间可以并发执行.

- 进程和线程的主要差别在于它们是不同的操作系统资源管理方式。进程有独立的地址空间，一个进程崩溃后，在保护模式
下不会对其它进程产生影响，而线程只是一个进程中的不同执行路径。线程有自己的堆栈和局部变量，但线程之间没有单独
的地址空间，一个线程死掉就等于整个进程死掉，所以多进程的程序要比多线程的程序健壮，但在进程切换时，耗费资源较
大，效率要差一些。但对于一些要求同时进行并且又要共享某些变量的并发操作，只能用线程，不能用进程。

```
**Python中多线程由于有GIL的影响， 导致在任何时刻仅有一个线程在执行**

**即便在多核心处理器上，使用 GIL 的解释器也只允许同一时间执行一个线程**
```
多进程和多线程最大的不同在于，

**多进程**中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响.

**多线程**中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改.

因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
```

```
Python多进程和多线程哪个快?

由于GIL的存在，很多人认为Python多进程编程更快，针对多核CPU，理论上来说也是采用多进程更能有效利用资源。结论。

    对CPU密集型代码(比如循环计算) - 多进程效率更高

    对IO密集型代码(比如文件操作，网络爬虫) - 多线程效率更高。

为什么是这样呢？其实也不难理解。对于IO密集型操作，大部分消耗时间其实是等待时间，在等待时间中CPU是不需要工作的，

那你在此期间提供双CPU资源也是利用不上的，相反对于CPU密集型代码，2个CPU干活肯定比一个CPU快很多。

那么为什么多线程会对IO密集型代码有用呢？这时因为python碰到等待会释放GIL供新的线程使用，实现了线程间的切换。

Python中多线程由于有GIL的影响， 导致在任意时间内只有一个线程在运行，所以Python的多线程在处理计算密集型任务上
效果反而不如单线程， 只有在处理IO密集型任务上多线程才能发挥实力，在等待IO过程中Python C源码会释放GIL， 最终
会导致线程在等待IO过程中会被暂停去执行其他的线程。python中GIL主要是由于历史原因导致Cpython虚拟机中的GIL难以
移除，同时GIL的存在保证了多线程之间数据完整性以及状态同步。

```


>>> **12.1 多进程 multiprocessing**

**12.1.1 启动一个子进程并等待其结束**   `os.getpid()  p.start()  p.join()`

单进程代码
```python3
import time
import os

def long_time_task():
    print('当前进程: {}'.format(os.getpid()))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))

if __name__ == "__main__":
    print('当前母进程: {}'.format(os.getpid()))
    start = time.time()
    for i in range(2):
        long_time_task()

    end = time.time()
    print("用时{}秒".format((end-start)))

### 
当前母进程: 14236
当前进程: 14236
结果: 1152921504606846976
当前进程: 14236
结果: 1152921504606846976
用时4.01080060005188秒
```

multiprocessing模块（具有跨平台特性）提供了一个Process类来代表一个进程对象

```python3
from multiprocessing import Process
import time,os

def run_proc(name):                           # 定义一个执行函数run_proc和函数的参数name
    print('Run child process %s (%s)...' % (name, os.getpid()))      #os.getpid()获取当前进程id , os.getppid()获取父进程id 

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())      # 打印当前进程(父进程)id
    start = time.time()
    p1=Process(target=run_proc, args=('test',))     # 传入参数，创建一个Process实例，即创建一个子进程；target为子进程函数，args中的test传给run_proc的参数
    p2=Process(target=run_proc, args=('test',))
    print('等待所有子进程完成。')
    p1.start()                                     # 开启一个进程
    p2.start()
    p1.join()                                      # 等待该进程运行结束
    p2.join()                                      # 等待该进程运行结束
    end = time.time()
    print("总共用时{}秒".format((end - start)))
    
# 在Windows 上实际并未看到子进程的输出，平台原因？？？ 
# 输出不对应
当前母进程: 6920
等待所有子进程完成。
子进程: 17020 - 任务1
子进程: 5904 - 任务2
结果: 1152921504606846976
结果: 1152921504606846976
总共用时2.131091356277466秒
```    

另一种方法：创建一个类继承Process类，并重写run方法。[参考](https://www.cnblogs.com/hypnus-ly/p/8129205.html)
    

**12.1.2 Pool  批量创建子进程**   `p.apply_async` 

```python3
下面介绍一下multiprocessing 模块下的Pool类的几个方法：

1.apply_async

函数原型：apply_async(func[, args=()[, kwds={}[, callback=None]]])

其作用是向进程池提交需要执行的函数及参数， 各个进程采用非阻塞（异步）的调用方式，即每个子进程只管运行自己的，不管其它进程是否已经完成。

2.map()

函数原型：map(func, iterable[, chunksize=None])

Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到结果返回。 注意：虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。

3.map_async()

函数原型：map_async(func, iterable[, chunksize[, callback]])
与map用法一致，但是它是非阻塞的。其有关事项见apply_async。

4.close()

关闭进程池（pool），使其不在接受新的任务。

5. terminate()

结束工作进程，不在处理未处理的任务。

6.join()

主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。
```

```python3
from multiprocessing import Pool, cpu_count
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))   # 用time.sleep结合随机函数来指定每个进程执行多长时间

if __name__=='__main__':
    print("CPU内核数:{}".format(cpu_count()))
    print('当前母进程: {}'.format(os.getpid()))
    p = Pool(4)                   # 同时跑4个进程，默认大小是CPU的核数
    for i in range(6):            # 总共6个进程，由于只能同时跑4个进程，需要等前边4个中某个结束才能加入一个新的进程
        p.apply_async(long_time_task, args=(i,))
    
    p.close()  # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()或terminate()方法，让其不再接受新的Process了。
    p.join()                                      # 等待该进程运行结束
    
# 在Windows 上实际并未看到子进程的输出？？？
```
 **12.1.3 多进程间的数据共享与Process间通信**
 
Python的multiprocessing模块包装了底层的机制，提供了`Queue、Pipes`等多种方式来交换数据。我们以``Queue``为例  
```python3
from multiprocessing import Process, Queue
queue 模块
queue.Queue         class 
queue.Queue.qsize() 
queue.Queue.empty()
queue.Queue.full()
queue.Queue.put(item, block=True, timeout=None) 
queue.Queue.put_nowait(item)
queue.Queue.get(block=True, timeout=None)
queue.Queue.get_nowait()
queue.Queue.join()
p = Process(target='xxx', args=('queue',))
```
生产者和消费者模型 
```python3
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
    pr.terminate()        ？？？
    
# 在Windows 上实际并未看到子进程的输出？？？
 ```

>>> **12.2 多线程 Threading** 

Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，

必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。

这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，

即使100个线程跑在100核CPU上，也**只能用到1个核**。

GIL(Global Interpreter Lock)全局解释器锁:是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，

除非重写一个不带GIL的解释器。所以，在Python中，可以使用多线程，但**不要指望能有效利用多核**。

如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然**不能**利用**多线程**实现多核任务，但可以通过**多进程**实现多核任务。

多个Python进程有各自独立的GIL锁，互不影响。

Python的标准库提供了两个**模块**：`_thread 和 threading`，`_thread`是低级模块，`threading`是高级模块，对_thread进行了封装。

绝大多数情况下，我们只需要使用threading这个高级模块。

**12.2.1 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：** 

```python3
# 标准格式`t = threading.Thread(target= '子线程函数', args=('子线程函数所的参数列表',), name='子线程名')`
threading.current_thread()           #返回当前运行的线程实例
threading.Thread(group=None, target=None, name=None, args=(), kwargs={})          class
threading.Thread.is_alive()   
threading.Thread.start()
threading.Thread.join()
threading.Thread.setDaemon(True)         #守护线程  主线程退出的时候，不管子线程运行到哪里，强行让子线程退出,需要注意的是 setDaemon(True) 在 start() 之前
threading.Lock().acquire()
threading.Lock().release()
threading.local()                      # 创建ThreadLocal对象
Queue()              class
```
由于任何**进程**默认就会启动一个**线程**，我们把该线程称为**主线程**，主线程又可以启动新的线程，

Python的`threading模块`有个`current_thread()函数`，它永远**返回当前线程的实例**。主线程实例的名字叫MainThread，

子线程的**名字在创建时用name参数指定**，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，

如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
```python3
import time, threading

# 新线程执行的代码:
def loop():                                                              # 新线程的代码
    print('thread %s is running...' % threading.current_thread().name)   # print(threading.current_thread().name)=传入的子线程的名字，此处为threading.Thread(target=loop, name='LoopThread')中的LoopThread
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)   # MainThread 正在运行
t = threading.Thread(target=loop, name='LoopThread')                 # Thread中传入loop函数，及name参数（子线程名），创建Thread子线程实例
t.start()                                                            # 子线程开始执行
t.join()                                                             # 主线程等待子线程执行完再退出
print('thread %s ended.' % threading.current_thread().name)          # MainThread 执行完毕

##### 输出
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
#####
join()方法作用     
MainThread在join之后一直停在join的地方，等待子线程 LoopThread 退出后才继续执行下去
没有join()方法的结果
##### 
thread MainThread is running...
thread LoopThread is running...
thread MainThread ended.
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
```

```python3
import threading
import time


def long_time_task(i):
    print('当前子线程: {} - 任务{}'.format(threading.current_thread().name, i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__=='__main__':
    start = time.time()
    print('这是主线程：{}'.format(threading.current_thread().name))
    t1 = threading.Thread(target=long_time_task, args=(1,))
    t2 = threading.Thread(target=long_time_task, args=(2,))
    t1.start()
    t2.start()

    end = time.time()
    print("总共用时{}秒".format((end - start)))
#
这是主线程：MainThread
当前子线程: Thread-1 - 任务1
当前子线程: Thread-2 - 任务2
总共用时0.0017192363739013672秒
结果: 1152921504606846976
结果: 1152921504606846976
#
#为什么总耗时居然是0秒? 我们可以明显看到主线程和子线程其实是独立运行的，主线程根本没有等子线程完成，而是自己结束后就打印了消耗时间。
#主线程结束后，子线程仍在独立运行，这显然不是我们想要的
```

如果要实现主线程和子线程的同步，我们必需使用join方法

```python3
# 如果要实现主线程和子线程的同步，我们必需使用join方法
import threading
import time


def long_time_task(i):
    print('当前子线程: {} 任务{}'.format(threading.current_thread().name, i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__=='__main__':
    start = time.time()
    print('这是主线程：{}'.format(threading.current_thread().name))
    thread_list = []
    for i in range(1, 3):
        t = threading.Thread(target=long_time_task, args=(i, ))
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()     

    end = time.time()
    print("总共用时{}秒".format((end - start)))
    
#
这是主线程：MainThread
当前子线程: Thread - 1 任务1
当前子线程: Thread - 2 任务2
结果: 1152921504606846976
结果: 1152921504606846976
总共用时2.0166890621185303秒
```

当我们设置多线程时，主线程会创建多个子线程，在python中，默认情况下主线程和子线程独立运行互不干涉。

如果希望让主线程等待子线程实现线程的同步，我们需要使用join()方法。如果我们希望一个主线程结束时不再执行子线程，

我们应该怎么办呢? 我们可以使用t.setDaemon(True)

```python3
import threading
import time


def long_time_task():
    print('当子线程: {}'.format(threading.current_thread().name))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__=='__main__':
    start = time.time()
    print('这是主线程：{}'.format(threading.current_thread().name))
    for i in range(5):
        t = threading.Thread(target=long_time_task, args=())
        t.setDaemon(True)
        t.start()

    end = time.time()
    print("总共用时{}秒".format((end - start)))

```
**12.2.2 通过继承Thread类重写run方法创建新线程**

除了使用Thread()方法创建新的线程外，我们还可以通过继承Thread类重写run方法创建新的线程，这种方法更灵活。

下例中我们自定义的类为MyThread, 随后我们通过该类的实例化创建了2个子线程。

```python3
import threading
import time


def long_time_task(i):
    time.sleep(2)
    return 8**20


class MyThread(threading.Thread):
    def __init__(self, func, args , name='', ):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
        self.result = None

    def run(self):
        print('开始子线程{}'.format(self.name))
        self.result = self.func(self.args[0],)
        print("结果: {}".format(self.result))
        print('结束子线程{}'.format(self.name))


if __name__=='__main__':
    start = time.time()
    threads = []
    for i in range(1, 3):
        t = MyThread(long_time_task, (i,), str(i))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    end = time.time()
    print("总共用时{}秒".format((end - start)))


# 输出结果如下所示:
开始子线程1
开始子线程2
结果: 1152921504606846976
结果: 1152921504606846976
结束子线程1
结束子线程2
总共用时2.005445718765259秒
```


**12.2.3 不同线程间的数据共享 比较危险 通常需要加锁 threading.Lock**

   一个进程所含的不同线程间共享内存，这就意味着任何一个变量都可以被任何一个线程修改，因此线程之间共享数据最大的危险在于多个线程同时改一个变量，

把内容给改乱了。如果不同线程间有共享的变量，其中一个方法就是在修改前给其上一把锁lock，确保一次只有一个线程能修改它。

threading.lock()方法可以轻易实现对一个共享变量的锁定，修改完后release供其它线程使用。比如下例中账户余额balance是一个共享变量，

使用lock可以使其不被改乱。

```python3
lock = threading.Lock()                # 创建一个锁
def run_thread(n):
    for i in range(100000):        
        lock.acquire()                 # 先要获取锁
        try:           
            change_it(n)               # 执行一段代码
        finally:            
            lock.release()             # 执行代码完了一定要释放锁,try...finally 确保锁一定会被释放。
```
```python3
import threading


class Account:
    def __init__(self):
        self.balance = 0

    def add(self, lock):
        # 获得锁
        lock.acquire()
        for i in range(0, 100000):
            self.balance += 1
        # 释放锁
        lock.release()

    def delete(self, lock):
        # 获得锁
        lock.acquire()
        for i in range(0, 100000):
            self.balance -= 1
        # 释放锁
        lock.release()


if __name__ == "__main__":
    account = Account()
    lock = threading.Lock()
    # 创建线程
    thread_add = threading.Thread(target=account.add, args=(lock,), name='Add')
    thread_delete = threading.Thread(target=account.delete, args=(lock,), name='Delete')

    # 启动线程
    thread_add.start()
    thread_delete.start()

    # 等待线程结束 
    thread_add.join()
    thread_delete.join()

    print('The final balance is: {}'.format(account.balance))
```
另一种实现不同线程间数据共享的方法就是使用消息队列queue。不像列表，**queue是线程安全的，可以放心使用**，见下文
 
**使用queue队列通信-经典的生产者和消费者模型**

下例中创建了两个线程，一个负责生成，一个负责消费，所生成的产品存放在queue里，实现了不同线程间沟通。

```python3
from queue import Queue
import random, threading, time


# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            print("{} is producing {} to the queue!".format(self.getName(), i))
            self.queue.put(i)
            time.sleep(random.randrange(10) / 5)
        print("%s finished!" % self.getName())


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            val = self.queue.get()
            print("{} is consuming {} in the queue.".format(self.getName(), val))
            time.sleep(random.randrange(10))
        print("%s finished!" % self.getName())


def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print('All threads finished!')


if __name__ == '__main__':
    main()
```
**队列queue的put方法**可以将一个对象obj放入队列中。如果队列已满，此方法将阻塞至队列有空间可用为止。

**queue的get方法**一次返回队列中的一个成员。如果队列为空，此方法将阻塞至队列中有成员可用为止。

queue同时还自带emtpy(), full()等方法来判断一个队列是否为空或已满，但是这些方法并不可靠，

因为多线程和多进程，在返回结果和使用结果之间，队列中可能添加/删除了成员。



>>> **12.3 ThreadLocal**

一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

```python3
import threading
   
local_school = threading.local()                      # 创建全局ThreadLocal对象
# print(type(local_school))        #  <class '_thread._local'>

def process_student():    
    std = local_school.student                        # 获取当前线程关联的student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(std_name):    
    local_school.student = std_name                   # 绑定ThreadLocal的student   local_school.student？？？local_school的属性？
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')  # 此处args传给process_thread函数的std_name,  name指定子线程的名字，传给threading.current_thread().name，不传则为Thread-1， Thread-2
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-A')
t1.start()
t2.start()
t1.join()
t2.join()
```

>>> **12.4 分布式进程**

可以在多台机子上跑

##### task_master.py
```python3
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
manager.shutdown()                                                QueueManager.shutdown()
print('master exit.')
```
##### task_worker.py  另一台机子
```python3
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
