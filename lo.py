import re
import json
import pickle

seq = "081109 203518 143 INFO dfs.DataNode$DataXceiver: Receiving block blk_-1608999687919862906 src: /10.250.19.102:54106 dest: /10.250.19.102:50010"
seq2 = "081109 203518 35 INFO dfs.FSNamesystem: BLOCK* NameSystem.allocateBlock: /mnt/hadoop/mapred/system/job_200811092030_0001/job.jar. blk_-160899968791986290608"


class lcsobj():

    def __init__(self, objid, seq, lineid, refmt):
        self._refmt = refmt
        if isinstance(seq, str) == True:
            # l r 左右截断空格
            # re.split 对右边字符串运用左边的正则     区别于str.split
            self._lcsseq = re.split(self._refmt, seq.lstrip().rstrip())
        else:
            self._lcsseq = seq
        self._lineids = [lineid]
        self._pos = []
        self._sep = "	"
        self._id = objid
        return

    def getlcs(self, seq):
        if isinstance(seq, str) == True:
            seq = re.split(self._refmt, seq.lstrip().rstrip())
        count = 0
        lastmatch = -1
        for i in range(len(self._lcsseq)):
            # if self._lcsseq[i] == '*':
            #if self._ispos(i) == True:
            # if self._ispos(i) == True:
            #     continue
            for j in range(lastmatch + 1, len(seq)):
                if self._lcsseq[i] == seq[j]:
                    lastmatch = j
                    count += 1
                    break
        return count


objid = 20

lineid = 25
refmt = "((\d)+ (\d)+ (\d)+ (\w)+ (\w)+)"
lc = lcsobj(objid, seq, lineid, refmt)
lc_content = lc.getlcs(seq)
print(lc_content)
