from pythonds.basic.deque import Deque


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


# print(palchecker("lsdkjfskf"))
# print(palchecker("radar"))


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

class OrderedList():
    def __init__(self):
        self.__head = None

    def add(self, item):
        temp = Node(item)
        current = self.__head
        while current.getNext().getData() != None:
            if current.getData() < item < current.getNext().getData():
                temp.setNext(self.head)
                self.head = temp
