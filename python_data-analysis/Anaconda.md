###  Anaconda

- Anaconda Navigtor ：用于管理工具包和环境的图形用户界面，后续涉及的众多管理命令也可以在 Navigator 中手工实现。
- Jupyter notebook ：基于web的交互式计算环境，可以编辑易于人们阅读的文档，用于展示数据分析的过程。
- qtconsole ：一个可执行 IPython 的仿终端图形界面程序，相比 Python Shell 界面，qtconsole 可以直接显示代码生成的图形，实现
  多行代码输入执行，以及内置许多有用的功能和函数。
- spyder ：一个使用Python语言、跨平台的、科学运算集成开发环境。

在Anaconda Prompt中输入
```
(base) C:\Users\linuix>ipython qtconsole
[TerminalIPythonApp] WARNING | Subcommand `ipython qtconsole` is deprecated and will be removed in future versions.
[TerminalIPythonApp] WARNING | You likely want to use `jupyter qtconsole` in the future
[JupyterQtConsoleApp] WARNING | kernel died: 3.0980682373046875
```
进入
```
Jupyter QtConsole 4.3.1
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.
```

 Ipython --> magic  ??? 怎么打开



















##### Jupyter notebook 安装 
>>>python -m pip install upgrade pip 

>>>pip3 install jupyter

报错tornado缺少  

>>>pip3 install tornado

>>>pip3 install jupyter  继续

安装好以后修改配置文件  C:\Users\linuix\.jupyter\jupyter_notebook_config.py  中大概第214行的

c.NotebookApp.notebook_dir = ' '   把路径改成自己的工作目录

c.NotebookApp.notebook_dir = 'G:\Python\Jupyter Notebook'

配置文件修改完成后， 以后在 jupyter notebook 中写的代码等都会保存在自己创建的目录中。

