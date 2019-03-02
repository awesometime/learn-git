# 节点  属性  elem next
# 链表  私有属性  __head

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
        node = SingleNode(item)  # 初始化node.elem= item /node.next = None
        # 新节点的下一个节点为旧链表的头结点
        node.next = self.__head  # 重写 node.next (替换None)
        # 新链表的头结点为新节点
        # 通过node.elem/node.next 构造的 完整node 赋值给新链表的head 不要和上一句调换
        self.__head = node

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
                return  # 返回
            else:
                # 没找到，往后移
                prev = current
                current = current.next

    def remove_another_method(self, item):
        current = self.__head
        prev = None
        found = False
        while not found:
            if current.elem == item:
                found = True
            else:
                prev = current
                current = current.next

        if prev == None:
            self.__head = current.next
        else:
            prev.next(current.next)

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

    # def reverse(self):
    #     head = self.__head
    #     prev = None
    #     while head:
    #         temp = head.next
    #         head.next = prev
    #         prev = head
    #         head = temp
    #     return prev

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
        # print(single_link_list)

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
