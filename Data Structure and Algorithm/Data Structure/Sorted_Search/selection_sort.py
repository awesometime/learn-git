def selectionSort(alist):
    co = 0
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]
        co +=1
        # temp = alist[fillslot]
        # alist[fillslot] = alist[positionOfMax]
        # alist[positionOfMax] = temp
    return co

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(selectionSort(alist))
print(alist)