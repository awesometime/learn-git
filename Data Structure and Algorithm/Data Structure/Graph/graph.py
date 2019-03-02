class Vertex:
    """顶点类"""

    def __init__(self, key):
        self.id = key  # 顶点名称
        self.connectedTo = {}  # 与该顶点连接的顶点 {"v1":4, "v3":5}  注意v1,v3为顶点对象

    def addNeighbor(self, nbr, weight=0):  # 权重
        self.connectedTo[nbr] = weight

    def __str__(self):
        # x 是connectedTo字典的键,即顶点对象,取其id为顶点名称
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
        # d = {"qwer": 3, "asd": 4}
        # for i in d:
        #     print(i)
        # qwer
        # asd

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        # {0: <adjGraph.Vertex instance at 0x41e18>, 1: <adjGraph.Vertex instance at 0x7f2b0>}
        self.vertList = {}  # { key(顶点名称) : 顶点对象}
        self.numVertices = 0  # graph包含的顶点个数

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
# {0: <adjGraph.Vertex instance at 0x41e18>,
#  1: <adjGraph.Vertex instance at 0x7f2b0>,
#  2: <adjGraph.Vertex instance at 0x7f288>,
#  3: <adjGraph.Vertex instance at 0x7f350>,
#  4: <adjGraph.Vertex instance at 0x7f328>,
#  5: <adjGraph.Vertex instance at 0x7f300>}
g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

# ( 0 , 5 )
# ( 0 , 1 )
# ( 1 , 2 )
# ( 2 , 3 )
# ( 3 , 4 )
# ( 3 , 5 )
# ( 4 , 0 )
# ( 5 , 4 )
# ( 5 , 2 )
