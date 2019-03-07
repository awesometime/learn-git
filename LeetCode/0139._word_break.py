def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    # ok = [True]
    # for i in range(1, len(s) + 1):
    #     ok += [any(ok[j] and s[j:i] in wordDict for j in range(i))]
    # print(ok)
    # return ok[-1]

    ok = [True]
    for i in range(1, len(s) + 1):
        li = []
        for j in range(i):
            li += [ok[j] and s[j:i] in wordDict]
        li2 = [any(li)]
        ok += li2
    print(ok)
    return ok[-1]


s = "leetcode"

wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))

# -----------------
[True, False, False, False, True, False, False, False, True]
True
