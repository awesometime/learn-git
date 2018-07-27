

```python
import pandas as pd
# DataFrame格式


# 将csv文件转化成DataFrame格式
foo_info = pd.read_csv('test.csv')
foo_info.head()
foo_info.tail()
foo_info.columns
col_name = foo_info.columns.tolist()
col_name.endwith('string')

foo_info.shape
foo_info.loc[3]  # 定位到某行
foo_info.loc[3：6]
foo_info['name_of_columns']
foo_info['name_of_columns']/100

# 以某列为基准降序排序,并新建一列
col_name = foo_info.columns.tolist()
foo_info.sort_values('name_of_columns', inplace=True， ascending=False)


# NaN   not a number
# 缺失值
age = foo_info['Age']
age_of_front_10 = age.loc[0:10]
age_is_null = pd.isnull(age) # boolean类型


# 求均值
good_ages = foo_info['Age'][age_is_null == False]
mean_age = sum(good_ages) / len(good_ages)


mean_age = foo_info['Age'].mean()
a = foo_info.pivot_table(index='xxx', values='xxx', aggfunc=np.mean)
b = foo_info.dropna(axis=1, subset=['Age', 'Sex'])


# 排序后重新排index
foo_info.sort_values('name_of_columns', inplace=True， ascending=False)
foo_info_reindexed = foo_info.reset_index(drop=True)


# apply函数
```


```python
import pandas as pd
# Series格式：DataFrame的子结构，相当于DataFrame的列                相当于 numpy 的 ndarray


```
