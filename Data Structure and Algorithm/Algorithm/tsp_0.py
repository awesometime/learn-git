import pprint as p

CityNumber = 4
CostList = [[0, 2, 6, 5],
            [2, 0, 4, 4],
            [6, 4, 0, 2],
            [5, 4, 2, 0]]
print(CostList)

dp = [[float("inf") for col in range(1 << CityNumber - 1)] for row in range(CityNumber)]
print(dp)
print(type(dp))
for j in range(1 << CityNumber - 1):  # 4 个城市 2的3次 range(8)
    for i in range(CityNumber):  # range(4)
        # 类似dp[1]{1,2,3} 的情形 从1出发经过{1,2,3}显然不合理，在dp表中应为inf
        if i == 0 and j == 0:
            continue
        # 类似dp[1]{1,2,3} 的情形 从1出发经过{1,2,3}显然不合理，在dp表中应为inf
        # dp[1]{1,2,3} dp[2]{2,3} dp[2]{1,2,3} dp[3]{1,2,3}
        # 发现对于一个i 若j的第i位为1 则应该跳过 dp为inf
        if i > 0:
            if (j >> (i - 1)) & 1 == 1:  # dp[i][j] j第i位为1,就continue
                continue
        if j == 0:
            dp[i][j] = CostList[i][0]
            p.pprint('dp[{}][{}]   '.format(i, j) + str(dp[i][j]))

        # dp[2][5] = dp[2]{1,3} = dp{101} 从2出发经过1,3回到0. 有两条路 不需要经过2 也就是{101}第2位是0
        # 这个通过(j >> (k - 1)) & 1 == 0就跳过 也就是不走CostList[2][2] + dp[2][?]实际也没有这条路
        # dp[2][5] = CostList[2][1] + dp[1]{3} = CostList[2][1] + dp[1][4]
        #          = CostList[2][3] + dp[3]{1} = CostList[2][3] + dp[3][1]
        # 最后两条路选花费少的
        else:
            for k in range(1, CityNumber):
                if (j >> (k - 1)) & 1 == 0:  # j的第k位为0
                    continue
                # dp[i][j] 初始化为无穷大
                if CostList[i][k] + dp[k][j ^ (1 << (k - 1))] < dp[i][j]:
                    dp[i][j] = CostList[i][k] + dp[k][j ^ (1 << (k - 1))]
            p.pprint('dp[{}][{}]   '.format(i, j) + str(dp[i][j]))

p.pprint(dp[0][(1 << (CityNumber - 1)) - 1])
import math

# 将inf 换成-1
for j in range(1 << CityNumber - 1):
    for i in range(CityNumber):
        if math.isinf(dp[i][j]):
            dp[i][j] = -1

p.pprint(dp)

# 【1】  (j >> (i - 1)) & 1
# 对于数字x，要看它的第i位是不是1，那么可以通过判断布尔表达式 (((x >> (i - 1) ) & 1) == 1的真值
# (j >> (i - 1)) & 1  ==1 则j的第i位是1
# (j >> (i - 1)) & 1  ==0 则j的第i位是0

# 【2】  j ^ (1 << (k - 1))
# dp[i][j] = CostList[i][k] + dp[k][j ^ (1 << (k - 1))]

# dp[0][7] = dp[0]{1,2,3} = dp{111} 说明j的三位均不为0,   k=1,2,3都要取到
# dp[0][7] = CostList[0][1] + dp[1]{2,3} = CostList[0][1] + dp[1][6]   6({2,3}) 7(111) k=(1)  -->  111^1<<(k-1)=6
# dp[0][7] = CostList[0][2] + dp[1]{1,3} = CostList[0][2] + dp[2][5]   5({1,3}) 7(111) k=(2)  -->  111^1<<(k-1)=5
# dp[0][7] = CostList[0][3] + dp[1]{1,2} = CostList[0][3] + dp[3][3]   3({1,2}) 7(111) k=(3)  -->  111^1<<(k-1)=3


# CostDict[i][{1,2,3}] 表示从i出发经过{123}回到0 任何时候都是回到0
# CostDict[2][{1,3}] 表示从2出发经过{13}回到0 任何时候都是回到0

# j 是123组成的列表的所有子集 因此只能求从0出发经过{1,2,3}回到0
# 如果j 是[][0][2][3][02][03][23][023]就可以求从1出发经过{0,2,3}回到1

# 该程序没有考虑从a到b没路的情形

# dp[i][j] dp[3][j] j取 4 5 6 7
# dp[3]{3}    dp[3]{1,3}  dp[3]{2,3}  dp[3]{1,2,3}
# dp[3]{100}  dp[3]{101}  dp[3]{110}  dp[3]{111}
# dp[3][4]    dp[3][5]    dp[3][6]    dp[3][7]


# [[0, 2, 6, 5], [2, 0, 4, 4], [6, 4, 0, 2], [5, 4, 2, 0]]
# [[inf, inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf, inf]]
# <class 'list'>
# 'dp[1][0]   2'
# 'dp[2][0]   6'
# 'dp[3][0]   5'
# 'dp[0][1]   4'
# 'dp[2][1]   6'
# 'dp[3][1]   6'
# 'dp[0][2]   12'
# 'dp[1][2]   10'
# 'dp[3][2]   8'
# 'dp[0][3]   12'
# 'dp[3][3]   8'
# 'dp[0][4]   10'
# 'dp[1][4]   9'
# 'dp[2][4]   7'
# 'dp[0][5]   11'
# 'dp[2][5]   8'
# 'dp[0][6]   13'
# 'dp[1][6]   11'
# 'dp[0][7]   13'
# 13
# [[-1, 4, 12, 12, 10, 11, 13, 13],
#  [2, -1, 10, -1, 9, -1, 11, -1],
#  [6, 6, -1, -1, 7, 8, -1, -1],
#  [5, 6, 8, 8, -1, -1, -1, -1]]
