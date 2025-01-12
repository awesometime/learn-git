/*
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
*/

// 注意哦，输入的 s1 是可以包含重复字符的，所以这个题难度不小

// 对于这道题的解法代码，基本上和最小覆盖子串一模一样，只需要改变几个地方：
//1、本题移动 left 缩小窗口的时机是窗口大小大于 s1.size() 时，因为排列嘛，显然长度应该是一样的。
//2、当发现 valid == need.size() 时，就说明窗口中就是一个合法的排列，所以立即返回 true。
//至于如何处理窗口的扩大和缩小，和最小覆盖子串完全相同。


// windows 控制长度
// need 控制每个字符的数量
func checkInclusion(s1 string, s2 string) bool {
    need, windows := make(map[byte]int), make(map[byte]int)
	slength := len(s2)

	for i := range s1 {
		need[s1[i]]++
	}

	left, right := 0, 0
	valid := 0
	for right < slength {
		c := s2[right]
		right++
		//fmt.Println(right)

        // 进行窗口内数据的一系列更新
		windows[c]++
		if windows[c] == need[c] {
			valid++
		}

        // 进行窗口内数据的一系列更新
        // if _, ok := need[c]; ok {
        //     window[c]++
        //     if window[c] == need[c] {
        //         valid++
        //     }
        // }

		//fmt.Printf("left: %d, right: %d\n", left, right)
		//fmt.Printf("windows %+v\n", windows)
        // 判断左侧窗口是否要收缩
		for right - left >= len(s1) {
            // 在这里判断是否找到了符合条件的子串
			if valid == len(need) {
				return true
			}
			f := s2[left]
			left++

            // 进行窗口内数据的一系列更新
			if _, ok := need[f]; ok {
				if windows[f] == need[f] {
					// windows中某个字符可能出现多次
					// 只要windows中该字符数量>need中该字符数量
					// valid 不变
					// 如BECODEBA left从第一个B移动后valid仍然是3
					valid--
				}
				windows[f]--
			}
		}

	}

	return false
}

/*
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ''

        cnt = collections.Counter(t)    # 哈希表：记录需要匹配到的各个元素的数目
        need = len(t)                   # 记录需要匹配到的字符总数【need=0表示匹配到了】

        n = len(s)
        start, end = 0, -1          # 记录目标子串s[start, end]的起始和结尾
        min_len = n + 1             # 符合题意的最短子串长度【初始化为一个不可能的较大值】
        left = right = 0            # 滑动窗口的左右边界

        for right in range(n):

            # 窗口右边界右移一位
            ch = s[right]               # 窗口中新加入的字符
            if ch in cnt:               # 新加入的字符位于t中
                if cnt[ch] > 0:         # 对当前字符ch还有需求
                    need -= 1           # 此时新加入窗口中的ch对need有影响
                cnt[ch] -= 1

            # 窗口左边界持续右移
            while need == 0:            # need=0，当前窗口完全覆盖了t
                if right - left + 1 < min_len:      # 出现了更短的子串
                    min_len = right - left + 1
                    start, end = left, right

                ch = s[left]            # 窗口中要滑出的字符
                if ch in cnt:           # 刚滑出的字符位于t中
                    if cnt[ch] >= 0:    # 对当前字符ch还有需求，或刚好无需求(其实此时只有=0的情况)
                        need += 1       # 此时滑出窗口的ch会对need有影响
                    cnt[ch] += 1
                left += 1               # 窗口左边界+1

        return s[start: end+1]

作者：flix
链接：https://leetcode.cn/problems/permutation-in-string/solutions/1503493/by-flix-ix7f/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/


/*
# // 输入：s1 = "ab" s2 = "eidbaooo"
# // 输出：true
# // 解释：s2 包含 s1 的排列之一 ("ba").
#
s1 = "ab"
s2 = "eidbaooo"
def checkInclusion(s1: str, s2: str) -> bool:
    need = {}
    for i in set(s1):
        need[i] = s1.count(i)
    windows= {}


    valid = 0
    left, right = 0,0
    while right < len(s2):
        in_char = s2[right]
        right+=1
        if in_char in need:
            windows[in_char] = windows.get(in_char, 0) + 1
            if windows[in_char] == need[in_char]:
                valid += 1

        while right - left > len(s2):
            if valid == 0:
                return True

            out_char = s2[left]
            left+=1
            if out_char in need:
                if windows[out_char] == need[out_char]:
                    valid -= 1
                windows[out_char] = windows.get(out_char, 0) - 1

    return False
print(checkInclusion(s1, s2))
*/