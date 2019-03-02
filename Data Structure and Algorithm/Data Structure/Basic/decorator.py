# def f():
#     it=0
#     while it < 5:
#         x = yield 100000000000000
#         print(x)
#         it -= 1
# 
# # 怎么迭代
# 
# listt = [_. for _ in f()]
# print(listt)
"""
https://www.zhihu.com/question/26930016
装饰器在Python使用如此方便都要归因于Python的函数能像普通的对象一样能作为参数传递给其他函数，
可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。
"""
# import os, time, logging
#
# # 设置日志格式，路径
# logdate = time.strftime('%Y-%m-%d', time.localtime())
# error_log_dir = os.path.dirname(__file__).split()[0] + "/log/"
# error_log = error_log_dir + "%s-my.log" % logdate
# logging.basicConfig(filename=error_log, filemode='a', level=logging.INFO,
#                     format='%(asctime)s-%(levelname)s:%(message)s')
#
# def use_logging(level):
#     """带参数的装饰器"""
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print("[{level}]: enter function {func}()".format(
#                 level=level, func=func.__name__))
#             logging.info("enter function {func}()".format(func=func.__name__))
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @use_logging(level='INFO')
# def say(something):
#     print("say {}!".format(something))
#
#
# @use_logging(level='DEBUG')
# def do(something):
#     print("do {}...".format(something))
#
#
# if __name__ == '__main__':
#     say('hello')
#     do("my work")

"""基于类实现装饰器"""
class Logging(object):
    def __init__(self, func):
        """类的构造函数 __init__ () 接受一个函数"""
        self.func = func

    def __call__(self, *args, **kwargs):
        """重载 __call__ () 让类对象拥有了被调用的行为, 并返回一个函数"""
        print("[DEBUG]: enter function {func}()".format(
            func=self.func.__name__))
        return self.func(*args, **kwargs)
@property
@Logging
def say(something):
    print("say {}!".format(something))
