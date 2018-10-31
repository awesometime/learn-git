<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**


   * [Python基础知识](#python基础知识)
      * [1 yield函数](#1-yield函数)
      * [2 Python中的反射](#2-python中的反射)
      * [3 sys.stdout sys.stdin](#3-sys.stdout-sys.stdin)
      * [4 sys.argv](#4-sys.argv)
      * [5 locals() globals()](#5-locals()-globals())
      * [6 break continue](#6-break-continue)
      * [7 str repr](#7-str-repr)
      * [8 and or](#8-and-or)
      * [9 arg kwarg](#9-arg-kwarg)
      * [10 @修饰符](#10-@修饰符)
      * [11 函数 类方法 实例方法](#11-函数-类方法-实例方法)
      * [12 赋值引用 浅拷贝 深拷贝](#12-赋值引用-浅拷贝-深拷贝)
      * [13 字符 编码与二进制  序列化](#13-字符-编码与二进制--序列化)
      * [14 try except](#14-try-except)
      * [15 new init super 方法](#15-new-init-super-方法)
      * [17 try except](#15-try-except)
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

### 2 Python中的反射

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




### 10 @修饰符

装饰符@类似于回调函数，把其它的函数（暂且称为目的函数）作为自己的入参，在目的函数执行前，执行一些自己的操作，

比如：计数、打印一些提示信息等，然后返回目的函数。

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
	return super(IntTuple, cls).__new__(cls,g)
        
	# 必须return init 才能接收到创建的实例
	# 调用父类的__new__方法
        # 找到IntTuple的父类（tuple），然后把 类IntTuple 的 类对象cls 转换为 类tuple 的对象，然后转换后的 类tuple对象 调用自己的__new__方法
	
    def __init__(self, iterable):
        print(self)
	super(IntTuple,self).__init__()
        # 找到IntTuple的父类（tuple），然后把 类IntTuple 的 对象self 转换为 类tuple 的对象，然后“被转换”的 类tuple对象 调用自己的__init__方法
	
t = IntTuple([1,-1,'abc',6,['x','y'],3])
print t

#输出：
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

### TODO
```
i = 5

def f(arg=i):
    print(arg)

i = 6
f()  # 5
```
### 
