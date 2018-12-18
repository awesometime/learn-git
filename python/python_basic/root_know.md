- [8000 star Python的面试题](https://github.com/taizilongxu/interview_python)
- [100 python 面试题](https://blog.csdn.net/weixin_41666747/article/details/79942847)

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**


   * [Python基础知识](#python基础知识)
      * [1 yield函数](#1-yield函数)
      * [2 Python中的反射 getattr hasattr setattr delattr](#2-python中的反射-getattr-hasattr-setattr-delattr)
      * [3 sys.stdout sys.stdin](#3-sys.stdout-sys.stdin)
      * [4 sys.argv](#4-sys.argv)
      * [5 locals() globals()](#5-locals()-globals())
      * [6 break continue](#6-break-continue)
      * [7 str repr](#7-str-repr)
      * [8 and or](#8-and-or)
      * [9 arg kwarg](#9-arg-kwarg)
      * [10 修饰符](#10-修饰符)
      * [11 函数 类方法 实例方法](#11-函数-类方法-实例方法)
      * [12 赋值引用 浅拷贝 深拷贝](#12-赋值引用-浅拷贝-深拷贝)
      * [13 字符 编码与二进制  序列化](#13-字符-编码与二进制--序列化)
      * [14 try except](#14-try-except)
      * [15 new init super 方法](#15-new-init-super-方法)
      * [16 单双下划线](#16-单双下划线)
      * [17 yeild iterator](#17-yeild-iterator)
      * [18 readline readlines](#18-readline-readlines)
      * [19 闭包](#19-闭包)
      * [20 list sort sorted](#20-list-sort-sorted)
      * [21 re正则表达式](#21-re正则表达式)
      * [22 python垃圾回收机制](#22-python垃圾回收机制)
      * [23 lambda](#23-lambda)
      * [24 python传参数是传址 引用](#24-python传参数是传址-引用)
      * [25 if not](#25-if-not)
      * [26 name main](#26-name-main)
      * [27 classmethod staticmethod](#27-classmethod-staticmethod)
      
         * [1 使用__new__方法](#1-使用__new__方法)
         * [2 共享属性](#2-共享属性)
         * [3 装饰器版本](#3-装饰器版本)
         * [4 import方法](#4-import方法)


## Python基础知识

### 1 yield函数

- [  yield 理解 ](https://blog.csdn.net/Ren_ger/article/details/81088903)
- [  yield用法总结  ](https://www.cnblogs.com/python-life/articles/4549996.html)

```python
def fun():
    print('good')
    yield 5

# fun().__next__()  
# fun().__next__()  
# fun().__next__()  # 不会抛异常

# good
# good
# good


f = fun()
print(f.__next__())
# f.__next__()  # 由于之后没有yield,再次next()就会抛出错误

try:
    print(f.__next__())
except StopIteration as e:
    print("StopIteration")

# good
# 5
# StopIteration
```

```python
def fun():
    for i in range(20):
        x = yield i  #表达式(yield i)的返回值将赋值给x
        print(x)
        print('good', x)

a = fun()
print(a.__next__())
# 0. 遇到yield就返回 相当于return     a.__next__()相当于a.send(None)
# 1. 第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的
# 2. send(msg) 和 next()是有返回值的，它们的返回值很特殊，返回的是下一个yield表达式的参数。
#    比如yield 5，则返回 5
print("---")
print(a.__next__())   # 从上次离开的地方执行

print("---")
l = a.send(5)         # (yield i) 表达式被赋予了 5 ,即 x = (yield i) = 5
print(l)              # 但是 a.send(5) 返回的是下一个yield表达式的参数 ,此处为2

print("---")
print(a.send(5))

print("---")
print(a.send('python :):):)'))


# 0
# ---
# None       # 函数内的结果
# good None  # 函数内的结果
# 1          # print(a.__next__())的结果
# ---
# 5
# good 5
# 2
# ---
# 5
# good 5
# 3
# ---
# python :):):)
# good python :):):)
# 4
```

```python
import time
def func(n):
    for i in range(0, n):
        arg = yield i
        print('func:', arg)


f = func(10)
while True:
    print('next:', next(f))
    print('send:', f.send(100))
    time.sleep(1)

# 输出
# next: 0
# func: 100
# send: 1
# func: None
# next: 2
# func: 100
# send: 3
# func: None
# next: 4
# func: 100
# send: 5
# func: None
# next: 6
# func: 100
# send: 7
# func: None
# next: 8
# func: 100
# send: 9
# func: None
# Traceback (most recent call last):
#   File "F:/Python/projects/yield.py", line 73, in <module>
#     print('next:', next(f))
# StopIteration

```

### 2 Python中的反射 getattr hasattr setattr delattr

- 反射  getattr hasattr setattr delattr

基于反射实现类Web框架的路由系统 [详见79行](https://github.com/awesometime/CMDB/blob/master/assets/asset_handler.py)
 

```python
class Foo(object):
 
    def __init__(self):
        self.name = 'abc'
 
    def func(self):
        return 'func--函数运行ok'
 
obj = Foo()

# 1 获取成员
# 判断ｏｂｊ中是否有第二个参数
# 如果第二个是属性，则返回属性值，如果是方法名，则返回方法的内存地址，如果第二个参数没有在对象中找到，程序报错

ret = getattr(obj, 'func')          # 获取的是个对象，返回ｆｕｎｃ的内存地址
print(ret)                          # <bound method Foo.func of <__main__.Foo object at 0x000002D08D42E7B8>>
r = ret()                           # 需要将对象实例化
print(r)                            # func--函数运行ok

ret1 = getattr(obj, 'name')         # 返回字符串
print(ret1)                         # abc


# 2 检查成员
ret = hasattr(obj,'func')            # 因为有func方法所以返回True
print(ret)                           # True


# 3 设置成员
print(obj.name)                      # abc
ret = setattr(obj,'name',19)
print(obj.name)                      # 19


# 4 删除成员属性
print(obj.name)                      # 19
delattr(obj,'name')
print(obj.name)                      # 报错

```
```python
#!/usr/bin/env python
#coding=utf-8
__author__ = 'lx'

#1.py           注意  1.py 2.py 在同一目录下
class Foo:
    def __init__(self,name):
        temp = "xxx"
        self.name = name
 
    def show(self):
        print('show wo')
        
#!/usr/bin/env python
#coding=utf-8
__author__ = 'lx'

#2.py
#导入模块
print('0')
m = __import__("1",fromlist=True)
print(m)

#去模块中找类
class_name = getattr(m,"Foo")
print(class_name)
#根据类创建对象
obj = class_name("Yj")
print(obj)
#去对象中找方法
ret = getattr(obj,'show')
print('1')
r = ret()
print(r)

#去对象中找name对应的值
print('2')
val = getattr(obj,'name')
print('3')
print(val)

结果
0
<module '1' from 'C:/Users/li/Desktop\\1.py'>
<class '1.Foo'>
<1.Foo object at 0x000001BD3AEDDB00>
1
show wo
None
2
3
Yj

```

### 3 sys.stdout sys.stdin


```python
# 在python中调用print时，事实上调用了sys.stdout.write(obj+'\n')
# print 将需要的内容打印到控制台，然后追加一个换行符
# 以下两行代码等价：

sys.stdout.write('hello' + '\n')
print('hello')

# sys.stdin与input

import sys
h1 = input()               # lin
h2 = sys.stdin.readline()  # lin
print(len(h1))  # 3
print(len(h2))  # 4

# sys.stdin.readline( )会将标准输入全部获取，包括末尾的'\n'，因此用len计算长度时是把换行符'\n'算进去了的，
# 但是input( )获取输入时返回的结果是不包含末尾的换行符'\n'的。

# 因此如果在平时使用sys.stdin.readline( )获取输入的话，不要忘了去掉末尾的换行符，可以用strip( )函数
#（sys.stdin.readline( ).strip('\n')）或sys.stdin.readline( )[:-1]这两种方法去掉换行。

```

### 4 sys.argv

[参考Python中 sys.argv[]的用法简明解释](http://www.cnblogs.com/aland-1415/p/6613449.html)

[Pycharm的传参 像cmd中执行一样 python 1.py arg1 arg2](http://www.mamicode.com/info-detail-2053390.html)

Run“ ---  "Edit Configurations" --- "Script parameters"  参数之间用空格隔开
```python
# 假如 G:/PyCharm/PythonProjects/cmdb/Client/bin下有一个main.py文件，里面有a_func b_func 方法
# main.py
if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)
def a_func():
   pass
def b_func():
   pass  
print(sys.argv)
for i in range(len(sys.argv)):
    print(sys.argv[i])

# 在G:/PyCharm/PythonProjects/cmdb/Client/bin/执行 
G:/PyCharm/PythonProjects/cmdb/Client/bin>main.py a_func b_func
['main.py', 'a_func', 'b_func', 't', 't', 'u', 'i', 'gik']
main.py
a_func
b_func
t
t
u
i
gik
```
```python
class ArgvHandler(object):  # 继承

    def __init__(self, args):  
        self.args = args
        self.parse_args()

    def parse_args(self):
        """
        分析参数，如果有参数指定的功能，则执行该功能，如果没有，打印帮助说明。
        :return:
        """
        if len(self.args) > 1 and hasattr(self, self.args[1]):
            func = getattr(self, self.args[1])
            func()
        else:
            self.b_func()
# G:/PyCharm/PythonProjects/cmdb/Client/bin>main.py a_func b_func
# 就会把a_func b_func当参数传给 self.args
```

### 5 locals() globals()

 参考 https://yq.aliyun.com/ziliao/114421
 
### 6 break continue

```python
#1   循环语句可以有一个 else 子句;
#    当（for）循环迭代完整个列表或（while）循环条件变为假，而非由break语句终止时，就会执行这个else语句
#    循环中的else子句  与   try语句的else子句有更多的共同点：   try语句的else子句在未出现异常时运行
for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...     
...     print('333')

break  跳出for...else...  到 print('333')

#2
for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found a number", num)
print('333')
continue  跳出for 到下一次循环！！！    而不是print('333')

```
### 7 str repr
```python
#  __repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员
class A(object):
    def __str__(self):
	    return 'this is A'   # 用print输出具体的信息；用t为对象

class B(object):
	pass
	    
class C(object):	
	def __repr__(self):
	    return 'this is A'        # 用print用t输出具体的信息

t = [A(),B(),C()]	

print(t)
# [<__main__.A object at 0x0000022149C58390>, <__main__.B object at 0x0000022149CB2B38>, this is A]

print(t[0])
print(t[1])
print(t[2])

# this is A      str  printt[0]时候才会显示
# <__main__.B object at 0x0000022149CB2B38>
# this is A      repr  任何时候都打印显示
```

### 8 and or

and:    遇假则假，所以前面为假就不执行和判断后面，前面为真则继续判断执行后面的;

or:     遇真则真，所以前面为真就不执行和判断后面，前面为假则继续判断执行后面的。

### 9 arg kwarg

*arg        任意个位置/形式参数     不加 * 为一个

**kwarg      任意个关键词参数  

https://www.jianshu.com/p/e0d4705e8293




### 10 修饰符

装饰符(修饰符)@类似于 [回调函数](https://www.zhihu.com/question/19801131)，把其它的函数（暂且称为目的函数）作为自己的入参，在目的函数执行前，执行一些自己的操作，

比如：计数、打印一些提示信息等，然后返回目的函数。

[python中闭包和装饰器的理解（关于python中闭包和装饰器解释最好的文章）](https://www.cnblogs.com/3me-linux/p/6761635.html)

```python
import time

def time(func):     # 传入啥 返回啥  中间执行自己的小动作
    print(time.ctime())
    return func()    # 
    
@time  # 从这里可以看出@time 等价于 time(xxx()),但是这种写法你得考虑python代码的执行顺序
def xxx():
    print('Hello world!')

运行结果：
Wed Jul 26 23:01:21 2017
Hello world!

```
### 11 函数 类方法 实例方法
```python
def aa(d, na=None, *kasd, **kassd):
    pass
class A(object):
    def f(self):
        return 1
a = A()
print '#### 各自方法描述 ####'
print '## 函数     %s' % aa
print '## 类方法   %s' % A.f
print '## 实例方法 %s' % a.f

#### 各自方法描述 ####
## 函数   <function aa at 0x000000000262AB38>
## 类方法   <unbound method A.f>
## 实例方法 <bound method A.f of <__main__.A object at 0x0000000002633198>>
```

### 12 赋值引用 浅拷贝 深拷贝

赋值引用   两个 a，b 指向同一对象 同时改变

浅拷贝    父对象（一级层面）是一个独立的对象，但是他们的子对象（内部 可理解为二级层面）还是指向同一对象，所以子对象会随着 a 的改变而改变

深拷贝    两个 a，b 两者是完全独立的

应用： 列表  **字典

[参考](http://www.cnblogs.com/wushuaishuai/p/7737917.html)

```python
import copy
a = [1, 2, 3, 4, ['a', 'b']] #原始对象
  
b = a                       #赋值，传对象的引用
c = copy.copy(a)            #对象拷贝，浅拷贝
d = copy.deepcopy(a)        #对象拷贝，深拷贝
  
a.append(5)                 #修改对象a
a[4].append('c')            #修改对象a中的['a', 'b']数组对象
  
print( 'a = ', a )
print( 'b = ', b )
print( 'c = ', c )
print( 'd = ', d )

#
('a = ', [1, 2, 3, 4, ['a', 'b', 'c'], 5])
('b = ', [1, 2, 3, 4, ['a', 'b', 'c'], 5])
('c = ', [1, 2, 3, 4, ['a', 'b', 'c']])
('d = ', [1, 2, 3, 4, ['a', 'b']])
```
### 13 字符 编码与二进制  序列化

[字符、编码与二进制——序列化](https://mp.weixin.qq.com/s/7tQIKpwH4J4djCM3l5pDnQ)


### 14 try except
[try except (异常捕获)](https://www.cnblogs.com/Keep-Ambition/p/7306074.html)

### 15 new init super 方法
**new init**
```
1、__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别

2、__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例

3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，
如果是其他类的类名，(  ????? 找个例子  )；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

```

```python
class A(object):
    def __init__(self):
        print("init function invoked", self)

    def __new__(cls):
        print("cls  id", id(cls))
        print("new function invoked", object.__new__(cls))
        return object.__new__(cls)


a = A()
print("A  id", id(A))
b = A()

# cls  id 2722172060296
# new function  <__main__.A object at 0x00000279D00D8438>
# init function <__main__.A object at 0x00000279D00D8438>
# A  id 2722172060296
# cls  id 2722172060296
# new function  <__main__.A object at 0x00000279D00D8358>
# init function <__main__.A object at 0x00000279D00D8358>
```


[Python类与对象实例详解](https://www.imooc.com/article/18018?block_id=tuijian_wz)

定义类IntTuple继承tuple,并实现new,修改实例化行为
先执行new  再执行init
new方法接受的参数虽然也是和init一样，但init是在类实例创建之后调用，而 new方法正是创建这个类实例的方法。new方法会返回所构造的对象，init则不会，在使用new返回对象的时候会隐式调用init函数。new函数必须以cls作为第一个参数，而init则以self作为其第一个参数

```python
class IntTuple(tuple):
    def __new__(cls, iterable):
        # 重写父类  new 方法 以满足自己需求
 	g = (x for x in iterable if isinstance(x,int) and x > 0)
        print(cls)
        # return super(IntTuple, cls).__new__(cls, g)
        return super().__new__(cls, g)   # 可省略  必须return
        # return tuple().__new__(cls, g)
        
	# 必须return init 才能接收到创建的实例
	# 调用父类的__new__方法
        # 找到IntTuple的父类（tuple），然后把 类IntTuple 的 类对象cls 转换为 类tuple 的对象，然后转换后的 类tuple对象 调用自己的__new__方法
	
    def __init__(self, iterable):
        print(self)
        # super(IntTuple,self).__init__()
	super().__init__()
        # 找到IntTuple的父类（tuple），然后把 类IntTuple 的 对象self 转换为 类tuple 的对象，然后“被转换”的 类tuple对象 调用自己的__init__方法
	
t = IntTuple([1,-1,'abc',6,['x','y'],3])
print t

# 输出：
<class '__main__.IntTuple'>
(1, 6, 3)
(1, 6, 3)
```
**super**
[super的使用详解](https://blog.csdn.net/brucewong0516/article/details/79121179)
```python
class Parent(object):
    Value = "Hi, Parent value"
    def fun(self):
        print("This is from Parent")

class Child(Parent):
    Value = "Hi, Child  value"
    def fun(self):
        print("This is from Child")
        Parent.fun(self)   #调用父类Parent的fun函数方法

c = Child()    
c.fun()

# This is from Child
# This is from Parent  #实例化子类Child的fun函数时，首先会打印上条的语句，再次调用父类的fun函数方法
```
```python
class Parent(object):
    Value = "Hi, Parent value"
    def fun(self):
        print("This is from Parent")

class Child(Parent):
    Value = "Hi, Child  value"
    def fun(self):
        print("This is from Child")
        #Parent.fun(self)
        super(Child,self).fun()  #相当于用super的方法与上一调用父类的语句置换

c = Child()    
c.fun()

# This is from Child
# This is from Parent  #实例化子类Child的fun函数时，首先会打印上条的语句，再次调用父类的fun函数方法

```
### 16 单双下划线
https://www.cnblogs.com/hester/articles/4936603.html
```python
#主要存在四种情形

object # public
__object__   # special, python system use, user should not define like it
__object     # private (私有变量轧压（Private name mangling）during runtime)
_object      # obey python coding convention, consider it as private

In [13]: class A(object):
    ...:        def __init__(self):
    ...:               self.__private()
    ...:               self.public()
    ...:        def _private(self):             # _
    ...:               print ('A.__private()')
    ...:        def public(self):
    ...:               print ('A.public()')
    ...: class B(A):
    ...:        def private(self):
    ...:               print ('B.__private()')
    ...:        def public(self):
    ...:               print ('B.public()')
    ...: b = B()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-13-542aaca0c968> in <module>
     12        def public(self):
     13               print ('B.public()')
---> 14 b = B()

<ipython-input-13-542aaca0c968> in __init__(self)
      1 class A(object):
      2        def __init__(self):
----> 3               self.__private()
      4               self.public()
      5        def _private(self):

AttributeError: 'B' object has no attribute '_A__private'
私有变量会在代码生成之前被转换为长格式（变为公有）。转换机制是这样的：在变量前端插入类名，
再在前端加入一个下划线字符。这就是所谓的私有变量轧压（Private name mangling）。
如类 A里的__private标识符将被转换为_A__private，

In [14]: class A(object):
    ...:        def __init__(self):
    ...:               self.__private()
    ...:               self.public()
    ...:        def __private(self):
    ...:               print ('A.__private()')
    ...:        def _public(self):
    ...:               print ('A.public()')
    ...: class B(A):
    ...:        def private(self):
    ...:               print ('B.__private()')
    ...:        def public(self):
    ...:               print ('B.public()')
    ...: b = B()
A.__private()
B.public()

In [15]: b._public()   #  "单下划线" 开始的类对象和子类对象自己能访问到这些变量
A.public()

In [16]: b.__private()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-16-e63e1c980c04> in <module>
----> 1 b.__private()

AttributeError: 'B' object has no attribute '__private'

In [17]: A.__private()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-17-55946f8ae125> in <module>
----> 1 A.__private()

AttributeError: type object 'A' has no attribute '__private'

In [20]: b._A__private()   # "双下划线" 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据
A.__private()              # 前面加上“单下划线”+类名,eg：_Class__object）机制就可以访问private了

```

### 17 yeild iterator
**Iterator  Iterable**
```python
# In [27]: Iterator.__abstractmethods__
# Out[27]: frozenset({'__next__'})


# In [29]: Iterable.__abstractmethods__
# Out[29]: frozenset({'__iter__'})

# In [1]: l = [1,2,3,4,5]

# In [3]: reversed(l)
# Out[3]: <list_reverseiterator at 0x29d9d6aa390>

# In [4]: iter(l)
# Out[4]: <list_iterator at 0x29d9d74d860>

# Iterable 如 list string      /Iterator 如 l = list 中的 l 有__next__()方法
# Iterable 实现了__iter__ 方法  /Iterator 实现了__next__方法
# 生成器 都是迭代器

import requests
from collections import Iterator, Iterable


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeathrerIterable(Iterable):  
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeathrerIterable([u'北京', u'上海', u'西安', u'齐齐哈尔', u'厦门', u'广州', u'香港', u'深圳', u'呼和浩特']):
    print(x)




In [11]: dir(l)   # list 实现的方法    index  reversed  __iter__
Out[13]:
Out[11]:
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
 '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
  '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
   '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
    'pop', 'remove', 'reverse', 'sort']


In [13]: dir(ll)   # ll = iter(list)   Iterator 实现的方法   __iter__  __next__
Out[13]:
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__',
 '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__',
  '__sizeof__', '__str__', '__subclasshook__']


In [22]: def fun():
    ...:     for i in range(20):
    ...:         x = yield i  #表达式(yield i)的返回值将赋值给x
    ...:         print(x)
    ...:         print('good', x)
    ...:
    ...: a = fun()

In [23]: dir(a)   # 生成器实现的方法   __iter__  __next__
Out[23]:
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', 
'__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 
 'gi_running', 'gi_yieldfrom', 'send', 'throw']
 
 print(a.__iter__() is a)   # true



In [6]: l = range(20)

In [7]: l
Out[7]: range(0, 20)

In [8]: print(l)
range(0, 20)

In [9]: for x in l:print(x)
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19


In [11]: l.__str__
Out[11]: <method-wrapper '__str__' of range object at 0x0000029D9D4B1FC0>

In [12]: l.__str__()
Out[12]: 'range(0, 20)'

In [13]: print(l.__str__())
range(0, 20)

In [14]: print(l.__repr__())
range(0, 20)

In [15]: t = iter(l)

In [17]: from itertools import islice

In [18]: for x in islice(t, 5,10):
    ...:     print(x)
5 6 7 8 9

In [20]: for x in t:
    ...:     print(x)
10 11 12 13 14 15 16 17 18 19  # 从10开始



In [21]: from random  import randint

In [22]: chinese = [randint(60, 100) for x in range(10)]

In [23]: math = [randint(60, 100) for x in range(10)]

In [24]: english = [randint(60, 100) for x in range(10)]

In [26]: for ch, m, en in zip(chinese, math, english):
    ...:     print(ch + m + en)
229 261 216 189 256 237 212 242 246 237



In [27]: from itertools import chain

In [30]: for x in chain(chinese, math, english):
    ...:     print(x)
61 86 69 61 94 93 74 86 70 91 98 88 61 64 62 70 66 74 80 84 70 87 86 64 100 74 72 82 96 62



set(dir(p1)) – set(dir(p2))
```

**反向迭代  __reversed__**
```python
class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    
    # 正向迭代
    def __iter__(self):

        t = self.start
        # while t <= self.end:
        while round(t, 2) <= round(self.end, 2):
            yield t
            t += self.step
    
    
    # 反向迭代
    def __reversed__(self):
        t = self.end
        # while t >= self.start:
        while round(t, 2) >= round(self.start, 2):
            yield t
            t -= self.step


if __name__ == "__main__":
    for x in FloatRange(1.0, 4.0, 0.5):
        print(x)
    print("")
    for x in reversed(FloatRange(1.0, 4.0, 0.5)):  # __reversed__ 方法的调用?
        print(x)

```
**使用生成器函数实现可迭代对象**
```python
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    
    def isPrimeNum(self, k):
        if k < 2:
            return False

        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    
    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k     # 由于yield 有__next__方法，可当做Iterator，从而通过生成器函数yield实现 Iterable(对象)

if __name__ == "__main__":
    for x in PrimeNumbers(1, 100):
        print(x)


#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

### 19 闭包
[看完这篇文章还不懂Python中的闭包，请拍死小编](https://baijiahao.baidu.com/s?id=1601023189180094497&wfr=spider&for=pc)


### 20 list sort sorted

**sort 无返回值，将原列表改变    sorted 返回一个序后的新列表，原列表未改变**
```python

In [51]: d = ['j', 'd', 'f', 'l', 'a']

In [52]: d.sort()

In [53]: type(d.sort)
Out[53]: builtin_function_or_method

In [54]: type(d.sort())  # sort 无返回值  但是会对列表的对象进行排序
Out[54]: NoneType

In [55]: res = "".join(d)  # join 中必须是iterable

In [56]: print(res)
adfjl



In [1]: list = [0,-1,3,-10,5,9]

In [2]: list.sort()

In [3]: list
Out[3]: [-10, -1, 0, 3, 5, 9]



In [4]: list1 = [0,-1,3,-10,5,9]

In [6]: res = sorted(list1,reverse=False)

In [7]: res
Out[7]: [-10, -1, 0, 3, 5, 9]

In [9]: list1
Out[9]: [0, -1, 3, -10, 5, 9]
```
### 21 re正则表达式
1、match        
	
	re.match(pattern, string[, flags])  

从**首字母**开始开始匹配，string如果包含pattern子串，则匹配成功，返回Match对象，失败则返回None，若要完全匹配，pattern要以$结尾。

2、search

        re.search(pattern, string[, flags])  
若string中包含pattern子串，则返回Match对象，否则返回None，注意，如果string中存在多个pattern子串，**只返回第一个**。

3、findall

        re.findall(pattern, string[, flags])  
返回string中所有与pattern相匹配的**全部子串**，返回形式为**列表**，**不需要group()**。

4、finditer

        re.finditer(pattern, string[, flags])  
返回string中所有与pattern相匹配的**全部子串**，返回形式为**迭代器**。


若匹配成功，match()/search()返回的是Match对象，finditer()返回的也是Match对象的迭代器，获取匹配结果需要**调用Match对象的group()、groups或group(index)方法**。
group()、groups()与group(index)的区别，如下所示：

```python
>>> import re  
>>> s = '23432werwre2342werwrew'  
>>> p = r'(\d*)([a-zA-Z]*)'  
>>> m = re.match(p,s)  
>>> m.group()  
'23432werwre'  
>>> m.group(0)  
'23432werwre'  
>>> m.group(1)  
'23432'  
>>> m.group(2)  
'werwre'  
>>> m.groups()  
('23432', 'werwre')  
>>> m = re.findall(p,s)  
>>> m  
[('23432', 'werwre'), ('2342', 'werwrew'), ('', '')]  
>>> p=r'(\d+)'  
>>> m=re.match(p,s)  
>>> m.group()  
'23432'  
>>> m.group(0)  
'23432'  
>>> m.group(1)  
'23432'  
>>> m.groups()  
('23432',)  
>>> m=re.findall(p,s)  
>>> m  
['23432', '2342']  
```

综上：

group()：母串中与模式pattern匹配的子串；

group(0)：结果与group()一样；

groups()：所有group组成的一个元组，group(1)是与patttern中第一个group匹配成功的子串，group(2)是第二个，

依次类推，如果index超了边界，抛出IndexError；

findall()：返回的就是所有groups的数组，就是group组成的元组的数组，母串中的这一撮组成一个元组，那一措组成一个元组，

这些元组共同构成一个list，就是findall()的返回结果。另，如果groups是只有一个元素的元组，findall的返回结果是子串的list，而不是元组的list了。


### 22 python垃圾回收机制

[python垃圾回收机制](https://www.cnblogs.com/Xjng/p/5128269.html)

### 23 lambda

```python
In [1]: a = ["ab", "cd", "", "", "hg",""]

In [3]: res = list(map(lambda x:"fill value" if x=="" else x, a))

In [4]: res
Out[4]: ['ab', 'cd', 'fill value', 'fill value', 'hg', 'fill value']
```


### 24 python传参数是传址 引用
```


```
### 25 if not

if ture  才会执行
[if not ](https://www.cnblogs.com/chenya/p/4218761.html)


### 26 name main
```
__name__就是标识模块的名字的一个系统变量。这里分两种情况：假如当前模块是主模块（也就是调用其他模块的模块），
那么此模块名字就是__main__，通过if判断这样就可以执行“__mian__:”后面的主函数内容；

假如此模块是被import的，则此模块名字为文件名字（不加后面的.py），通过if判断这样就会跳过“__mian__:”后面的内容。
```
### 27 classmethod staticmethod
```python
class A(object):
    def foo(self, x): 
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod  # 有@staticmethod (x)(self, x)效果一样
    def static_foo(x):    # self cls 粉色显示  三个x白色显示
        print("executing static_foo(%s)" % x)
a = A()
m = "ML"
a.foo(m)
a.class_foo(m)
a.static_foo(m)

>>>
executing foo(<__main__.A object at 0x000001C7D0614588>,ML)
self: <__main__.A object at 0x000001C7D0614588>
executing class_foo(<class '__main__.A'>,ML)
cls: <class '__main__.A'>
executing static_foo(ML)

```
```python
class A(object):
    def foo(self, x):         # x白色显示
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    # @classmethod 
    def class_foo(cls, x):    # x白色显示
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    # @staticmethod  不加@staticmethod 的话需要(self, x)
    def static_foo(x):        # self cls 粉色显示  此处x粉色显示，默认传入自己 所以后面报错
        print("executing static_foo(%s)" % x)
a = A()
m = "ML"
a.foo(m)
a.class_foo(m)
a.static_foo(m)

>>>
executing foo(<__main__.A object at 0x0000029EC0C8B8D0>,ML)
self: <__main__.A object at 0x0000029EC0C8B8D0>
executing class_foo(<__main__.A object at 0x0000029EC0C8B8D0>,ML)
cls: <__main__.A object at 0x0000029EC0C8B8D0>
Traceback (most recent call last):
  File "F:/hw_data/code/e.py", line 23, in <module>
    a.static_foo(m)
TypeError: static_foo() takes 1 positional argument but 2 were given
```
### TODO
```
i = 5

def f(arg=i):
    print(arg)

i = 6
f()  # 5
```

### 

