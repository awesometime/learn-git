### 递归
```python3
def Merge(self, pHead1, pHead2):
    if not pHead1:
        return pHead2
    if not pHead2:
        return  pHead1
    if pHead1.val <= pHead2.val:
        pHead1.next = self.Merge(pHead1.next, pHead2)
        return pHead1
    else:
        pHead2.next = self.Merge(pHead1, pHead2.next)
        return pHead2

# 
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        
        pMergeHead = None
        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next,pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1,pHead2.next)
        return pMergeHead

```

### 非递归

```python3
class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None
 
def function(listNode1,listNode2):
    p = merge = ListNode(0)
    while listNode1 and listNode2:
        if listNode1.val > listNode2.val:
            merge.next = listNode2
            listNode2 = listNode2.next
        elif listNode2.val >= listNode1.val:
            merge.next = listNode1
            listNode1.next = listNode1
        merge.next = merge
    #注意：当由于其中一链表listNode1或者listNode2为null，导致跳出while循环时，
    #此时，还需要将另一不为null的链表的后续部分赋给合并链表。 
    merge = listNode1 or listNode2
    return p.next
```
