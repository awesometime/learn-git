def shellSort(alist):
    # len(alist) 每次除2
    sublistcount = len(alist) // 2
    # 直到最后sublistcount=1,即gap=1 变成插入排序,步长为1,最后全部排序完毕
    while sublistcount > 0:

        for startposition in range(sublistcount):
            # n/2   gap=4
            # gapInsertionSort(alist[0],alist[4],alist[8])
            # gapInsertionSort(alist[1],alist[5])
            # gapInsertionSort(alist[2],alist[6])
            # gapInsertionSort(alist[3],alist[7])
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    """ 通过插入排序对每个子列表进行排序 """
    global count
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            count +=1
            position = position - gap

        alist[position] = currentvalue

count = 0
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)
print(count)  # 10

# n/2   gap=4   3次移位
# gapInsertionSort(alist[0],alist[4],alist[8])
# gapInsertionSort(alist[1],alist[5])
# gapInsertionSort(alist[2],alist[6])
# gapInsertionSort(alist[3],alist[7])
# After increments of size 4 The list is [20, 26, 44, 17, 54, 31, 93, 55, 77]

# n/4   gap=2    2次移位
# gapInsertionSort(alist[0],alist[2],alist[4],alist[6],alist[8])
# gapInsertionSort(alist[1],alist[3],alist[5],alist[7])
# After increments of size 2 The list is [20, 17, 44, 26, 54, 31, 77, 55, 93]

# n/8   gap=1  此时就是插入排序    5次移位
# gapInsertionSort()
# After increments of size 1 The list is [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]