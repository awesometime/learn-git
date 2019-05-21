# 时间复杂度：O(n2)  2、空间复杂度：O(1)  3、稳定排序  4、原地排序

# 一次遍历后，最大的项在正确的地方

def bubbleSort(alist):
    # range(start, stop, step)
    co = 0
    for passnum in range(len(alist) - 1, 0, -1):
        # co +=1   统计进行了几次大循环
        # print(passnum) 
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                co +=1    # 统计交换了几次
                # temp = alist[i]
                # alist[i] = alist[i+1]
                # alist[i+1] = temp
    return co


# 假如从开始的第一对到结尾的最后一对，相邻的元素之间都没有发生交换的操作，这意味着右边的元素总是大于等于左边的元素，
# 此时的数组已经是有序的了，我们无需再对剩余的元素重复比较下去了。
def shortBubbleSort(alist):
    """短冒泡排序"""
    exchanges = True
    passnum = len(alist) - 1
    co = 0
    while passnum > 0 and exchanges:                 #【tricky】exchange 标志
        # print(passnum)  统计进行了几次大循环
        co +=1
        # 第一次大循环完以后,列表已排序好，第二次进来以后没有发生交换,exchange=False,冒泡排序提前停止,后续不再循环
        # 而第一种bubbleSort会傻乎乎的循环len(alist) - 1次
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # temp = alist[i]
                # alist[i] = alist[i + 1]
                # alist[i + 1] = temp
        passnum = passnum - 1
    return co


def bubble_sort1(array):
    n = len(array)
    for i in range(n):  # i从0到n
        for j in range(1, n-i):  # 1开始，即j-1=0开始
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array


# 优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
# 用一个标记记录这个状态即可。
def bubble_sort2(ary):
    n = len(ary)
    for i in range(n):
        flag = 1                    #标记
        for j in range(1,n-i):
            if  ary[j-1] > ary[j] :
                ary[j-1],ary[j] = ary[j],ary[j-1]
                flag = 0
        if flag :                   #全排好序了，直接跳出
            break
    return ary


# 优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort3(ary):
    n = len(ary)
    k = n                           #k为循环的范围，初始值n
    for i in range(n):
        flag = 1
        for j in range(1,k):        #只遍历到最后交换的位置即可
            if  ary[j-1] > ary[j] :
                ary[j-1],ary[j] = ary[j],ary[j-1]
                k = j               #记录最后交换的位置
                flag = 0
        if flag :
            break
    return ary


if __name__ == "__main__":
    # alist1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # print(bubbleSort(alist1))
    # print(alist1)
    #
    # alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    # print(shortBubbleSort(alist1))
    # print(alist1)

    alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(bubbleSort(alist2))
    print(alist2)
    # print(shortBubbleSort(alist2))
    # print(alist2)
