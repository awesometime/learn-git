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
### 
[Keras学习笔记(完结)](https://www.cnblogs.com/limitlessun/p/9296614.html#_label0)
```
阅读目录

基本概念
序贯(Sequential)模型
函数式(Functional)模型
常用层Core
卷积层Convolutional
池化层Pooling
局部连接层LocallyConnceted
循环层Recurrent
嵌入层Embedding
融合层Merge
高级激活层Advanced Activation
规范层BatchNormalization
噪声层Noise:
包装器Wrapper:
编写自己的层:
序列预处理:
文本预处理:
图片预处理:
损失函数Loss:
 优化器Optimizer
激活函数Activation
性能评估Metrices
初始化方法Initializers
正则化Regularizer
约束项Constraint
回调函数Callback
预训练模型Application
常用数据库
模型可视化
工具utils
使用Keras中文文档学习

回到顶部
基本概念

Keras的核心数据结构是模型,也就是一种组织网络层的方式,最主要的是序贯模型(Sequential).创建好一个模型后就可以用add()向里面添加层.模型搭建完毕后需要使用complie()来编译模型,之后就可以开始训练和预测了(类似于sklearn).
Sequential其实是模型的一种特殊情况,单输入单输出,层与层之间只有相邻关系.而通用的模型被称为函数式模型(function model API),支持多输入多输出,层与层之间可以任意相连.
Keras的底层库是Theano或TensorFlow,它们是符号式的库,也就是首先定义各种变量,然后建立一个规定各个变量之间计算关系的计算图,最后再把运算的输入放进去形成数据流从而输出.
张量(tensor)是向量或矩阵的自然推广,也就是数字的多阶排列.张量的阶数也称为维度或者轴(axis).
深度学习的优化算法一般是梯度下降,一般采用的是小批量梯度下降(mini-batch gradient decent),需要把数据分为若干批,按批来更新参数.Keras中的batch指的就是这个批,每个batch对应网络的一次更新.
epochs指的就是所有批次的单次训练迭代,也就是总数据的训练次数.每个epoch对应网络的一轮更新.
model.save(filepath)可以保存模型及权重,配置信息在一个HDF5文件中,models.load_model(filepath)可以重新实例化模型.
回到顶部
序贯(Sequential)模型

可以通过向Sequential传递一个layer的list来构造模型,也可以通过add将layer一个个加入模型.
Sequential的第一层需要接受一个关于输入数据shape的参数,后面的各个层可以自动推导出中间数据的shape.这个参数可以由input_shape(),input_dim(),input_length()等方法传递,还可以通过传递batch_size参数来指定一个固定大小的batch.注意,input_dim=x意味着传入一个x维向量,也就等同于一个一阶张量,即input_shape=(x,).
compile()用于编译模型,它接收三个参数:
优化器(optimizer):已预定义的优化器名或一个Optimizer类对象,模型采用的优化方式
损失函数(loss):已预定义的损失函数名或一个损失函数,模型试图最小化的目标函数
指标列表(metrics):已预定义指标的名字或用户定制的函数,用于评估模型性能
fit()用于训练模型,需要传入Numpy数组形式的输入数据和标签,可以指定epochs和batch_size等参数.
处理多分类问题时使用keras.utils.to_categorical()进行独热编码.
Sequential Model API
回到顶部
函数式(Functional)模型

只要模型不是一条路走到底的模型,或者模型需要多于一个的输出,那么都应该选择函数式模型.这是最广泛的一类模型.
层对象接受张量为参数,返回一个张量.输入和输出都是张量的一个框架就是一个模型,可以像Sequential一样被训练.
使用Model来初始化一个函数式模型,它需要一个或多个Input层作为输入,一个或多个层作为输出.常用的Model属性有layers,inputs,outpus.
所有的模型都是可调用的,就像层一样用一个张量来调用它.当调用一个模型时,它的结构和权重同时被重用了.
函数式模型的典型场景是多输入,多输出的模型:
根据层之间的关系建立不同的层
用layers.concatenate将不同层串联起来
用Model()中的inputs和outpus参数确定模型的输入与输出,这两个参数都是layer的list
用compile()编译模型
用fit()进行训练,x和y是对应输入和输出大小的数据的list
如果输入和输出是用name参数命名过的话,可以用名字与参数对应的字典来进行编译和训练.
函数式模型还可以用在使用共享层.当我们处理具有对称性的问题时需要对不同输入重复使用某一个模型,就可以让它们共享同一层.此时这个层拥有多个计算节点,所以需要使用layer.get_output_at(node_index)来得到对应节点的输出.
Functional Model API
回到顶部
常用层Core

Dense(全连接层):输入和输出都是n维张量.实现的运算是output=activation(dot(input,kernel)+bias).作为第一层时需要指定输出维度units和输入维度input_shape,后续层只用指定units即可.主要参数有激活函数activation以及对权值,偏置向量和输出的各种设置.
Activation(激活层):对一个层的输出施加激活函数,参数只有activation,作为第一层时要指定input_shape.
Dropout:在训练过程中每次更新参数时按一定概率随机断开输入神经元,用于防止过拟合.主要参数有断开比例rate.
Flatten:把多维的输入一维化,常用在从卷积层到全连接层的过渡,不会影响batch的大小.
Reshape:把输入shape转换为特定的shape,参数只有target_shape.当shape的其余维度确定后,可以用-1来指代剩下一个未确定的值.
Permute:将输入的维度按照规定模式进行重排,例如将RNN和CNN网络连接时.参数只有dims,用整数tupel指定了重排的模式.
RepeatVector:将输入重复n次,参数只有n.
Lambda:对上一层的输入施加任何Theano/TensorFlow表达式.主要参数有函数function和output_shape
AvtivityRegularizer:不会改变数据,但是会基于激活值更新损失函数值.参数有l1正则因子l1和l2正则因子l2
Masking:根据给定的值对输入的序列信号进行屏蔽.如果输入张量在某个时间步上都等于给定值,则该时间步将在模型接下来所有支持masking的层被屏蔽.参数只有mask_value.
回到顶部
卷积层Convolutional

1D一般指时域序列,2D一般指图像,3D一般指连续的图像序列.
Conv1D:一维卷积层(时域卷积),用于在一维输入信号上进行邻域滤波.
Conv2D:二维卷积层(图像的空域卷积),对二维输入进行滑动窗卷积.
SeparableConv2D:深度可分离卷积层.
Conv2DTranspose:进行转置的卷积操作(反卷积).
Conv3D:对三维输入进行滑动窗卷积,例如连续帧图像.
Cropping1D(2D/3D):在时间轴上对1D(2D/3D)输入进行裁剪,需要指定首尾裁掉多少个元素.
UpSampling1D(2D/3D):在时间轴(行和列/三个维度)上将每个时间步重复size次.
ZeroPadding1D(2D/3D):对1D(2D/3D)输入的首尾端填充0,以控制卷积以后向量的长度/特征图的大小.
回到顶部
池化层Pooling

MaxPooling1D(2D/3D):对时域1D(空域/3D)信号进行最大值池化.
AveragePoling1D(2D/3D):对时域1D(空域/3D)信号进行平均值池化.
GlobalMaxPooling1D/2D:对于时间/空域信号的全局最大池化.
GlobalAveragePooling1D/2D:为时域/空域信号施加全局平均值池化.
回到顶部
局部连接层LocallyConnceted

LocallyConnected1D/2D:与Conv1D/2D类似,区别是不进行权值共享.
回到顶部
循环层Recurrent

Recurrent:循环层的抽象类,所有的循环层(LSTM,GRU,SimpleRNN)都继承本层.
SimpleRNN:全连接RNN,输出会被回馈到输入.
GRU:门控循环单元.
LSTM:长短期记忆模型.
ConvLSTM2D:输入变换和循环变换通过卷积实现的LSTM网络.
SimpleRNNCell:SimpleRNN的Cell类.
GRUCell:GRU的Cell类.
LSTMCell:LSTM的Cell类
StackedRNNCells:用于将多个recurrent cell包装起来,实现高效的stacked RNN.
CuDNNGRU:基于CuDNN的快速GRU实现,只能在GPU上运行.
CuDNNLSTM:基于CuDNN的快速LSTM实现,只能在GPU上运行.
回到顶部
嵌入层Embedding

Embedding:将正整数转换为具有固定大小的向量,只能作为第一个隐藏层,与词向量有关.
回到顶部
融合层Merge

提供了一系列用于融合两个层或张量的层对象和方法.
Add:接收一个列表张量并返回它们的和
SubStract:将两个输入的层相减
Multiply/Average/Maximum/Concatenate:接收一个列表的同shape张量并返回它们的逐元素积/逐元素均值/逐元素最大值/按照给定轴相接构成的张量,shape不变
Dot:计算两个张量中样本的张量成绩.
add/substract/multiply/average/maximum/concatenate/dot:上述层的函数式包装
回到顶部
高级激活层Advanced Activation

LeakyReLU:是ReLU的特殊版本,当不可激活时仍会有非零输出值,从而获得一个小梯度.
PReLU:参数化的ReLU,f(x) = alpha * x for x < 0, f(x) = x for x>=0
ELU:指数线性单元,f(x) = alpha * (exp(x) - 1.) for x < 0, f(x) = x for x>=0
ThresholdedReLU:带有门限的ReLU,f(x) = x for x > theta,f(x) = 0 for x <= theta
回到顶部
规范层BatchNormalization

BatchNormalization:在每个batch上将前一层的激活值重新规范化,使得其输出数据的均值接近0,标准差接近1.
BN层的作用:
加速收敛
控制过拟合
降低网络对初始化权重不敏感
允许使用较大学习率
回到顶部
噪声层Noise:

GaussianNoise:为数据施加均值为0,标准差为参数的加性高斯噪声.在克服过拟合时比较有用,起正则化作用,只在训练时有效.
GaussianDropout:为数据施加均值为1,标准差为sqrt(rate/(1-rate))的乘性高斯噪声,同样起正则化作用,只在训练时有效.
AlphaDropout:为输入施加一种保持输入均值和方差不变的Dropout,与selu激活函数配合较好.
回到顶部
包装器Wrapper:

TimeDistributed包装器:把一个层应用到输入的每一个时间步上
Bidirectional包装器:双向RNN包装器
回到顶部
编写自己的层:

如果需要一个具有可训练权重的定制层,可以自己实现.一个定制层需要实现三个方法:
build(input_shape):定义权重的方法
call(x):定义层功能的方法
compute_output_shape(input_shape):指定shape变化的方法
回到顶部
序列预处理:

pad_sequences:填充序列,将标量序列转化为2D的numpy array.
skipgrams:跳字,将一个词向量下标的序列转化为一对tuple:对于正样本,转化为同一窗口中的序列,对于负样本,转化为随机的单词.
make_sampling_table:获取采样表,采样的结果为数据集中词的常见概率.
回到顶部
文本预处理:

text_to_word_sequence:句子分割,将一个句子拆分成单词构成的列表
one_hot:独热编码
hashing_trick:特征哈希,将文本转换为固定大小的哈希空间中的索引序列
Tokenizer:分词器,用于向量化文本或将文本转换为序列.
回到顶部
图片预处理:

ImageDataGenerator:图片生成器,用以生成一个batch的图像数据
回到顶部
损失函数Loss:

目标函数是编译模型必要的两个参数之一,可通过传递预定义目标函数名字指定目标函数,也可以传递一个符号函数作为目标函数.
可用的目标函数:
mean_squared_error(mse):均方误差
mean_absolute_error(mae):平均绝对误差
mean_absolute_percentage_error(mape):平均绝对百分误差
mean_squared_logarithmic_error(msle):平均对数平方误差
squared_hinge:平方铰链误差,主要用于SVM.
hinge:铰链误差,主要用于SVM.
categorical_hinge
binary_crossentropy（ogloss）:对数损失函数
logcosh:预测误差的双曲余弦函数的对数
categorical_crossentropy：多类的对数损失
sparse_categorical_crossentrop：接受稀疏标签的多类对数损失
kullback_leibler_divergence:相对熵,KL散度
poisson：(predictions - targets * log(predictions))的均值
cosine_proximity：预测误差的余弦距离平均值的相反数
回到顶部
 优化器Optimizer

优化器是编译模型必要的两个参数之一,可以初始化一个优化器对象传入,也可以传递一个预定义优化器名(参数将使用默认值).
可用的优化器:
SGD:随机梯度下降法
RMSprop:root mean square prop(均方根传播?),适用于递归神经网络.
Adagrad
Adadelta
Adam
Adamax
Nadam
TFOptimizer
回到顶部
激活函数Activation

激活函数可以通过设置单独的激活层实现,也可以在构造层对象时通过传递activation参数实现.
预定义激活函数:
softmax
elu
selu
softplus
softsign
relu
tanh
sigmoid
hard_sigmoid
linear
回到顶部
性能评估Metrices

性能评估类似于目标函数,只不过该性能的评估结果不会用于训练.在模型编译时由metrics设置.可以用预定义的函数,也可以自己定制.
预定义张量(参数均为y_ture,y_pred):
binary_accuracy:二分类问题的平均正确率
categorical_accuracy:多分类问题的平均正确率
sparese_categorical_accuracy:同上,适用于稀疏情况
top_k_categorical_accracy:top-k正确率
sparese_top_k_categorical_accuracy:同上,适用于稀疏情况
回到顶部
初始化方法Initializers

初始化方法定义了对keras层设置初始化权重的方法,一般由kernel_initializer和bias_initializer来指定.可以用预定义初始化器也可以自定义函数.
预定义初始化方法:
Zeros:全零初始化
Ones:全1初始化
Constant:初始化为一个固定值
RandomNormal:正态分布初始化
RandomUniform:均匀分布初始化
TruncatedNormal:截尾高斯分布初始化,是神经网络权重和滤波器的推荐初始化方法
VarianceScaling:可以根据参数distribution决定不同的初始化方式
Orthogonal:随机正交矩阵初始化
Identiy:单位矩阵初始化
lecun_uniform:LeCun均匀分布初始化
lecun_normal:LeCun正态分布初始化
glorot_normal:Glorot正态分布初始化
glorot_uniform:Glorot均匀分布初始化
he_normal:He正态分布初始化
he_uniform:He均匀分布初始化
回到顶部
正则化Regularizer

正则化为优化过程中层的参数或激活值添加惩罚项.
预定义正则项:
l1
l2
l1_l2
回到顶部
约束项Constraint

约束项在优化过程中为网络的参数施加约束
预定义约束项:
max_norm:最大模约束
non_neg:非负性约束
unit_norm:单位范数约束
min_max_norm:最小/最大范数约束
回到顶部
回调函数Callback

回调函数用于在训练的特定阶段来观察训练过程中网络内部的状态和统计信息.
BaseLogger:对每个epoch累加metrics指定的监视指标的epoch平均值
ProgbarLogger:将metrics指定的监视指标输出到标准输出上
History:会自动调用,即fit方法的返回值
ModelCheckpoing:将在每个epoch后保存到filepath
EarlyStopping:用于早停
RemoteMonitor:用于向服务器发送事件流
LearningRateScheduler:学习率调度器
TensorBoard:可视化展示器
ReduceLROnPlateau:当评价指标不再提升时减少学习率
CSVLogger:将epoch的训练结果保存在csv中
LambdaCallback:用于创建简单的callback类
回到顶部
预训练模型Application

Keras提供了带有预训练权重的Keras模型.
Xception
VGG16
VGG19
ResNet50
InceptionV3
InceptionResNetV2
MobileNet
回到顶部
常用数据库

CIFAR10小图片分类数据集
CIFAR100小图片分类数据库
IMDB影评倾向分类
路透社新闻主题分类
MNIST手写数字识别
Fashion-MNIST数据集
Boston房屋价格回归数据集
回到顶部
模型可视化

keras的utils库中的plot_model提供了模型可视化的方法
回到顶部
工具utils

CustomObjectScope:提供定制类的作用域
HDF5Matrix:使用HDF5数据集代替Numpy数组
Sequence:序列数据的基类
to_categorical:将类别向量映射为二值类别矩阵
normalize:对numpy数组规范化
custom_object_scope:提供定制类的作用域
get_custom_objets:检索全局定制类
convert_all_kernels_in_model:将模型中全部卷积核在theano和tensorflow中切换
plot_model:绘制模型结构图
serialize_keras_object:将keras对象序列化
deserialize_keras_object:从序列中恢复keras对象
get_file:从给定的URL中下载文件
multi_gpu_model:将模型在多个GPU上复制
```  
### Tokenizer 进行文本预处理

[Tokenizer 进行文本预处理 ](https://blog.csdn.net/edogawachia/article/details/79446354)
