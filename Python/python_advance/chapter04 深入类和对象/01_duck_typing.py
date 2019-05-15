# https://www.cnblogs.com/crazymagic/articles/10066543.html


# 鸭子类型（英语：duck typing）在程序设计中是【动态类型】的一种风格
# 一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。
# 当我们在多个类中，定义了相同的方法，那么我们就可以给它归为一类，这就是鸭子类型

# 其它语言区别
# Java  【多态】 继承父类 重写父类同名方法
# 每次需要指明 函数、类的类型  强类型


# 考虑用于一个使用鸭子类型的语言的以下伪代码：
# 
# function calculate(a, b, c) => return (a+b)*c
# 
# example1 = calculate (1, 2, 3)
# example2 = calculate ([1, 2, 3], [4, 5, 6], 2)
# example3 = calculate ('apples ', 'and oranges, ', 3)
# 
# print to_string example1
# print to_string example2
# print to_string example3
# 在样例中，每次对calculate的调用都使用的对象（数字、列表和字符串）在继承关系中没有联系。
# 只要对象支持“+”和“*”方法，操作就能成功。例如，翻译成Ruby或Python语言，运行结果应该是：
# 
# 9
# [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# apples and oranges, apples and oranges, apples and oranges, 
# 这样，鸭子类型在不使用继承的情况下使用了多态。唯一的要求是calculate函数需要作为参数的对象拥有“+”和“*”方法。

class Cat(object):
    def say(self):
        print("i am a cat")

class Dog(object):
    def say(self):
        print("i am a fish")

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

company = Company(["tom", "bob", "jane"])

class Duck(object):
    def say(self):
        print("i am a duck")

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


dog = Dog()
a = ["bobby1", "bobby2"]

b = ["bobby2", "bobby"]
name_tuple = ["bobby3", "bobby4"]
name_set = set()
name_set.add("bobby5")
name_set.add("bobby6")
a.extend()
print(a)

