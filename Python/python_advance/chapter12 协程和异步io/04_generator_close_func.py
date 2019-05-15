def gen_func():
    try:
        yield "http://projectsedu.com"
    except GeneratorExit:
        pass

    yield 2
    yield 3
    return "bobby"


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    # RuntimeError: generator ignored GeneratorExit
    # close的目的是要关掉yield语句，如果【后面还有yield语句时】,捕获异常却pass掉，就会执行yield
    # 显然不是我们想要的，所以报RuntimeError 不能将异常pass
    print("bobby")

#-------------------------------
def gen_func():
    try:
        yield "http://projectsedu.com"
    except GeneratorExit:
        pass
    return "job"


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()  # 会将gen_func() 的return语句的内容也屏蔽
    # RuntimeError: generator ignored GeneratorExit
    # close的目的是要关掉yield语句，【后面没有yield语句】,捕获异常却pass掉，就会执行yield
    # 显然不是我们想要的，所以报RuntimeError 不能将异常pass
    try:
        print(next(gen))
    except StopIteration as e:
        print(e.value)
        # return e.value           此处若return错  只能出现在函数里
    print("bobby")
    # print
    # http://projectsedu.com
    # None  # 会将gen_func() 的return语句的内容也屏蔽 如果没有close语句 会打印return的job
    # bobby


# def gen_func():
#     try:
#         yield "http://projectsedu.com"
#     except GeneratorExit:
#         raise StopIteration
#     yield 2
#     yield 3
#     return "job"
#
#
# if __name__ == "__main__":
#     gen = gen_func()
#     print(next(gen))
#     gen.close()
#     # print(next(gen))
#     print("bobby")



# GeneratorExit是继承自BaseException, 而不是Exception
# 注意异常是向上抛出的 抛给__main__
# try:
#     yield "http://projectsedu.com"
# except BaseException:
#     pass

# try:
#     yield "http://projectsedu.com"
# except Exception:       # 可以pass
#     pass