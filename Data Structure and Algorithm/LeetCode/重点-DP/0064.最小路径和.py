

grid = [[1,3,1],[1,5,1],[4,2,1]]

#链接：https://leetcode.cn/problems/minimum-path-sum/solutions/25943/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/
def minPathSum1(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == j == 0: continue
            elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
            elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
            else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    return grid[-1][-1]

def minPathSum2(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    rows, columns = len(grid), len(grid[0])

    # 状态定义 dp[i][j] 表示从左上角出发到 (i,j) 位置的最小路径和
    dp = []
    for i in range(rows):
        dp.append([])
        dp[i] = [0] * columns
    # print(dp)

    # base case
    dp[0][0] = grid[0][0]

    # 第一列
    # 由于需要用到i-1,所以i需要从1开始
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # 第一行
    # 由于需要用到j-1,所以j需要从1开始
    for j in range(1, columns):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # i>0 j>0
    # 由于需要用到i-1,j-1,所以i j均需要从1开始
    for i in range(1, rows):  # 上到下
        for j in range(1, columns):  # 左到右
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[rows - 1][columns - 1]


print(minPathSum1(grid))