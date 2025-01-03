[树  Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide/blob/master/docs/dataStructures-algorithms/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.md#%E6%A0%91)

## 树
  * ### 1 二叉树
  
     [二叉树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%A0%91)（百度百科）

    (1)[完全二叉树](https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91)——若设二叉树的高度为h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第h层有叶子结点，并且叶子结点都是从左到右依次排布，这就是完全二叉树。
    
    (2)[满二叉树](https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91)——除了叶结点外每一个结点都有左右子叶且叶子结点都处在最底层的二叉树。
    
    (3)[平衡二叉树](https://baike.baidu.com/item/%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91/10421057)——平衡二叉树又被称为AVL树（区别于AVL算法），它是一棵二叉排序树，且具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。 

  * ### 2 完全二叉树

    [完全二叉树](https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91)（百度百科）
    
    完全二叉树：叶节点只能出现在最下层和次下层，并且最下面一层的结点都集中在该层最左边的若干位置的二叉树。
  * ### 3 满二叉树
    
     [满二叉树](https://baike.baidu.com/item/%E6%BB%A1%E4%BA%8C%E5%8F%89%E6%A0%91)（百度百科，国内外的定义不同）

     国内教程定义：一个二叉树，如果每一个层的结点数都达到最大值，则这个二叉树就是满二叉树。也就是说，如果一个二叉树的层数为K，且结点总数是(2^k) -1 ，则它就是满二叉树。
  * ### 堆
  
     [数据结构之堆的定义](https://blog.csdn.net/qq_33186366/article/details/51876191)

    堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。
  *  ### 4 二叉查找树（BST）    树 值大小关系
    
     [浅谈算法和数据结构: 七 二叉查找树](http://www.cnblogs.com/yangecnu/p/Introduce-Binary-Search-Tree.html)

      二叉查找树的特点：

      1. 若任意节点的左子树不空，则左子树上所有结点的     值均小于它的根结点的值；
      2. 若任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
      3. 任意节点的左、右子树也分别为二叉查找树；
      4. 没有键值相等的节点（no duplicate nodes）。

  *  ### 5 平衡二叉树（Self-balancing binary search tree）   树结构
  
     [ 平衡二叉树](https://baike.baidu.com/item/%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91)（百度百科，平衡二叉树的常用实现方法有红黑树、AVL、替罪羊树、Treap、伸展树等）
  * ### 6 红黑树
    
     - 红黑树特点:
    1. 每个节点非红即黑；
    2. 根节点总是黑色的；
    3. 每个叶子节点都是黑色的空节点（NIL节点）；
    4. 如果节点是红色的，则它的子节点必须是黑色的（反之不一定）；
    5. 从根节点到叶节点或空子节点的每条路径，必须包含相同数目的黑色节点（即相同的黑色高度）。
    
     - 红黑树的应用：
    
         TreeMap、TreeSet以及JDK1.8之后的HashMap底层都用到了红黑树。
    
     - 为什么要用红黑树
    
       简单来说红黑树就是为了解决二叉查找树的缺陷，因为二叉查找树在某些情况下会退化成一个线性结构。详细了解可以查看 [漫画：什么是红黑树？](https://juejin.im/post/5a27c6946fb9a04509096248#comment)（也介绍到了二叉查找树，非常推荐）
    
     - 推荐文章： 
       -  [漫画：什么是红黑树？](https://juejin.im/post/5a27c6946fb9a04509096248#comment)（也介绍到了二叉查找树，非常推荐）
       -  [寻找红黑树的操作手册](http://dandanlove.com/2018/03/18/red-black-tree/)（文章排版以及思路真的不错）
       -  [红黑树深入剖析及Java实现](https://zhuanlan.zhihu.com/p/24367771)（美团点评技术团队）    
  *  ### 7 B-，B+，B*树
  
      [二叉树学习笔记之B树、B+树、B*树 ](https://yq.aliyun.com/articles/38345)

      [《B-树，B+树，B*树详解》](https://blog.csdn.net/aqzwss/article/details/53074186)

      [《B-树，B+树与B*树的优缺点比较》](https://blog.csdn.net/bigtree_3721/article/details/73632405)
        
     B-树（或B树）是一种平衡的多路查找（又称排序）树，在文件系统中有所应用。主要用作文件的索引。其中的B就表示平衡(Balance) 
    1. B+ 树的叶子节点链表结构相比于 B- 树便于扫库，和范围检索。
    2. B+树支持range-query（区间查询）非常方便，而B树不支持。这是数据库选用B+树的最主要原因。
    3. B\*树 是B+树的变体，B\*树分配新结点的概率比B+树要低，空间使用率更高；
  *  ### 8 LSM 树
    
     [[HBase] LSM树 VS B+树](https://blog.csdn.net/dbanote/article/details/8897599)
     
     B+树最大的性能问题是会产生大量的随机IO

     为了克服B+树的弱点，HBase引入了LSM树的概念，即Log-Structured Merge-Trees。
        
     [LSM树由来、设计思想以及应用到HBase的索引](http://www.cnblogs.com/yanghuahui/p/3483754.html)

