[Segment Tree 简介](http://wulc.me/2016/08/05/Segment%20Tree%20%E7%AE%80%E4%BB%8B/)

[https://github.com/keon/algorithms/blob/master/algorithms/tree/segment_tree/segment_tree.py](https://github.com/keon/algorithms/blob/master/algorithms/tree/segment_tree/segment_tree.py)

[https://blog.csdn.net/Yaokai_AssultMaster/article/details/79599809](https://blog.csdn.net/Yaokai_AssultMaster/article/details/79599809)

```
实现原理
从数据结构的角度来说，线段树是用一个完全二叉树来存储对应于其每一个区间（segment）的数据。该二叉树的每一个结点中保存着相对应于这一个区间的信息。同时，线段树所使用的这个二叉树是用一个数组保存的，与堆（Heap）的实现方式相同。

例如，给定一个长度为N的数组arr，其所对应的线段树T各个结点的含义如下： 
1. T的根结点代表整个数组所在的区间对应的信息，及arr[0:N]（不含N)所对应的信息。 
2. T的每一个叶结点存储对应于输入数组的每一个单个元素构成的区间arr[i]所对应的信息，此处0≤i<N。 
3. T的每一个中间结点存储对应于输入数组某一区间arr[i:j]对应的信息，此处0≤i<j<N。

以根结点为例，根结点代表arr[0:N]区间所对应的信息，接着根结点被分为两个子树，分别存储arr[0:(N-1)/2]及arr[(N-1)/2+1:N]两个子区间对应的信息。也就是说，对于每一个结点，其左右子结点分别存储母结点区间拆分为两半之后各自区间的信息。也就是说对于长度为N的输入数组，线段树的高度为logN。

对于一个线段树来说，其应该支持的两种操作为： 
1. Update：更新输入数组中的某一个元素并对线段树做相应的改变。 
2. Query：用来查询某一区间对应的信息（如最大值，最小值，区间和等）。

```
