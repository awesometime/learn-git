# -*- coding: utf-8 -*-

import multiprocessing
from getv import Getlog
import commands
import time

"""
多进程处理文件
"""

def process_to_csv(process_th, dir, file_name_list):
    length = len(file_name_list)
    for i in range(length):
        print("this is process ---{}--- task ---{}---".format(process_th + 1, i + 1))
        datetime_hour = file_name_list[i][12:18]
        process_hour = Getlog()
        process_hour.get_log(dir, datetime_hour)


if __name__ == '__main__':
    start_time = time.time()
    dir = "/home/users/e/log"
    cmd = "ls " + dir + " | grep csv"
    status, output = commands.getstatusoutput(cmd)
    file_name_list = output.split("\n")
    file_len = len(file_name_list)

    one_process_file_num = 10
    process_num = int(file_len / one_process_file_num)
    if process_num * one_process_file_num < file_len:
        process_num += 1

    process_pool = []
    for i in range(process_num):
        left = i * one_process_file_num
        right = (i + 1) * one_process_file_num
        if right > file_len:
            right = file_len
        cur_file_list = file_name_list[left: right]
        p = multiprocessing.Process(target=process_to_csv, args=(i, dir, cur_file_list,))
        process_pool.append(p)

    for p in process_pool:  #
        p.start()

    for p in process_pool:  # 貌似不用join比较快
        p.join()

    print(time.time() - start_time)
