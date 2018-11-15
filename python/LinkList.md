  * [1 python 实现单链表](#1-python-实现单链表)
  * [2 python 实现循环单链表](#2-python-实现循环单链表)
  * [3 python 实现双链表](#3-python-实现双链表)
  * [4 python实现linklist](#4-python实现linklist)
  * [5 leetcode题2](#5-leetcode题2)

### 1 python 实现单链表 

https://baagee.vip/index/article/id/100.html
```python
# 节点  属性  elem next
# 链表  属性  __head

class SingleNode(object):
    """节点"""

    def __init__(self, elem):
        # 标识数据域
        self.elem = elem
        # 标识链接域
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        # 私有属性头结点  是一个node
        self.__head = node

    # is_empty() 链表是否为空
    def is_empty(self):
        return self.__head == None

    # length() 链表长度
    def length(self):
        count = 0  # 数目
        # 当前节点
        current = self.__head
        while current != None:
            count += 1
            # 当前节点往后移
            current = current.next
        return count

    # travel() 遍历整个链表
    def travel(self):
        # 访问的当前节点
        current = self.__head
        print('[ ', end='')
        while current != None:
            print(current.elem, end=' ')
            current = current.next
        print(']')

    # add(item) 链表头部添加元素
    def add(self, item):
        node = SingleNode(item)           # 初始化node.elem= item /node.next = None
        # 新节点的下一个节点为旧链表的头结点
        node.next = self.__head           # 重写 node.next (替换None)
        
        # 新链表的头结点为新节点
        self.__head = node               # 通过node.elem/node.next 构造的 完整node 赋值给新链表的head

    # append(item) 链表尾部添加元素
    def append(self, item):
        node = SingleNode(item)
        if self.is_empty():
            # 为空链表时
            self.__head = node
        else:
            # 让指针指向最后节点
            current = self.__head
            while current.next != None:
                current = current.next
            #
            # 最后节点的下一个为新添加的node
            current.next = node

    # insert(index, item) 指定位置（从0开始）添加元素  （ 2,9）index=2 处插入9
    def insert(self, index, item):
        if index <= 0:
            # 在前方插入
            self.add(item)
        elif index > (self.length() - 1):
            # 在最后添加
            self.append(item)
        else:
            # 创建新节点
            node = SingleNode(item)
            # 遍历次数
            count = 0
            # 插入节点位置的上一个节点
            prev = self.__head
            # 查找到插入节点的上一个节点
            while count < (index - 1):
                count += 1
                prev = prev.next
            # 新节点的下一个节点为上一个节点的下一个节点
            node.next = prev.next  # 重写 node.next
            # 上一个节点的下一个节点为新的节点
            prev.next = node  # 构造完整的 node 后赋值给prev ，和上一句不能调换

    # 这块逻辑挺强 多看几遍
    # remove(item) 删除节点
    def remove(self, item):
        current = self.__head
        prev = None
        while current != None:
            if current.elem == item:
                # 找到要删除的节点元素
                # 最外层 if 才有return  ，最外层 else没有
                if not prev:
                    # 删除头结点 ，没有上一个元素
                    self.__head = current.next
                else:
                    # 删除其他结点，上一个节点的下一个节点指向当前节点的下一个节点
                    prev.next = current.next
                return  # 返回当前节点
            else:
                # 没找到，往后移
                prev = current
                current = current.next

    # search(item) 查找节点是否存在
    def search(self, item):
        # 当前节点
        current = self.__head
        while current != None:
            if current.elem == item:
                # 找到了
                return True
            else:
                current = current.next
        return False

    # 反转链表
    def reverse(self):
        # 方法1  返回列表  不太好
        # node = self.__head
        # list = []
        # while node:
        #     list.append(node.elem)
        #     node = node.next
        # list.reverse()   # list.reverse() 直接反转原列表 返回none
        # return list

        # 方法2  add 方法   返回singlelistnode对象
        current = self.__head
        list = []
        while current:
            list.append(current.elem)
            current = current.next
        # 原来single_link_list 置none
        self.__head = None
        for i in list:
            single_link_list.add(i)  # 头插直接相当于反转 = list.reverse()+append
        #print(single_link_list)

        # 方法3   先list.reverse()再append  返回singlelistnode对象
        # node = self.__head
        # list = []
        # while node:
        #     list.append(node.elem)
        #     node = node.next
        # 先反转
        # list.reverse()  # list.reverse() 直接反转原列表 返回none
        # self.__head = None
        # 再append
        # for i in list:
        #     single_link_list.append(i)


if __name__ == '__main__':
    print('test:')
    single_link_list = SingleLinkList()

    print('--------判断是否为空-------')
    print(single_link_list.is_empty())

    print('-----------长度------------')
    print(single_link_list.length())
    print('-----------append 遍历------------')
    single_link_list.append(2)
    single_link_list.append(3)
    single_link_list.append(5)
    single_link_list.travel()

    print('-----------反转 遍历------------')
    single_link_list.reverse()
    single_link_list.travel()
    # print(single_link_list.reverse())

    print('-----------add insert 遍历------------')
    single_link_list.add(1)
    single_link_list.add(0)
    single_link_list.insert(4, 4)
    single_link_list.insert(-1, -1)
    single_link_list.travel()

    print('-----------再次反转 遍历------------')
    single_link_list.reverse()
    single_link_list.travel()

    print('-----------查找------------')
    print(single_link_list.search(49))

    print('-----------删除  遍历------------')
    single_link_list.remove(-1)
    single_link_list.travel()

    print('-----------长度------------')
    print(single_link_list.length())

```
### 2 python 实现循环单链表
```python
class SingleNode(object):
    """节点"""

    def __init__(self, elem):
        # 标识数据域
        self.elem = elem
        # 标识链接域
        self.next = None

class SingleCircleLinkList(object):
    """单向循环链表"""

    def __init__(self, node=None):
        # 私有属性头结点
        self.__head = node
        if node:
            # 不是构造空的链表
            # 头结点的下一个节点指向头结点
            node.next = node

    # is_empty() 链表是否为空
    def is_empty(self):
        return self.__head == None

    # length() 链表长度
    def length(self):
        if self.is_empty():
            # 空链表
            return 0
        count = 1  # 数目
        # 当前节点
        current = self.__head
        # 当前节点的下一个节点不是头结点则继续增加
        while current.next != self.__head:
            count += 1
            # 当前节点往后移
            current = current.next
        return count

    # travel() 遍历整个链表
    def travel(self):
        # 访问的当前节点
        if self.is_empty():
            return False
        current = self.__head
        print('[ ', end='')
        while current.next != self.__head:
            print(current.elem, end=' ')
            current = current.next
        # 打印最后一个元素
        print(current.elem, end=' ')
        print(']')

    # add(item) 链表头部添加元素
    def add(self, item):
        node = SingleNode(item)
        if self.is_empty():
            # 空链表
            self.__head = node         # 第一个节点  既是头节点 也是最后节点的下一个节点  所以 有两个指向他的（2步骤）
            node.next = node
        else:
            # 非空链表添加
            current = self.__head
            # 查找最后一个节点
            while current.next != self.__head:
                current = current.next
            # 新节点的下一个节点为旧链表的头结点
            node.next = self.__head               # 重写node.next
            
            # 新链表的头结点为新节点  （2步骤）
            self.__head = node                   # 构造好node后赋值给self.__head
            # 最后节点的下一个节点指向新节点
            current.next = node                  # 构造好node同时赋值给最后一个的下一个

    # append(item) 链表尾部添加元素
    def append(self, item):
        node = SingleNode(item)
        if self.is_empty():
            # 为空节点时
            self.__head = node
            node.next = node
        else:
            # 让指针指向最后节点
            current = self.__head
            while current.next != self.__head:
                current = current.next
            # 最后节点的下一个为新添加的node
            current.next = node
            # 新节点下一个节点指向头结点
            node.next = self.__head

    # insert(index, item) 指定位置（从0开始）添加元素
    def insert(self, index, item):
        if index <= 0:
            # 在前方插入
            self.add(item)
        elif index > (self.length() - 1):
            # 在最后添加
            self.append(item)
        else:
            # 创建新节点
            node = SingleNode(item)
            # 遍历次数
            count = 0
            # 插入节点位置的上一个节点
            prev = self.__head
            # 查找到插入节点的上一个节点
            while count < (index - 1):
                count += 1
                prev = prev.next
            # 新节点的下一个节点为上一个节点的下一个节点
            node.next = prev.next
            # 上一个节点的下一个节点为新的节点
            prev.next = node

    # remove(item) 删除节点
    def remove(self, item):
        if self.is_empty():
            return False
        current = self.__head
        prev = None
        while current.next != self.__head:
            if current.elem == item:
                # 找到要删除的节点元素
                if current == self.__head:
                    # 删除结点,先找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 头结点指向当前节点的下一个节点
                    self.__head = current.next
                    # 尾节点的下一个节点指向头结点
                    rear.next = self.__head
                else:
                    # 中间节点，上一个节点的下一个节点指向当前节点的下一个节点
                    prev.next = current.next
                return  # 返回当前节点
            else:
                # 没找到，往后移
                prev = current
                current = current.next
        # 循环结束current指向尾节点
        if current.elem == item:
            if prev:
                # 如果删除最后一个节点
                prev.next = current.next
            else:
                # 删除只含有一个头结点的链表的头结点
                self.__head = None

    # search(item) 查找节点是否存在
    def search(self, item):
        # 当前节点
        if self.is_empty():
            # 空链表直接返回False
            return False
        current = self.__head
        while current.next != self.__head:
            if current.elem == item:
                # 找到了
                return True
            else:
                current = current.next
        # 判断最后一个元素
        if current.elem == item:
            return True
        return False


if __name__ == '__main__':
    print('test:')
    single_circle_link_list = SingleCircleLinkList()

    print('--------判断是否为空-------')
    print(single_circle_link_list.is_empty())

    print('-----------长度------------')
    print(single_circle_link_list.length())

    single_circle_link_list.append(2)
    single_circle_link_list.append(3)
    single_circle_link_list.append(5)
    #
    print('-----------遍历------------')
    single_circle_link_list.travel()
    #
    single_circle_link_list.add(1)
    single_circle_link_list.add(0)
    single_circle_link_list.insert(4, 4)
    single_circle_link_list.insert(-1, -1)
    #
    print('-----------遍历------------')
    single_circle_link_list.travel()
    #
    print('-----------查找------------')
    print(single_circle_link_list.search(4))
    #
    print('-----------删除------------')
    single_circle_link_list.remove(4)

    print('-----------遍历------------')
    single_circle_link_list.travel()

    print('-----------长度------------')
    print(single_circle_link_list.length())

    # print('-----------删除只含有一个头结点的链表------------')
    # single_circle_link_list.add(3)
    # single_circle_link_list.travel()
    # print(single_circle_link_list.remove(3))
```
### 3 python 实现双链表
```python
class DoubleNode(object):
    """节点"""

    def __init__(self, elem):
        # 标识数据域
        self.elem = elem
        # 标识前一个链接域
        self.prev = None
        # 标识后一个链接域
        self.next = None


class DoubleLinkList(object):
    """双链表"""

    def __init__(self, node=None):
        # 私有属性头结点
        self.__head = node

    # is_empty() 链表是否为空
    def is_empty(self):
        return self.__head == None

    # length() 链表长度
    def length(self):
        count = 0  # 数目
        # 当前节点
        current = self.__head
        while current != None:
            count += 1
            # 当前节点往后移
            current = current.next
        return count

    # travel() 遍历整个链表
    def travel(self):
        # 访问的当前节点
        current = self.__head
        print('[ ', end='')
        while current != None:
            print(current.elem, end=' ')
            current = current.next
        print(']')

    # add(item) 链表头部添加元素
    def add(self, item):
        node = DoubleNode(item)
        # 新节点的下一个节点为旧链表的头结点
        node.next = self.__head
        # 新链表的头结点为新节点
        self.__head = node
        # 下一个节点的上一个节点指向新增的节点
        node.next.prev = node

    # append(item) 链表尾部添加元素
    def append(self, item):
        node = DoubleNode(item)
        if self.is_empty():
            # 为空节点时
            self.__head = node
        else:
            # 让指针指向最后节点
            current = self.__head
            while current.next != None:
                current = current.next
            # 最后节点的下一个为新添加的node
            current.next = node
            # 新添加的结点上一个节点为当前节点
            node.prev = current

    # search(item) 查找节点是否存在
    def search(self, item):
        # 当前节点
        current = self.__head
        while current != None:
            if current.elem == item:
                # 找到了
                return True
            else:
                current = current.next
        return False

    # insert(index, item) 指定位置（从0开始）添加元素
    def insert(self, index, item):
        if index <= 0:
            # 在前方插入
            self.add(item)
        elif index > (self.length() - 1):
            # 在最后添加
            self.append(item)
        else:
            # 创建新节点
            node = DoubleNode(item)
            current = self.__head
            # 遍历次数
            count = 0
            # 查找到插入节点的上一个节点
            while count < index:
                count += 1
                current = current.next
            # 新节点的下一个节点指向当前节点
            node.next = current
            # 新节点的上一个节点指向当前节点的上一个节点
            node.prev = current.prev
            # 当前节点的上一个节点的下一个节点指向新节点
            current.prev.next = node
            # 当前节点的上一个节点指向新节点
            current.prev = node

    # remove(item) 删除节点
    def remove(self, item):
        current = self.__head
        while current != None:
            if current.elem == item:
                # 找到要删除的节点元素
                if current == self.__head:
                    # 头结点
                    self.__head = current.next
                    if current.next:
                        # 如果不是只剩下一个节点
                        current.next.prev = None
                else:
                    # 当前节点的上一个节点的下一个节点指向当前节点的下一个节点
                    current.prev.next = current.next
                    if current.next:
                        # 如果不是删除最后一个元素，当前节点的下一个节点的上一个节点指向当前节点的上一个节点
                        current.next.prev = current.prev
                return  # 返回当前节点
            else:
                # 没找到，往后移
                current = current.next


if __name__ == '__main__':
    print('test:')
    double_link_list = DoubleLinkList()

    print('--------判断是否为空-------')
    print(double_link_list.is_empty())

    print('-----------长度------------')
    print(double_link_list.length())

    double_link_list.append(2)
    double_link_list.append(3)
    double_link_list.append(5)

    print('-----------遍历------------')
    double_link_list.travel()

    double_link_list.add(1)
    print('-----------遍历------------')
    double_link_list.travel()
    double_link_list.add(0)
    print('-----------遍历------------')
    double_link_list.travel()
    double_link_list.insert(4, 4)
    print('-----------遍历------------')
    double_link_list.travel()
    double_link_list.insert(-1, -1)

    print('-----------遍历------------')
    double_link_list.travel()

    print('-----------查找------------')
    print(double_link_list.search(4))

    print('-----------删除------------')
    double_link_list.remove(5)
    double_link_list.remove(-1)

    print('-----------遍历------------')
    double_link_list.travel()

    print('-----------长度------------')
    print(double_link_list.length())

```
### 4 python实现linklist

[LISTNODE的PYTHON 实现](http://www.cnblogs.com/yuanmingzhou/p/9661152.html)

### 5 leetcode题2
```python
# -*- coding:utf-8 -*-
"""
【https://github.com/DinnerHowe/LeetCode/blob/master/2_Add_Two_Numbers.py】
Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.
This program is free software; you can redistribute it and/or modify
"""
import time

carray = False

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None

class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        #add a new node pointed to previous node
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print '\nnode: ', node, ' value: ', node.val, ' next: ', node.next
            node = node.next


    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result

    def get_list(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        return list

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        global carry
        carry = False
        result_handle = ListNode_handle()
        result = ListNode()
        while l1 != None or l2 != None:
            if not carry:
                if l1 != None and l2 != None:
                    l3_val = l1.val + l2.val
                elif l1 == None and l2 != None:
                    l3_val = l2.val
                elif l1 != None and l2 == None:
                    l3_val = l1.val
                else:
                    pass
            else:
                if l1 != None and l2 != None:
                    l3_val = l1.val + l2.val + 1
                elif l1 == None and l2 != None:
                    l3_val = l2.val + 1
                elif l1 != None and l2 == None:
                    l3_val = l1.val + 1
                else :
                    pass
                carry = False
            if l3_val < 10:
                result = result_handle.add(l3_val)
            else:
                result = result_handle.add(l3_val%10)
                carry = True
            try:
                l1 = l1.next
            except:
                pass
            try:
                l2 = l2.next
            except:
                pass
        result = result_handle._reverse(result)
        result_list = []
        result_list = result_handle.get_list(result)
        if carry:
            result_list.append(1)
            result = result_handle.add(1)
            result = result_handle._reverse(result)
        # result_handle.print_ListNode(result)
        return result_list

class ListNode1(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution1:
# @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode1(0)
        # print 'root: ', root.val, root.next
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode1(val)
            n = n.next
        return root

if __name__ == "__main__":
    # creat 2 linked lists
    ListNode_1 = ListNode_handle()
    l1 = ListNode()
    l1_list = [2,4,3]
    for i in l1_list:
        l1 = ListNode_1.add(i)

    ListNode_2 = ListNode_handle()
    l2 = ListNode()
    l2_list = [5,6,4]
    for i in l2_list:
        l2 = ListNode_2.add(i)
    #reverse 2 linked lists
    l1 = ListNode_1._reverse(l1)
    l2 = ListNode_2._reverse(l2)

    # ListNode_1.print_ListNode(l1)
    #get result
    now = time.time()
    result = Solution().addTwoNumbers(l1, l2)
    # print time.time()-now
    # print result

    now1 = time.time()
    result1 = Solution1().addTwoNumbers(l1, l2)
    result1_node = ListNode_handle()
    result1_node.print_ListNode(result1)
    # print time.time()-now1
    # print result1
```
