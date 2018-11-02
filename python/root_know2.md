### 字典根据键从小到大排序
```
In [62]: dict = {'name':'hanmeimei', 'age':13, 'city':'chin', 'tel':138}

In [63]: print(dict.items())
dict_items([('name', 'hanmeimei'), ('age', 13), ('city', 'chin'), ('tel', 138)])

In [64]: list = sorted(dict.items(),key=lambda i:i[0],reverse=False)

In [65]: list
Out[65]: [('age', 13), ('city', 'chin'), ('name', 'hanmeimei'), ('tel', 138)]

In [70]: new_dict ={}

In [71]: for i in list:
    ...:     new_dict[i[0]] = i[1]

In [72]: new_dict
Out[72]: {'age': 13, 'city': 'chin', 'name': 'hanmeimei', 'tel': 138}
```
