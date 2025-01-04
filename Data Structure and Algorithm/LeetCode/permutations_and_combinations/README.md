公式

https://www.cnblogs.com/1024th/p/10623541.html

https://blog.csdn.net/wusj3/article/details/82848946

## 排列 

https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/

https://leetcode-cn.com/problems/permutations/solution/

全排列 A(n,n)  有重复数字须加剪枝去重

所有排列   A(n,n) + A(n,n-1) + A(n,n-2) +...+ A(n,2) + A(n,1) + A(n,0)  有重复数字须加剪枝去重

```py3
def permuteUnique(nums):
    res = []
    nums.sort()                # sort排序
    dfs1(nums, [], res)
    return res


def dfs1(nums, path, res):                  # path 是当前排列  res 是全部结果
    if not nums:                # A(n,n)  不加这个if判断就是A(n,n) + A(n,n-1) + A(n,n-2) +...+ A(n,2) + A(n,1) + A(n,0)
        res.append(path)                   
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:        # i=0 是第一种,i > 0从第二个开始只要等于第一个就continue
            continue                                # 已经排序了 所以相同元素一定相邻
        dfs1(nums[:i] + nums[i + 1:], path + [nums[i]], res)  # nums[:i] + nums[i + 1:] == nums[i]的补集,保证nums中所有数字都取到

nums = [1,1,2,3]
print(permuteUnique(nums))
print(len(permuteUnique(nums)))

# 剪枝
# 1 1 2 3  A(n,n)                                                           12种
# 1 1 2 3  A(n,n) + A(n,n-1) + A(n,n-2) +...+ A(n,2) + A(n,1) + A(n,0)      35种

# 1 2 3 4  A(n,n)                                                           24种
# 1 2 3 4  A(n,n) + A(n,n-1) + A(n,n-2) +...+ A(n,2) + A(n,1) + A(n,0)      65种
```

## 组合

C(n,n) + C(n,n-1) + C(n,n-2) +...+ C(n,2) + C(n,1) + C(n,0) = 2^n

有重复数字要剪枝
```py3
def subsets(nums):
    res = []
    nums.sort()
    dfs(nums, 0, [], res)
    return res


def dfs(nums, index, path, res):
    res.append(path)                      # C(n,n) + C(n,n-1) + C(n,n-2) +...+ C(n,2) + C(n,1) + C(n,0) = 2^n
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i-1]:   # 我们的解法把剪枝条件加这里
            continue
        dfs(nums, i + 1, path + [nums[i]], res)
        
        
nums = [1,4,4,5,5]
print(subsets(nums))
```
