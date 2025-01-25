# 可以转化为斐波那契数列的方式进行求解，假设要跳N阶台阶，那么
# 第一步有两种跳法：
# （1）跳一步，后面还有n-1个台阶需要跳；
# （2）跳两步，后面还有n-2个台阶需要跳。
# 可以看到跳n阶台阶的跳法数等于跳n-1和n-2阶台阶数的和，即f(n) = f(n-1) + f(n-2)
def JumpSteps_digui(n):
    if n in (1, 2):
        return n
    return JumpSteps_digui(n-1)+JumpSteps_digui(n-2)

def JumpFloor(n):
    dp= [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 优化
def JumpFloor_new(n):
    if n in (1, 2):
        return n
    temp1, temp2 = 1, 2
    for i in range(2, n):
        temp = temp1 + temp2
        temp1, temp2 = temp2, temp
        i += 1
    return temp

print(JumpSteps_digui(7))
print(JumpFloor(7))
print(JumpFloor_new(7))
