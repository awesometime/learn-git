"""
小明是名算法工程师， 同时也是名铲屎官。 某天，他突发奇想，想从猫咪的视频里挖据一些猫咪的运动信息。
为了提取运动信息，他需要从视频的每一帧提取“猫咪特征”。一个猫咪特征是一个两维的vectorc<x, y>。
如果x_1=x 2andy_1=y _2, 那么这俩是同一个特征。
因此，如果猫咪特征连续一致，可以认为猫咪在运动。也就是说，如果特征<a, b>在持续帧里出现，
那么它将构实特征运动。比如，特征<a b>在第2/3/4/7/8帧出现，那么该特征将形成两个特征运动2-3- 4和7-8。
现在，给定每一帧的特征， 特征的数量可能不一样。小明期望能找到最长的特征运动。

输入描述：
第一行包含一个正整数N，代表测试用例的个数。

每个测试用例的第一行包含一个正整数M， 代表视频的帧数。

接下来的M行，每行代表一帧。其中，第一个数字是该帧的特征个数，接下来的数字是在特征的取值:
比如样例输入第三行里，2代表该帧有两个猫咪特征，<1， 1>和<2, 2>

所有用例的输入特征总数和<100000
N满足1<=N<=100000. M满足1<=M<=10000.一帧的特征个数满足S<=10000。
特征取值均为非负整数。

输出描述：对每一个测试用例，输出特征运动的长度作为一行

输入：
# 1
# 8
# 2 1 1 2 2  # 2 个特征 <1,1>  <2,2>
# 2 1 1 1 4
# 2 1 1 2 2
# 2 2 2 1 4
# 0
# 0
# 1 1 1
# 1 1 1

输出：
# 3
"""
# 【本质求每种特征的最大连续出现次数】

from collections import defaultdict

# vectors = list(zip([1,2], [1,2]))
# print(vectors)  [(1, 1), (2, 2)]

all_p_vectors_1 = [[(1, 1), (2, 2)],
                   [(1, 1), (1, 4)],
                   [(1, 1), (2, 2)],
                   [(2, 2), (1, 4)],
                   [],
                   [],
                   [(1, 1)],
                   [(1, 1)]]

all_p_vectors_2 = [[(1, 1), (2, 2)],
                   [(1, 1), (1, 4)],
                   [(1, 1), (2, 2)],
                   [(2, 2), (1, 4)],
                   [],
                   [],
                   [(1, 1)],
                   [(1, 1)],
                   [(1, 1)],
                   [(1, 1)],
                   [(1, 1)]]
all_p_vectors = all_p_vectors_2
# all_p_vectors = all_p_vectors_2
n_frame = len(all_p_vectors)

# from collections import defaultdict 很舒服
# 否则如果字典没有key 执行赋值dict[key] = value 会报Keyerror
# defaultdict可以解决这个问题

# 截止当前行|每个vecter(x, y)连续出现过的最大次数 features_dict字典
features_dict = defaultdict(int)
# -----全局|每个vecter(x, y)连续出现过的最大次数 features_dict_max字典
features_dict_max = defaultdict(int)
# 比如本测试例子 all_p_vectors_1 截止第7行 (1,1)出现2次 但全局最大次数为3

# 添加第一帧
for i in all_p_vectors[0]:
    features_dict[i] = 1
    # features_dict_max[i] = 1  不初始化也行
# print(type(features_dict[(1,1)]))
# print(features_dict[(1,1)])
# print(features_dict)

# 添加除第一帧以外的帧
for i in range(1, n_frame):
    # 该帧为空 continue
    if all_p_vectors[i]:
        # 进入当前帧
        for vector in all_p_vectors[i]:
            # features_dict_max[vector] = features_dict[vector] error
            # 当前帧的vector在前一帧中也出现 则计数加 1
            if vector in all_p_vectors[i - 1]:
                features_dict[vector] += 1
            # 当前帧的vector在前一帧中没有出现, 置为 1
            else:
                features_dict[vector] = 1

            # 截止当前行|的某个vecter(x, y)连续出现过的最大次数
            # 比全局大的话更新全局中vector对应的次数
            if features_dict[vector] > features_dict_max[vector]:
                features_dict_max[vector] = features_dict[vector]


print(features_dict)
print(features_dict_max)
print(max(features_dict_max.items(), key=lambda x: x[1])[1])
print(max(features_dict_max.values()))

# 需要字典中数值最大的那个键的名字，使用max(dict, key=dict.get)函数非常的方便
# key_name = max(my_dict, key=my_dict.get)
print(features_dict_max[max(features_dict_max, key=features_dict_max.get)])
