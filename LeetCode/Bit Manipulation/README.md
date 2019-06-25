https://blog.csdn.net/weixin_40041218/article/details/88667215

[补码](https://blog.csdn.net/mengzhengjie/article/details/80611422)

[ 位运算的简单应用 ](https://blog.csdn.net/C20180630/article/details/57076374)

[ 位运算奇技淫巧 ](https://blog.csdn.net/deaidai/article/details/78167367)

https://blog.csdn.net/qq_21275321/article/details/83008810

[不用加减乘除做加法](https://github.com/awesometime/learn-git/blob/master/%E5%89%91%E6%8C%87Offer/48-%E4%B8%8D%E7%94%A8%E5%8A%A0%E5%87%8F%E4%B9%98%E9%99%A4%E5%81%9A%E5%8A%A0%E6%B3%95.md)

[深度剖析凭什么python中整型不会溢出](https://segmentfault.com/a/1190000015284473)

> 二进制中1的个数：

注意到每个非零整数n和n-1进行按位与运算，整数n的二进制数中最右边的1就会变成0，那么二进制数中的1的个数就会减少一个，因此可以利用一个循环，使得 n = n&(n-1) ，计算经过几次运算减少到0，就是有几个1。

> 判断一个数值是不是2得整数次方，如果是的话，这个数的二进制数中有且只有一个1，那么这个数n会有 n&(n-1) == 0。

> 求两个整数m和n需要改变m二进制中的多少位才能得到n，可以先做 m^n 的异或运算，然后求这个数中有多少个1。


不使用任何中间变量如何将a、b的值进行交换（三种方法）
https://blog.csdn.net/sugarbliss/article/details/80323604
