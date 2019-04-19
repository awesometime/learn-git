# True
#                18              8
#              /    \           / \
#             8       7        9   2
#           /   \                   \
#          9     2                   7    
#               / \
#              4   7

# False
#               18             8
#              /  \           / \
#             8    7         9   2
#           /   \                 \
#          9     2                 7    

```python3
Q: 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

A: 在树A中查找和树B根节点一致的值，然后判断树A中以该节点为根节点的子树，是不是和树B有相同的结构。可以通过递归实现。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right,pRoot2)
        
        return result
        
    def DoesTree1haveTree2(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        
        return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)

```
