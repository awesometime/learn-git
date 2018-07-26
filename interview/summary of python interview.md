5400+star的 关于Python的面试题 -学习总结-

#### 1 Python的函数参数传递

类型是属于 对象(可变、不可变)的，而不是变量
```
a = 1                a为变量，也叫引用，对地址的引用
def fun(a):          1是对象------strings, tuples, numbers是不可更改的对象
    a = 2                 |------list, dict, set           是可以修改的对象
fun(a)               当一个 引用a 传递给函数的时候, 函数自动复制一份引用, 这个函数里的引用和外边的引用没有半毛关系了
print a  # 1
```
#### 7
```
class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"
mc = MyClass()
#print(mc.__superprivate)   error

print(mc._MyClass__superprivate)  #Hello     通过   *对象名._类名__xxx*   这样的方式可以访问.

print(mc._semiprivate)            #, world
```
#### 默认参数是可变的！
函数可以传递默认参数，默认参数的绑定发生在函数定义的时候，以后每次调用默认参数时都会使用同一个引用。
```
def f(x = []):
    x.append(1)
    return x

print f()
print f()
print f()
print f(x = [9,9,9])
print f()
print f()
[1]
[1, 1]
[1, 1, 1]
[9, 9, 9, 1]
[1, 1, 1, 1]
[1, 1, 1, 1, 1]



def f(x = None):
    if x is None:
        x = []
    x.append(1)
    return x

print f()
print f()
print f()
print f(x = [9,9,9])
print f()
print f()
[1]
[1]
[1]
[9, 9, 9, 1]
[1]
[1]
```
