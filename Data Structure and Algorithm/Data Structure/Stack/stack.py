# 从空栈开始，从左到右处理括号字符串。
# 如果一个符号是一个 ( ，将其作为一个信号，对应的 ) 稍后会出现。
# 另一方面，如果符号是 ) ，弹出栈，只要弹出栈的 ( 可以匹配每个 ) ，则括号保持匹配状态。
# 如果任何时候栈上没有出现符合 ( 的 ) ，则字符串不匹配。
# 最后，当所有符号都被处理后，栈应该是空的。


from pythonds.basic.stack import Stack


def parChecker(symbolString):
    """
    single "(" ")"
    :param symbolString:
    :return:
    """
    s = Stack()
    balanced = True  # 匹配状态
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        # symbol == ")"
        else:
            # s 是空栈
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    # 最后，当所有符号都被处理后，栈应该是空的。而且是匹配的
    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChecker('((()))'))    # True
print(parChecker('((()())())'))# True
print(parChecker('(()'))       # False
print(parChecker(''))          # True

def parChecker1(symbolString):
    """
    serveral   "(" "[" "{"
    :param symbolString:
    :return:
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker1('{{([][])}()}'))  # T
print(parChecker1('[{()]'))         # F
print(parChecker1('([)]'))          # F
print(parChecker1('( [ ) ]'))       # error  不能有空格
