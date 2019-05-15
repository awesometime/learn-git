# python3.3新加了yield from语法
from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "bobby1": "http://projectsedu.com",
    "bobby2": "http://www.imooc.com",
}

# chain库
# for value in chain(my_list, my_dict, range(5, 10)):
#     print(value)
# # 1
# # 2
# # 3
# # bobby1
# # bobby2
# # 5
# # 6
# # 7
# # 8
# # 9


#---------------------------------
# 自己实现一个chain
# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         for value in my_iterable:
#             yield value
#
#
# for value in my_chain(my_list, my_dict, range(5, 10)):
#     print(value)


#-----------------------------------
# yield from iterable 实现chain
# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         yield from my_iterable
#
#
# for value in my_chain(my_list, my_dict, range(5, 10)):
#     print(value)


#------------------------------------
# yield   yield from 区别
# def g1(iterable):
#     yield iterable
#
# def g2(iterable):
#     yield from iterable
#
# for value in g1(range(10)):
#     print(value)
# for value in g2(range(10)):
#     print(value)

# range(0, 10)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


#---------------------------------------
# def g1(gen):
#     yield from gen
#
#
# def main():
#     g = g1()
#     g.send(None)

# main(调用方)   g1(委托生成器)    gen(子生成器)
# yield from会在调用方与子生成器之间建立一个双向通道
