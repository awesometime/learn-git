# # 输入输出
# stopword = ''
# InputList = []
# for line in iter(input, stopword):  # iter是一个迭代器，第二个参数指定了迭代停止的条件
#     InputList.append(list(map(int, line.split())))
# # print("InputList=",InputList)

# 输入输出
# nums = int(input())
# points = []
# for i in range(0, nums):
#     read_list = list(map(int, input().split()))
#     # read_list = [int(i) for i in input().split()]
#     points.append((read_list[0], read_list[1]))


"""
题目描述
公司的程序员不够用了，决定把产品经理都转变为程序员以解决开发时间长的问题。
在给定的矩形网格中，每个单元格可以有以下三个值之一:
.值0代表空单元格;

.值1代表产品经理;

.值2代表程序员;
每分钟，任何与程序员(在4个正方向上)相邻的产品经理都会变成程序员。
返回直到单元格中没有产品经理为止所必须经过的最小分钟数。
如果不可能，返回-1。

输入描述:
不固定多行〈行数<= 10)，毎行是按照空格分割的数字(不固定，毎行数字个数<= 10)

其中每个数组项的取值仅为0、1、2三种

 (读取时可以按行读取，直到读取到空行为止，再对读取的所有行做转换处理)

输出描述:

如果能够将所有产品经理变成程序员，则输出最小的分钟数。

 如果不能够将所有的产品经理变成程序费，则返回-1.

示例1：

0 2

1 0

输出：

-1

 

示例2：

输入：

1 2 1

1 1 0

0 1 1

输出：

3

"""


def ifExist1(grid):
    for grid_row in grid:
        if 1 in grid_row:
            return True
    return False


def find2(grid):
    # 找到此时所有的为 2 的坐标 添加到coord
    coord = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                coord.append([i, j])

    # 如果之前这个2 的四周已经change为1 就不需要再改变了
    global change_dict
    # 所有的为 2 的 有可能前边的change时已经将当前的变成2了  当前就不需要再change了
    # 为2的几个点中只要有一个改变了 就发生了改变
    at_least_changed_once = []
    for e_coord in coord:
        i, j = e_coord
        if (i, j) in change_dict:
            continue
        else:
            changed = change2To1(grid, i, j)
            at_least_changed_once.append(changed)

    for ii in grid:
        print(ii)
    print()
    return any(at_least_changed_once)


def change2To1(grid, i, j):
    global change_dict
    ischange = False
    coord_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 下右左上
    for x, y in coord_dir:
        r = x + i  # i+=x  i=i+x 不行 每次循环应保证i j 不变
        c = y + j
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
            grid[r][c] = 2
            ischange = True
            # 将周围的变量已经更新过的2记录在字典里，避免重复搜索，减少时间复杂度
            change_dict[(i, j)] = 1  # tricky {(2, 3): 1, (2, 2): 1}
    return ischange


change_dict = {}


def main(grid):
    for ii in grid:
        print(ii)
    print()
    if not grid:
        return -1
    min_time = 0
    # 停止条件：       矩阵中不存在1了
    # 另外一种停止条件：矩阵中还有1，上一轮中没有1变成2，这种情况说明有1更新不到，返回-1.
    while ifExist1(grid):
        if not find2(grid):
            min_time = -1
            break
        else:
            # 每更新一次就对时间变量加1
            min_time += 1
            continue
    return min_time


grid0 = [[0, 2],
         [1, 0]]

grid1 = [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 1]]

grid2 = [[1, 2, 1],
         [1, 1, 0],
         [0, 1, 1]]

grid3 = [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 2]]

grid4 = [[1, 2],
         [2, 1],
         [1, 2],
         [0, 1],
         [0, 1],
         [1, 1]]

grid5 = [[0, 2],
         [0, 1],
         [1, 1]]

grid6 = []

# print(main(grid0))
# print(main(grid1))
# print(main(grid2))
# print(main(grid3))
# print(main(grid4))
# print(main(grid5))
# print(main(grid6))
