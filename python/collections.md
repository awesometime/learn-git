[The Python Standard Library] (https://docs.python.org/3/library/index.html)

» 8. Data Types 

» 8.3. collections — Container datatypes

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
