[0/1 Knapsack Problem](https://blog.csdn.net/mu399/article/details/7722810)

[清晰的思路 geeksforgeeks ](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)

https://zxi.mytechroad.com/blog/sp/knapsack-problem/

0-1背包问题的通常定义是：

一共有N件物品，第i件物品的重量为w[i]，价值为v[i]。在总重量不超过背包承载上限W的情况下，能够获得的最大价值是多少？每件物品可以使用0次或者1次。

决策：

为了背包中物品总价值最大化，第 i件物品应该放入背包中吗 ？

[![pic](https://github.com/awesometime/learn-git/blob/master/Data%20Structure%20and%20Algorithm/Data%20Structure/Dynamic_Programming/20190630201427.jpg)](https://github.com/awesometime/learn-git/blob/master/Data%20Structure%20and%20Algorithm/Data%20Structure/Dynamic_Programming/20190630201427.jpg)

f[i,j]表示在前i件物品中选择若干件放在承重为 j 的背包中，可以取得的最大价值。

Pi表示第i件物品的价值。

**01背包的状态转换方程 f[i,j] = Max{ f[i-1,j-Wi]+ Pi  (j >= Wi),  f[i-1,j] }**

为了体积V的背包中物体总价值最大化，件物品中第件应该放入背包中吗？

dp[i-1][j]  代表的就是不将这件物品放入背包的`总价值`，

dp[i-1][j-Vi] + Wi  则代表将第i件放入背包之后的`总价值`，

比较两者的价值，得出最大的价值存入现在的背包之中。
```python3
# 二维数组
# dp[i,j]表示在  前i件物品中  选择若干件 放在承重为j  的背包中，可以取得的最大价值。

# 遍历每件物品 遍历最大承重j  更新dp[i][j]
# 每次到i时有两个选择 
# 不选i  前i-1件物品    承重j         的前提下的最大价值
# 选i    前i-1件物品    承重j-w[i]    的前提下的最大价值
# 最终达到前i件 承重j 的最大价值

# 应该 遍历承重j的循环再外边    再遍历物品i比较好

def knapsack01(w, v, W):
    dp = [[0] * (W + 1) for _ in range(N+1)]     # 多加一行一列 便于遍历
    for i in range(1, N + 1):                    # 遍历每件物品
        dp[i] = dp[i-1].clone()
        for j in range(w[i], W + 1):             # j 是背包能承受的最大重量 
            dp[i][j] = max(dp[i-1][j],  dp[i-1][j-w[i]]  + v[i])
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
