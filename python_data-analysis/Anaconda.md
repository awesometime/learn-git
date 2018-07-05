###  Anaconda






















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

