#!/bin/env python3.1
# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005, 2010
#

import unittest

"""
暂时弃用此方法  python库里的方法  不太好理解
二叉查找树 BST :大小从左到右依次排
特色: 跟踪了self.parent = parent的二叉查找树实现方法
"""
class BinarySearchTree:
    '''
    Author:  Brad Miller
    Date:  1/15/2005
    Description:  Imlement a binary search tree with the following interface
                  functions:
                  __contains__(y) <==> y in x
                  __getitem__(y) <==> x[y]
                  __init__()
                  __len__() <==> len(x)
                  __setitem__(k,v) <==> x[k] = v
                  clear()
                  get(k)
                  items()
                  keys()
                  values()
                  put(k,v)
                  in
                  del <==>
    '''

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, val):
        """树中按照大小插入一个新节点"""
        # todo 重复的键不能正确处理
        # root不为空 继续向下寻找，与左右子节点比较大小
        if self.root:
            self._put(key, val, self.root)
        # root为空 是一个空树
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        """调用put方法来重载赋值[]运算符"""
        self.put(k, v)

    def get(self, key):
        """实现对给定 键key 的 值value 的检索"""
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        """
        :param key:
        :param currentNode:
        :return: 找到返回TreeNode 外部可以访问除了payload之外的TreeNode的其他属性。
                未找到返回None
        """
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        """实现 __getitem__ 方法，我们可以编写一个类似于访问字典的 Python 语句"""
        res = self.get(key)
        if res:
            return res
        else:
            raise KeyError('Error, key not in tree')

    def __contains__(self, key):
        """该方法用来实现 in 操作"""
        if self._get(key, self.root):
            return True
        else:
            return False

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def delete(self, key):
        """删除一个键
        step1: 通过_get()搜索树来找到要删除的节点
        step2:
        """
        # 树节点数>1
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        # 只有root节点 且root.key==key
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        # 其他情况
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        """
        situation1: 要删除的节点(currentNode)是叶节点,没有子节点。
        situation2: 要删除的节点(currentNode)只有一个子节点。
        situation3: 要删除的节点(currentNode)有两个子节点。
        """
        # currentNode is leaf
        if currentNode.isLeaf():  # currentNode is leaf
            if currentNode == currentNode.parent.leftChild:# left leaf
                currentNode.parent.leftChild = None
            else:# right leaf
                currentNode.parent.rightChild = None

        # currentNode has both children
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        # currentNode only has one child
        else:
            # 当前节点只有一个左孩子
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():# 当前左节点只有一个左孩子
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():# 当前右节点只有一个左孩子
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else: # 当前节点是root且只有一个左孩子
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            # 当前节点只有一个右孩子
            else:
                if currentNode.isLeftChild():# 当前左节点只有一个右孩子
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():# 当前右节点只有一个右孩子
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:# 当前节点是root且只有一个右孩子
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tree):
        """中序遍历"""
        if tree != None:
            self._inorder(tree.leftChild)
            print(tree.key)
            self._inorder(tree.rightChild)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tree):
        """后序遍历"""
        if tree:
            self._postorder(tree.rightChild)
            self._postorder(tree.leftChild)
            print(tree.key)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, tree):
        """前序遍历"""
        if tree:
            print(tree.key)
            self._preorder(tree.leftChild)
            self._preorder(tree.rightChild)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key      # 键
        self.payload = val  # 值   有效载荷
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        """左子节点 :有父节点且父节点的左子是自己"""
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        """替换节点值"""
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        """
        在寻找 Successor 时，有3种情况需要考虑：
        1 如果节点有右子节点，则后继节点是右子树中的最小的键。
        2 如果节点没有右子节点并且是父节点的左子节点，则父节点是后继节点。
        3 如果节点是其父节点的右子节点，并且它本身没有右子节点，
          则此节点的后继节点是其父节点的后继节点，不包括此节点。
        return:: tree node
        """
        succ = None
        # todo 有两个孩子为啥还判断有右孩子
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def spliceOut(self):
        """拼接
        1 Successor无子节点
        2 Successor有一个子节点,因为Successor是左(右)子树中最小的,最多可能有一个节点
        """
        # 1 Successor is leaf
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        # 2 Successor hasAnyChildren
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findMin(self):
        """任何二叉搜索树中的最小值键是树的最左子节点  return node"""
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def __iter__(self):
        """The standard inorder traversal of a binary tree."""
        # 按中序遍历树中的所有键
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
                    
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put(50, 'a')
    bst.put(10, 'b')
    bst.put(70, 'c')
    bst.put(30, 'd')
    bst.put(85, 'd')
    bst.put(15, 'e')
    bst.put(45, 'f')
    bst.inorder()
    print("-----")
    bst.delete(30)
    bst.inorder()
