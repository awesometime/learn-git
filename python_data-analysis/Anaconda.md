###  1  Anaconda

- Anaconda Navigtor ：用于管理工具包和环境的图形用户界面，后续涉及的众多管理命令也可以在 Navigator 中手工实现。
- Jupyter notebook ：基于web的交互式计算环境，可以编辑易于人们阅读的文档，用于展示数据分析的过程。
- qtconsole ：一个可执行 IPython 的仿终端图形界面程序，相比 Python Shell 界面，qtconsole 可以直接显示代码生成的图形，实现
  多行代码输入执行，以及内置许多有用的功能和函数。
- spyder ：一个使用Python语言、跨平台的、科学运算集成开发环境。
```
在Anaconda Prompt中输入

(base) C:\Users\linuix> jupyter qtconsole
[TerminalIPythonApp] WARNING | Subcommand `ipython qtconsole` is deprecated and will be removed in future versions.
[TerminalIPythonApp] WARNING | You likely want to use `jupyter qtconsole` in the future
[JupyterQtConsoleApp] WARNING | kernel died: 3.0980682373046875

进入

Jupyter QtConsole 4.3.1
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

即可运行github李金老师的代码
```

 Ipython --> magic  ??? 怎么打开
 
from scipy.misc import lena  不能导入???
 
 [Jupyter Notebook 快速入门（上）](http://codingpy.com/article/getting-started-with-jupyter-notebook-part-1/)
 
 [最详尽使用指南：超快上手Jupyter Notebook](https://blog.csdn.net/DataCastle/article/details/78890469)
```
在完成Ananconda安装后，在cmd窗口中输入jupyter notebook，随即将会在默认浏览器中打开jupyter notebook主界面（建议将Chrome设置为默认浏览器）。

jupyter notebook  笔记本使用

在Files  -->  右上角New  -->  Notebook:Python3  就会进入一个Python的笔记本，在Files和Running中均可看到.ipynb的notebook文件

也可运行github李金老师的代码
```
```
In[1]: %%cmd
       pip install pygal         # jupyter notebook中pip的方法
 
      Microsoft Windows [版本 10.0.17134.165]
      (c) 2018 Microsoft Corporation。保留所有权利。

      (base) G:\Python\Jupyter Notebook>pip install pygal
      Collecting pygal
      Using cached         
      https://files.pythonhosted.org/packages/5f/b7/201c9254ac0d2b8ffa3bb2d528d23a4130876d9ba90bc28e99633f323f17/pygal-2.4.0-
      py2.py3-none-any.whl
      Installing collected packages: pygal
      Successfully installed pygal-2.4.0

      (base) G:\Python\Jupyter Notebook>
      distributed 1.21.8 requires msgpack, which is not installed.

In[2]: import pygal         # 可以导入
```
```
jupyter nbextensions
[jupyter_contrib_nbextensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions)
jupyter cell 重排序 ？？
jupyter 调整画出来的图的大小 ？？


```
### 2   Anaconda中模块的安装
```
在Anaconda Prompt中输入
(base) C:\Users\li>            anaconda search -t conda pygal

(base) C:\Users\li>            anaconda show Alges/pygal
To install this package with conda run:
     conda install --channel https://conda.anaconda.org/Alges pygal

(base) C:\Users\li>            conda install --channel https://conda.anaconda.org/Alges pygal

```

### 3

Ipython 提供了一个很好的解释器界面。

Matplotlib 提供了一个类似 Matlab 的画图工具。

Numpy 提供了 ndarray 对象，可以进行快速的向量化计算。

Scipy 是 Python 中进行科学计算的一个第三方库，以 Numpy 为基础。

Pandas 是处理时间序列数据的第三方库，提供一个类似 R 语言的环境。

StatsModels 是一个统计库，着重于统计模型。

Scikits 以 Scipy 为基础，提供如 scikits-learn 机器学习和scikits-image 图像处理等高级用法。











### 4  Jupyter notebook 单独安装(不基于Anaconda) 
>>>python -m pip install upgrade pip 

>>>pip install jupyter

>>>jupyter notebook   # 安装完打开notebook

安装好以后修改配置文件  C:\Users\linuix\.jupyter\jupyter_notebook_config.py  中大概第261行的

c.NotebookApp.notebook_dir = ' '   把路径改成自己的工作目录

c.NotebookApp.notebook_dir = 'G:\\Python\\JupyterNotebookDir'

或者在cmd窗口输入jupyter-notebook –generate-config会返回一个文件的路径，打开该文件，找到下面所示的代码,修改
```
## The directory to use for notebooks and kernels.
#c.NotebookApp.notebook_dir = u''
```
配置文件修改完成后， 以后在 jupyter notebook 中写的代码等都会保存在自己创建的目录中。

