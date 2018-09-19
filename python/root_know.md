<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**


   * [Python基础知识](#python基础知识)
      * [1 yield函数](#1-yield函数)
      * [2 Python中的反射](#2-python中的反射)
      * [3 恩sys.stdout sys.stdin](#3-恩sys.stdout-sys.stdin)
      * [4 恩sys.argv](#4-恩sys.argv)
      * [5 恩locals() globals()](#5-恩locals()-globals())
      * [6 break continue](#6-break-continue)
         * [1 使用__new__方法](#1-使用__new__方法)
         * [2 共享属性](#2-共享属性)
         * [3 装饰器版本](#3-装饰器版本)
         * [4 import方法](#4-import方法)


## Python基础知识

### 1 yield函数

- [  yield 理解 ](https://blog.csdn.net/Ren_ger/article/details/81088903)

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
