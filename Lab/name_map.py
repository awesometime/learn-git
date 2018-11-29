#!/usr/bin/env python
# coding: utf-8

# In[65]:


import pandas as pd
import os
#os.path.abspath(__file__)
os.getcwd()


# In[66]:


# 需要有 xlrd 包
excel_path = ('D:\\date analysis\\cols_map.xlsx')
df = pd.read_excel(excel_path)
df


# In[67]:


df.info()


# In[75]:


df_field_name = df.ix[0:194,[1,4]].dropna(axis=0, how='all')
df_field_name


# In[76]:


#df_field_name[:,[0]]
# field_name_dict = dict(zip(df_field_name[0],df_field_name[1]))
# field_name_dict
map_dict = df_field_name.to_dict('index')
map_dict


# In[77]:


list1= []
list2= []
for value in map_dict:
    list1.append(map_dict[value]['字段名'])
    list2.append(map_dict[value]['CIP数据字典定义'])
print(list1)
#list2
# name_dict=dict(zip(list1,list2))
# print(name_dict)
# print(list1)
print(list2)    
    # print(map_dict[value]['字段名'])


# In[78]:


zipped = zip(list1,list2)     # zip 会去重 
zipped
# name_dict=dict(zip(list1,list2))
# print(name_dict)


# In[79]:


# dict(zipped)  ??????   


# In[ ]:




