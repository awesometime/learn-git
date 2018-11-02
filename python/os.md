```
>>> BASE_DIR = os.path.dirname(os.path.abspath('G:\\PyCharm\\PythonProjects\\Django\\static'))
>>> print(BASE_DIR)
G:\PyCharm\PythonProjects\Django

>>> BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('G:\\PyCharm\\PythonProjects\\Django\\static')))
>>> print(BASE_DIR)
G:\PyCharm\PythonProjects

>>> BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('G:\\PyCharm\\PythonProjects\\Django\\static'))))
>>> print(BASE_DIR)
G:\PyCharm
```
找路径下的文件  或以.py结尾的文件

```python

import os
root = "E:\\admin\\c0o3ao"

for dirpath, dirnames, filenames in os.walk(root):
    for filepath in filenames:
        print(os.path.join(dirpath, filepath))
```
