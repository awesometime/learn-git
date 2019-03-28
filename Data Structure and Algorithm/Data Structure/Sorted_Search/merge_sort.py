"""
归并排序: recursive   https://www.geeksforgeeks.org/merge-sort/
         iterative   https://www.geeksforgeeks.org/iterative-merge-sort/

iterative  https://www.jianshu.com/p/3f27384387c1

如果列表有多个项，我们分割列表，并递归调用两个半部分的合并排序。
一旦对这两半排序完成，就执行称为合并的基本操作。
合并是获取两个较小的排序列表并将它们组合成单个排序的新列表的过程。
"""


class recursiveMergeSort():
    def __init__(self):
        pass

    def mergeSort(self, alist):
        """
        直接对原列表操作
        :param alist: alist
        :return: None 直接对原列表操作 不需要返回
        """
        #print("Splitting ", alist)
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            # 对原列表采用归并排序后形成的*有序*的列表
            self.mergeSort(lefthalf)

            # 对原列表采用归并排序后形成的*有序*的列表
            self.mergeSort(righthalf)

            # 合并
            # lefthalf = [17, 20, 26, 31]   righthalf = [44,54,55,77,93]
            # alist= [54,26,93,17,77,31,44,55,20]
            i = 0
            j = 0
            k = 0
            # 左边右边比较 将小的放在原来列表的前面, 小的这边的指针i(j)和k 同时右移加1
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1
                else:
                    alist[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            # 如果i这边最大的比j这边最大的的小,i(j) 会先走完, 此时j(i)还没走完
            # 将j中没走完的更新到原列表alist中 j 、k都右移加1
            # 注意：此时i已经超出了lefthalf 的index,while循环直接跳过,进入j的while循环
            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j = j + 1
                k = k + 1
        #print("Merging ", alist)

    # alist = [54,26,93,17,77,31,44,55,20]
    # mergeSort(alist)
    # print(alist)
    """
    Splitting  [54, 26, 93, 17, 77, 31, 44, 55, 20]
        Splitting  [54, 26, 93, 17]
            Splitting  [54, 26]
                Splitting  [54]
                Merging  [54]
                Splitting  [26]
                Merging  [26]
            Merging  [26, 54]
            Splitting  [93, 17]
                Splitting  [93]
                Merging  [93]
                Splitting  [17]
                Merging  [17]
            Merging  [17, 93]
        Merging  [17, 26, 54, 93]
        Splitting  [77, 31, 44, 55, 20]
            Splitting  [77, 31]
                Splitting  [77]
                Merging  [77]
                Splitting  [31]
                Merging  [31]
            Merging  [31, 77]
            Splitting  [44, 55, 20]
                Splitting  [44]
                Merging  [44]
                Splitting  [55, 20]
                    Splitting  [55]
                    Merging  [55]
                    Splitting  [20]
                    Merging  [20]
                Merging  [20, 55]
            Merging  [20, 44, 55]
        Merging  [20, 31, 44, 55, 77]
    Merging  [17, 20, 26, 31, 44, 54, 55, 77, 93]
    
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """

    def merge_sort_bizhan(self, alist):
        """
        操作新列表 原列表不变 需要返回
        :param alist:
        :return: 排序后的列表
        """
        n = len(alist)
        # 控制递归的条件
        if n <= 1:
            return alist
        mid = n // 2

        # left_list 采用归并排序后形成的*有序*的新的列表
        left_list = self.merge_sort_bizhan(alist[:mid])
        # right_list 采用归并排序后形成的*有序*的新的列表
        right_list = self.merge_sort_bizhan(alist[mid:])

        # 合并
        # 将两个有序子序列合并为一个新的整体
        left_pointer, right_pointer = 0, 0
        result = []

        while left_pointer < len(left_list) and right_pointer < len(right_list):
            if left_list[left_pointer] < right_list[right_pointer]:
                result.append(left_list[left_pointer])
                left_pointer += 1
            else:
                result.append(right_list[right_pointer])
                right_pointer += 1

        # 如果左边最大的比右边最大的的小,left_pointer会先走完, 此时right_pointer还没走完
        # 直接全部加到result中
        result += left_list[left_pointer:]
        result += right_list[right_pointer:]
        return result

class iterativeMergeSort():
    # Iterative Merge sort (Bottom Up)
    
    # Iterative mergesort function to
    # sort arr[0...n-1]
    def mergeSort(self ,a):
        current_size = 1
    
        # Outer loop for traversing Each
        # sub array of current_size
        while current_size < len(a) - 1:
            print('current_size -->' +str(current_size))
            print('l m r ')
            print('------')
            left = 0
            # Inner loop for merge call
            # in a sub array
            # Each complete Iteration sorts
            # the iterating sub array
            while left < len(a) - 1:
                # mid index = left index of
                # sub array + current sub
                # array size - 1
                mid = min(left + current_size - 1, len(a) - 1)
    
                # (False result,True result)
                # [Condition] Can use current_size
                # if 2 * current_size < len(a)-1
                # else len(a)-1
                # right = ((2 * current_size + left - 1, len(a) - 1)[2 * current_size + left - 1 > len(a) - 1])
                right = min(2 * current_size + left - 1, len(a) - 1)
                print(left, mid, right)
    
                # Merge call for each sub array
                self.merge(a, left, mid, right)
                left = left + current_size * 2
    
            # Increasing sub array size by
            # multiple of 2
            current_size = 2 * current_size
    
        # Merge Function
    
    
    def merge(self, a, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = a[l + i]
        for i in range(0, n2):
            R[i] = a[m + i + 1]
    
        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] > R[j]:
                a[k] = R[j]
                j += 1
            else:
                a[k] = L[i]
                i += 1
            k += 1
    
        while i < n1:
            a[k] = L[i]
            i += 1
            k += 1
    
        while j < n2:
            a[k] = R[j]
            j += 1
            k += 1

   

if __name__ == "__main__":
    # recursiveMergeSort
    # 第一种
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    r_m = recursiveMergeSort()
    r_m.mergeSort(alist)
    print(alist)

    # 第二种
    alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    rst = r_m.merge_sort_bizhan(alist2)
    print(alist2)
    print(rst)
    
    ########################
    # iterativeMergeSort
    a = [12, 11, 13, 4, 7, 8, 9, 1, 3, 2]
    print("Given array is ")
    print(a)
    i_m = iterativeMergeSort()
    i_m.mergeSort(a)

    print("Sorted array is ")
    print(a)

# Given array is 
# [12, 11, 13, 4, 7, 8, 9, 1, 3, 2]
# current_size -->1
# l m r 
# ------
# 0 0 1
# 2 2 3
# 4 4 5
# 6 6 7
# 8 8 9
# current_size -->2
# l m r 
# ------
# 0 1 3
# 4 5 7
# 8 9 9
# current_size -->4
# l m r 
# ------
# 0 3 7
# 8 9 9
# current_size -->8
# l m r 
# ------
# 0 7 9
# Sorted array is 
# [1, 2, 3, 4, 7, 8, 9, 11, 12, 13]
    
