#归并 快排 堆排 快速实现练习
#https://blog.csdn.net/u010005281/article/details/80084994


#快速排序，O(nLogn)
def GetLeastNumbers_Solution(self, tinput, k):
    if len(tinput) < k:
        return []
    return self.quick_sort(tinput)[:k]

def quick_sort(self, list):
    if len(list) < 2:
        return list[:]
    left = (self.quick_sort([i for i in list[1:] if i <= list[0]]))
    right = (self.quick_sort([i for i in list[1:] if i > list[0]]))
    return left + [list[0]] + right

#归并排序，O(nLogn)
def GetLeastNumbers_Solution(self, tinput, k):
    if len(tinput) < k:
        return []
    return self.merge_sort(tinput)[:k]

def merge_sort(self, list):
    if len(list) < 2:
        return list[:]
    left = self.merge_sort(list[:len(list)//2])
    right = self.merge_sort(list[len(list)//2:])
    return self.merge(left,right)

def merge(self,left, right):
    res = []
    while left and right:
        res.append(left.pop(0)) if left[0] < right[0] else res.append(right.pop(0))
    res += left if not right else right
    return res
    
# 最大堆，O(nLogk)
def GetLeastNumbers_Solution(self, tinput, k):
    if len(tinput) < k:
        return []
    res = []
    for i in tinput:
        heapq.heappush(res, -i) if len(res) < k else heapq.heappushpop(res, -i)
    return sorted(list(map(lambda x: -x, res)))
