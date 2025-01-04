/*
定长滑动窗口
简单

输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
*/

func findMaxAverage(nums []int, k int) float64 {
	k_total := 0
	sum := 0
	for _, v := range nums[:k] {
		sum += v
	}

	maxSum := sum
	// maxSum := math.MinInt64

	for i, v := range nums {
		// 入
		k_total += v
		// 初始化大小为k的窗口
		if i < k-1 {
			continue
		}
        // 更新结果
		maxSum = max(maxSum, k_total)
		// 出
		k_total -= nums[i-k+1]
	}

	return float64(maxSum) / float64(k)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/*
c++

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        double ans = INT_MIN, sum = 0;
        for (int right = 0; right < n; right++) {
            // 入
            sum += nums[right];
            // 初始化大小为k的窗口
            if (right < k - 1) continue;
            // 更新ans
            ans = max(ans, sum/k);
            // 出
            sum -= nums[right - k + 1];
        }
        return ans;
    }
};
*/
