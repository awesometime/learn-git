[知识清单](https://uule.iteye.com/blog/2429508)

[硬盘基本知识（磁头、磁道、扇区、柱面）](https://www.jianshu.com/p/9aa66f634ed6)

[从 MongoDB 及 Mysql 谈B/B+树 ](https://blog.csdn.net/wwh578867817/article/details/50493940)

[MySQL索引背后的数据结构及算法原理](http://blog.codinglabs.org/articles/theory-of-mysql-index.html)

[视频 ](https://www.youtube.com/watch?v=IcDMCoyPFG0)

```
B-树由来
平衡二叉树是通过旋转来保持平衡的，而旋转是对整棵树的操作，若部分加载到内存中则无法完成旋转操作。
其次平衡二叉树的高度相对较大为 log n（底数为2），这样逻辑上很近的节点实际可能非常远，无法很好的利用磁盘预读（局部性原理）
，所以这类平衡二叉树在数据库和文件系统上的选择就被 pass 了

B-树的 插入 和 删除 就不具体介绍了，很多资料都描述了这一过程。在普通平衡二叉树中，插入删除后若不满足平衡条件则进行 旋转 操作，
而在B-树中，插入删除后不满足条件则进行 分裂 及 合并 操作

-----------------------
B+树 
index_node
data_node
B+树内节点不存储数据，所有 data 存储在叶节点
导致查询时间复杂度固定为 log n。而B-树查询时间复杂度不固定，与 key 在树中的位置有关，最好为O(1)

-----------------------
增加 区间访问性，一般会对B+优化
```
