# stack 这种 迭代思想

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def has_next(self):
        return bool(self.stack)

    def next(self):
        node = self.stack.pop()
        tmp = node
        if tmp.right:
            tmp = tmp.right
            while tmp:
                self.stack.append(tmp)
                tmp = tmp.left
        return node.val
