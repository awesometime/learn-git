### 0 函数传不同参数动态创建类,仍然需要写 class 语句

```py3
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

    
if __name__ == "__main__":
    MyClass = create_class("user")
    my_obj = MyClass()
    print(my_obj)
    
# user    
```


### 1 通过type动态创建类, 类也是对象, type创建类的类

type(object_or_name, bases, dict)
type(object) -> the object's type
type(name, bases, dict) -> a new type

```py3
if __name__ == "__main__":
    User = type("User", (), {})
    my_obj = User()
    print(my_obj)
    
# <__main__.User object at 0x00000209062CC0B8>
```
属性 方法
```py3
def say(self):
    return "i am a user"
    # return self.name


if __name__ == "__main__":
    User = type("User", (), {"name": "zhangsan", "say": say})
    my_obj = User()
    print(my_obj.say())
```
继承
```py3
def say(self):
    return "i am a user"
    # return self.name


class BaseClass():
    def answer(self):
        return "i am baseclass"


if __name__ == "__main__":
    User = type("User", (BaseClass,), {"name": "zhangsan", "say": say})
    my_obj = User()
    print(my_obj.answer())

```

### 2 通过指定metaclass创建类

什么是元类， 元类是创建类的类 对象<-class(对象)<-type

不指定metaclass的话, python类的实例化时，会去调用type这个类去创建类对象, 再由类对象创建实例对象

指定metaclass的话, python中类的实例化过程,会首先寻找metaclass，通过metaclass去创建user类

有什么好处？？？
```py3
class WoshiMetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=WoshiMetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"


a = User("my name is a string")
print(a)
print(a.name)
```
