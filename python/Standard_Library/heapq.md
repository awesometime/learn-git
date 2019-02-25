[heapq — Heap queue algorithm 官方文档](https://docs.python.org/3.8/library/heapq.html)

[heapq 源码分析](https://www.codercto.com/a/49843.html)

### heapq 的使用
```python
#heapq 的使用
#创建堆有两个基本的方法： heappush() 和 heapify() ，取出堆顶元素用 heappop() 。

#heappush() 是用来向已有的堆中添加元素，一般从空列表开始构建：

import heapq

data = [97, 38, 27, 50, 76, 65, 49, 13]
heap = []

for n in data:
    heapq.heappush(heap, n)

print('pop:', heapq.heappop(heap)) # pop: 13
print(heap) # [27, 50, 38, 97, 76, 65, 49]


#如果数据已经在列表中，则使用 heapify() 进行重排：

import heapq

data = [97, 38, 27, 50, 76, 65, 49, 13]

heapq.heapify(data)

print('pop:', heapq.heappop(data)) # pop: 13
print(data) # [27, 38, 49, 50, 76, 65, 97]
```python

### 堆排序算法

堆排序需要解决三个问题：

> 如何由一个无序序列建立成一个堆？
> 如何在输出堆顶元素之后，调整剩余元素，使之成为一个新的堆？
> 新添加元素和，如何调整堆？


**注意**把目标元素放置列表最后，然后进行上浮。尽管它命名叫 down ,但这个过程是上浮的过程，这个命名也让我困惑，

后来我才知道它是因为元素的索引不断减小，所以命名 down 。下沉的过程它也就命名为 up 了

```python
# 1
# 新添加元素和，如何调整堆？上浮 索引down
# 首先将新元素放置列表的最后，然后新元素与其父节点比较，若比父节点小，与父节点交换；
# 重复过程直到比父节点大或到根节点。这个过程使得元素从底部不断上升，从下至上恢复堆的顺序，称为**上浮**

def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
    


def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
    
# 一样是通过 newitem 不断与父节点比较。不一样的是这里缺少了元素交换的过程，而是计算出新元素最后所在的位置 pos 并进行的赋值。
# 显然这是优化后的代码，减少了不断交换元素的冗余过程。
```

```python
# 2
# 输出堆顶元素的函数 heappop() :

def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt
# 通过 heap.pop() 获得列表中的最后一个元素，然后替换为堆顶 heap[0] = lastelt ，再进行下沉：

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # 左节点，默认替换左节点
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1  # 右节点
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos  # 当右节点比较小时，应交换的是右节点
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
# 这边的代码将准备要下沉的元素视为新元素 newitem ，将其当前的位置 pos 视为空位置，由其子节点中的小者进行取代，
# 反复如此，最后会在叶节点留出一个位置，这个位置放入 newitem ，再让新元素进行上浮。

```

```python
# 3
# 再来看看让无序数列重排成堆的 heapify() 函数：
# 如何由一个无序序列建立成一个堆？从无序序列的第 n/2 个元素 （即此无序序列对应的完全二叉树的最后一个非叶结点 ）起 ，
# 至第一个元素止，依次进行下沉，下沉时选择叶节点中较小的一个比较，调整排序

def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)
# 这部分就和理论上的一致，从最后一个非叶节点 (n // 2) 到根节点为止，进行下沉。
```
