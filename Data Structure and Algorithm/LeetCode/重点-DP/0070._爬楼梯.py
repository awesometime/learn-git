def climbStairs(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

def climbStairs(n):
    a = [1, 2]
    for i in range(2, n):
        a.append(a[i - 1] + a[i - 2])
    return a[n - 1]


# //go 递归
# func climbStairs(n int) int {
#     if n == 1 {
#         return 1
#     }
#     if n == 2 {
#         return 2
#     }
#     // 初始化两个变量表示到达前两个台阶的方法数
#     prev1, prev2 := 1, 2
#     for i := 3; i <= n; i++ {
#         cur := prev1 + prev2
#         prev1, prev2 = prev2, cur
#     }
#     return prev2
# }