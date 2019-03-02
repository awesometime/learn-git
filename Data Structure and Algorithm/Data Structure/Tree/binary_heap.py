# from pythonds.trees.binheap import BinHeap
#
# bh = BinHeap()
# bh.insert(5)
# bh.insert(7)
# bh.insert(3)
# bh.insert(11)
#
# print(bh.delMin())
#
# print(bh.delMin())
#
# print(bh.delMin())
#
# print(bh.delMin())

"""
堆顺序属性:
1.树的根是树中的最小(大)项   根节点比子节点小(大)
2.最大（最小）堆是一棵每一个节点的键值都大于（小于）其子节点键值的树,左右子节点大小没有顺序
3.父两子节点索引分别为 n 、2n 、2n+1
4.n = 叶节点个数 + 度数为1节点个数 + 度数为2节点个数 ,且度数为 1节点个数为 0或 1
堆结构属性


alist [5 33 14 ]
currentSize  0   1   2  3   4   5   6    7     8    9  10
heapList     0   5   9  11  14  18  19   21    33  17  27
"""


# this heap takes key value pairs, we will assume that the keys are integers
class BinHeap():  # 此处讨论根比节点小的堆
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0  # 可以理解为索引

    def buildHeap(self, alist):
        """从一个列表建立一个堆的方法
        思路:
        从树的中间i=len(alist)//2开始，每次调用percDown(i)方法,使子堆满足堆结构,i-1直到向上返回到根节点。

        也就是从最后一个节点[len(alist)对应的节点]的父节点[i]开始,
        运用percDown(i)方法:如果 i大于其子节点,将i向下交换,直到找到其正确的位置
        """
        # i为最后一个节点的父节点
        i = len(alist) // 2  # 序号len(list)对应最后一个节点,  len(alist)//2即最后一个节点的父节点
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        # print(len(self.heapList), i)
        # 从最后一层(无子节点那层)的上一层(这一层开始有子节点)开始走循环,
        # 走完一次循环后下边的层已经满足堆的大小顺序要求,直到根节点i=1
        while (i > 0):
            # print(self.heapList, i)
            # 父节点与最小子节点交换
            self.percDown(i)
            i = i - 1
        # print(self.heapList, i)

    def percUp(self, i):
        """小顶堆:比较新添加的节点i与其父节点，如果新添加的项i小于其父节点，则与其父节点交换,层层往上。
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        """思路:
        1 先将k追加到列表最后
        2 通过 percUp()方法:如果k比其父节点小,向上交换,直到找到正确的位置
        """
        # k先追加到列表最后
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        # 比较其父节点  向上交换
        self.percUp(self.currentSize)

    def percDown(self, i):
        """传入节点 i 和 其最小子节点交换,知道索引越界  参数 -->根节点序号 i  """
        # 根节点*2  为子节点
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            # 小顶堆: 当前节点与其子节点值比较,如果大则交换
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        """对于一个节点i,返回其子节点(2i,2i+1)中值较小的那个对应的索引
        """
        # 找到最小项对应的索引
        # (i * 2) <= self.currentSize 那步跳进来的,所以不用担心索引越界
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        """
        删除最小项,对于小顶堆即删除 heapList[1],返回其值
        思路是:
        1 将 heapList 列表最后一项的值赋给第一项
        2 从 heapList中 pop出最后一项
        3 通过 percDown(1)方法:如果第一项大于其子节点,将第一项向下交换直到找到其正确的位置
        """
        # 根位置即最小项
        retval = self.heapList[1]
        # 获取列表中的最后一个项并将其移动到根位置来恢复根项
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        # 最后一个项pop出去
        self.heapList.pop()
        # 第一项  比较其子节点  向下交换
        self.percDown(1)
        return retval

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False
