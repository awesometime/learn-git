TopK

先排序 再找

堆排显然最快


### 快排 必会
```python3
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k > len(tinput):
            return []
        tinput = self.quick_sort(tinput)
        return tinput[:k]
    
    def quick_sort(self,lst):
        if not lst:
            return []
        pivot = lst[0]
        left = self.quick_sort([x for x in lst[1: ] if x < pivot])
        right = self.quick_sort([x for x in lst[1: ] if x >= pivot])
        
        return left + [pivot] + right
```

### 堆排序
```python3
# https://www.nowcoder.com/questionTerminal/6a296eb82cf844ca8539b57c23e6e9bf

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def siftup(lst, temp, begin, end):
            if lst == []:
                return []
            i, j = begin, begin * 2 + 1
            while j < end:
                if j + 1 < end and lst[j + 1] > lst[j]:
                    j += 1
                elif temp > lst[j]:
                    break
                else:
                    lst[i] = lst[j]
                    i, j = j, 2 * j + 1
            lst[i] = temp
 
        def heap_sort(lst):
            if lst == []:
                return []
            end = len(lst)
            for i in range((end // 2) - 1, -1, -1):
                siftup(lst, lst[i], i, end)
            for i in range(end - 1, 0, -1):
                temp = lst[i]
                lst[i] = lst[0]
                siftup(lst, temp, 0, i)
            return lst
 
        if tinput == [] or k > len(tinput):
            return []
        tinput = heap_sort(tinput)
        return tinput[: k]
```

### 快速排序的 partition() 方法

https://blog.csdn.net/sty945/article/details/80300182
```python3
class Solution:
    """
    最小的 K 个数
    """
    def find_kth_smallest(self, nums, k):
        l, h = 0, len(nums) - 1
        while l < h:
            j = self.partition(nums, l, h)
            if j == k:
                break
            if j > k:
                h = j - 1
            else:
                l = j + 1
        return nums[k]

    def partition(self, nums, low, high):
        parti = nums[low]
        while low < high:
            while low < high and nums[high] >= parti:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= parti:
                low += 1
            nums[high] = nums[low]
        nums[low] = parti
        return low

    def GetLeastNumbers_Solution(self, tinput, k):
        res = []
        if k > len(tinput) or k <= 0:
            return res
        kth_smallest = self.find_kth_smallest(tinput, k - 1)
        print(tinput)
        for i in range(k):
            res.append(tinput[i])
        return sorted(res)

# a = Solution()
# print(a.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4))
```

### 其他排序
```
方法一：蒂姆排序

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == [] or k > len(tinput):
            return []
        tinput.sort()
        return tinput[: k]
方法二：快速排序

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def quick_sort(lst):
            if not lst:
                return []
            pivot = lst[0]
            left = quick_sort([x for x in lst[1: ] if x < pivot])
            right = quick_sort([x for x in lst[1: ] if x >= pivot])
            return left + [pivot] + right
 
        if tinput == [] or k > len(tinput):
            return []
        tinput = quick_sort(tinput)
        return tinput[: k]
		
方法三：归并排序

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def merge_sort(lst):
            if len(lst) <= 1:
                return lst
            mid = len(lst) // 2
            left = merge_sort(lst[: mid])
            right = merge_sort(lst[mid:])
            return merge(left, right)
        def merge(left, right):
            l, r, res = 0, 0, []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            res += left[l:]
            res += right[r:]
            return res
        if tinput == [] or k > len(tinput):
            return []
        tinput = merge_sort(tinput)
        return tinput[: k]

方法4：冒泡排序

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def bubble_sort(lst):
            if lst == []:
                return []
            for i in range(len(lst)):
                for j in range(1, len(lst) - i):
                    if lst[j-1] > lst[j]:
                        lst[j-1], lst[j] = lst[j], lst[j-1]
            return lst
 
        if tinput == [] or k > len(tinput):
            return []
        tinput = bubble_sort(tinput)
        return tinput[: k]
		
方法5：直接选择排序

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def select_sort(lst):
            if lst == []:
                return []
            for i in range(len(lst)-1):
                smallest = i
                for j in range(i, len(lst)):
                    if lst[j] < lst[smallest]:
                        smallest = j
                lst[i], lst[smallest] = lst[smallest], lst[i]
 
            return lst
 
        if tinput == [] or k > len(tinput):
            return []
        tinput = select_sort(tinput)
        return tinput[: k]
		
方法6：插入排序

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def Insert_sort(lst):
            if lst == []:
                return []
            for i in range(1, len(lst)):
                temp = lst[i]
                j = i
                while j > 0 and temp < lst[j - 1]:
                    lst[j] = lst[j - 1]
                    j -= 1
                lst[j] = temp
            return lst
 
        if tinput == [] or k > len(tinput):
            return []
        tinput = Insert_sort(tinput)
        return tinput[: k]
```
