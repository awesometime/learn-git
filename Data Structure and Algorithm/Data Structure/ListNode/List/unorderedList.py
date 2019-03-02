class Node:
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


class UnorderedList:
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head == None

    def travel(self):
        # 访问的当前节点
        current = self.__head
        print('[ ', end='')
        while current != None:
            print(current.getData(), end=' ')
            current = current.getNext()
        print(']')

    def add(self, item):
        """头插"""
        temp = Node(item)
        temp.setNext(self.__head)
        self.__head = temp

    def size(self):
        current = self.__head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
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


uol = UnorderedList()
print(uol.isEmpty())
uol.add("13")
uol.add("23")
uol.add("33")
uol.add("43")
print(uol.size())
uol.travel()
print(uol.search("43"))
uol.remove("23")
uol.travel()
# True
# 4
# [ 43 33 23 13 ]
# True
# [ 43 33 13 ]
