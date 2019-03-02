from pythonds.basic.queue import Queue


def hot_potato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    # l = [x for x in simqueue.items]
    # print(l)


    # 每次砍掉一个人 循环simqueue.size()-1次
    while simqueue.size() > 1:
        # 每次 hot_potato 的传递次数num
        for i in range(num):
            # 每次从[queue首simqueue.dequeue()]传递到queue对尾[simqueue.enqueue()]
            simqueue.enqueue(simqueue.dequeue())
        # 传递完一轮后将queue首砍掉
        simqueue.dequeue()
        # print(simqueue.dequeue())

    return simqueue.dequeue()


#print(hot_potato(["x1", "x2", "x3", "x4", "x5", "x6"], 7))
hot_potato(["x1", "x2", "x3", "x4", "x5", "x6"], 7)
# ['x6', 'x5', 'x4', 'x3', 'x2', 'x1']