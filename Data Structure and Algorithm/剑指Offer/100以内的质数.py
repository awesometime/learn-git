# 遍历从 2 到该数平方根的所有整数，
# 如果发现任何一个数能整除该数，则返回 False。
# 如果没有发现任何因数，则返回 True

# python 求平方根
print(9 ** 0.5)


def zhishu():
    a = []
    for num in range(2, 101):
        flag = False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = True
        if not flag:
            a.append(num)
            print(num)
    print(len(a))


zhishu()


# 优化 除2以外,所有质数都是奇数,所以从3开始 只遍历奇数
# 内层也只遍历奇数,奇数除2肯定除不尽,没必要除
def zhishu2():
    a = [2]
    print(2)
    for num in range(3, 101, 2):
        flag = False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                flag = True
        if not flag:
            a.append(num)
            print(num)
    print(len(a))


zhishu2()
