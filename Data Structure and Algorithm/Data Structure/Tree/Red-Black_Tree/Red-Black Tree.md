```
BST二叉搜索树

平衡
AVL平衡二叉搜索树   Red-Black Tree
```
Red-Black Tree is a self-balancing Binary Search Tree (BST) where every node follows following rules.

    1.节点是红色或黑色。

    2.根节点是黑色。

    3.每个叶子节点都是黑色的空节点（NIL节点）。

    4 每个红色节点的两个子节点都是黑色。(从每个叶子到根的所有路径上不能有两个连续的红色节点)

    5.从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点。  （保证了高度平衡）

# 红黑树 教科书 维基百科
```
1
https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/03.01.md

Left-Leaning Red-Black Trees, Dagstuhl Workshop on Data Structures, Wadern, Germany, February, 2008，
直接下载：http://www.cs.princeton.edu/~rs/talks/LLRB/RedBlack.pdf。

原文链接：https://blog.csdn.net/v_JULY_v/article/details/6105630

2 http://dandanlove.com/2018/03/18/red-black-tree/

3 程序员小黑 https://juejin.im/post/5a27c6946fb9a04509096248#comment
```
> 在二叉树基础上 调整建立 红黑树 

**变色、左旋、右旋**

- 我们插入黑色节点的时候担心违背第5条，插入红色节点时担心违背第4条，所以我们将将插入的节点改为【红色】，

  然后判断插入的节点的父亲是不是红色，是的话进行修改调整（变色、左旋、右旋）。同时在调整的过程中我们需要遵守5条特性。

> 插入
```
1、如果我们添加的【红色节点】的【父节点】是黑色，那么树不需要做调整。
2、如果我们添加的【红色节点】的【父节点】是红色，那么树需要做调整。
  2.1）、父节点是红色，叔叔节点（父节点的兄弟节点）是红色的。
  2.2）、父节点是红色，叔叔节点是黑色，添加的节点是父节点的左孩子。
  2.3）、父节点是红色，叔叔节点是黑色，添加的节点是父节点的右孩子。
```  
> 删除

```
1 如果要删除的节点正好是叶子节点，直接删除就 Ok 了；
2 如果要删除的节点还有子节点，就需要建立父节点和子节点的关系：
    2.1 如果只有左孩子或者右孩子，直接把这个孩子上移放到要删除的位置就好了；
    2.2 如果有两个孩子，就需要选一个合适的孩子节点作为新的根节点，该节点称为 继承节点。（新节点要求
        比所有左子树要大、比右子树要小，我们可以选择左子树中的最大节点，或者选择右子树中的最小的节点。）
```
  
  
  
  
  
  
  
  
  
红黑树与 平衡二叉查找树区别？ https://mp.weixin.qq.com/s/jz1ajDUygZ7sXLQFHyfjWA


