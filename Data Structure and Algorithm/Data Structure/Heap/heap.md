### 传入列表alist去Build Heap并在列表发生变化时候重新建堆Build Heap

```python3
class Solution:
    def __init__(self):
        pass
        
    def MaxHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):   # 从最后一个节点的父节点开始循环
            k = i
            temp = alist[k]                        # 把初始的小数存到temp
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] < alist[index + 1]:
                        index += 1
                if temp >= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index                      # 关键步骤
                    # 大顶堆是小数往下沉,下沉一次可能仍然比子节点小，需要赋值继续下沉直到没有子节点也就是
                    # 不满足2*k<length-1为止
            alist[k] = temp                        # 循环完k是叶节点,也就是最下层处,自然是最小的数temp

    def MinHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] > alist[index + 1]:   #
                        index += 1
                if temp <= alist[index]:                  #
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
                    # 小顶堆是大数往下沉,下沉一次可能仍然比子节点小，需要赋值继续下沉直到没有子节点也就是
                    # 不满足2*k<length-1为止
            alist[k] = temp

```
堆排序
```python3
# https://www.geeksforgeeks.org/heap-sort/
# 
# 父节点的值大于子节点    大顶堆
#
# step1: 依次排好相当于建了一个堆 但是不满足root大于子节点的条件
# step2: 从最后一个节点的父节点开始调整堆 heapify()
# step3: root(max)和最后一个节点交换,最后一个节点到root处，并下沉调整堆 heapify()
#
#
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:  # 实际上(2*i+1)<n  i从(n-1)//2开始执行
        largest = l

    # See if right child of root exists and is
    # greater than root
    # root(i)与左孩子比较时可能largest变成了l,所以此处用arr[largest]
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    # largest != i相当于意思是根节点i与子节点largest发生了交换，根节点交换下沉以后
    # (仍然比子节点小)可能还需要继续交换下沉直到满足根节点大于子节点
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # after swap arr[i]此时是大的(根)

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # for i in range(n, -1, -1):  # i 从n倒回0 实际从(n-1)//2倒回0即可
    for i in range((n - 1) // 2, -1, -1):  # i 从n倒回0 实际从(n-1)//2倒回0即可 从最后一个节点的父节点开始
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):  # n个只需要交换n-1次
        arr[i], arr[0] = arr[0], arr[i]  # swap  最后一个位置arr[i]为堆顶的那个最大值
        # 交换以后arr[0]需要下沉
        heapify(arr, i, 0)

    # Driver code to test above


arr = [12, 11, 13, 5, 6, 7]
arr2 = [5, 6, 11, 12, 7, 13]
heapSort(arr2)
n = len(arr2)
print("Sorted array is")
for i in range(n):
    print("%d" % arr2[i]),
```

### Insert插入一个元素时直接将它插入末尾然后上浮到正确的位置 ; POP一个元素时直接将最后一个元素(较小的元素)放到堆顶,并下沉调整堆

```python3
class Solution:
    def __init__(self):
        self.minNums = []
        self.maxNums = []

    # 前面已经符合堆了,因为是按堆规则一步步建的堆
    # 接着插入一个新的 num 到最后,不断与其父节点比较, 比父节点大的话就交换到上一层, 终止条件 上浮直到 i<0
    def maxHeapInsert(self, num):
        self.maxNums.append(num)
        lens = len(self.maxNums)
        i = lens - 1
        while i > 0:                                # 终止条件
            if self.maxNums[i] > self.maxNums[(i - 1) // 2]:
                t = self.maxNums[(i - 1) // 2]
                self.maxNums[(i - 1) // 2] = self.maxNums[i]
                self.maxNums[i] = t
                i = (i - 1) // 2                    # 重置到上一层
            else:
                break
    
    # 将堆顶元素也就是最大元素 maxNums[0]存起来,最后返回
    # 将最后一个(小元素)放到堆顶,并下沉调整堆
    def maxHeapPop(self):
        t = self.maxNums[0]
        self.maxNums[0] = self.maxNums[-1]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2 * i + 1 < lens:                      # 自上而下下沉 所以终止条件 2 * i + 1 < lens
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.maxNums[nexti + 1] > self.maxNums[nexti]:
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                tmp = self.maxNums[i]
                self.maxNums[i] = self.maxNums[nexti]
                self.maxNums[nexti] = tmp
                i = nexti
            else:
                break
        return t                   # 注意返回堆顶元素

    def minHeapInsert(self, num):
        self.minNums.append(num)
        lens = len(self.minNums)
        i = lens - 1
        while i > 0:
            if self.minNums[i] < self.minNums[(i - 1) // 2]:
                t = self.minNums[(i - 1) // 2]
                self.minNums[(i - 1) // 2] = self.minNums[i]
                self.minNums[i] = t
                i = (i - 1) // 2
            else:
                break

    def minHeapPop(self):
        t = self.minNums[0]
        self.minNums[0] = self.minNums[-1]
        self.minNums.pop()
        lens = len(self.minNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.minNums[nexti + 1] < self.minNums[nexti]:
                nexti += 1
            if self.minNums[nexti] < self.minNums[i]:
                tmp = self.minNums[i]
                self.minNums[i] = self.minNums[nexti]
                self.minNums[nexti] = tmp
                i = nexti
            else:
                break
        return t


# 测试

t = Solution()
t.Insert(5)
print(t.GetMedian())
t.Insert(2)
print(t.GetMedian())
t.Insert(3)
print(t.GetMedian())
t.Insert(4)
print(t.GetMedian())
t.Insert(1)
print(t.GetMedian())
t.Insert(6)
print(t.GetMedian())
t.Insert(7)
print(t.GetMedian())
t.Insert(0)
print(t.GetMedian())
t.Insert(8)
print(t.GetMedian())
