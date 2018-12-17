https://www.cnblogs.com/cnooye/p/5685670.html

### 三种格式化 format 和 %s 和 f"{}"
```python
temp = "Zc"
str3 = f"i am {'Zc'}"
str4 = f"i am {temp}"
print(str3)
print(str4)

i am Zc
i am Zc


```
### 进度条
```python
###############1
import time
import sys

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("%s%% |%-100s|" % (int(i % 101), int(i % 101) * '#'))
    sys.stdout.flush()
    time.sleep(0.5)
sys.stdout.write('\n')

>>>
100% |####################################################################################################|


###############2
import sys,time
for i in range(100):
    k = i + 1
    str = '>'*(i//5)+' '*((100-k)//5)    # > 和' ' 控制总共的长度  然后后面加 [  %]
    sys.stdout.write('\r'+str+'[{}%]'.format(i+1))    sys.stdout.flush()
    time.sleep(0.1)
sys.stdout.write('\n')

>>>
>>>>>>>>>>>>>>>>>>[100%]


###############3
import sys, time

total =5
for i in range(total):

    if i + 1 == total:
        percent = 100.0
        sys.stdout.write('\r'+'当前核算进度 : %s [%d/%d]' % (str(percent) + '%', i + 1, total))
        sys.stdout.flush()
    else:
        percent = round(1.0 * i / total * 100, 2)
        sys.stdout.write('\r'+'当前核算进度 : %s [%d/%d]' % (str(percent) + '%', i + 1, total))
        sys.stdout.flush()
    time.sleep(0.05)
    
>>>
当前核算进度 : 100.0% [5/5]
```
