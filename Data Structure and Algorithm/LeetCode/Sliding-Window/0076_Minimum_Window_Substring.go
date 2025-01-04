/*
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
 */


// 这个题难在细节处理上
func minWindow(s string, t string) string {
	need, windows := make(map[byte]int), make(map[byte]int)
	for i := range t {
		need[t[i]]++
	}

	left, right := 0, 0
	valid := 0
	start, reslen := 0, math.MaxInt32
    slength := len(s)
	for right < slength {
		c := s[right]
		right++
		//fmt.Println(right)
		windows[c]++
		if windows[c] == need[c] {
			valid++
		}

		//fmt.Printf("left: %d, right: %d\n", left, right)
		//fmt.Printf("windows %+v\n", windows)
		for valid == len(need) {
			if right-left < reslen {
				start = left
				reslen = right - left
			}
			//start = left // 这个不对 只有在reslen变化时才需要刷新start
			//reslen = min(reslen, right-left)
			//fmt.Printf("valid %d, left=%d, right=%d, res=%+v\n", valid, left, right, s[left:right])
			f := s[left]
			left++

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
		//fmt.Printf("left: %d, right: %d\n\n", left, right)

	}
	// 注意边界情况
	if left == 0 {
		return ""
	}
	// left已经+1了 不满足valid了
	// 满足valid的真正left需要-1
	return s[start : start+reslen]
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

func minWindow2(s string, t string) string {
	need, windows := make(map[byte]int), make(map[byte]int)
	for i := range t {
		need[t[i]]++
	}

	left, right := 0, 0
	valid := 0
	start, reslen := 0, math.MaxInt32
    slength := len(s)
	for right < slength {
		c := s[right]
		right++
		//fmt.Println(right)
		windows[c]++
		if windows[c] == need[c] {
			valid++
		}

		//fmt.Printf("left: %d, right: %d\n", left, right)
		//fmt.Printf("windows %+v\n", windows)
		for valid == len(need) {
			if right-left < reslen {
				start = left
				reslen = right - left
			}
			//start = left
			//reslen = min(reslen, right-left)
			//fmt.Printf("valid %d, left=%d, right=%d, res=%+v\n", valid, left, right, s[left:right])
			f := s[left]
			left++

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
		//fmt.Printf("left: %d, right: %d\n\n", left, right)

	}
	// 注意边界情况
	if left == 0 {
		return ""
	}
	// left已经+1了 不满足valid了
	// 满足valid的真正left需要-1
	return s[start : start+reslen]
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}


func minWindow3(s string, t string) string {
	length := len(s)
	need, windows := map[byte]int{}, map[byte]int{}

	for i := range t {
		need[t[i]]++ // map[103:1 105:1 110:1 114:1 115:1 116:1]
	}
	valid := 0 // need 中每个元素数量满足后 valid +1

	left, right := -1, 0
	start, minLen := 0, math.MaxInt32
	for right < length {
		char := s[right]
		right++
		// 如果need 当前字符 更新window中该字符的次数
		// 更新valid
		if _, ok := need[char]; ok {
			windows[char]++
			if need[char] == windows[char] {
				valid++
			}
		}

		// 如果window中集齐了，收缩left，优化窗口
		for valid == len(need) {
			if right-left < minLen {
				start = left
				minLen = right - left
			}
			left++
			charD := s[left]
			if _, ok := need[charD]; ok {
				windows[charD]--
				if windows[charD] < need[charD] {
					valid--
				}
			}
		}

	}
	// 说明s中没有满足的子串
	if left == -1 {
		return ""
	}
	return s[start+1 : start+minLen]
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}