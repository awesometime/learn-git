"""
第四题：
题目描述:  https://blog.csdn.net/skj1995/article/details/89303470 
小明目前在做一份毕业旅行的规划。打算从北京出发，分别去若干个城市，然后再回到北京，每个城市之间均乘坐高铁，且每个城市只去一次。
由于经费有限，希望能够通过合理的路线安排尽可能的省些路上的花销。给定一组城市和每对城市之间的火车票的价钱，
找到每个城市只访问一次并返回起点的最小车费花销。

解题参考:
https://www.cnblogs.com/youmuchen/p/6879579.html

旅行商TSP 问题，是一个NP难问题，用动态规划解决
"""

import sys
import copy
import pprint as p


def subsets(nums):
    # 返回某个列表（集合）的所有子集
    res = [[]]
    for num in nums:
        for temp in res[:]:
            x = temp[:]
            x.append(num)
            res.append(x)
    # for num in sorted(nums):
    #     res += [item + [num] for item in res]
    return res


# 读入城市数量和城市之间的花费
# CityNumber = int(sys.stdin.readline().strip())
CityNumber = 4
CostList = [[0, 2, 6, 5],
            [2, 0, 4, 4],
            [6, 4, 0, 2],
            [5, 4, 2, 0]]
print(CostList)
# for i in range(CityNumber):
#     CostList.append(list(map(int, sys.stdin.readline().strip().split())))

# CostDict存储动态规划需要的表，表的每一行对应每一个城市0,1,2,...,CityNumber-1
CostDict = {}
CityNumber_subsets = subsets(list(range(1, CityNumber)))
print(CityNumber_subsets)
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
for j in CityNumber_subsets:  # 4 个城市 2的3次 range(8)
    for i in range(0, CityNumber):# range(4)
        if j == []:
            CostDict[(i, tuple(j))] = CostList[i][0]
            p.pprint('{}   '.format((i, tuple(j))) + str(CostDict[(i, tuple(j))]))
            print()
        else:
            CostDict_values = []
            for j_sub in j:
                j_temp = copy.deepcopy(j)
                j_temp.remove(j_sub)
                # print(CostList[i][j_sub], CostDict[(j_sub, tuple(j_temp))])
                CostDict_values.append(CostList[i][j_sub] + CostDict[(j_sub, tuple(j_temp))])

            # CostDict[(2, (1, 3))] = min((CostList[2][1] + CostDict[(1, (3, ))]),
            #                            (CostList[2][3] + CostDict[(3, (1, ))]))
            CostDict[(i, tuple(j))] = min(CostDict_values)
            p.pprint('{}   {}'.format((i, tuple(j)), str(CostDict[(i, tuple(j))])))
            print()


p.pprint(CostDict[(0, tuple(list(range(1, CityNumber))))])
#p.pprint(CostDict)

# 13

# 注意
# CostDict[i][{1,2,3}] 表示从i出发经过{123}回到0 任何时候都是回到0
# CostDict[2][{1,3}] 表示从2出发经过{13}回到0 任何时候都是回到0

# 改进
# j 是123组成的列表的所有子集 因此只能求从0出发经过{1,2,3}回到0
# 如果j 是[][0][2][3][02][03][23][023]就可以求从1出发经过{0,2,3}回到1

# 该程序没有考虑从a到b没路的情形    //不能到b城市，continue

# 该程序没处理类似(1, (1, 2, 3)) 的情形 从1出发经过{1,2,3}显然不合理，在CostDict表中应为-1
# 所以CostDict[i][j]表中其实好多数据都没价值
# 具体参考https://www.cnblogs.com/youmuchen/p/6879579.html中表格为-1的项都没用
# //如果已经到过j了，就continue

# 该程序没有用移位将 CostDict[i][{1,2,3}] 处理成CostDict[i][7]

