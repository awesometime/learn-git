"""
归并排序:  https://www.geeksforgeeks.org/divide-and-conquer/
如果列表有多个项，我们分割列表，并递归调用两个半部分的合并排序。
一旦对这两半排序完成，就执行称为合并的基本操作。
合并是获取两个较小的排序列表并将它们组合成单个排序的新列表的过程。
"""


class Merge():
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


if __name__ == "__main__":
    # 第一种
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    m = Merge()
    m.mergeSort(alist)
    print(alist)

    # 第二种
    alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    rst = m.merge_sort_bizhan(alist2)
    print(alist2)
    print(rst)
