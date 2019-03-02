from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

# 初始化为white,
def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)  # insert(0)  # 直接用list也行

    # 循环时(只要Queue不为空)首先从Queue队尾dequeue出点v
    # 找v的邻接点然后enqueue进入队首
    # 将v置为black
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()  # pop()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


traverse(g.getVertex('sage'))
