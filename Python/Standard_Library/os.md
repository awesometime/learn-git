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
root = "E:\\强力Django 和杀手级xadmin\\c0o3ao"

for dirpath, dirnames, filenames in os.walk(root):
	for filepath in filenames:
		if os.path.splitext(filepath)[1]=='.py':
			print(os.path.join(dirpath, filepath))


In [83]: import os

In [84]: help(os.path.splitext)
Help on function splitext in module ntpath:

splitext(p)
    Split the extension from a pathname.

    Extension is everything from the last dot to the end, ignoring
    leading dots.  Returns "(root, ext)"; ext may be empty.
