[ Boyer-Moore 字符串匹配算法 ](https://www.cnblogs.com/gaochundong/p/boyer_moore_string_matching_algorithm.html)


### KMP

> [KMP youtube讲解](https://www.youtube.com/watch?v=GTJr8OvyEVQ)

> [阮一峰 字符串匹配的KMP算法 原理](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html)

> [KMP算法 python实现 leetcode 28题 ](https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0028._implement_strstr().md)

> [KMP算法 python实现 的本质原理是什么]()

> [KMP算法 python实现 2 多一种思路](https://www.cnblogs.com/zrdm/p/8590670.html)

```python3
# KMP算法
 
def Index_KMP(s1,s2,pos=0):
    next = get_next(s2)
    i = pos
    j = 0
    while(i < len(s1) and j < len(s2)):
        if(j == -1 or s1[i] == s2[j]):
            i += 1
            j += 1
        else:
            j = next[j]
 
    if(j >= len(s2)):
        return i - len(s2)
    else:
        return 0
 
def get_next(s2):
    i = 0
    next = [-1]
    j = -1
    while(i <len(s2)-1):
        if(j == -1 or s2[i] == s2[j]):
            i += 1
            j += 1
            next.append(j)
        else:
            j = next[j]
    return next
 
if __name__ == "__main__":
    s1 = "acabaabaabcacaabc"
    s2 = "abaabcac"
    print(Index_KMP(s1,s2))
```
