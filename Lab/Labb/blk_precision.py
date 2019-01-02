import pandas as pd
import re


class BlkPrecision():
    def __init__(self):
        pass

    def pattern_blk(self):
        """
        11197705 个pattern和blk合一起
        :return:
        """
        log_pattern_path = "F:/hw_data/200nodes/sorted_log_pattern.log"
        sorted_blk_path = "F:/hw_data/200nodes/sorted_blk.log"
        log_pattern_blk_path = "F:/hw_data/200nodes/sorted_pattern_blk_11197705.log"
        df1 = pd.read_csv(log_pattern_path, header=None)
        # print(df1)
        df2 = pd.read_csv(sorted_blk_path, header=None)
        rst = pd.concat([df1, df2], axis=1)
        rst.to_csv(log_pattern_blk_path, sep=' ', index=False, header=False)

    def drop_top_g(self):
        """
        get pat_label
        将 anamoly_bsg_10w.txt 中的 top-g 去掉 只留 pattern 和训练后的 label
        :return:
        """
        # todo 有时需要去掉首尾的一些无用的行
        path = "F:/hw_data/200nodes/anamoly_bsg_10w.txt"
        path2 = "F:/hw_data/200nodes/anamoly_bsg_10w_pro.txt"
        outf = open(path2, 'w')
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                rst1 = re.search("(\d+)(, {.*}, )(\d)", line).group(1)
                rst3 = re.search("(\d+)(, {.*}, )(\d)", line).group(3)
                li = str(rst1) + " " + str(rst3) + "\n"
                outf.write(li)
        outf.close()

    def get_pat_blk_labelaftr(self):
        """
        1 pattern_blk   1-29 和 blk   <-- pattern_blk()
        2 pattern_label               <-- drop_top_g()
        3 pattern_blk_label
        4 save to
        :return:
        """
        # 1 pat_blk_df   1-29 和 blk
        df1 = pd.read_csv('F:/hw_data/200nodes/sorted_pattern_blk_11197705.log', header=None, sep=' ',
                          names=['pattern', 'blk'])
        print(df1.shape)  # (11197705, 2)

        df2 = df1.iloc[100010:, :]
        print(df2.shape)  # (11097695, 2)

        df3 = df2[~(df2["pattern"].isin([30]) | df2["pattern"].isin([31]) | df2["pattern"].isin([32]) |
                    df2["pattern"].isin([33]) | df2["pattern"].isin([34]))]
        print(df3.shape)  # (11075641, 2)

        pat_blk_df = df3.reset_index(drop=True)  # .iloc[:match_num,:][ "abnormal"]
        # 去掉最后一行
        row = pat_blk_df.shape[0] - 1
        pat_blk_df = pat_blk_df.iloc[:row, :]
        print(pat_blk_df.shape)  # (11075640, 2)

        # 2 pat_labelaftr_df
        pat_labelaftr_df = pd.read_csv('F:/hw_data/200nodes/anamoly_bsg_10w_pro.txt', header=None, sep=' ',
                                       names=['pattern_n', 'label_after_train'])
        print(pat_labelaftr_df.shape)  # (11075640, 2)

        # 3 pat_blk_labelaftr
        pat_blk_labelaftr = pd.concat([pat_blk_df, pat_labelaftr_df], axis=1)
        # 去掉重复的pattern列
        pat_blk_labelaftr = pat_blk_labelaftr.drop(columns=['pattern_n'])
        print(pat_blk_labelaftr.shape)  # (11075640, 3)
        print(pat_blk_labelaftr.head())

        # 4 save to
        path3 = "F:/hw_data/200nodes/pat_blk_labelaftr.txt"
        pat_blk_labelaftr.to_csv(path3, sep=' ', index=False, header=False)

    # def precision():
    # 16900 blk==1 save to  list[blk...]
    # log   --> log_blk  -->label_test
    # 对每条log
    # if label_test == 1
    # re  get blk 对list[blk...]
    # tp_list =[]  fp_list =[]  fn_list=[]
    # if 匹配到 tp+1   tp_list =[blk.  ]
    # if 匹配不到 fp+1   fp_list =[blk.  ]
    # if label_test == 1  匹配tp_list =[blk.  ]   fp_list =[blk.  ]
    # 再匹配 fn_list=[]
    # for line in

    def pat_blk_labelaftr_1blk(self):
        """
        pat_blk_label 中 blk有两个相同的,去掉一个    <-- get_pat_blk_labelaftr()
        :return:
        """
        path = "F:/hw_data/200nodes/pat_blk_labelaftr.txt"
        path2 = "F:/hw_data/200nodes/pat_blk_labelaftr_1blk.txt"
        outf = open(path2, "w")
        with open(path, "r") as f:
            for line in f:
                rst1 = re.search("(\d+\s)(.*)(\s\d)", line).group(1)
                rst2 = re.findall("(blk_-\d+|blk_\d+)", line)[0]
                rst3 = re.search("(\d+\s)(.*)(\s\d)", line).group(3)
                new_line = rst1 + rst2 + rst3
                outf.write(new_line + "\n")
        outf.close()

    def precision(self):
        """
        1 test blk label dict
        2 raw  blk label dict
        3 calculate tp fp fn
        """
        """1 从处理后的pattern blk label 中取出训练完的blk label 保存到字典,并取blk==1
        """
        # pat_blk_labelaftr_1blk 只有一个blk
        blk_lab_dict_test = {}
        with open("F:/hw_data/200nodes/pat_blk_labelaftr_1blk.txt", "r") as f:
            for line in f:
                try:
                    blk = re.search("(\d+)\s(blk.*)\s(\d)", line).group(2)
                    label_int = int(re.search("(\d+)\s(blk.*)\s(\d)", line).group(3))
                    if blk not in blk_lab_dict_test.keys():
                        blk_lab_dict_test[blk] = label_int
                    else:
                        blk_lab_dict_test[blk] = blk_lab_dict_test[blk] or label_int
                except:
                    continue
        print(len(blk_lab_dict_test))  # 572533        574939

        # value 为0,1各自存成字典
        test_0_dict = {}
        test_1_dict = {}
        for k, v in blk_lab_dict_test.items():
            # v is int
            if v == 0:
                test_0_dict[k] = v
            else:
                test_1_dict[k] = v
        print(len(test_0_dict))  # 552904     104814
        print(len(test_1_dict))  # 19629      470125

        """2 将nameIndex mlabel 中blk==1的保存到字典
        """
        blk_list = []
        blk_path = "F:/hw_data/200nodes/nameIndex.txt"
        with open(blk_path, 'r') as f:
            for line in f:
                line = line.strip()
                blk_list.append(line)

        label_list = []
        label_path = "F:/hw_data/200nodes/mlabel.txt"
        with open(label_path, 'r') as f:
            for line in f:
                line = line.strip()
                res = re.search("(\d)(.*)", line).group(1)
                label_list.append(res)

        # 全部 575139 万 blk_
        # dict以后 key 会去重
        blk_label_dict_raw = dict(zip(blk_list, label_list))
        print(len(blk_label_dict_raw))  # 575060

        # 取label为1异常的(Abnormity)的blk_   {"blk_" :"1"}
        for key in list(blk_label_dict_raw.keys()):
            if blk_label_dict_raw[key] == "0":
                del blk_label_dict_raw[key]
        print(len(blk_label_dict_raw))  # 16837

        """2 匹配 得到tp fp fn
        """
        tp = 0
        for key in test_1_dict.keys():  # v is int and v=="1"
            # "blk_raw":1   "blk_tets":1  准确率tp
            # blk_label_dict_raw   v is str and v=="1"
            if key in blk_label_dict_raw.keys() and blk_label_dict_raw[key] == "1":
                tp += 1
        # "blk_raw":0   "blk_tets":1  误报fp
        fp = len(test_1_dict) - tp

        fn = 0
        for key in test_0_dict.keys():  # v is int and v=="0"
            # "blk_raw":1   "blk_tets":0  漏报fn
            # blk_label_dict_raw   v is str and v=="1"
            if key in blk_label_dict_raw.keys() and blk_label_dict_raw[key] == "1":
                fn += 1
        # "blk_raw":0   "blk_tets":0  剩余rem
        rem = len(test_0_dict) - fn

        print("tp  " + str(tp) + "  fp  " + str(fp) + "  fn  " + str(fn) + "  rem  " + str(rem))
        print("total  " + str(tp + fp + fn + rem))  #

        precision = round(tp / (tp + fp), 2)
        print("precision  " + str(precision))
        recall = round(tp / (tp + fn), 2)
        print("recall  " + str(recall))
        f_measure = 2 * precision * recall / (precision + recall)
        print("f_measure  " + str(f_measure))
    # 100w train
    # 572533
    # 552904
    # 19629
    # 575060
    # 16837
    # tp  12582  fp  7047  fn  2954  rem  549950
    # total  572533
    # precision  0.64
    # recall  0.81
    # f_measure  0.7150344827586207

    # 10w train
    # 574939
    # 104814
    # 470125
    # 575060
    # 16837
    # tp  13793  fp  456332  fn  2922  rem  101892
    # total  574939
    # precision  0.03
    # recall  0.83
    # f_measure  0.057906976744186045


if __name__ == "__main__":
    bp = BlkPrecision()
    bp.pattern_blk()  # pattern_blk
    bp.drop_top_g()  # pattern_label
    bp.get_pat_blk_labelaftr()  # pattern_blk_label
    bp.pat_blk_labelaftr_1blk()  # 处理pattern_blk_label 中blk只留一个
    bp.precision()  # test_blk_label 与57的原始raw_blk_label对比 计算tp fp fn
