<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**


   * [Python基础知识](#python基础知识)
      * [1 yield 函数](#1-yield-函数)
      * [2 Python 中的反射](#2-python-中的反射)
      * [3 sys.stdout sys.stdin](#3-sys.stdout-sys.stdin)
      * [4 类变量和实例变量](#4-类变量和实例变量)
      * [16 单例模式](#16-单例模式)
         * [1 使用__new__方法](#1-使用__new__方法)
         * [2 共享属性](#2-共享属性)
         * [3 装饰器版本](#3-装饰器版本)
         * [4 import方法](#4-import方法)


## Python基础知识

### 1 yield 函数

- [  yield 理解 ](https://blog.csdn.net/Ren_ger/article/details/81088903)

### 2 Python 中的反射

- 反射  基于反射实现类Web框架的路由系统 [详见79行](https://github.com/awesometime/CMDB/blob/master/assets/asset_handler.py)
 

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

### 3 sys.stdout-sys.stdin
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
