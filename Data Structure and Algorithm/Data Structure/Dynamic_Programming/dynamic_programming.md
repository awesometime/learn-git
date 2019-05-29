# 选
# 不选

### problem1 : 求一个数组中不相邻数字的最大和

求一个数组中不相邻数字的最大和  arr = [1, 2, 4, 1, 7, 8, 3]

> recursion method
```python3
def rec_opt(arr, i):
    # 递归出口 i == 0  i == 1
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    #
    else:
        return max(rec_opt(arr, i - 2) + arr[i], rec_opt(arr, i - 1))

print('---rec_opt')
for index in range(len(arr)):
    print(rec_opt(arr, index))
```
> Dynamic Programming method
```python3
import numpy as np


def dp_opt(arr):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], opt[1])
    for i in range(2, len(arr)):
        opt[i] = max(opt[i - 2] + arr[i], opt[i - 1])
    return opt[len(arr) - 1]


print('---dp_opt')
print(dp_opt(arr))
```

### problem2 : 返回数组中是否可以找到几个数使得 和为S

> recursion method
```python3
# 返回数组中是否可以找到几个数使得 和为S
def rec_subset(arr, i, s):
    # 从后往前遍历 边界好确定一些
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_subset(arr, i - 1, s)
    else:
        return rec_subset(arr, i - 1, s - arr[i]) or rec_subset(arr, i - 1, s)


arr2 = [3, 34, 4, 12, 5, 2]
print('---rec_subset')
print(rec_subset(arr2, len(arr2) - 1, 9))
```


> Dynamic Programming method
```python3
def dp_subset(arr, S):
    subset = np.zeros((len(arr), S + 1), dtype=bool)
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, S + 1):
            if arr[i] > s:
                subset[i, s] = subset[i - 1, s]
            else:
                subset[i, s] = subset[i - 1, s - arr[i]] or subset[i - 1, s]
    r, c = subset.shape
    return subset[r - 1, c - 1]

print('---dp_subset')
print(dp_subset(arr2, 9))
print(dp_subset(arr2, 13))
```
