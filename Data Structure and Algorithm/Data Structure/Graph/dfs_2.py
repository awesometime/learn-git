# https://facert.gitbooks.io/python-data-structure-cn/7.%E5%9B%BE%E5%92%8C%E5%9B%BE%E7%9A%84%E7%AE%97%E6%B3%95/7.15.%E9%80%9A%E7%94%A8%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2/
from pythonds.graphs import Graph
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        # self是 DFSGraph 类的一个实例，遍历图实例中的所有顶点   todo 怎么理解
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        # 调用图中所有的顶点迭代，这些节点是白色的。迭代所有节点而不是简单地从所选择的起始节点
        # 进行搜索的原因是为了确保图中的所有节点都被考虑到，没有顶点从深度优先森林中被遗漏
        for aVertex in self:   # meige
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        # 就是将startVertex.disc = self.time
        # def setDiscovery(self, dtime):
        #     self.disc = dtime

        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
                # dfsvisit 使用栈.在代码中没有看到栈，但是它在dfsvisit的递归调用中是隐含的
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)