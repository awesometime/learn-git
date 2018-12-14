# -*- coding: UTF-8 -*-

import re
import difflib
import pprint


class LogKeyLabel(object):
    def __init__(self):
        pass

    def pattern_dict(self, inpath, outpath):
        """
        实现 ：将29个 pattern 存成字典 pattern dict(这里是list)
        :param inpath:
        :param outpath:
        :return:  list of tuple of sorted pattern dict
        """
        outf = file(outpath, 'w')
        index_list = []
        pattern_list = []
        with open(inpath, 'r') as f:
            for line in f:
                line = line.strip()
                line = re.sub('\(\.\*\)', '', line)
                line = re.sub('\(\[-\]\?\[0-9]\+\)|\(\[-\]\?\[0-9]\+\)', '', line)
                il = re.search('(\d+)(\.)(.*)', line).group(1)
                index_list.append(il)
                pl = str(re.search('(\d+)(\.)(.*)', line).group(3))
                pattern_list.append(pl)
        pattern_dict = zip(index_list, pattern_list)
        # 字典排序返回元组组成的列表(出现1 10 11 12 问题 deprecated)
        # log_dict = OrderedDict(sorted(log_dict.items(), key=lambda x: x[0], reverse=False))
        # print (pattern_dict)
        outf.write(str(pattern_dict))
        outf.close()
        return pattern_dict

    def get_log_key(self, inpath, outpath):
        """
        逐行实现 ：log 处理,过滤数字、变量，获得关键词 log key
        TODO log 去重 spell或者ft_tree 那样
        :return:
        """
        outf = file(outpath, 'w')
        with open(inpath, 'r') as f:
            for line in f:
                line = line.strip()
                line = re.search('(.*?)(\:\s)(.*)', line).group(3)  # 非贪婪匹配 尽可能少
                # line = re.search('(\:\s)(.*)', line).group(2)
                line = re.sub('blk_.(\d+)', '', line)
                # /10.250.19.102:54106  10.250.19.102:54106  3456
                line = re.sub('(\/((\d+)\.){3}(\d+)\:(\d+))|((\d+)\.){3}(\d+)\:(\d+)|\d+', '', line)
                line = re.sub('\/.*', '', line)
                line = re.sub('\:|,', '', line)
                outf.write(line + "\n")
        outf.close()

    def label(self, pattern, inpath, outpath):
        """
        实现 ：log key 与pattern dict 的匹配,并给log key 打label  输出到文件
        :return:  none
        """
        label = 0
        label_list = []
        with open(inpath, 'r') as f:
            for line in f:
                ini_percent = 0
                for p in pattern:
                    now_percent = difflib.SequenceMatcher(None, p[1], line).quick_ratio()
                    if now_percent > ini_percent:
                        ini_percent = now_percent
                        label = p[0]
                    else:
                        pass
                label_list.append(label)
        outf = file(outpath, 'w')
        for i in label_list:
            outf.write(i + "\n")
        outf.close()

    # def diff(self, pattern, every_line):
    #     list = []
    #     for p in pattern:
    #         difflib.SequenceMatcher(None, every_line, p[1]).quick_ratio()
    #
    #     pass


class AbnormityLabel(object):
    def __init__(self):
        pass

    def blk_label_dict(self, blkpath, labelpath):  # , blkoutpath, labeloutpath):
        # bof = file(blkoutpath, 'w')
        blk_list = []
        with open(blkpath, 'r') as f:
            for line in f:
                line = line.strip()
                blk = re.sub('%', '', line)
                blk_list.append(blk)

        # bof.close()

        # lf = file(labelpath, 'w')
        # lof = file(labeloutpath, 'w')
        label_list = []
        with open(labelpath, 'r') as f:
            for line in f:
                res = re.search("(\d)(.*)", line).group(1)
                label_list.append(res)

        # 全部blk_
        blk_label_dict = dict(zip(blk_list, label_list))
        # print(len(blk_label_dict))  # 575139

        # 取label为1(Abnormity)的blk_
        for key, value in blk_label_dict.items():
            if value == "0":
                del blk_label_dict[key]
        # print(len(blk_label_dict))  # 16916
        return blk_label_dict
        # for _ in range(126):
        #     pprint.pprint(blk_label_dict[_])
        # lof.write(str(label_list))
        # lof.close()

    def fetch_blk(self, inpath, outpath):
        """
        implement : fetch blk in every log
        :return:
        """
        outf = file(outpath, 'w')
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


    def label(self, dict):
        """
        implement : 每条log 的 blk 去匹配 blk_label_dict, 若匹配到则将log的label置为1(Abnormity),其余为0(nomal)
        :return:
        """
        # 匹配到就break
        # 1个blk 遍历 17000 blk_label_dict 匹配到break
        # 2个blk 遍历 17000  相同则匹配一次  不同则每个都要匹配 blk_label_dict 匹配到1 break
        # 多个blk 每个遍历 17000 blk_label_dict 匹配一个 1 到break
        pass


def main():
    lp = LogKeyLabel()
    pattern_list = lp.pattern_dict(path1, path2)
    print("pattern list ok")
    lp.get_log_key(path3, path4)
    print("get log key ok")
    lp.label(pattern_list, path4, path5)
    print("label ok")
    print("enjoy ~~~")


def main2():
    al = AbnormityLabel()
    # blk_label_dict = al.blk_label_dict(path6, path7)
    al.fetch_blk(path3, path10)
    # al.label(blk_label_dict)


if __name__ == "__main__":
    path1 = "D:/data analysis/200nodes/col_header.txt"
    path2 = "D:/data analysis/200nodes/col_header_dict.txt"
    path3 = "D:/data analysis/200nodes/sorted-10000.log"
    path4 = "D:/data analysis/200nodes/sorted-10000_log_key.log"
    path5 = "D:/data analysis/200nodes/log_label.txt"
    path6 = "D:\data analysis/200nodes/nameIndex.txt"
    path7 = "D:\data analysis/200nodes/mlabel.txt"
    path8 = "D:\data analysis/200nodes/nameIndex1.txt"
    path9 = "D:\data analysis/200nodes/mlabel1.txt"
    path10 = "D:/data analysis/200nodes/sorted-10000_blk.log"
    # main()
    main2()
