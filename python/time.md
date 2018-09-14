- [time模块详解](https://blog.csdn.net/you_are_my_dream/article/details/61616465)
```python
import time

print(time.time())
# 1536909646.688967


print(time.localtime()) 
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=14, 
#                  tm_hour=15, tm_min=17, tm_sec=57, 
#                  tm_wday=4, tm_yday=257, tm_isdst=0)


struct_time = time.strptime('2018-09-14 15:15:50', "%Y-%m-%d %H:%M:%S")
print(struct_time)
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=14, 
#                  tm_hour=15, tm_min=15, tm_sec=50, 
#                  tm_wday=4, tm_yday=257, tm_isdst=-1)


format_time = time.strftime("%Y-%m-%d %X", (2018,9,14,15,15,50,4,257,-1))  # strptime 逆操作
print(format_time)
# 2018-09-14 15:15:50


# 将一个struct_time元组转化为时间戳
timestamp1 = time.mktime(time.localtime())
print(timestamp1)
# 1536909477.0

timestamp2 = time.mktime((2018,9,14,15,15,50,4,257,-1))
print(timestamp2)
# 1536909350.0
```
