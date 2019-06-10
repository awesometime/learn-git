# 自己总结  heapq 库
# heapq.heappush(res, -i)   
# heapq.heappushpop  
#【https://github.com/awesometime/learn-git/blob/c9edbb1ece42d3b2e4cae0ee44af0fc617933eb4/python/Standard_Library/heapq.md】

# https://www.geeksforgeeks.org/heap-sort/
# 
# 父节点的值大于子节点    大顶堆
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


# This code is contributed by Mohit Kumra






###########################################
# 版本2

# step1: Build_MAX_Heap 
#        从最后一个节点的父节点开始调整构建大顶堆 满足root大于子节点 不满足排序 子节点之间未排序而且不满足从小到大
# step2: HeapSort
#        root(max)和最后一个节点交换,root(max)到最后，调整除了最后一个节点的其余节点,具体是root比子节点小的话下沉
# 具体调整当然是用 MAX_Heapify


# 构造一个大顶堆 每次调整的过程
def MAX_Heapify(heap, HeapSize, root):  # 在堆中做结构调整使得父节点的值大于子节点

    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:  # 确定到底和左还是右节点换，先判断做节点
        larger = right
    if larger != root:                       # 如果做了堆调整：则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger], heap[root] = heap[root], heap[larger]
        MAX_Heapify(heap, HeapSize, larger)  # 从顶端递归往下调整，用larger是因为larger是数组索引，并且已经在比较时候更新过，而root没有更新过！


# 从最后一个根节点开始倒着循环构造一个大顶堆，这个堆只满足根比子节点大 并不满足 从上到下 从左到右依次排序
def Build_MAX_Heap(heap):  
    HeapSize = len(heap)
    for i in range((HeapSize - 1) // 2, -1, -1):         # 从后往前出数(z最后一个节点的父节点)  '//' got integer
        MAX_Heapify(heap, HeapSize, i)                   # 这里堆的大小是固定，root是i逐步减小


# 排序
def HeapSort(heap):               # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    # 1 构建大顶堆 这个堆只满足根比子节点大  【注意】这个堆并未排序
    Build_MAX_Heap(heap)     
    
    # 2 将堆顶元素(最大元素)放到堆尾,重新调整剩余节点，使其满足大顶堆
    #   这样循环完 最大元素从末尾开始依次放置好 就排序完成
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        MAX_Heapify(heap, i, 0)  
        # 这里堆的大小是逐步缩小，root永远是0
        # 因为堆顶最大值置换到最后不需要做调整, 只需从最顶端root向下调整其余节点即可
    return heap


arr3 = [12, 11, 13, 5, 6, 7]
print(HeapSort(arr3))
