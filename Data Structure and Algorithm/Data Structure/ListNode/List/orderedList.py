class Node():
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList():
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head == None

    def size(self):
        current = self.__head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def travel(self):
        # 访问的当前节点
        current = self.__head
        print('[ ', end='')
        while current != None:
            print(current.getData(), end=' ')
            current = current.getNext()
        print(']')

    def add(self, item):
        """按值大小顺序插入"""
        current = self.__head
        previous = None
        stop = False
        # 找到current.getData() > item的那个
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        # 找到以后插入 previous temp current
        temp = Node(item)
        # 第一个
        if previous == None:
            temp.setNext(self.__head)
            self.__head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def search(self, item):
        """大于item还没找到就stop """
        current = self.__head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def remove(self, item):
        current = self.__head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())


# 13 23 33 43
ol = OrderedList()
print(ol.isEmpty())
ol.add("13")
ol.add("23")
ol.add("33")
ol.add("43")
print(ol.size())
ol.travel()
print(ol.search("43"))
ol.remove("23")
ol.travel()
# True
# 4
# [ 13 23 33 43 ]
# True
# [ 13 33 43 ]
