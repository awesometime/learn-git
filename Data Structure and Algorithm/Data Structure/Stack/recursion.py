# 递归recursion
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]
    # [Previous line repeated 995 more times]
    # RecursionError: maximum recursion depth exceeded


# print(toStr(233, 16))
# print(toStr(1453, 16))  # 5AD

# ------------------------------------------
from pythonds.basic.stack import Stack

rStack = Stack()


# 非递归
def toStr2(n, base):
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


# print(toStr2(1453, 16))  # 5AD
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

# drawSpiral(myTurtle,100)
# # myWin.exitonclick()