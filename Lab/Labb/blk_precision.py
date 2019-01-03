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

    def pattern_label(self):
        """
        get pat_label
        将 anamoly_bsg_10w.txt 中的 top-g 去掉 只留 pattern 和训练后的 label
        :return:   anamoly_bsg_10w_pro.txt
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

    def pat_blk_label_test(self):
        """
        1 pattern_blk   1-29 和 blk   <-- pattern_blk()
        2 pattern_label               <-- pattern_label()
        3 pattern_blk_label
        4 save to
        :return:
        """
        # 1 pat_blk_df   1-29 和 blk
        df1 = pd.read_csv('F:/hw_data/200nodes/sorted_pattern_blk_11197705.log', header=None, sep=' ',
                          names=['pattern', 'blk'])
        print(df1.shape)  # (11197705, 2)

        df2 = df1.iloc[1000010:, :]
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
        pat_labelaftr_df = pd.read_csv('F:/hw_data/200nodes/anamoly_bsg_100w_pro.txt', header=None, sep=' ',
                                       names=['pattern_n', 'label_after_train'])
        print(pat_labelaftr_df.shape)  # (11075640, 2)

        # 3 pat_blk_labelaftr
        pat_blk_labelaftr = pd.concat([pat_blk_df, pat_labelaftr_df], axis=1)
        # 去掉重复的pattern列
        pat_blk_labelaftr = pat_blk_labelaftr.drop(columns=['pattern_n'])
        print(pat_blk_labelaftr.shape)  # (11075640, 3)
        print(pat_blk_labelaftr.head())

        # 4 save to
        path3 = "F:/hw_data/200nodes/pat_blk_label_test_100w.txt"
        pat_blk_labelaftr.to_csv(path3, sep=' ', index=False, header=False)

    def pat_blk_label_test_one_blk(self):
        """
        pat_blk_label 中 blk有两个相同的,去掉一个    <-- pat_blk_label_test()
        :return:
        """
        path = "F:/hw_data/200nodes/pat_blk_label_test_100w.txt"
        path2 = "F:/hw_data/200nodes/pat_blk_label_test_100w_oneblk.txt"
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
        0 找到前10w中出现过的blk
        1 test blk label dict
        2 raw  blk label dict
        3 calculate tp fp fn
        """
        """0 找到前10w中出现过的blk  tenw_list
        """
        from itertools import islice
        # todo save to a file
        tenw_list = []
        with open('F:/hw_data/200nodes/sorted_pattern_blk_11197705.log') as f:
            for a in islice(f, 0, 100000):
                a = a.strip()
                rst = re.findall("(blk_-\d+|blk_\d+)", a)[0]
                if rst not in tenw_list:
                    tenw_list.append(rst)
        # print(tenw_list)
        print(len(tenw_list))  # 100w-->66120     10w-->7938

        """1 将nameIndex mlabel 中blk==1的保存到字典
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

        # 全部 575139 万 blk_    dict以后 key 会去重
        blk_label_dict_raw = dict(zip(blk_list, label_list))
        print(len(blk_label_dict_raw))  # 575060

        # value 为0,1各自存成字典
        raw_0_dict = {}
        raw_1_dict = {}
        for k, v in blk_label_dict_raw.items():
            # v is str and v =="0"
            if v == "0":
                raw_0_dict[k] = v
            # v is str and v =="1"
            else:
                raw_1_dict[k] = v
        print(len(raw_0_dict))  # 558223
        print(len(raw_1_dict))  # 16837

        """2 从处理后的pattern blk label 中取出训练完的blk label 保存到字典,并取blk==1
        """
        # pat_blk_label_test_one_blk 只有一个blk
        blk_lab_dict_test = {}
        with open("F:/hw_data/200nodes/10w/pat_blk_label_test_10w_oneblk.txt", "r") as f:
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
        print(len(blk_lab_dict_test))  # 100w-->572533        10w-->574939

        # 1 第一次处理 blk_lab_dict_test中去掉前10w中出现过的blk
        # # RuntimeError: dictionary changed size during iteration
        # for key in list(blk_lab_dict_test.keys()):
        #     if key in tenw_list:
        #         del blk_lab_dict_test[key]
        # print(len(blk_lab_dict_test))

        # 2 blk_lab_dict_test中去掉前10w中出现过且blk_label==0的blk
        # 通过比对原来的 blk_label(label==0) 字典 raw_0_dict
        # RuntimeError: dictionary changed size during iteration
        # todo  new a dict
        for key in list(blk_lab_dict_test.keys()):
            if key in tenw_list and key in raw_0_dict.keys() and raw_0_dict[key] == "0":
                del blk_lab_dict_test[key]
        print(len(blk_lab_dict_test))  # 100w >>510590   10w >>567312

        # blk_lab_dict_test 处理完后, 将value 为0,1的各自存成字典
        test_0_dict = {}
        test_1_dict = {}
        for k, v in blk_lab_dict_test.items():
            # v is int  v == 0
            if v == 0:
                test_0_dict[k] = v
            # v is int  v == 1
            else:
                test_1_dict[k] = v
        print(len(test_0_dict))  # 100w >>491729 >552904     10w >>104814  10w >104814
        print(len(test_1_dict))  # 100w >>18861  >19629      10w >>462498  10w >470125

        """3 test_1/0_dict 与 raw_1/0_dict 匹配 得到tp fp fn
        """
        tp = 0
        for key in test_1_dict.keys():  # v is int and v==1
            # (1)"blk_raw":1   "blk_test":1  准确率tp
            # raw_1_dict   v is str and v=="1"
            if key in raw_1_dict.keys() and raw_1_dict[key] == "1":
                tp += 1
        # (2)"blk_raw":0   "blk_test":1  误报fp
        fp = len(test_1_dict) - tp

        fn = 0
        for key in test_0_dict.keys():  # v is int and v==0
            # (3)"blk_raw":1   "blk_test":0  漏报fn
            # raw_1_dict   v is str and v=="1"
            if key in raw_1_dict.keys() and raw_1_dict[key] == "1":
                fn += 1
        # (4)"blk_raw":0   "blk_test":0  剩余rem
        rem = len(test_0_dict) - fn

        print("tp  " + str(tp) + "  fp  " + str(fp) + "  fn  " + str(fn) + "  rem  " + str(rem))
        print("total  " + str(tp + fp + fn + rem))  #

        precision = round(tp / (tp + fp), 2)
        print("precision =(tp/(tp + fp))= " + str(precision))
        recall = round(tp / (tp + fn), 2)
        print("recall =(tp/(tp + fn))= " + str(recall))
        f_measure = 2 * precision * recall / (precision + recall)
        print("f_measure = 2*precision*recall / (precision + recall)= " + str(f_measure))

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

    # 100w   >test去掉前100w train里出现的blk
    # 66120
    # 572533
    # 508941
    # 491445
    # 17496
    # 575060
    # 16837
    # tp  11217  fp  6279  fn  2670  rem  488775
    # total  508941
    # precision  0.64
    # recall  0.81
    # f_measure  0.7150344827586207

    # 100w   >>test去掉前100w train里的blk==0
    # 66120
    # 575060
    # 558223
    # 16837
    # 572533
    # 510590
    # 491729
    # 18861
    # tp  12582  fp  6279  fn  2954  rem  488775
    # total  510590
    # precision  0.67
    # recall  0.81
    # f_measure  0.7333783783783785

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

    # 10w test去掉前10w train里的blk
    # 7938
    # 574939
    # 567123
    # 104814
    # 462309
    # 575060
    # 16837
    # tp  13604  fp  448705  fn  2922  rem  101892
    # total  567123
    # precision  0.03
    # recall  0.82
    # f_measure  0.05788235294117647

    # 10w   >>test去掉前10w train里的blk==0
    # 7938
    # 575060
    # 558223
    # 16837
    # 574939
    # 567312
    # 104814
    # 462498
    # tp  13793  fp  448705  fn  2922  rem  101892
    # total  567312
    # precision =(tp/(tp + fp))= 0.03
    # recall =(tp/(tp + fn))= 0.83
    # f_measure = 2*precision*recall / (precision + recall)= 0.057906976744186045


if __name__ == "__main__":
    bp = BlkPrecision()
    # bp.pattern_blk()  # pattern_blk
    # bp.pattern_label()  # pattern_label
    # bp.pat_blk_label_test()  # pattern_blk_label
    # bp.pat_blk_label_test_one_blk()  # 处理pattern_blk_label 中blk只留一个
    bp.precision()  # test_blk_label 与57w的原始raw_blk_label对比 计算tp fp fn
