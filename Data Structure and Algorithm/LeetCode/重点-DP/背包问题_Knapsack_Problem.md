[背包问题](https://blog.csdn.net/huanghaocs/article/details/77920358)

https://labuladong.online/algo/dynamic-programming/knapsack1/

```
一个背包总容量为V, 现在有N个物品, 第i个物品容量为weight[i], 价值为value[i], 
现在往背包里面装东西,怎样装才能使背包内物品总价值最大.主要分为3类：

1 状态 和 选择
状态有两个，就是「背包的容量V」和「可选择的物品」

2 dp 数组的定义
dp[i][j] 定义：对于前i个物品，当前背包的容量为j，情况下可以装的最大价值是 dp[i][j]。

3 根据「选择」，思考状态转移的逻辑
dp[i][j] = max(选第i件物品    dp[i-1,j-Wi] + vi  (j >= Wi),  
               不选第i件物品  dp[i-1,j]    )



0-1背包, 每个物品只能取0个,或者1个.  【两个for循环, 二维数组dp[i][j],可优化成一维数组】
f[i][j] = max{f[i-1][j-weight[i]] + value[i],    选第i件物品
              f[i-1][j]                          不选第i件物品
              }

完全背包, 每个物品可以取无限次.  【三个for循环, 二维数组dp[i][j]】
f[i][j] = max{f[i-1][j-k*weight[i]] + k*value[i] (其中0 <= k <= j/weight[i]),  选第i件物品
              f[i-1][j]                                                        不选第i件物品
             }

多重背包, 每种物品都有个数限制, 第i个物品最多可以为num[i]个.
【三个for循环, 二维数组dp[i][j]】
f[i][j] = max{f[i-1][j-k*weight[i]] + k*value[i]} (其中0 <= k <= min{j/weight[i], num[i]}),  选第i件物品
              f[i-1][j]                                                  不选第i件物品
              }
```


### 0-1背包

[0/1 Knapsack Problem](https://blog.csdn.net/mu399/article/details/7722810)

[清晰的思路 geeksforgeeks ](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)

https://zxi.mytechroad.com/blog/sp/knapsack-problem/

0-1背包问题的通常定义是：

一共有N件物品，第i件物品的重量为w[i]，价值为v[i]。在总重量不超过背包承载上限W的情况下，能够获得的最大价值是多少？每件物品可以使用0次或者1次。

决策：

为了背包中物品总价值最大化，第 i件物品应该放入背包中吗 ？

[![pic](https://github.com/awesometime/learn-git/blob/master/Data%20Structure%20and%20Algorithm/Data%20Structure/Dynamic_Programming/20190630201427.jpg)](https://github.com/awesometime/learn-git/blob/master/Data%20Structure%20and%20Algorithm/Data%20Structure/Dynamic_Programming/20190630201427.jpg)

dp[i,j]表示在前i件物品中选择若干件放在承重为 j 的背包中，可以取得的最大价值。

vi表示第i件物品的价值。

**01背包的状态转换方程 dp[i,j] = Max{选 dp[i-1,j-Wi] + vi  (j >= Wi),  不选 dp[i-1,j] }**

为了体积V的背包中物体总价值最大化，N件物品中第i件应该放入背包中吗？

注意由于weight、value数组下标从0开始，第i个物品的容量为weight[i-1],价值为value[i-1]

dp[i-1][j]          不选 代表不将第i件物品放入背包的`总价值`，

dp[i-1][j-Vi] + Wi  选   代表将第i件放入背包之后的`总价值`，

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

def knapsack01(w, v, N, W):
    dp = [[0] * (W + 1) for _ in range(N+1)]     # 多加一行一列 便于遍历
    for i in range(1, N + 1):                    # 遍历每件物品
        dp[i] = dp[i-1].clone()
        for j in range(w[i], W + 1):             # j 是背包能承受的最大重量
            # j 范围也可以(1,W+1)
            # 此处j 从w[i]开始,所以不需要判断 j是否大于w[i]
            dp[i][j] = max(dp[i-1][j],  dp[i-1][j-w[i]]  + v[i])
    return max(dp[N])
```  
  
  
```python3 
# 自己画一次dp[i][j]图  
# 不难理解 可以降维 
# 节省空间
# 但还是不降维版本 比较通用 适合刷题

def knapsack01R(w, v, N, W):
    dp = [0] * (W + 1)
    for i in range(0, N):
        tmp = list(dp)
        for j in range(w[i], W + 1):  # j 范围也可以(1,W+1)
            tmp[j] = max(tmp[j], dp[j - w[i]] + v[i])
        dp = tmp
    return max(dp)
```
### 完全背包

```py3
def CompletePack(N, V, weight, value):
    """
    完全背包问题(每个物品可以取无限次)
    :param N: 物品个数, 如 N=5
    :param V: 背包总容量, 如V=15
    :param weight: 每个物品的容量数组表示, 如weight=[5,4,7,2,6]
    :param value: 每个物品的价值数组表示, 如value=[12,3,10,3,6]
    :return: 返回最大的总价值
    """
    # 初始化f[N+1][V+1]为0，f[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    f = [[0 for col in range(V + 1)] for row in range(N + 1)]

    for i in range(1, N+1):
        for j in range(1, V+1):
            # 注意由于weight、value数组下标从0开始，第i个物品的容量为weight[i-1],价值为value[i-1]
            # j/weight[i-1]表示容量为j时，物品i最多可以取多少次
            
            # 继承 前i-1个物品的总价值，即f[i-1][j]
            f[i][j] = f[i - 1][j]  
            
            # 初始取k=0为最大，下面的循环是把取了k个物品i能获得的最大价值赋值给f[i][j]
            for k in range(j/weight[i-1]+1):
                if f[i][j] < f[i-1][j-k*weight[i-1]]+k*value[i-1]:
                    f[i][j] = f[i-1][j-k*weight[i-1]]+k*value[i-1]  # 状态方程

            # 上面的f[i][j]也可以通过下面一行代码求得
            #  f[i][j] = max([f[i-1][j-k*weight[i-1]]+k*value[i-1] for k in range(j/weight[i-1]+1)])
    max_value = f[N][V]
    return max_value
```

### 多重背包

```py3
def MultiplePack(N, V, weight, value, num):
    """
    多重背包问题(每个物品都有次数限制)
    :param N: 物品个数, 如 N=5
    :param V: 背包总容量, 如V=15
    :param weight: 每个物品的容量数组表示, 如weight=[5,4,7,2,6]
    :param value: 每个物品的价值数组表示, 如value=[12,3,10,3,6]
    :param num: 每个物品的个数限制，如num=[2,4,1,5,3]
    :return: 返回最大的总价值
    """

    # 初始化f[N+1][V+1]为0，f[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    f = [[0 for col in range(V + 1)] for row in range(N + 1)]
    for i in range(1, N+1):
        for j in range(1, V+1):
            # 对于物品i最多能取的次数是j/weight[i-1]与num[i-1]中较小者
            max_num_i = min(j/weight[i-1], num[i-1])

            f[i][j] = f[i - 1][j]  # 初始取k=0为最大，下面的循环是把取了k个物品i能获得的最大价值赋值给f[i][j]
            for k in range(max_num_i+1):
                if f[i][j] < f[i-1][j-k*weight[i-1]]+k*value[i-1]:
                    f[i][j] = f[i-1][j-k*weight[i-1]]+k*value[i-1]  # 状态方程

            # 上面的f[i][j]也可以通过下面一行代码求得
            # f[i][j] = max([f[i-1][j-k*weight[i-1]]+k*value[i-1] for k in range(max_num_i+1)])
    max_value = f[N][V]
    return max_value
```
