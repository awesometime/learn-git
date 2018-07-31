import re
```
re.search
大小写敏感，返回第一个匹配到的位置
.  *                          出换行外任意字符
\d                            任意数字
[a-z]
ab{3}c  ab{3,10}c
[0-255]                       匹配0，1，2,5 ，[]括起来只表示一位，最大[0-9]没有[0-10][0-100]这些
[01]\d\d|2[0-4]\d|25[0-5]     0-255
([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5]\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])    192.168.1.1
(?:[01]?\d?\d|2[0-4]\d|25[0-5]\.){3}(?:[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])            192.168.1.1
(?表示正则表达式扩展语法    ?: 非捕获组           ?匹配0或1次
fish(c|d) 
(fish)\1
(fish)\060
(fish)\141
[^b]   查找除了b的元素          ^b 查找开头位置是否有b
$b     查找结束位置是否有b
()括起来视为子组
```
```
# match
# 匹配string 开头，成功返回Match object, 失败返回None，只匹配一个。

# search
# 在string中进行搜索找到第一次出现的，成功返回Match object, 失败返回None, 只匹配一个。

# findall
# 在string中查找所有 匹配成功的组, 即用括号括起来的部分。返回list对象，每个list item是由每个匹配的所有组组成的list。

# finditer
# 在string中查找所有 匹配成功的字符串, 返回iterator，每个item是一个Match object。

# group
# 是将所有匹配符合条件的字符串，打包成一个组，即group。
# 其中编号为0的group，即group(0)表示匹配的整个字符串。
# 其他编号分别为1,2,3，…的表示匹配成功返回的组中的每个字符串。
  [正则表达式中 group groups区别](https://www.cnblogs.com/zyy98877/p/8482371.html)
```

```
a = re.match('pw', 'pwkewkejht') # 匹配开头
aa = a.group()                   # 显示所有匹配部分
a1 = re.match('pw', 'pwkepwkejht')
aa1= a.groups()                  # 若果匹配规则为'()()()'三个子组，匹配上以后就会，显示三个部分，就会有group(0),group(1),group(2)
b = re.match('pwkewkejht', 'pw') # 第一个参数为标准模式

print(a)   #<_sre.SRE_Match object; span=(0, 2), match='pw'>
print(aa)  #pw   
print(a1)  #<_sre.SRE_Match object; span=(0, 2), match='pw'>
print(aa1) #()
print(b)   #None

c = re.search('pw', 'pwkepwkejht')
d = re.findall('pw', 'pwkepwkepwjht')
e = re.finditer('pw', 'pwkepwkepwjht')
print(c)          # <_sre.SRE_Match object; span=(0, 2), match='pw'>
print(d)          #['pw', 'pw', 'pw']

for result in e:
    print(result)
#<_sre.SRE_Match object; span=(0, 2), match='pw'>
#<_sre.SRE_Match object; span=(4, 6), match='pw'>
#<_sre.SRE_Match object; span=(8, 10), match='pw'>
```
