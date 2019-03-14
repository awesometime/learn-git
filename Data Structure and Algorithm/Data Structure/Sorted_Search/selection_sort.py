# 1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、非稳定排序  4、原地排序
# Python program for implementation of Selection Sort
# https://www.geeksforgeeks.org/selection-sort/

# 一次 loop 后最小的到最左边
def selection_sort(li):
    # Traverse through all array elements 
    for i in range(len(li)):

        # Find the minimum element in remaining 
        # unsorted array 
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        li[i], li[min_idx] = li[min_idx], li[i]   # 注意缩进 一定要放在第二层循环外边
        #print(li)
        # temp = li[i]
        # li[i] = li[min_idx]
        # li[min_idx] = temp

    return li


print(selection_sort([7, 6, 58, 3, 2, 9, 10]))

[2, 6, 58, 3, 7, 9, 10]
[2, 3, 58, 6, 7, 9, 10]
[2, 3, 6, 58, 7, 9, 10]
[2, 3, 6, 7, 58, 9, 10]
[2, 3, 6, 7, 9, 58, 10]
[2, 3, 6, 7, 9, 10, 58]
[2, 3, 6, 7, 9, 10, 58]

[2, 3, 6, 7, 9, 10, 58]

# 2
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
