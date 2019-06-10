"""
https://www.geeksforgeeks.org/quick-sort/

快速排序:单向扫描  https://blog.csdn.net/k_koris/article/details/80585979  单 两 三路
快速排序:双向扫描  本文

优化：

1 Pick a random element as pivot

2 快速排序:三路快排  https://www.jianshu.com/p/9eff99d403fb
    LeetCode75
  在使用有序或者近乎有序的数组测试时，算法的执行时间大大增加，经过分析发现：
  原来该算法O(nlogn)的复杂度会退化成为O(n^2)，这显然是和快排这个名称不想符的，
  于是笔者又经过分析与查阅资料了解到了所谓三路快排，该算法应用更加广泛，
  甚至Java将三路快排作为系统库中默认的排序算法


快速排序

我们从数组中选择一个元素，我们把这个元素称之为中轴元素吧，然后把数组中所有小于中轴元素的元素放在其左边，
所有大于或等于中轴元素的元素放在其右边，显然，此时中轴元素所处的位置的是有序的。
也就是说，我们无需再移动中轴元素的位置。

从中轴元素那里开始把大的数组切割成两个小的数组(两个数组都不包含中轴元素)，接着我们通过递归的方式，
让中轴元素左边的数组和右边的数组也重复同样的操作，直到数组的大小为1，此时每个元素都处于有序的位置。
"""

import random
import numpy as np


class Quick():
    def __init__(self):
        pass

    # 两路快排
    def quickSort(self, alist):
        self.quickSortHelper(alist, 0, len(alist) - 1)

    def quickSortHelper(self, alist, first, last):
        if first < last:
            splitpoint = self.two_partition(alist, first, last)
            print(splitpoint)

            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    def two_partition(self, alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:
            # 左指针 右移
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
            # 右指针 左移
            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            # 指针交叉 找到了分裂点
            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        # 找到分裂点应该处的正确索引rightmark后 将枢轴点 与rightmark 交换
        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

    # 两路快排 b站总结
    def quick_sort_bizhan(self, alist, first, last):
        if first >= last:
            return
        mid_value = alist[first]
        low = first
        high = last
        while low < high:
            # high 左移
            while low < high and alist[high] >= mid_value:
                high -= 1
            alist[low] = alist[high]

            # low 右移
            while low < high and alist[low] < mid_value:
                low += 1
            alist[high] = alist[low]

        # 循环退出时 low==high
        alist[low] = mid_value

        # 对low左边的列表执行快速排序
        self.quick_sort_bizhan(alist, first, low - 1)

        # 对low右边的列表执行快速排序
        self.quick_sort_bizhan(alist, low + 1, last)

    # 三路快排 https://www.jianshu.com/p/9eff99d403fb
    # 图片 https://upload-images.jianshu.io/upload_images/4703859-71526a975e5c443b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp
    def quick_sort_three_partition(self, arr, left, right):  # right=len(arr)-1
        """
        arr= [left][left+1...lt][lt+1...i...gt-1][gt...right]
                   [   <pivot  ][     =pivot    ][   >pivot ]
        lt初始化为left,  gt初始化为right+1,  i从left+1开始,  pivot=arr[left]或者随机一个
        """
        # 只有left < right 排序
        if left >= right:
            return
        # 在列表里随机选一个数来作为基准元素
        random_index = random.randint(left, right)
        # 把基准元素和第一个元素交换
        arr[left], arr[random_index] = arr[random_index], arr[left]

        pivot = arr[left]
        # 定义lt：小于v部分元素 的下标，初始是空的，因为arr[left]是基准元素
        lt = left  # arr[left+1...lt]  < v

        # gt 大于v 部分开始的下标，初始为空
        gt = right + 1  # arr[gt...right]   > v
        i = left + 1  # arr[lt+1...i]    == v
        # 终止条件：下标i 和gt 遇到一起，说明都排完了
        while i < gt:
            if arr[i] < pivot:
                arr[i], arr[lt + 1] = arr[lt + 1], arr[i]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt - 1] = arr[gt - 1], arr[i]
                gt -= 1
            else:
                i += 1
        # 最后把第一个元素 pivot = arr[left]（基准元素）放到等于v的部分
        arr[left], arr[lt] = arr[lt], arr[left]
        
        # 递归排序
        self.quick_sort_three_partition(arr, left, lt - 1)
        self.quick_sort_three_partition(arr, gt, right)

    # 三路快排 recursive
    def quick_sort_recursive(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[int(len(arr) / 2)]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort_recursive(left) + middle + self.quick_sort_recursive(right)


if __name__ == "__main__":
    # 第1种
    q = Quick()
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # alist = [26,20]
    # alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    q.quickSort(alist)
    print(alist)
    # [31, 26, 20, 17, 44, 54, 77, 55, 93]
    # 5
    # [17, 26, 20, 31, 44, 54, 77, 55, 93]
    # 3
    # [17, 26, 20, 31, 44, 54, 77, 55, 93]
    # 0
    # [17, 20, 26, 31, 44, 54, 77, 55, 93]
    # 2
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]
    # 7
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]

    # 第2种
    alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    q.quick_sort_bizhan(alist2, 0, len(alist2) - 1)
    print(alist2)

    # 第3种

    y = np.random.randint(0, 100, 30)
    print(y)
    q.quick_sort_three_partition(y, 0, len(y)-1)
    print(y)

    # 第4种
    alist4 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(q.quick_sort_recursive(alist4))

    x = np.random.randint(0, 100, 30)
    print(x)
    print(q.quick_sort_recursive(x))


# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [55 43 29 58 23 22  0  8 45 16 22 93 52 54 14 40 27 30  4  9 72 87 73 34
#  68 50 32 28 60 60]
# [ 0  4  8  9 14 16 22 22 23 27 28 29 30 32 34 40 43 45 50 52 54 55 58 60
#  60 68 72 73 87 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17 54 33  6 84 95 77 29 15 42 63 21 19 68 11 42 36 16  8 68 22 52 81 84
#   1 52 39  6 10 63]
# [1, 6, 6, 8, 10, 11, 15, 16, 17, 19, 21, 22, 29, 33, 36, 39, 42, 42, 52, 52, 54, 63, 63, 68, 68, 77, 81, 84, 84, 95]
    
