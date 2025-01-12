###
#二叉树的产生及递归遍历


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left  # 左子树
        self.right = right  # 右子树

root = TreeNode('D', TreeNode('B', TreeNode('A'), TreeNode('C')), TreeNode('E', right=TreeNode('G', TreeNode('F'))))
print(root.value)    #D
print(root.left.value)   #B
print(root.left.left.value)   #A
print(root.right)  # 地址
###

class Node:  
     def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left    #左子树
        self.right=right  #右子树


def preTraverse(root):
    '''
    前序遍历
    '''
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def midTraverse(root):
    '''
    中序遍历
    '''
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)

def afterTraverse(root):
    '''
    后序遍历
    '''
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)


if __name__=='__main__':
    # [原始二叉树图](https://www.cnblogs.com/freeman818/p/7252041.html)
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    print('前序遍历：')
    preTraverse(root)
    print('\n')
    print('中序遍历：')
    midTraverse(root)
    print('\n')
    print('后序遍历：')
    afterTraverse(root)
    print('\n')
    
"""
前序遍历：
D
B
A
C
E
G
F


中序遍历：
A
B
C
D
E
F
G


后序遍历：
A
C
B
F
G
E
D
"""
