#!encoding:utf8

import re
import sys
import csv
from pprint import pprint


def falseMatchHandler(line):
    # print "[False] ",line
    pass


def successMatchHandler(g):
    #print(type(g.groups())) # 元组
    #pprint(g.groups())
    #header= [i for i in range(1,16)]
    row = [(item for item in g.groups())]   # 元组
    # a+追加方式打开,newline=''去掉中间空行
    with open('ten_log.csv', 'a+', newline='') as f:
        f_csv = csv.writer(f)
        #f_csv.writerow(header)
        f_csv.writerows(row)

def parseLine(line):
    if len(line) == 0:
        return
    pattern = r'(.*) - - (.*) (\[.*\]) (.*) "(.*)" (.*) (.*) (.*) "(.*)" "(.*)" "(.*)" "(.*)" (.*) "(.*)" (.*)'
    g = re.match(pattern, line, re.M | re.I)
    if g is None:
        falseMatchHandler(line)
    else:
        successMatchHandler(g)


# def parseLineTest():
#     s = """112.84.34.103 - - cnki.cdn.bcebos.com [12/Sep/2018:19:00:08 +0800] 68 "GET /2018CUMCM-AB.rar HTTP/1.1" 404 600 117 "http://cumcm.cnki.net/cumcm//studentHome/studentHome" "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0" "220.195.66.7,116.95.27.55" 5547950 "MISS" 58.216.2.35"""
#     parseLine(s)


def parseFile(filename):
    inf = open(filename, "r")

    count = 0
    for line in inf:
        parseLine(line.strip())
        count += 1
        if count % 100 == 0:
            sys.stdout.write("\r =========================> processed {}\n".format(count))
            sys.stdout.flush()
        #parseLine(line.strip())
    inf.close()


if __name__ == "__main__":
    parseFile("ten_data.txt")
