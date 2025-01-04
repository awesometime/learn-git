"""
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
"""
// 题 76 567 438

// 注意哦，输入的 s1 是可以包含重复字符的，所以这个题难度不小

// 对于这道题的解法代码，基本上和最小覆盖子串一模一样，只需要改变几个地方：
//1、本题移动 left 缩小窗口的时机是窗口大小大于 s1.size() 时，因为排列嘛，显然长度应该是一样的。
//2、当发现 valid == need.size() 时，就说明窗口中就是一个合法的排列，所以立即返回 true。
//至于如何处理窗口的扩大和缩小，和最小覆盖子串完全相同。


// windows 控制长度
// need 控制每个字符的数量
func findAnagrams(s string, p string) []int {
    need, windows := make(map[byte]int), make(map[byte]int)
	slength := len(s)

	for i := range p {
		need[p[i]]++
	}

	left, right := 0, 0
	valid := 0
    var res []int
	for right < slength {
		c := s[right]
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
		for right - left >= len(p) {
            // 在这里判断是否找到了符合条件的子串
			if valid == len(need) {
				res = append(res, left)
			}
			f := s[left]
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

	return res
}

func findAnagrams2(s string, p string) []int {
    need, windows := map[byte]int{}, map[byte]int{}
	for _, va := range p {
		need[byte(va)]++
	}
	// fmt.Println(need)

	valid := 0
	left, right := -1, 0
	var res []int
	for right < len(s) {
		char := s[right]
		right++
		if _, ok := need[char]; ok {
			windows[char]++
			if need[char] == windows[char] {
				valid++
			}
		}

		for valid == len(need) {
			// 更新
			left++
			// left加1, 计算right-left位数是否等于s1位数
			if right-left == len(p) { // right 索引已经到了eidbao,left也加1了
				res = append(res, left)
			}
			charLeft := s[left]
			if _, ok := need[charLeft]; ok {
				windows[charLeft]--
				if windows[charLeft] < need[charLeft] {
					valid--
				}
			}

		}
	}
	return res
}