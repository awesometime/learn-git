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

### DP


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        p = [False] * len(s)
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                p[i] = True
                continue
            for k in range(i):
                if p[k] and s[k + 1:i + 1] in wordDict:
                    p[i] = True
        # print(p)
        return p[-1]


# 一个DP问题。定义possible[i] 为S字符串上[0,i]的子串是否可以被segmented by dictionary.
#
# possible[i] = true if S[0,i]在dictionary里面
#
# = true if possible[k] == true 并且 S[k+1,i]在dictionary里面， 0<k<i
#
# = false if no such k exist.

# s = "leetdogcode"
# wordDict = ["le","etd", "og", "code"]


### 其它写法

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok = [True]
        for i in range(1, len(s)+1):
            ok += [any(ok[j] and s[j:i] in wordDict for j in range(i))]
        # print(ok)
        return ok[-1]
        
    
    # 等价于下边
    def wordBreak(s, wordDict):
        ok = [True]
        for i in range(1, len(s) + 1):
            li = []
            for j in range(i):
                li += [ok[j] and s[j:i] in wordDict]
            li2 = [any(li)]
            ok += li2
        print(ok)
        return ok[-1]

# TC: O(N^2)  SC: O(N)
def word_break(s, word_dict):
    """
    :type s: str
    :type word_dict: Set[str]
    :rtype: bool
    """
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(0, i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[-1]


s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))

# -----------------
[True, False, False, False, True, False, False, False, True]
True
