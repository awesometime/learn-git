TODO  yield 遍历树

```python3
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

def generate_node(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            yield node
            queue.extend([x for x in (node.left, node.right) if x != None])
        # (node.left, node.right) is tuple


tree2list = [x.data for x in generate_node()]
print('the BinarySearchTree is %s' % tree2list)

```
