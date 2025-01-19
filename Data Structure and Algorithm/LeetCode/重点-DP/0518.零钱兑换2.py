

# https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247486107&idx=1&sn=e5fa523008fc5588737b7ed801caf4c3&chksm=fd9ca184caeb28926959c0987208a3932ed9c965267ed366b5b82a6fc16d42f1ff40c29db5f1&token=660810714&lang=zh_CN#rd
amount = 5
coins = [1, 2, 5]

def change(amount, coins):
    # dp[len(coins)][amount]
    dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
    dp[0][0] = 1

    # 先遍历coin 保证不会重复计算不同的排列 如 112 121 211
    for i in range(1, len(coins) + 1):
        for j in range(0, amount + 1): # amount 可取0
            dp[i][j] = dp[i - 1][j] # 其实就是k=0
            for k in range(1,j // coins[i - 1] + 1): # 所以此处k从1开始
                # 用前i种硬币凑齐j有dp[i][j]种方案
                # 前面方案的基础上又多了一种方案
                dp[i][j] = dp[i][j] + dp[i-1][j - k * coins[i - 1]]
                #dp[i][j] = min(dp[i][j - k * coins[i - 1]] + k, dp[i - 1][j])
    print(dp)
    return dp[len(coins)][amount]


print(change(amount, coins))
