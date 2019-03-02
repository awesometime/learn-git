# 一次遍历后，最大的项在正确的地方

def bubbleSort(alist):
    # range(start, stop, step)
    co = 0
    for passnum in range(len(alist) - 1, 0, -1):
        #co +=1
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                co +=1
                # temp = alist[i]
                # alist[i] = alist[i+1]
                # alist[i+1] = temp
    return co

def shortBubbleSort(alist):
    """短冒泡排序"""
    exchanges = True
    passnum = len(alist) - 1
    co = 0
    while passnum > 0 and exchanges:
        co +=1
        # 如果发现列表已排序，可以修改冒泡排序提前停止
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