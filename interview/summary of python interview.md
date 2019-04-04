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
[ 从输入 URL 到页面展示到底发生了什么？](https://mp.weixin.qq.com/s?__biz=MzUzMzk0NDc5Nw==&mid=2247486570&idx=1&sn=ad5cab1a16e5756e1c66f11f5297a6e5&chksm=fa9d0cd8cdea85cecef06f9a64cb190c2b21e567ed37243f9f418a09d359a201465fe1b4c602&mpshare=1&scene=1&srcid=04032oLBdBXfjIlwN1ROHgPz&pass_ticket=Sj1ytt%2Bvj6SmSFv5uejuICDR1WUmfkQC5bC9dnxsRCYAKrkvu8kqRrc8%2BHBWxJfn#rd)

[前端经典面试题: 从输入URL到页面加载发生了什么？](https://segmentfault.com/a/1190000006879700)
