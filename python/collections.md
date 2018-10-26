- [The Python Standard Library] (https://docs.python.org/3/library/index.html)
- [collections 文档中文](https://yiyibooks.cn/xx/python_352/library/collections.html)

» 8. Data Types 

» 8.3. collections — Container datatypes

### collections.namedtuple
» 8.3.5. namedtuple() Factory Function for Tuples with Named Fields

collections.namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)

```
from collections import namedtuple

# 返回一个名为"Skin"的元组子类，字段名为"id skin region x y"，相当于tuple(id， skin， region， x， y)
Skin = namedtuple("Skin", "id skin region x y")


s = Skin(199, 2, 4, 5, x=6)        # 实例化元组
for i in range(5):
    print(s[i])

结果输出
199
2
4
5
6
```
### collections.deque  双向队列
### collections.defaultdict
### collections.OrderedDict  有序字典
### collections.Counter  计数器
