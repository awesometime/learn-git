# https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%9C%A8O%281%29%E6%97%B6%E9%97%B4%E5%86%85%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%BB%93%E7%82%B9.py

'''
https://download.csdn.net/blog/column/11081219/131031237
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None

class Solution:
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None

        if pToBeDeleted.next != None:
            # 如果pToBeDeleted 不是尾节点，
            # 那么可以直接将下一个节点的值value赋给该节点，
            # 然后令该节点指向下下个节点，再删除下一个节点，时间复杂度为O(1)。
            # 如图./Doc/img_0.png
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val
            pToBeDeleted.next = pNext.next
            pNext.__del__()
        elif pListHead == pToBeDeleted:
            # 只有一个节点
            pToBeDeleted.__del__()
            pListHead.__del__()
        else:
            # 如果pToBeDeleted 是尾节点
            # 需要先遍历链表，找到节点的前一个节点，然后让前一个节点指向 null，
            # 时间复杂度为O(N)
            # 如图img_1.png
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()
S.DeleteNode(node1, node3)
print(node3.val)
S.DeleteNode(node1, node3)
print(node3.val)
print(node2.val)
S.DeleteNode(node1, node1)
print(node1.val)
S.DeleteNode(node1, node1)
print(node1.val)