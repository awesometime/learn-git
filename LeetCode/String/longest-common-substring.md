动态规划

[最长公共子串  子序列 动态规划 有图 有代码](https://www.cnblogs.com/yuling-chao/p/7383096.html?utm_source=itdadao&utm_medium=referral):最后用回溯法将子串子序列打印出来

[最长公共子序列与最长公共子串](https://github.com/AngelKitty/Algorithm/blob/master/docs/Dynamic-programming/README.md#3%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97%E4%B8%8E%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E4%B8%B2)

暴力解法：

假设 m<n ， 对于母串 X ，我们可以暴力找出 2的m次方 个子序列，然后依次在母串 Y 中匹配，算法的时间复杂度会达到指数级 O(n∗2m) 。显然，暴力求解不太适用于此类问题

动态规划
假设 Z=<z1,z2,⋯,zk> 是 X 与 Y 的 LCS ， 我们观察到

如果 xm=yn ，则 zk=xm=yn ，有 Zk−1 是 Xm−1 与 Yn−1 的 LCS ；

如果 xm≠yn ，则 Zk 是 Xm 与 Yn−1 的 LCS ，或者是 Xm−1 与 Yn 的 LCS


![最长公共子串](https://github.com/AngelKitty/Algorithm/blob/master/docs/Dynamic-programming/figure/DP-solved-LCS-2.png)

![最长公共子序列](https://github.com/AngelKitty/Algorithm/raw/master/docs/Dynamic-programming/figure/DP-solved-LCS-1.png)

https://www.cnblogs.com/wangzaizhen/p/5168909.html

https://www.cnblogs.com/ider/p/longest-common-substring-problem-optimization.html
