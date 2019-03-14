def insertionSort(alist):
    #
    # 遍历 1-(n-1)
    global count
    for index in range(1, len(alist)):
        # 假设index=5,前5个已经正确排序，第6个即alist[5] 插入排好的子序列中
        currentvalue = alist[index]  # 关键 将alist[index]赋值给一个变量
        position = index             # 小tricky   position currenrvalue 【】

        # 前5个倒着分别与第6个比较，如果大的话放到最后
        # position-1
        while position > 0 and alist[position - 1] > currentvalue:
        # while position > 0 and alist[position - 1] > alist[index]:  是错的   alist[index]已经修改了 
        # [54, 54, 93, 93, 93, 93, 93, 93, 93]  会出现这种情况
            alist[position] = alist[position - 1]
            count += 1
            position = position - 1

        # 走过while: 如果前5个中某一个小于第6个 将第6个放在"某一个"所在的位置
        # 没走过while: 当前值不变
        alist[position] = currentvalue

count = 0
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)
print(count)  # 20
