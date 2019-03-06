0/1 Knapsack Problem

[清晰的思路 geeksforgeeks ](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)

https://zxi.mytechroad.com/blog/sp/knapsack-problem/

```python3
# 二维数组

def knapsack01(w, v, W):
  dp = [[0] * (W + 1) for _ in range(N+1)]
  for i in range(1, N + 1):
    dp[i] = dp[i-1].clone()
    for j in range(w[i], W + 1):
      # 每次j时有两个选择 
      # 不选j  直接到j-1
      # 选j  j - w[i]
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
  return max(dp[N])
```  
  
  
```python3 
# 降维 节省空间

def knapsack01R(w, v, W):
dp = [0] * (W + 1)
for i in range(0, N):
  tmp = list(dp)
  for j in range(w[i], W + 1):
    tmp[j] = max(tmp[j], dp[j - w[i]] + v[i])
  dp = tmp
return max(dp)
```
