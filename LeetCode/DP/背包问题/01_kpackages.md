0/1背包
https://www.cnblogs.com/Christal-R/p/Dynamic_programming.html

https://mp.weixin.qq.com/s/2_KVD2Uk0Wzu2DTZWu04Dw

完全背包
https://mp.weixin.qq.com/s/XEa5RUm4l5S9ZXVlAxd7CA

多重背包
https://mp.weixin.qq.com/s/GXXO4orhy2yt0Diws3gAgA

混合背包
https://mp.weixin.qq.com/s/wtN3tSZXYaviLQukT2Bb6w

背包问题 https://blog.csdn.net/huanghaocs/article/details/77920358

一个背包总容量为V, 现在有N个物品, 第i个物品容量为weight[i], 价值为value[i], 现在往背包里面装东西, 怎样装才能使背包内物品总价值最大.主要分为3类：

0-1背包, 每个物品只能取0个,或者1个.

完全背包, 每个物品可以取无限次.

多重背包, 每种物品都有个数限制, 第i个物品最多可以为num[i]个

### 0/1背包
```py3
# https://www.cnblogs.com/Christal-R/p/Dynamic_programming.html
import pprint as p

"""
注意
1 可以优化成一维,此时需要倒着遍历,这样就可以用上前一轮的结果,不然就覆盖了
2 优化成一维后遍历要倒序
3 注意weigh及value的 补一位0 及dp补一行一列
"""


def ZeroOnePack(N, V, weight, value):
    """
    0-1 背包问题(每个物品只能取0次, 或者1次)
    :param N: 物品个数, 如 N=5
    :param V: 背包总容量, 如V=15
    :param weight: 每个物品的容量数组表示, 如weight=[5,4,7,2,6]
    :param value: 每个物品的价值数组表示, 如value=[12,3,10,3,6]
    :return:  返回最大的总价值
    """
    # 初始化dp[N+1][V+1]为0, dp[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    dp = [[0 for col in range(V + 1)] for row in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, V + 1):
            if j < weight[i]:  # 总容量j小于物品i的容量时，直接不考虑物品i
                dp[i][j] = dp[i - 1][j]
            else:  # 注意由于weight、value数组下标从0开始，第i个物品的容量为weight[i-1],价值为value[i-1]
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])  # 状态方程
    max_value = dp[N][V]
    return max_value, dp


def ZeroOnePack_advance(N, V, weight, value):
    """优化成一维 但是一维不能找物品路径了 """
    dp = [0 for col in range(V + 1)]
    for i in range(1, N + 1):
        for j in range(V, -1, -1):  # 必须倒序
            if j >= weight[i]:  # 总容量j小于物品i的容量时，直接不考虑物品i
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])  # 状态方程
        print(dp)
    max_value = dp[-1]
    return max_value, dp


def find_path(i, j, weight, value, dp):
    """根据最优解回溯找出解由哪些商品组成"""
    if i >= 0:
        if dp[i][j] == dp[i - 1][j]:  # 相等说明没装i
            select[i] = 0  # 全局变量，标记未被选中
            find_path(i - 1, j, weight, value, dp)
        elif (j - weight[i]) >= 0 and dp[i][j] == dp[i - 1][j - weight[i]] + value[i]:
            select[i] = 1  # 标记已被选中
            find_path(i - 1, j - weight[i], weight, value, dp)  # 回到装包之前的位置


# N = 5
# V = 15
# weight = [5, 4, 7, 2, 6]
# value = [12, 3, 10, 3, 6]

N = 4
V = 8
weight = [2, 3, 4, 5]
value = [3, 4, 5, 6]

weight.insert(0, 0)
value.insert(0, 0)
max_res, dp = ZeroOnePack(N, V, weight, value)
# max_res, dp = ZeroOnePack_advance(N, V, weight, value)
print(max_res)

# 找出解由哪些商品组成
select = [0] * (N + 1)  # 全局变量
p.pprint(dp)
find_path(N, V, weight, value, dp)
print(select)
for i in range(N + 1):
    if select[i] == 1:
        print(i)
```
### 完全背包问题

```
伪代码为

for i 遍历物品
    for j 遍历体积 从小到大
        for k 遍历当前物品个数
            当k*体积<=背包容量的时候 说明我们的背包是可以放下这么多物品的
            dp[i][j]=max ( dp[i-1][j-k*wi]+k*vi  ,   dp[i-1[j])
            这个表达式的意思就是 要么选择K个这样的物品，要么不选，看看哪个是最优的解，然后更新即可

            当k*体积<背包容量的时候说明我们的背包是放不下这么多物品的
            直接就是dp[i][j]=dp[i-1][j]
```

完全背包表示每个物品可以取**无限次**，只要加起来总容量不超过V就可以。

同样可以用f[i][j]表示前i间物品恰放入一个容器为j的背包可以获得的最大价值。则其状态转移方程为：

`f[i][j] = max{f[i-1][j-k*weight[i]] + k*value[i]} ,其中(0 <= k <= j/weight[i])`

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
    weight.insert(0, 0)
    value.insert(0, 0)
    # 初始化f[N+1][V+1]为0，f[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    f = [[0 for col in range(V + 1)] for row in range(N + 1)]

    for i in range(1, N+1):
        for j in range(1, V+1):
            # 注意由于weight、value数组已经补0，第i个物品的容量为weight[i],价值为value[i]
            # j/weight[i]表示容量为j时，物品i最多可以取多少次
            f[i][j] = f[i - 1][j]  # 初始取k=0为最大，下面的循环是把取了k个物品i能获得的最大价值赋值给f[i][j]
            for k in range(j/weight[i-1]+1):
                if f[i][j] < f[i-1][j-k*weight[i]]+k*value[i]:
                    f[i][j] = f[i-1][j-k*weight[i]]+k*value[i]  # 状态方程

            # 上面的f[i][j]也可以通过下面一行代码求得
            #  f[i][j] = max([f[i-1][j-k*weight[i]]+k*value[i] for k in range(j/weight[i]+1)])
    max_value = f[N][V]
    return max_value
```


### 多重背包问题

多重背包是`每个物品有不同的个数限制`，如第i个物品个数为num[i]。

同样可以用f[i][j]表示前i间物品恰放入一个容器为j的背包可以获得的最大价值，且每个物品数量不超多num[i]。则其状态转移方程为：

`f[i][j] = max{f[i-1][j-k*weight[i]] + k*value[i]} ,其中(0 <= k <= min{j/weight[i], num[i]})`


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
    weight.insert(0, 0)
    value.insert(0, 0)
    num.insert(0,0)
    
    # 初始化f[N+1][V+1]为0，f[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    f = [[0 for col in range(V + 1)] for row in range(N + 1)]
    for i in range(1, N+1):
        for j in range(1, V+1):
            # 对于物品i最多能取的次数是j/weight[i]与num[i]中较小者
            max_num_i = min(j/weight[i], num[i])

            f[i][j] = f[i - 1][j]  # 初始取k=0为最大，下面的循环是把取了k个物品i能获得的最大价值赋值给f[i][j]
            for k in range(max_num_i+1):
                if f[i][j] < f[i-1][j-k*weight[i]]+k*value[i]:
                    f[i][j] = f[i-1][j-k*weight[i]]+k*value[i]  # 状态方程

            # 上面的f[i][j]也可以通过下面一行代码求得
            # f[i][j] = max([f[i-1][j-k*weight[i]]+k*value[i] for k in range(max_num_i+1)])
    max_value = f[N][V]
    return max_value
```
