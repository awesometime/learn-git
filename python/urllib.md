
* [1 urllib.request](#1-urllib.request)
* [2 urllib.parse](#2-urllib.parse)
* [3 urllib.error](#3-urllib.error)
* []()
* []()





urllib.request

urllib.error

urllib.parse

urllib.robotparse


### 1 urllib.request
1 urllib.request.urlopen()
```python
response = urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

print(type(response))            # <class ’ http.client.HTTPResponse ’ >
# read （） 、readinto （）、getheader(name ）、getheaders （） 、fileno （）等方法
# msg 、version 、status 、reason 、debuglevel 、closed 等属性
response.read().decode('utf-8')
print(response .status)
print(response .getheaders())
print(response. getheader ('Server'))
# 200
# [('Server ', ’ nginx'), ('Content-Type ', ’text/html; charset=utf-8'), (’ X-Frame-Options ’,’ SAMEORIGIN'),
#  ( ’X-Clacks-Overhead t ,’GNU Terry Pratchett ’) , ('Content- Length ’ 3 ’47397 ' ), (’ Accept-Ranges ’, t bytes ’),
#  (’ Date', 'Mon, 01Aug201609:57:31GMT'), (’Via ’,’1.1 varnish ’），（『Age ’，’ 2473 『），（『Conn ect ion' ,’ close'),
#  (’ X-Served-By ’,’ cache-lcy112s-LCY ' ), (' X-Cache’,’ HIT'), (’ X-Cache-Hits ',’ 23')' (’ Vary ’,' Cookie' ),
#  ('Strict-Transport-Security', 'max-age=63072000; includeSubDomains')
# ]
# nginx

```


2 urllib.request.Request

```python
request = urllib.request.Request (url, data=None, headers={}, origin_req_host=None, unverifiable=False, method =None)
request.add_header()
response = urllib.request.urlopen(request)
print(response.read().decode(’utf-8'))
```


3 urllib.request.BaseHandler

```


```






### 2 urllib.parse

```python
urllib . parse . urlencode({'word ’:’ hello'})    # 将字典转化为字符串

data = bytes(urllib . parse . urlencode({'word ’:’ hello'}), encoding ＝’ utf-8')
# 转字节流采用了bytes （）方法
# 该方法的第一个参数需要是str （字符串）类型，需要用urllib.parse 模块里的urlencode （）方法来将参数字典转化为字符串；
# 第二个参数指定编码格式，这里指定为utf8

response= urllib.request.urlopen('http://httpbin.org/post ’, data=data)
# 添加该参数，必须传bytes（字节流）类型的,则它的请求方式是POST 方式。

```

### 3 urllib.error

```
urllib. error. URL Error: <Urlope n error timed out>







```
### 附
有些网站在打开时就会弹出提示框，直接提示你输入用户名和密码

build_opener(auth_handler).open(url)
