
"""
动态规划解析：
状态定义： 设 dp 为一维数组，其中 dp[i] 的值代表 斐波那契数列第 i 个数字 。
转移方程： dp[i+1]=dp[i]+dp[i−1] ，即对应数列定义 f(n+1)=f(n)+f(n−1) 。
初始状态： dp[0]=0, dp[1]=1 ，即初始化前两个数字。
返回值： dp[n] ，即斐波那契数列的第 n 个数字。


状态压缩：
若新建长度为 n 的 dp 列表，则空间复杂度为 O(N) 。

由于 dp 列表第 i 项只与第 i−1 和第 i−2 项有关，
因此只需要初始化三个整形变量 sum, a, b ，
利用辅助变量 sum 使 a,b 两数字交替前进即可 （具体实现见代码） 。
节省了 dp 列表空间，因此空间复杂度降至 O(1) 。
"""

# 方法一 暴力递归(自顶向下) 不推荐
def fib(N: int) -> int:
    if N == 1 or N == 2:
        return 1
    return fib(N - 1) + fib(N - 2)

# 带着备忘录进行递归(自顶向下)
def fib(N: int) -> int:
    # 备忘录全初始化为 0
    memo = [0] * (N + 1)
    # 进行带备忘录的递归
    return dp(memo, N)

def dp(memo: List[int], n: int) -> int:
    # base case
    if n == 0 or n == 1: return n
    # 已经计算过，不用再计算了
    if memo[n] != 0: return memo[n]
    memo[n] = dp(memo, n - 1) + dp(memo, n - 2)
    return memo[n]

# 动态规划(自底向上)
def fib(N: int) -> int:
    if N == 0:
        return 0
    dp = [0] * (N + 1)
    # base case
    dp[0] = 0
    dp[1] = 1
    # 状态转移
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]

# 动态规划(自底向上) 基础上空间优化
def fib(n: int) -> int:
    if n == 0 or n == 1:
        # base case
        return n
    # 分别代表 dp[i - 1] 和 dp[i - 2]
    dp_i_1, dp_i_2 = 1, 0
    for i in range(2, n + 1):
        # dp[i] = dp[i - 1] + dp[i - 2];
        dp_i = dp_i_1 + dp_i_2
        # 滚动更新
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i
    return dp_i_1