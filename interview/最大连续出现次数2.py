# 测试用例数量
n_sample = int(sys.stdin.readline().strip())

for i in range(n_sample):
    # 视频帧数
    n_frame = int(sys.stdin.readline().strip())
    # 所有帧的特征向量
    all_p_vectors = []
    for p in range(n_frame):
        # 特征数量和具体特征
        row_input = map(int, sys.stdin.readline().strip().split())
        # 特征数量
        n_vector = row_input[0]
        v_x = row_input[1:][::2]
        v_y = row_input[2:][::2]
        # 特征
        vectors = zip(v_x, v_y)
        all_p_vectors.append(vectors)
        # print vectors


    # 接下来需要找到最长的特征向量
    # 考虑bfs，从当前帧的某一个特征向量开始，判断下一帧是否有同样的特征向量

    # 从当前帧数开始置为1, 然后遍历后边的每一行只要出现v就加1 否则(没出现 断开不连续出现了)break
    # 这样的话下次再出现 重新从1开始计数 如果大于它曾经的max_count 则更新
    def get_max_cont_l(p, v):  # 当前帧数p 当前向量v
        cnt = 1    # 重新一轮开始 初始为1
        all_p = all_p_vectors[p + 1:]
        # 当前行之后的每行each_p
        for each_p in all_p:
            # 当前传入向量v 在each_p中
            if v in each_p:
                cnt += 1
            else:
                break
        return cnt


    p = 0
    max_l = 0

    # 遍历每行的每个向量
    for p in range(n_frame):
        # 每个vector 从当前行开始往后连续出现的最大次数
        # list_max_cnt_from_cur_frame = []
        for v in all_p_vectors[p]:
            cur_l = get_max_cont_l(p, v)
            # list_max_cnt_from_cur_frame.append(cur_l)
            if cur_l > max_l:
                max_l = cur_l
        # print(list_max_cnt_from_cur_frame)

    print(max_l)
    
    
    
# all_p_vectors_1 = [[(1, 1), (2, 2)],
#                    [(1, 1), (1, 4)],
#                    [(1, 1), (2, 2)],
#                    [(2, 2), (1, 4)],
#                    [],
#                    [],
#                    [(1, 1)],
#                    [(1, 1)]]
# 
# all_p_vectors_2 = [[(1, 1), (2, 2)],
#                    [(1, 1), (1, 4)],
#                    [(1, 1), (2, 2)],
#                    [(2, 2), (1, 4)],
#                    [],
#                    [],
#                    [(1, 1)],
#                    [(1, 1)],
#                    [(1, 1)],
#                    [(1, 1)],
#                    [(1, 1)]]
# output of all_p_vectors_2
# [3, 1]
# [2, 1]
# [1, 2]
# [1, 1]
# []
# []
# [5]
# [4]
# [3]
# [2]
# [1]
# 5
