
ASCII编码
  |
  |
  |
GB2312(中文)编码  ...   各国自己的编码
  |
  |
  |
Unicode编码: 16位长度一样     【decode】其他格式编码 --> Unicode
  |
  |
  |
utf-8编码: 可变长            【encode】Unicode编码 --> utf-8

python3 默认均为Unicode编码
Windows 默认GB2312
Linux   默认utf-8

```python
import sys
sys.getdefaultencoding

# python 3 

s = '我用python'
# Windows下  gb2312 --> Unicode--> utf8
s.decode('gb2312').encode('utf8')

# Linux下  utf8 --> Unicode--> utf8
s.decode('utf8').encode('utf8')


# 直接encode 其实默认先调用decode
s.encode('utf8')
```
