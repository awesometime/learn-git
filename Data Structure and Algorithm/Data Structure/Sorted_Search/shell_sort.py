# 时间复杂度：O(nlogn)  2、空间复杂度：O(1)  3、非稳定排序  4、原地排序
# todo 好处 

def shellSort(alist):
    # len(alist) 每次除2
    sublistcount = len(alist) // 2  # sublistcount分组数目
    # 直到最后sublistcount=1,即gap=1 变成插入排序,步长为1,最后全部排序完毕
    while sublistcount > 0:
        # 对sublistcount 组中的每组进行insert_sort
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    """ 通过插入排序 insert_sort 对每个子列表进行排序 """
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

"""
n//2<--- 2就是每组个数  ,组数=gap=4        # 3次移位,重点不在这儿
gapInsertionSort(alist[0],alist[4],alist[8])
......从alist[4]开始分别于alist[4]前边的去进行insert_sort
......从alist[8]开始分别于alist[4]、list[0]去进行insert_sort
gapInsertionSort(alist[1],alist[5])  
......从alist[5]开始分别于alist[5]前边的去进行insert_sort
gapInsertionSort(alist[2],alist[6])
gapInsertionSort(alist[3],alist[7])
After increments of size 4 The list is [20, 26, 44, 17, 54, 31, 93, 55, 77]
--------------------
n//4<--- 4就是每组个数  ,组数=gap=2        # 2次移位
gapInsertionSort(alist[0],alist[2],alist[4],alist[6],alist[8])
gapInsertionSort(alist[1],alist[3],alist[5],alist[7])
After increments of size 2 The list is [20, 17, 44, 26, 54, 31, 77, 55, 93]
--------------------
n//8   gap=1  此时就是gap==1的插入排序       # 5次移位
gapInsertionSort()
After increments of size 1 The list is [17, 20, 26, 31, 44, 54, 55, 77, 93]
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
