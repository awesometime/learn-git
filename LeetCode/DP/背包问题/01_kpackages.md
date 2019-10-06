0/1背包
https://www.cnblogs.com/Christal-R/p/Dynamic_programming.html

https://mp.weixin.qq.com/s/2_KVD2Uk0Wzu2DTZWu04Dw

完全背包
https://mp.weixin.qq.com/s/XEa5RUm4l5S9ZXVlAxd7CA

多重背包
https://mp.weixin.qq.com/s/GXXO4orhy2yt0Diws3gAgA

混合背包
https://mp.weixin.qq.com/s/wtN3tSZXYaviLQukT2Bb6w


> 0/1背包
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
