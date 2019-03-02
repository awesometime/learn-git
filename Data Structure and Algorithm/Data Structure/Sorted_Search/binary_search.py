"""
顺序查找:

二分查找:

"""

class Search():
    def __init__(self):
        pass

    def sequentialSearch(self, alist, item):
        pos = 0
        found = False

        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = True
            else:
                pos = pos + 1

        return found

    def orderedSequentialSearch(self, alist, item):
        pos = 0
        found = False
        stop = False
        while pos < len(alist) and not found and not stop:
            if alist[pos] == item:
                found = True
            else:
                if alist[pos] > item:
                    stop = True
                else:
                    pos = pos + 1

        return found

    def binarySearch(self, alist, item):
        first = 0
        last = len(alist) - 1
        found = False

        while first <= last and not found:
            midpoint = (first + last) // 2
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        return found


if __name__ == "__main__":
    s = Search()
    testlist1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(s.sequentialSearch(testlist1, 3))
    print(s.sequentialSearch(testlist1, 13))

    testlist2 = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(s.orderedSequentialSearch(testlist2, 3))
    print(s.orderedSequentialSearch(testlist2, 13))

    testlist3 = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(s.binarySearch(testlist3, 3))
    print(s.binarySearch(testlist3, 13))
