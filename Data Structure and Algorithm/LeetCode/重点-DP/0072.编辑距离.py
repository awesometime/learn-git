# https://labuladong.online/algo/dynamic-programming/edit-distance/

# 如何定义dp[][]
# 如何翻译  插入 删除 替换 动作
# 如何优化


# 方法一: 自顶向下
def minDistance(self, s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    # i，j 初始化指向最后一个索引
    return self.dp(s1, m - 1, s2, n - 1)

# 定义：返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
def dp(self, s1: str, i: int, s2: str, j: int) -> int:
    # base case
    # i 走完 s1 或 j 走完 s2，可以直接返回另一个字符串剩下的长度
    # 因为剩余字符都需要删除
    if i == -1:
        return j + 1
    if j == -1:
        return i + 1

    if s1[i] == s2[j]:
        # 啥都不做
        return self.dp(s1, i - 1, s2, j - 1)
    # 解释：
    # 本来就相等，不需要任何操作
    # s1[0..i] 和 s2[0..j] 的最小编辑距离等于
    # s1[0..i-1] 和 s2[0..j-1] 的最小编辑距离
    # 也就是说 dp(i, j) 等于 dp(i-1, j-1)

    return min(
        # 插入
        self.dp(s1, i, s2, j - 1) + 1,
        # 解释：
        # 我直接在 s1[i] 插入一个和 s2[j] 一样的字符
        # 那么 s2[j] 就被匹配了，前移 j，继续跟 i 对比
        # 别忘了操作数加一

        # 删除
        self.dp(s1, i - 1, s2, j) + 1,
        # 解释：
        # 我直接把 s[i] 这个字符删掉
        # 前移 i，继续跟 j 对比
        # 操作数加一

        # 替换
        self.dp(s1, i - 1, s2, j - 1) + 1
        # 解释：
        # 我直接把 s1[i] 替换成 s2[j]，这样它俩就匹配了
        # 同时前移 i，j 继续对比
        # 操作数加一
    )

# int dp(i, j) {
#     dp(i - 1, j - 1); // #1
#     dp(i, j - 1);     // #2
#     dp(i - 1, j);     // #3
# }
# 对于子问题 dp(i-1, j-1)，如何通过原问题 dp(i, j) 得到呢？
# 有不止一条路径，比如 dp(i, j) -> #1 和 dp(i, j) -> #2 -> #3。
# 一旦发现一条重复路径，就说明存在巨量重复路径，也就是重叠子问题。


# 优化方法2: 备忘录解法
# 递归解法是自顶向下求解（从原问题开始，逐步分解到 base case）
class Solution:
    def __init__(self):
        self.memo = []

    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # 备忘录初始化为特殊值，代表还未计算  m X n
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(s1, m - 1, s2, n - 1)

    def dp(self, s1: str, i: int, s2: str, j: int) -> int:
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        # 查备忘录，避免重叠子问题
        if self.memo[i][j] != -1:
            return self.memo[i][j]

        # 状态转移，结果存入备忘录
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i - 1, s2, j - 1)
        else:
            self.memo[i][j] = min(
                self.dp(s1, i, s2, j - 1) + 1,
                self.dp(s1, i - 1, s2, j) + 1,
                self.dp(s1, i - 1, s2, j - 1) + 1
            )

        return self.memo[i][j]


# 优化方法3: DP table 解法
# 自底向上求解（从 base case 开始，向原问题推演）
class Solution2:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # 定义：s1[0..i] 和 s2[0..j] 的最小编辑距离是 dp[i+1][j+1]
        # (m+1)*(n+1)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # base case
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        # 自底向上求解
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )
        # 储存着整个 s1 和 s2 的最小编辑距离
        return dp[m][n]