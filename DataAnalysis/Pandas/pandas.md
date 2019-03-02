```python
import pandas as pd
import numpy as np
path1 = "F:/200nodes/log_key_label_1119w.log"
path2 = "F:/200nodes/sorted_log_key_1119w.log"
path3 = "F:/200nodes/sorted_labelAndLogKey_1119w.log"
path4 = "F:/200nodes/sorted_labelAndLogKey_1119w_process.log"

# num_list = [0,1,2,3,4,5,6,7,8,9] num_list_new = [str(x) for x in num_list] print ",".join(num_list_new)
num_list = np.array(['1','3','4','5','6','8','9','12','13','15','16','18','19','21','22','23','26','27'])
#print(type(num_list))  # numpy.ndarray
def save():
    df1 = pd.read_csv(path1, header=None)
    df2 = pd.read_csv(path2, header=None)
    # 将两个文件(每个文件有一列 无列名)合并concat到一个文件
    df3 = pd.concat([df1, df2], axis=1)
    # 保存 成csv 用' '代替 ,  
    df3.to_csv(path3, sep=' ', index=False, header=False)
    # 添加列名
    df3.columns = ["label", "log_key"]
    
    # https://blog.csdn.net/luocheng7430/article/details/80330566
    # 删除/选取某列含有特殊数值的行    删除/选取某行含有特殊数值的列    删除含有空值的行或列
    for i in num_list:
        # ~取反  删除某列含有特殊数值的行
        df3 = df3[~df3['label'].isin([i])]
    # 删除 log_key 列含有特殊数值 PacketResponder  for block  terminating 的行
    df3 = df3[~df3['log_key'].isin(['PacketResponder  for block  terminating'])]
    df3 = df3[~df3['log_key'].isin(['Verification succeeded for '])]
    df3.to_csv(path4, sep=' ', index=False, header=False)
    print("ok :) ")

save()

```

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

