


"""
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

https://leetcode.cn/problems/word-break/solutions/1/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/
"""

def wordBreak(s, wordDict) -> bool:
    # 初始化dp数组
    # dp[i] 代表s的前i位 能否由单词表wordDict中的单词组成
    dp = [False ] *(len(s ) +1)

    # base case
    # 空串可以被表示
    dp[0] = True

    # 遍历字符串的所有子串
    for i in range(len(s)): # [0,n)
        for j in range( i +1 ,len(s ) +1): # [i+1,n+1)
            # 若 dp[i]=True 且 s[i,⋯,j) 在 wordlist 中：dp[j]=True
            # 解释：dp[i]=True 说明 s 的前 i 位可以用 wordDict 表示，
            # 并且 s[i,⋯,j) 出现在 wordDict 中，说明 s 的前 j 位可以表示
            if dp[i] and s[i:j] in wordDict:
                dp[j] = True

    return dp[len(s)]
