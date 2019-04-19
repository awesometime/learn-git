```python3
Q:操作给定的二叉树，将其变换为源二叉树的镜像。

A: 【前序遍历】这棵树的每个节点，如果遍历到的节点有子节点，就交换它的子节点，当交换完所有非叶节点的左右子节点后，得到树的镜像。
【也就是需要自上root而下的改变成对称的】
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return
        if root.left == None and root.right == None:
            return root
        
        # 【前序遍历】
        ptemp = root.left
        root.left = root.right
        root.right = ptemp
        
        self.Mirror(root.left)
        self.Mirror(root.right)
```
