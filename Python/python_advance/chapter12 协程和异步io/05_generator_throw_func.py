def gen_func():
    #1. 可以产出值， 2. 可以接收值(调用方传递进来的值)
    try:
        yield "http://projectsedu.com"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))  # http://projectsedu.com
    gen.throw(Exception, "download error1")
    print(next(gen))  # 3   yield 被跳过
    gen.throw(Exception, "download error111")