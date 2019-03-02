import operator
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


# 叶节点    存数据
# 非叶节点  存操作符
def buildParseTree(fpexp):
    # 按空格分开
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            # 保持跟踪父对象的简单解决方案是使用栈
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def postorder_eval(tree):
    """后序遍历的常见用法  ---->  计算分析树"""
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorder_eval(tree.getLeftChild())
        res2 = postorder_eval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


def inorder_printexp(tree):
    """ 中序遍历的常见应用  ---->  打印带括号的原始运算表达式"""
    sVal = ""
    if tree:
        sVal = '(' + inorder_printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + inorder_printexp(tree.getRightChild()) + ')'
    return sVal


# def postorder(tree):
#     """ 后序遍历"""
#     if tree != None:
#         postorder(tree.getLeftChild())
#         postorder(tree.getRightChild())
#         print(tree.getRootVal())
#
#
# def evaluate(parseTree):
#     """ 算出结果 核对评估"""
#     opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
#
#     leftC = parseTree.getLeftChild()
#     rightC = parseTree.getRightChild()
#
#     if leftC and rightC:
#         fn = opers[parseTree.getRootVal()]
#         return fn(evaluate(leftC),evaluate(rightC))
#     else:
#         return parseTree.getRootVal()

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(postorder_eval(pt))
print(inorder_printexp(pt))
# 10
# 5
# +
# 3
# *
# 45
