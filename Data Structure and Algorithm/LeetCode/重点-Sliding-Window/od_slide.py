s1 = "ab"
s2 = "saaabcd"
k = 1

"""
https://labuladong.online/algo/essential-technique/sliding-window-framework/

最左侧冗余覆盖子串
举例：
s1 = “ab”
s2 = “aabcd”
k = 1
则子串 “aab” 和 “abc” 均满足此条件，由于 “aab” 在 “abc” 的左侧，“aab” 的第一个元素下部为 0，因此输出 0
s1 ab
s2 saaabcd
https://blog.csdn.net/CodeClimb/article/details/144537643
"""
def find_str_index():
    n1 = len(s1)
    n2 = len(s2)
    if n2 < n1 + int(k):
        return -1
    need = {char: s1.count(char) for char in set(s1)}
    #print(need) # {'c':3, 'b': 2, 'a': 1}
    # 这里need count 可以是负数
    # match_total 代表一共需匹配的字符总数 初始为len(s1)
    match_total = len(s1)

    """
    最左侧冗余覆盖子串
    s1 ab
    s2 saaabcd 
     index = 0 {'b': 1, 'a': 1} match_total 2 
     index = 1 {'b': 1, 'a': 0} match_total 2-> 1
     index = 2 {'b': 1, 'a': -1} match_total 1 
    """
    # 滑动窗口匹配
    # 初始化 先处理字符串s2的前n1+k个字符
    for index in range(n1 + int(k)):
        # 匹配到一个字符 这个字符的need数量减1
        if s2[index] in need:
            # 先判断   -1后need[s2[index]]已经变了再判断就不对
            if need[s2[index]] > 0:
                # 若need<=0 说明已经不需要了 找到也不能减match_total
                match_total -= 1
            need[s2[index]] -= 1
            print(need)
        if match_total == 0:
            return 0
          
    # 动态调整窗口
    for index in range(1, n2 - (n1 + int(k)) + 1):
        del_char = s2[index - 1]
        add_char = s2[index + n1 + int(k) - 1]
        print(index)
        print(s2[index:index + n1 + int(k)])
        if del_char in need:
            if need[del_char] >= 0:
                match_total += 1
            need[del_char] += 1
            print(need)
        if add_char in need:
            if need[add_char] >= 0:
                match_total -= 1
            need[add_char] -= 1
            print(need)
        if match_total == 0:
            return index
    return -1


print(find_str_index())
