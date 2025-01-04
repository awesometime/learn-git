# https://blog.csdn.net/whuwangyi/article/details/42451289
# 159. Longest Substring with At Most Two Distinct Characters
import collections


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        lookup = collections.defaultdict(int)
        # loopup = {}
        # loopup[char] = loopup.get(char, 0) + 1
        l, r, counter, res = 0, 0, 0, 0
        while r < len(s):
            lookup[s[r]] += 1
            if lookup[s[r]] == 1:  # =1 说明出现了新的字符 counter+1
                counter += 1
            r += 1  # r 永远指向下一个待处理的字符

            # 内层循环维护 counter=2 ,及lookup中不为0的只有两种字符
            # 只要 counter>2 就会循环直到counter=2
            while l < r and counter > 2:
                lookup[s[l]] -= 1  # 每次将lookup[s[l]] -1
                if lookup[s[l]] == 0:  # 如果某个字符s[l]=0 说明这个字符消失了 counter-1
                    counter -= 1
                l += 1  # l右移

            # r-l维护一个区间长度,在这个区间内只有两种字符
            res = max(res, r - l)  # r 永远指向下一个待处理的字符,因此这里是r-l而不是r-l+1
            print(l, r, counter, res, lookup)
        return res


# s = "ecebeea"
# s = "cebeea"
s = "ceabeea"

print(Solution().lengthOfLongestSubstringTwoDistinct(s))


# 0 1 1 1 defaultdict(<class 'int'>, {'c': 1})
# 0 2 2 2 defaultdict(<class 'int'>, {'c': 1, 'e': 1})
# 1 3 2 2 defaultdict(<class 'int'>, {'c': 0, 'e': 1, 'a': 1})
# 2 4 2 2 defaultdict(<class 'int'>, {'c': 0, 'e': 0, 'a': 1, 'b': 1})
# 3 5 2 2 defaultdict(<class 'int'>, {'c': 0, 'e': 1, 'a': 0, 'b': 1})
# 3 6 2 3 defaultdict(<class 'int'>, {'c': 0, 'e': 2, 'a': 0, 'b': 1})
# 4 7 2 3 defaultdict(<class 'int'>, {'c': 0, 'e': 2, 'a': 1, 'b': 0})
# 3
