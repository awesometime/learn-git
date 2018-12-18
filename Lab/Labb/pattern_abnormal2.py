##python3

import re
import pandas as pd


class LogKeyLabel(object):
    """
    implement :
    1 简单处理log pattern
    2 得到每行log的log key
    3 log key匹配log pattern然后加label (1-29)
    """

    def __init__(self):
        pass

    def pattern_list(self, inpath):
        """
        实现 ： 输入是 29行 n.pattern
        将 29个 pattern 存成 (index, pattern) 组成的列表
        :param inpath:
        :return:  list of tuple of sorted pattern dict
        """
        index_list = []
        log_content_list = []
        with open(inpath, 'r') as f:
            for line in f:
                if line == "\n":
                    break
                else:
                    line = line.strip()
                    il = re.search('(\d+)(\.)(.*)', line).group(1)
                    index_list.append(il)
                    pl = str(re.search('(\d+)(\.)(.*)', line).group(3))
                    log_content_list.append(pl)
        # print(index_list)
        # print(log_content_list)
        pattern_list = list(zip(index_list, log_content_list))
        return pattern_list

    def label(self, inpath1, inpath2, labeloutpath, logoutpath):
        """
        实现 ：log key 与pattern dict 的匹配,并给log key 打label  输出到文件
        :return:  none
        """
        pattern_list = self.pattern_list(inpath1)

        # 打开 get, total = total line of file 关闭,否则readlines后读到内存里,文件就空了,后边打开内容为空
        inf = open(inpath2, 'r')
        total = len(inf.readlines())
        inf.close()

        label_list = []
        with open(inpath2, 'r') as f:
            #outf = open(logoutpath, 'w')
            match_num = 0
            for line in f:
                label = 0
                for p in pattern_list:
                    regex = re.compile(p[1])
                    res = regex.search(line)
                    # match 从开头开始
                    # res=regex.match(line)
                    if res:
                        label = p[0]
                        break
                label_list.append(label)

                match_num += 1
                if match_num == total:
                    percent = 100.0
                    outf = open(logoutpath, 'a')
                    outf.write('current per : {} [{}/{}] log_pattern have been completed\n'.format(str(percent) + '%',
                                                                                                   match_num, total))
                    outf.close()
                elif match_num % 10000 == 0:
                    percent = round(1.0 * match_num / total * 100, 2)
                    outf = open(logoutpath, 'a')
                    outf.write('current per : {} [{}/{}] log_pattern have been completed\n'.format(str(percent) + '%',
                                                                                                   match_num, total))
                    outf.close()

        outf = open(labeloutpath, 'w')
        for i in label_list:
            # print(type(i)) # str
            outf.write(str(i) + "\n")
        outf.close()


class AbnormityLabel(object):
    """
    implement :
    1 得到blk和label对应关系字典 保存成字典
    2 得到每行log 的blk 保存到文件
    3 给每行log加label(abnormal 1  or normal 0)
    """

    def __init__(self):
        pass

    def blk_label_dict(self, blkpath, labelpath):
        """
        实现 得到label 为1 的blk的字典
        """
        blk_list = []
        with open(blkpath, 'r') as f:
            for line in f:
                line = line.strip()
                blk = re.sub('%', '', line)
                blk_list.append(blk)

        label_list = []
        with open(labelpath, 'r') as f:
            for line in f:
                line = line.strip()
                res = re.search("(\d)(.*)", line).group(1)
                label_list.append(res)

        # 全部 57 万 blk_
        # dict以后 key 会去重
        blk_label_dict = dict(zip(blk_list, label_list))
        # print(len(blk_label_dict))  # 575138

        # 取label为1异常的(Abnormity)的blk_   {"blk_" :"1"}
        for key in list(blk_label_dict.keys()):
            if blk_label_dict[key] == "0":
                del blk_label_dict[key]
        # print(len(blk_label_dict))  # 16915
        return blk_label_dict

    def fetch_blk(self, inpath, outpath):
        """
        implement : fetch blk in every log
        :return:
        """
        outf = open(outpath, 'w')
        with open(inpath, 'r') as f:
            for line in f:
                line = line.strip()
                # rest 是一个列表
                rest = re.findall("blk_-\d+|blk_\d+", line)
                for i in rest:
                    outf.write(i)
                # 每行blk_输出后换行
                outf.write("\n")
                # print(rest)
                # print(len(rest))
        outf.close()

    def match(self, blk_label_dict, blk_list):
        """
        implement : input blk list and blk_label_dict,   return label 0 1 of every line
        :return:
        """
        log_key_normal_label_everyline = []
        current_label = []
        for every_blk in blk_list:
            # 遍历 17000 个异常 blk_label_dict 匹配到label=1 匹配不到label=0
            for k in blk_label_dict.keys():
                if every_blk == k:
                    current_label.append("1")
                    break
            # 遍历一条 blk 有1 的话直接label = 1 break
            if "1" in current_label:
                log_key_normal_label_everyline.append("1")
                break
        # 如果所有均为0 则label = 0
        if "1" not in current_label:
            log_key_normal_label_everyline.append("0")
        return log_key_normal_label_everyline

    def label(self, inpath1, inpath2, inpath3, labeloutpath, logoutpath):
        """
        implement : 每条log 的 blk 去匹配 blk_label_dict, 若匹配到则将log的label置为1(Abnormity),其余为0(nomal)
        :return:
        """
        # check file is existed
        try:
            f = open(inpath3, 'r')
            f.close()
        except FileNotFoundError:
            print("File is not found.")
        # get blk_label_dict
        blk_label_dict = self.blk_label_dict(inpath1, inpath2)
        # init var
        log_key_normal_label = []

        # 打开 get, total = total line of file 关闭,否则readlines后读到内存里,文件就空了,后边打开内容为空
        inf = open(inpath3, 'r')
        total = len(inf.readlines())
        inf.close()

        # 再次打开
        with open(inpath3, 'r') as f:
            match_num = 0
            for line in f:
                line = line.strip()
                blk_list = re.findall("blk_-\d+|blk_\d+", line)
                if len(blk_list) == 2 and blk_list[0] == blk_list[1]:
                    # blk_list_中两个 且一样先pop掉最后一个
                    blk_list.pop()
                    log_key_normal_label.append(self.match(blk_label_dict, blk_list)[0])
                else:
                    log_key_normal_label.append(self.match(blk_label_dict, blk_list)[0])

                # 打印进度条
                match_num += 1
                if match_num == total:
                    percent = 100.0
                    outf = open(logoutpath, 'a')
                    outf.write('current per : {} [{}/{}] log_abnormal have been completed\n'.format(str(percent) + '%',
                                                                                                    match_num, total))
                    outf.close()
                elif match_num % 10000 == 0:
                    percent = round(1.0 * match_num / total * 100, 2)
                    outf = open(logoutpath, 'a')
                    outf.write('current per : {} [{}/{}] log_abnormal have been completed\n'.format(str(percent) + '%',
                                                                                                    match_num, total))
                    outf.close()
        # print(log_key_normal_label)
        # print(len(log_key_normal_label))
        # return log_key_normal_label

        # log_key_normal_label   list 输出到文件中
        outf = open(labeloutpath, 'w')
        for i in log_key_normal_label:
            outf.write(i + "\n")
        outf.close()

    def save_pattern_abnormal(self, path1, path2, path3):
        """
        implement : save pattern abnormal label to a file
        :return:
        """
        df1 = pd.read_csv(path1, header=None)
        # print(df1)
        df2 = pd.read_csv(path2, header=None)
        re = pd.concat([df1, df2], axis=1)
        re.to_csv(path3, sep=' ', index=False, header=False)


def main():
    lp = LogKeyLabel()
    lp.label(path1, path2, path3, path9)
    print("1 put tag on every log ok:)  please see log pattern label in --> {}".format(path3) + "\n")
    print("  please see log percent in ----> {}".format(path9) + "\n")


def main2():
    al = AbnormityLabel()
    al.fetch_blk(path2, path4)
    print("2 fetch blk of every line ok:)  please see in {}".format(path4) + "\n")
    al.label(path6, path7, path4, path5, path10)
    print("\n" + "3 label abnormal ok:)  please see in {}".format(path5) + "\n")
    al.save_pattern_abnormal(path3, path5, path8)
    print("4 save pattern and abnormal ok:)  please see in {}".format(path8) + "\n")


if __name__ == "__main__":
    
    # path1 path2 path6 path7 为事先存在的文件
    # path1 是34 个log key pattern
    path1 = "F:/_data/200nodes/col.txt"
    path2 = "F:/_data/200nodes/sorted-10000.log"
    path3 = "F:/_data/200nodes/sorted-10000_log_pattern.log"
    path4 = "F:/_data/200nodes/sorted-10000_blk.log"
    path5 = "F:/_data/200nodes/abnormal_label.log"
    path6 = "F:/_data/200nodes/nameIndex.txt"
    path7 = "F:/_data/200nodes/mlabel.txt"
    path8 = "F:/_data/200nodes/pattern_abnormal.log"
    path9 = "F:/_data/200nodes/log_pattern_percent.log"
    path10 = "F:/_data/200nodes/log_abnormal_percent.log"
    main()
    main2()
