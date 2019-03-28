https://zhuanlan.zhihu.com/p/58385984?utm_source=wechat_session&utm_medium=social&utm_oi=631526660110028800

[ 九大经典排序算法 知乎 动画 ](https://zhuanlan.zhihu.com/p/52884590?utm_source=wechat_session&utm_medium=social&utm_oi=631526660110028800)

[ 十大排序讲解 微信 动画](https://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652080829&idx=2&sn=93e06fa9ebce06d86d617931a0399a89&chksm=f1748158c603084e07945e4583bba798c71c3fa1481ae32c6915f1fe57807c5c6c57ae5b3d3a&mpshare=1&scene=1&srcid=&pass_ticket=aLYvowPftZdxv0ID6JVJgjpNRL9Tvs5KIwUlWwzj6h%2FJPCVAhZBzpnwqCcQEYlLW#rd)

[十大经典排序算法动画与解析 微信](https://mp.weixin.qq.com/s/vn3KiV-ez79FmbZ36SX9lg)

[其他排序1 https://github.com/keon/algorithms/tree/master/algorithms/sort ](https://github.com/keon/algorithms/tree/master/algorithms/sort)

[其他排序2 https://github.com/TheAlgorithms/Python/tree/master/sorts](https://github.com/TheAlgorithms/Python/tree/master/sorts)

###  O()  O() 对比

- `选择排序` : 一次loop最小的到了最左边

- `插入排序` : 原理:对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入    注意 变量currentvalue

- `冒泡排序` : 一次loop最大的到了最右边

   - 非优化版本

   - 优化版本 : 加 flag 提前停止

- `希尔排序` : 实质是**分组插入排序**

- `归并排序` ：

   - 递归式归并排序

   - 非递归式归并排序

- `快速排序` : 一次排完以后**pivot**处于正确位置 而且pivot左边的都比pivot小 右边的都比pivot大

- `堆排序` ：堆排序**构建堆**的时间复杂度是N,而**重调堆**的时间复杂度是logN

- `计数排序` ：

   - 非优化版本

   - 优化版本 ： 针对负数 和非从0开始的时候   max-min 索引从0开始

- `桶排序` : 桶内会用到**插入排序**

- `基数排序` ：


### 适用情况

只需记住一句话（快些选一堆美女一起玩儿）是不稳定的，其他都是稳定的

不同情况下的合适排序方法

初始数据越无序，快速排序越好。

已经基本有序时，用直接插入排序最快。

在随机情况下，快速排序是最佳选择。

既要节省空间，又要有较快的排序速度，堆排序是最佳选择，其不足之处是建堆时需要消耗较多时间。

若希望排序是稳定的，且有较快的排序速度，则可选用2路归并排序，其缺点需要较大的辅助空间分配。
