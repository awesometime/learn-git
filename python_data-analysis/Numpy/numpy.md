- [清华大学 李金老师 Python笔记 《自学Python——编程基础、科学计算及数据分析》](https://github.com/lijin-THU/notes-python)
  
  [李金老师github.io](https://lijin-thu.github.io/)
- [人工智能 机器学习 深度学习 入门及进阶资料](Python入门网络爬虫之精华版)

<p align="center">
   <h2 align="center">学习笔记</h2>
   <br>
   <p align="center">03-numpy</p>   
</p>


<p align="center"> Numpy 基础 </p> 

```python
关于shape
a = np.array([ 0,  1,  2])
a.shape
(3,)
-----------------------------------------------
a = np.array([[ 0,  1,  2]])
a.shape
(1, 3)
-----------------------------------------------
a = np.array([[ 0] ,
             [ 1] , 
             [ 2]])
a.shape
(3, 1)
-----------------------------------------------
x = np.linspace(-.1,.1, 5)
x.shape
(21,)
x
array([ -0.1 , -0.05,  0.  ,  0.05,  0.1  ])
-----------------------------------------------
y = x[:, np.newaxis]    x 转换为列向量
y.shape
(21, 1)
y
array([[-0.1 ],
       [-0.05],
       [ 0.  ],
       [ 0.05],
       [ 0.1 ]])        
-----------------------------------------------
from numpy.random import rand
import numpy as np
# 每次运行代码时设置相同的seed，则每次生成的随机数也相同，如果不设置seed，则每次生成的随机数都会不一样
# 不使用seed
a = rand(5)
print('第一次列表a：',a)

# In[2]:

a = rand(5)
print('第二次列表a：',a)

# In[3]:

# 使用seed
np.random.seed(3)
b = rand(5)
print('第一次列表b：',b)

# In[4]:

np.random.seed(3)
b = rand(5)
print('第二次列表b：',b)
```

<p align="center"> array和asarray 区别 </p> 

```python
#array和asarray都可以将结构数据转化为ndarray，但是主要区别就是
#当数据源不是ndarray时，array  asarray 都会copy出一个副本，占用新的内存
#当数据源是ndarray时，array仍然会copy出一个副本，占用新的内存，但asarray不会复制副本

import numpy as np
 
#example 1:
data1=[[1,1,1],[1,1,1],[1,1,1]]  # list
arr2=np.array(data1)
arr3=np.asarray(data1)
data1[1][1]=2
print ('data1:\n',data1)
print 'arr2:\n',arr2
print 'arr3:\n',arr3

data1:
[[1, 1, 1], [1, 2, 1], [1, 1, 1]]
arr2:
[[1 1 1]
 [1 1 1]
 [1 1 1]]
arr3:
[[1 1 1]
 [1 1 1]
 [1 1 1]]
--------------------------------------

import numpy as np
 
#example 2:
arr1=np.ones((3,3))
arr2=np.array(arr1)
arr3=np.asarray(arr1)
arr1[1]=2
print 'arr1:\n',arr1
print 'arr2:\n',arr2
print 'arr3:\n',arr3

arr1:
[[ 1.  1.  1.]
 [ 2.  2.  2.]
 [ 1.  1.  1.]]
arr2:
[[ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]]
arr3:
[[ 1.  1.  1.]
 [ 2.  2.  2.]
 [ 1.  1.  1.]]
```




<p align="center"> 花式索引 </p> 
<p align="center"> https://github.com/lijin-THU/notes-python/blob/master/03-numpy/03.03-numpy-arrays.ipynb</p>

```python
arr=np.arange(32).reshape((8,4))
print(arr)

#以特定顺序选取子集,这里选取的就是第5，4,1,7行的子数组
print(arr[[4,3,0,6]])

#如果我们使用负数索引，则选取的从末尾开始-1为最后一行,-2为倒数第二行
print(arr[[-1,-2]])

#这里输出的分别是arr第5行的第一个数，第4行的第2个数，第1行的第3个数和第7行的第4个数组成的数组
print(arr[[4,3,0,6],[0,1,2,3]])

#这里输出分别为arr第5，4,1,7行的第1，2，3个数组成的数组
#[[16 17 18] [12 13 14] [ 0  1  2] [24 25 26]]
print(arr[[4,3,0,6]][:,[0,1,2]])

```
<p align="center"> 03.17--choose 函数实现条件筛选 </p>  
    
```python
----------------------------------------------------------------
control = np.array([[1,0,1],
                    [2,1,0],
                    [1,2,2]])
np.choose(control, [10, 11, 12])
Out:
array([[11, 10, 11],
       [12, 11, 10],
       [11, 12, 12]])
在上面的例子中， [0,1,2] 分别对应 [10, 11, 12],相当于列表[10,11,12]的索引，
control相当于一个指示数组，将 0,1,2索引 指向的数字放到 数组对应位置，
意味着control中的数字不能超过0,1,2这个范围，因为他表示[10,11,12]的索引。

---------------------------------------------------------------------
事实上， choose 不仅仅能接受下标参数，还可以接受下标所在的位置：
i0 = np.array([[0,1,2],
               [3,4,5],
               [6,7,8]])
i2 = np.array([[20,21,22],
               [23,24,25],
               [26,27,28]])
control = np.array([[1,0,1],
                    [2,1,0],
                    [1,2,2]])

np.choose(control, [i0, 10, i2])
Out:
array([[10,  1, 10],
       [23, 10,  5],
       [10, 27, 28]])
这里，control 中0,1,2分别对应i0,10,i2,第一次映射完是
[[10,i0,10],
 [i2,10,i0],
 [10,i2,i2]])
然后在将i0，i2换成原来数组相应位置的值。

--------------------------------------------------------------------
下面的例子将数组中所有小于 10 的值变成了 10。
a = np.array([[ 0, 1, 2], 
              [10,11,12], 
              [20,21,22]])
a < 10
Out:
array([[ True,  True,  True],
       [False, False, False],
       [False, False, False]], dtype=bool)

In [5]:
np.choose(a < 10, (a, 10))
Out[5]:
array([[10, 10, 10],
       [10, 11, 12],
       [20, 21, 22]])

array([[ True,  True,  True],                                                   array([[ 1,  1,  1],
       [False, False, False],                 <==choose （a<10）相当于==>               [ 0,  0,  0],
       [False, False, False]], dtype=bool)                                             [ 0,  0,  0]], dtype=bool)
0,1分别映射 a，10,  a代表对应位置a数组中的值

------------------------------------------------------------
下面的例子将数组中所有小于 10 的值变成了 10，大于 15 的值变成了 15。
a = np.array([[ 0, 1, 2], 
              [10,11,12], 
              [20,21,22]])

lt = a < 10
gt = a > 15

choice = lt + 2 * gt      //  a<10, true = 1,false = 0. 对于第一行[0,1,2],满足a<10,lt=1.不满足a>15，gt=0,算得choice=1
choice
Out[6]:
array([[1, 1, 1],
       [0, 0, 0],
       [2, 2, 2]])
In [7]:
np.choose(choice, (a, 10, 15))
Out[7]:
array([[10, 10, 10],
       [10, 11, 12],
       [15, 15, 15]])
choice算得 array([[1, 1, 1],
                  [0, 0, 0],
                  [2, 2, 2]])
以后 0,1,2 分别对应 a，10, 15
```

<p align="center">03.18--Numpy 数组广播机制</p>

```python
General Broadcasting Rules:
    对于 Numpy 来说，维度匹配当且仅当：
    - 维度相同
    - 有一个的维度是1
    匹配会从最后一维开始进行，直到某一个的维度全部匹配为止.
可以理解为：从末位开始一一(位置)对应匹配，维度1可以与任意维度数匹配到。如下
Image  (3d array): 256 x 256 x 3
Scale  (1d array):             3
Result (3d array): 256 x 256 x 3

A      (4d array):  8 x 1 x 6 x 1
B      (3d array):      7 x 1 x 5
Result (4d array):  8 x 7 x 6 x 5

A      (2d array):  5 x 4
B      (1d array):      1
Result (2d array):  5 x 4

A      (2d array):  5 x 4
B      (1d array):      4
Result (2d array):  5 x 4

A      (3d array):  15 x 3 x 5
B      (3d array):  15 x 1 x 5
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 5
Result (3d array):  15 x 3 x 5

A      (2d array):      2 x 1
B      (3d array):  8 x 4 x 3 # second from last dimensions mismatched #倒数第二个维度不兼容

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 1
Result (3d array):  15 x 3 x 5
```
<p align="center"> 结构化数组 </p>

我们使用 dtype 创造自定义的 结构类型 ，然后用自定义的结构来解释 数组 所占的内存。



