```python3

# 动态规划基础题

# 连续数组当前最大和记为A 
# 走到下一个B时：
#     如果当前最大和A正, 则A+B
#     如果当前最大和A负, 则A+B的和会比B还小, B重新开始, 寻找最大连续和

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        
        cur_sum = 0
        max_sum = array[0]
        
        for i in range(len(array)):
            if cur_sum <= 0:
                cur_sum = array[i]
            else:
                cur_sum += array[i]
                
            if cur_sum > max_sum:
                max_sum = cur_sum
                
        return max_sum
        

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return 0
         
        dp = [array[0]]
         
        i = 1
        for num in array[1:]:
            if dp[i - 1] <= 0:
                dp.append(num)
            else:
                dp.append(dp[i - 1] + num)
            i += 1
         
        return max(dp)       # max 一下
        

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n = len(array)
        dp = [ i for i in array]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+array[i],array[i])
         
        return max(dp)       # max 一下  
```
