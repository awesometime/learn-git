

# 自底向上  for循环+初始化数组 迭代
# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/target-sum/solutions/2119041/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-s1cx/
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    # 正数和 p, 全部数字绝对值的和s
    # 负数绝对值和 s-p
    # p-(s-p) = target
    # p = (target +s) / 2
    target += sum(nums)
    if target < 0 or target % 2:  # 余数为1 是奇数
        return 0
    target //= 2
    # 转化成在nums中取一些数 使得和为(target +s) / 2 的方案数量

    n = len(nums)
    f = [[0] * (target + 1) for _ in range(n + 1)]
    f[0][0] = 1
    for i, x in enumerate(nums):
        for c in range(target + 1):
            if c < x:
                f[i + 1][c] = f[i][c]  # 只能不选
            else:
                f[i + 1][c] = f[i][c] + f[i][c - x]  # 不选 + 选
    return f[n][target]


# 自顶向下 递归 击败5%
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    # 正数和 p, 全部数字绝对值的和s
    # 负数绝对值和 s-p
    # p-(s-p) = target
    # p = (target +s) / 2
    target += sum(nums)
    if target < 0 or target % 2: # 余数为1 是奇数
        return 0
    target //= 2
    # 转化成在nums中取一些数 使得和为(target +s) / 2 的方案数量

    n = len(nums)
    def dfs(i ,c):
        if i< 0:  # i从n-1 遍历到0
            if c == 0:  # target==0说明找到了一种方案
                return 1
            else:
                return 0
        if c < nums[i]:
            # 目标 比实际小  只能不选
            return dfs(i - 1, c)
        # 注意是相加
        #        不选             选
        return dfs(i - 1, c) + dfs(i - 1, c - nums[i])

    # 从最后一个数开始 倒着
    return dfs(n - 1, target)