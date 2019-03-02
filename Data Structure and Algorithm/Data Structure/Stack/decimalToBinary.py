from pythonds.basic.stack import Stack


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


# print(divideBy2(233))


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        rem = digits[rem]
        # print(rem,end=" ")
        remstack.push(rem)
        decNumber = decNumber // base
    # print()

    newString = ""
    while not remstack.isEmpty():
        # newString = newString + digits[remstack.pop()]
        newString = newString + str(remstack.pop())

    return newString


# print(baseConverter(233,2))  #11101001
# print(baseConverter(233,8))  #351
# print(baseConverter(233,16)) #E9


# 递归recursion
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]
    # [Previous line repeated 995 more times]
    # RecursionError: maximum recursion depth exceeded

print(toStr(233, 16))
print(toStr(1453, 16))  # 5AD

from pythonds.basic.stack import Stack

rStack = Stack()

def toStr2(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])  # if-else 可以合一起
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr2(1453,16))  # 5AD