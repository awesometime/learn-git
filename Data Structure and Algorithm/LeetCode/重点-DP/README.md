动态规划自底向上(从0到n)

将分解后的子问题理解为相互间有联系,有重叠部分，

需要记忆，通常用迭代来做

递归会有重复计算

https://mp.weixin.qq.com/s?__biz=Mzg5MjcwMDc3MQ==&mid=2247502148&idx=1&sn=f90f292a7017dd62600ca2c7e0d20a40&chksm=c16f3cf3210b252b823ea4ae95d7773417acdaf67d26b9022a31fe0961d4b3b23e09ea7a42c5&mpshare=1&scene=1&srcid=02070zUxPRGd3snO6mI3I0Qt&sharer_shareinfo=3f12d08973070569cc6a936e08475594&sharer_shareinfo_first=e762c9a3a4bdd7b8309e98b8e97c1b75#rd

[golang 大彬 LIB](http://lessisbetter.site/2016/04/04/learn-dynamic-programming/)

[浅谈我对动态规划的一点理解](https://github.com/AngelKitty/Algorithm/blob/master/docs/Dynamic-programming/README.md)


- [背包问题](https://github.com/awesometime/learn-git/blob/master/Data%20Structure%20and%20Algorithm/Data%20Structure/Dynamic_Programming/Knapsack_Problem.md)

- [最长公共子串  子序列 动态规划](https://www.cnblogs.com/yuling-chao/p/7383096.html?utm_source=itdadao&utm_medium=referral)

- [n-queens](https://github.com/awesometime/learn-git/blob/master/LeetCode/Backtracking/0051._n-queens.md)

- [leetcode 0300._longest_increasing_subsequence](https://github.com/awesometime/learn-git/blob/master/LeetCode/String/0300._longest_increasing_subsequence.md)

- [leetcode 0005._longest_palindromic_substring](https://github.com/awesometime/learn-git/blob/master/LeetCode/String/0005._longest_palindromic_substring.md)

- [硬币找零问题](https://github.com/AngelKitty/Algorithm/blob/master/docs/Dynamic-programming/README.md#14%E7%A1%AC%E5%B8%81%E6%89%BE%E9%9B%B6%E9%97%AE%E9%A2%98)


https://mp.weixin.qq.com/s?__biz=Mzg5MjcwMDc3MQ==&mid=2247502148&idx=1&sn=f90f292a7017dd62600ca2c7e0d20a40&chksm=c16f3cf3210b252b823ea4ae95d7773417acdaf67d26b9022a31fe0961d4b3b23e09ea7a42c5&mpshare=1&scene=1&srcid=02070zUxPRGd3snO6mI3I0Qt&sharer_shareinfo=3f12d08973070569cc6a936e08475594&sharer_shareinfo_first=e762c9a3a4bdd7b8309e98b8e97c1b75#rd
什么是动态规划，动态规划的好处
原创 神技圈子 力扣LeetCode 2025年01月16日 17:08 上海
图片

动态规划是一种高效解决复杂问题的算法方法，特别适用于具有 重叠子问题 和 最优子结构 性质的问题。本文将围绕 什么是动态规划 及 动态规划的好处 这两个核心问题展开讨论，并通过典型案例进一步加深理解。

图片

什么是动态规划
动态规划是一种优化决策问题的算法方法，核心在于 分解问题、缓存中间结果，避免重复计算，从而高效求解复杂问题。

动态规划的两个核心特性

1. 最优子结构：

一个问题的最优解可以由其子问题的最优解组合而成。例如，在爬楼梯问题中，爬到第 n 阶的方式是由爬到 n-1 和 n-2 阶的方式决定的。

2. 重叠子问题：

原问题可以分解为若干个重复出现的子问题。例如，在斐波那契数列计算中，计算 F(5) 需要同时计算 F(4) 和 F(3) ，而这两个子问题在计算中会重复多次。

动态规划的两种求解方法

1. 自顶向下（递归 + 缓存，Memoization）：

递归地分解问题，同时缓存已经计算的结果，防止重复计算。

适用于问题规模较小的场景。

2. 自底向上（迭代）：

从最小的子问题开始，逐步计算出更大问题的解。

通常更加高效，避免了递归的函数调用开销。
图片
什么是状态转移方程
在动态规划中，状态转移方程 是算法的核心，它描述了一个问题的解如何通过子问题的解递推而来。换句话说，状态转移方程是动态规划的“递归公式”，它体现了问题的 最优子结构。

状态转移方程的定义
状态转移方程描述了一种关系，即在问题的某个状态下，如何利用更小规模问题的解来递推计算当前问题的解。它通常依赖于以下两点：

1. 状态的定义：明确用什么变量表示子问题的解。

2. 转移的逻辑：描述从已知状态如何递推到新的状态。

状态转移方程的构建步骤
1. 明确问题的目标：确定最终需要求解的问题，以及问题的约束条件。

2. 定义状态：用某种方式表示问题的子问题解。例如：二维数组 dp[i][j] 表示从前 i 个元素或字符出发的解。

3. 分析递归关系：利用问题的性质，确定从哪些更小的子问题可以递推出当前问题的解。

4. 构造状态转移方程：将递归关系用数学或代码形式表达出来。

状态转移方程的特点
1. 递归性：当前问题的解可以通过若干子问题的解递推得出。

2. 最优性：如果问题具有最优子结构性质，状态转移方程可以保证通过最优的子问题解递推出最优解。

3. 有限性：动态规划通过迭代计算或递归加缓存来避免重复计算子问题，从而在有限步骤内完成整个问题的求解。

图片

动态规划的好处

动态规划的最大优势在于其能够显著提升计算效率。以下是动态规划的具体好处：

1. 提高效率

动态规划通过缓存中间结果，避免了大量重复计算。例如，在斐波那契数列问题中，传统递归的时间复杂度是 O(2^n) ，而动态规划通过记录已经计算过的结果，将时间复杂度降至 O(n) 。

2. 降低时间复杂度

动态规划通常能将指数级时间复杂度的问题降低到多项式时间复杂度。例如：

0-1 背包问题：传统解法复杂度为 O(2^n)，动态规划可以优化至 O(nW)，其中 n 为物品数量， W 为背包容量。

字符串编辑距离：通过动态规划可以在 O(mn) 的时间内解决，而非暴力解法的 O(3^n)。

3. 适合解决复杂问题

动态规划擅长解决需要多个步骤决策的问题，例如：

路径规划：如迷宫最短路径问题。

资源分配：如背包问题、硬币兑换问题。

字符串处理：如最长公共子序列、编辑距离。

图片

动态规划的分类及实例
动态规划可以根据问题特性分为多种类型，以下是几种经典问题类型及对应的实例。

背包问题
背包问题是一种资源类问题，涉及在给定约束条件下如何最大化目标值。常见的是 0-1 背包、完全背包、多重背包。

0-1 背包问题：每个物品只选择一次

典型题目：分割等和子集

题目描述：给定一个只包含正整数的数组，判断是否可以将它分割成两个子集，使得两个子集的和相等。

解题思路：

这个题目可以换一种思路，给定一个只包含正整数的非空数组，判断是否可以从数组中选出一些数字，使得这些数字的和等于整个数组的元素和的一半。因此这个问题可以转换成 0−1 背包问题。这道题与传统的 0−1 背包问题 的区别在于，传统的 0−1 背包问题 要求选取的物品的重量之和不能超过背包的总容量，这道题则要求选取的数字的和恰好等于整个数组的元素和的一半。

在使用动态规划求解之前，首先需要进行以下判断：

1. 根据数组的长度 n 判断数组是否可以被划分。如果 n<2，则不可能将数组分割成元素和相等的两个子集，因此直接返回 false。

2. 为了能实现目标值为 target/2，如果 target 是奇数直接返回 false。

创建动态数组 dp，dp[j] 表示能否从数组的前几个元素中选出一个子集，使得子集的和等于 j。dp[j] 是一个布尔值，初始状态是 dp[0] 为 true,因为不选任何元素，和为 0 是可行的。对于每个 nums[i]，我们有两种选择：

如果不选 nums[i]：子集的和仍然是 j，所以 dp[j] = dp[j]；

如果选 nums[i]：在选这个数之前，子集的和仍然是 j-nums[i]。如果能从之前的元素中找到和为 j-nums[i]，那么 dp[j] = dp[j-nums[i]] || dp[j]。其中，dp[j] 表示上一次的值，即以前就可以组成和为 j 的子集（不依赖 nums[i]），那么此时依然可以组成和为 j。

代码如下：

bool canPartition(vector<int>& nums) {
    int sum = accumulate(nums.begin(), nums.end(), 0);
    if (sum % 2 != 0) return false;
    int target = sum / 2;
    vector<bool> dp(target + 1, false);
    dp[0] = true;  // 和为 0 总是可以实现的
    for (int num : nums) {
        for (int j = target; j >= num; --j) {
            dp[j] = dp[j] || dp[j - num];
        }
    }
    return dp[target];
}
时间复杂度：O(n*target)

空间复杂度：O(target)

完全背包问题：每个物品可以选无限次

典型题目：零钱兑换 II

题目描述：给定不同面值的硬币和一个总金额，计算有多少种组合可以凑成这个金额。

思路：给定总金额 amount 和数组 coins，要求计算金额之和等于 amount 的硬币组合数。其中，coins 的每个元素可以选取多次，且不考虑选取元素的顺序，因此这道题需要计算的是选取硬币的组合数。

可以通过动态规划的方法计算可能的组合数。用 dp[x] 表示金额之和等于 x 的硬币组合数，目标是求 dp[amount]。

动态规划的边界是 dp[0] = 1。只有当不选取任何硬币时，金额之和才为 0，因此只有 1 种硬币组合。

对于面额为 coin 的硬币，当 coin≤i≤amount 时，如果存在一种硬币组合的金额之和等于 i−coin，则在该硬币组合中增加一个面额为 coin 的硬币，即可得到一种金额之和等于 i 的硬币组合。因此需要遍历 coins，对于其中的每一种面额的硬币，更新数组 dp 中的每个大于或等于该面额的元素的值。

因此，动态规划做法如下：

初始化 dp[0] = 1；

遍历 coins，对于其中的每个元素 coin，进行如下操作：

遍历 i 从 coin 到 amount，将 dp[i−coin] 的值加到 dp[i]

最终得到 dp[amount] 的值即为答案。

例如 coins = [1,2]，对于 dp[3] 的计算，一定是先遍历硬币面额 1 后遍历硬币面额 2，只会出现以下 2 种组合：

3 = 1 + 1 + 1
3 = 1 + 2
面值 2 不可能出现在 1 之前，即不能出现 2+1 的情况。

int change(int amount, vector<int>& coins) {
    vector<int> dp(amount + 1, 0);
    dp[0] = 1;  // 凑成金额 0 的方式有 1 种
    for (int coin : coins) {
        for (int j = coin; j <= amount; ++j) {
            dp[j] += dp[j - coin];
        }
    }
    return dp[amount];
}
时间复杂度：O(n*amount)

空间复杂度：O(amount)

最长递增子序列问题
最长递增子序列问题要求在数组中找到一个递增的子序列，使其长度最大。

典型题目：最长递增子序列

题目描述：给定一个整数数组，找到其中最长严格递增子序列的长度。

思路：定义 dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度，注意 nums[i] 必须被选取。

那么，从小到大计算 dp 数组的值，在计算 dp[i] 之前，已经计算出 dp[0…i−1] 的值，则状态转移方程为：

dp[i] = max(dp[j])+1，其中 0≤j<i 且 num[j]<num[i]。

即考虑往 dp[0…i−1] 中最长的上升子序列后面再加一个 nums[i]。由于 dp[j] 代表 nums[0…j] 中以 nums[j] 结尾的最长上升子序列，所以如果能从 dp[j] 这个状态转移过来，那么 nums[i] 必然要大于 nums[j]，才能将 nums[i] 放在 nums[j] 后面以形成更长的上升子序列。

最后，整个数组的最长上升子序列即所有 dp[i] 中的最大值。

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = (int)nums.size();
        if (n == 0) {
            return 0;
        }
        vector<int> dp(n, 0);
        for (int i = 0; i < n; ++i) {
            dp[i] = 1;
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};
时间复杂度：O(n^2)

空间复杂度：O(n)

字符串匹配问题
字符串匹配问题涉及子序列、编辑距离、字符串等内容。

典型题目：最长公共子序列

题目描述：给定两个字符串，求它们的最长公共子序列长度。

思路：最长公共子序列问题是典型的二维动态规划问题。

1. 定义：

用 dp[i][j] 表示字符串 A 的前 i 个字符和字符串 B 的前 j 个字符的最长公共子序列长度。

2. 边界条件：

当 i = 0 或 j = 0 时（即其中一个字符串为空），最长公共长度为 0:

dp[i][0] = 0,

dp[0][j] = 0

 状态转移分析

如果当前字符相等即 A[i-1] = B[j-1]，则当前状态为之前状态加 1：

dp[i][j] = dp[i-1][j-1] + 1

如果当前字符不相等，则当前状态为之前状态的最大值：

dp[i][j] = max(dp[i-1][j], dp[i][j-1])

int longestCommonSubsequence(string text1, string text2) {
    int m = text1.size(), n = text2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (text1[i - 1] == text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[m][n];
}
时间复杂度：O(m*n)

空间复杂度：O(m*n)

典型题目：编辑距离

题目描述：

给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。

思路：转换过程中的操作

如果两个单词某个位置的字符相同，可以跳过这一位置，不需要额外的操作。

如果字符不同，则需要进行以下操作之一：

插入一个字符：使 word1 的当前部分匹配 word2 的当前部分。

删除一个字符：使 word1 的当前部分匹配 word2 的当前部分。

替换一个字符：将 word1 的当前字符修改为 word2 的当前字符。

那么，这个时候就得采用动态规划的方式，逐步计算从 word1 的前 i 个字符转换为 word2 的前 j 个字符的最小操作数。

1. 定义

采用二维数组 dp[i][j]，它表示将字符串 word1 的前 i 个字符转换为 word2 的前 j 个字符的最少操作数。

2. 初始状态

当 i = 0（即 word1 为空字符串）时，需要插入 j 个字符才能转成 word2 的前 j 个字符，dp[0][j] = j

当 j = 0（即 word2 为空字符串）时，需要删除 i 个字符才能将 word1 变为空字符串dp[i][0] = i

3. 状态转移分析

对于任意 i >0, j > 0 ，则考虑 word1[i-1] 和 word2[j-1] 是否相同

如果相同（word1[i-1] == word2[j-1]）：无需操作，结果等于转换前 i-1 个字符和 j-1 个字符的结果。dp[i][j] = dp[i-1][j-1]

如果不同（word1[i-1]! = word2[j-1]）：此时就需要选择插入、删除和替换的最优解：

dp[i][j] = min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])

dp[i-1][j]：对应删除操作，表示删除word1的当前字符

dp[i][j-1]：对应插入操作，表示在word1的当前追加最后一个字符

dp[i-1][j-1]：对应替换操作，表示将当前字符替换为目标字符。

具体代码如下：

int minDistance(string word1, string word2) {
    int m = word1.size(), n = word2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 0; i <= m; ++i) dp[i][0] = i;
    for (int j = 0; j <= n; ++j) dp[0][j] = j;
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (word1[i - 1] == word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
            }
        }
    }
    return dp[m][n];
}
时间复杂度：O(m*n)

空间复杂度：O(m*n)

图片

总结
动态规划是一种强大的算法工具，其核心在于分解问题和缓存中间结果，避免重复计算，从而大幅提升效率。动态规划的优势体现在以下几个方面：

1. 显著提升效率，避免重复计算。

2. 降低时间复杂度，解决大规模问题。

3. 应用广泛，擅长路径规划、字符串匹配、资源分配等问题。

动态规划的关键在于合理地定义状态和状态转移方程，在实际应用中，准确抓住问题的最优子结构和重叠子问题特性，是成功应用动态规划的核心。



BY / 

本文作者：神技圈子

编辑&版式：歪歪替

声明：本文归“力扣”版权所有，如需转载请联系。

图片

修改于2025年01月17日


​

微信扫一扫
关注该公众号


