- [collections 文档](https://docs.python.org/3/library/collections.html)
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

[理解 Python 语言中的 defaultdict](http://kodango.com/understand-defaultdict-in-python)

### collections.OrderedDict  有序字典
### collections.Counter  计数器

```python
In [73]: from collections import Counter

In [74]: a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

In [76]: print(Counter(a))
Counter({'l': 9, ';': 6, 'h': 6, 'f': 5, 'a': 4, 'j': 3, 'd': 3, 's': 2, 'k': 1, 'g': 1, 'b': 1})
```
