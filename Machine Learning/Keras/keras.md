[Keras 中文文档](https://keras-cn.readthedocs.io/en/latest/)
[Keras 官方中文文档](https://keras.io/zh/)
###  ML概念
```
Batch Size：批尺寸。机器学习中参数更新的方法有三种：

（1）Batch Gradient Descent，批梯度下降，遍历全部数据集计算一次损失函数，进行一次参数更新，这样得到的方向能够更加准确的指向极值的方向，但是计算开销大，速度慢；

（2）Stochastic Gradient Descent，随机梯度下降，对每一个样本计算一次损失函数，进行一次参数更新，优点是速度快，缺点是方向波动大，忽东忽西，不能准确的指向极值的方向，有时甚至两次更新相互抵消；

（3）Mini-batch Gradient Decent，小批梯度下降，前面两种方法的折中，把样本数据分为若干批，分批来计算损失函数和更新参数，这样方向比较稳定，计算开销也相对较小。Batch Size就是每一批的样本数量。

Iteration：迭代，可以理解为w和b的一次更新，就是一次Iteration。

Epoch：样本中的所有样本数据被计算一次就叫做一个Epoch。
```
### Keras学习笔记
[Keras学习笔记(完结)](https://www.cnblogs.com/limitlessun/p/9296614.html#_label0)

### Tokenizer 进行文本预处理

[Tokenizer 进行文本预处理 ](https://blog.csdn.net/edogawachia/article/details/79446354)
