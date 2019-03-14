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
