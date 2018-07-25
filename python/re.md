import re

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
