### 非递归

一个指向当前结点的指针，两个分别指向当前结点的前后结点的指针，防止断裂。

主要注意当头结点为空或者整个链表只有一个结点时，翻转后的链表断裂，

返回的翻转之后的头节点不是原来的尾节点。所以需要一个翻转后的头节点，

一个指向当前结点的指针，两个分别指向当前结点的前后结点的指针，防止断裂。

```python3
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pReversedHead = None
        pNode = pHead
        pPrev = None
        while pNode != None:
            pNext = pNode.next
            if pNext == None:
                pReversedHead = pNode
                
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead
```

### 使用递归

https://www.cnblogs.com/tianqizhi/p/9673894.html

```python3
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next=pHead
            pHead.next=None
            return newHead          
```    
