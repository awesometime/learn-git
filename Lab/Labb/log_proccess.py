# -*- coding: UTF-8 -*-

import re
import difflib
from collections import OrderedDict


class LogPreproccess(object):
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
        实现 ：log key 与pattern dict 的匹配,并给log key 打label
        :return:
        """
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


def main():
    lp = LogPreproccess()
    path1 = "D:/data analysis/200nodes/col_header.txt"
    path2 = "D:/data analysis/200nodes/col_header_dict.txt"
    path3 = "D:/data analysis/200nodes/sorted-10000.log"
    path4 = "D:/data analysis/200nodes/sorted-10000_log_key.log"
    path5 = "D:/data analysis/200nodes/log_label.txt"
    pattern_list = lp.pattern_dict(path1, path2)
    print("pattern list ok")
    lp.get_log_key(path3, path4)
    print("get log key ok")
    lp.label(pattern_list, path4, path5)
    print("label ok")
    print("enjoy ~~~")


if __name__ == "__main__":
    main()
