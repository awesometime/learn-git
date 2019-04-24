class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

# 层序遍历
# https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0102._binary_tree_level_order_traversal.md

# 返回 [[8], [6, 10], [5, 7, 9, 11]]
class Solution:
    def level_order_traversal(self, root):
        """层序递归"""
        rst = []
        self.level_order_traversal_helper(root, 0, rst)
        return rst  

    def level_order_traversal_helper(self, root, level, rst):
        if not root:
            return
        if len(rst) < level + 1:
            rst.append([])
        rst[level].append(root.val)
        self.level_order_traversal_helper(root.left, level + 1, rst)
        self.level_order_traversal_helper(root.right, level + 1, rst)

# 返回 [8, 6, 10, 5, 7, 9, 11] 
class Solution:
    def level_order_traversal(self, root):
        """层序递归"""
        rst = []
        self.level_order_traversal_helper(root, 0, rst)
        res = []
        for every_level in rst:
            for i in every_level:
                res += [i]
        return res

    def level_order_traversal_helper(self, root, level, rst):
        if not root:
            return
        if len(rst) < level + 1:
            rst.append([])
        rst[level].append(root.val)
        self.level_order_traversal_helper(root.left, level + 1, rst)
        self.level_order_traversal_helper(root.right, level + 1, rst)
        
        
        
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

print("------------")
preorder(r)
print("------------")
inorder(r)
print("------------")
postorder(r)

