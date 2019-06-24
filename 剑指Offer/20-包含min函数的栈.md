[![pic](https://images2015.cnblogs.com/blog/381412/201509/381412-20150902002211263-1563001427.jpg)](https://images2015.cnblogs.com/blog/381412/201509/381412-20150902002211263-1563001427.jpg)


调用min、push及pop的时间复杂度都是O(1)。

```python3
class Solution:
    def __init__(self):
        self.stack = []       # 栈
        self.minStack = []    # 辅助栈  两栈长度一样
        
    def push(self, node):
        self.stack.append(node)
       
        # 辅助栈中 添加最小元素（之前的最小元素和新压入栈的元素两者的较小值）
        # 新压入栈的元素比较小
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        # 之前的最小元素 比较小
        else:
            temp = self.min()
            self.minStack.append(temp)
        
    # 同时 pop
    def pop(self):
        if self.stack == None or self.minStack == None:
            return None
        self.minStack.pop()
        self.stack.pop()
        
    def top(self):   # 貌似没用
        return self.stack[-1]
        
    def min(self):
        return self.minStack[-1]
```       
    
