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
