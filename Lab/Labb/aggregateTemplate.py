#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : 
# * Email         : 
# * Create time   : 
# * Last modified : 
# * Filename      : aggregateTemplate.py
# * Description   :
'''python27
'''
# **********************************************************

def aggregateTemplate(indata, outdata):
    """
    此函数实现聚合日志功能，即将日志按长度调整顺序重排
    """

    data_dir = indata
    output_dir = outdata

    # 1 将日志存起来
    log_list = []
    outFile = file(output_dir, 'w')
    # 将indata 加到log_list
    with open(data_dir) as IN:
        for log in IN:
            log_list.append(log.strip())  # 去头尾空格

    # 2 定义临时 temp_dir 保存每条日志的 index 和len长度
    temp_dir = {}
    for i, log in enumerate(log_list):
        temp_dir[i] = len(log)
    # temp_dir.items()
    # def items(self) -> list[Tuple[_KT, _VT_co]]
    # 对list tuple 中每一项降序排列reverse     key先按列表子项tuple的x(1)再按x(0)
    # temp_dir 是list[Tuple[_KT, _VT_co]]
    temp_dir = sorted(temp_dir.items(), key=lambda x: (x[1], x[0]), reverse=True)
    # 取日志按长度排序后index 成list
    temp_index = [x[0] for x in temp_dir]

    # 3 new_log_list 将日志按长度调整顺序后保存
    new_log_list = []
    for index in temp_index:
        new_log_list.append(log_list[index])

    for log in new_log_list:
        outFile.writelines(log + "\n")


if __name__ == "__main__":
    input = 'D:/data analysis/input.dat'
    output = 'D:/data analysis/output.dat'
    aggregateTemplate(input, output)
    print 'Templates have aggregated '
