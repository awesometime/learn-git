7 斐波那契数列

不使用递归实现数列，需要把前面两个数字存入在一个数组中,实际一直在更新。

```py
class Solution:
    def Fibonacci(self, n):
        # write code here
        tempArray = [0,1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]
```
8 跳台阶

```py
class Solution:
    def jumpFloor(self, number):
        # write code here
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                tempArray[(i+1)%2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1)%2]
```

9 变态跳台阶

[变态跳台阶](https://blog.csdn.net/friendbkf/article/details/50060239)
```py
class Solution:
    def jumpFloorII(self, number):
        # write code here
        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2
        return ans
```
