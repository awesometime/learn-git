#!encoding:utf8

import re
import sys
from pprint import pprint

class FileHandler(object):
  def __init__(self, filename):
    self.f = open(filename, "w+") if filename is not None else None
  def __del__(self):
    assert self.f is not None, "f is not init"
    self.f.close()
  def handle(self, items):
    assert self.f is not None, "f is not init"
    self.f.write("{}\n".format(self._toLine(items)))
  def _toLine(self, items):
    raise NotImplementedError

class FalseMatchFileHandler(FileHandler):
  def _toLine(self, items):
    return items

class SuccessMatchFileHandler(FileHandler):
  def _toLine(self, items):
    return "@".join(items)

def parseLine(line, falseHandler, succHandler):
  if len(line) == 0:
    return
  pattern = r'(.*) - - (.*) (\[.*\]) (.*) "(.*)" (.*) (.*) (.*) "(.*)" "(.*)" "(.*)" "(.*)" (.*) "(.*)" (.*)'
  g = re.match(pattern, line, re.M|re.I)
  if g is None:
    falseHandler.handle(line)
  else:
    succHandler.handle(g.groups())

def parseLineTest():
  s = """112.84.34.103 - - cnki.cdn.bcebos.com [12/Sep/2018:19:00:08 +0800] 68 "GET /2018CUMCM-AB.rar HTTP/1.1" 404 600 117 "http://cumcm.cnki.net/cumcm//studentHome/studentHome" "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0" "220.195.66.7,116.95.27.55" 5547950 "MISS" 58.216.2.35"""
  a = FalseMatchFileHandler("false")
  b = SuccessMatchFileHandler("succ")
  parseLine(s, a, b)

def parseFile(filename):
  inf = open(filename, "r")
  succHandler = SuccessMatchFileHandler("success.data")
  falseHandler = FalseMatchFileHandler("false.data")
  count = 0
  for line in inf:
    parseLine(line.strip(), falseHandler, succHandler)
    count += 1
    if count % 100 == 0:
      sys.stdout.write("\r ==> processed {}".format(count))
      sys.stdout.flush()
  inf.close()

if __name__ == "__main__":
  # parseFile("thh_data.txt")
  parseFile("a.txt")
  # parseLineTest()
