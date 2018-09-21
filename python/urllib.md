* [1 urllib.request](#1-urllib.request)
* [2 urllib.parse](#2-urllib.parse)
* [3 urllib.error](#3-urllib.error)
* [4 urllib.robotparse](#4-urllib.robotparse)
[]()





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

4 Opener

使用场景：一打开就需要用户名密码，后者需要使用代理时，Cookies
```python
build_opener(auth_handler).open(url)
proxy _handler = ProxyHandler({
                           'http ':'http://127.0.0.1:9743',
                           'https ':'https://127.0 .0.1:9743',
                             })
opener = build_opener(proxy_handler)
response = opener.open (’ https://www.baidu.com')

#将网站的Cookies 获取下来，相关代码如下：
import http .cookiejar, urllib.request
cookie = http. cookie jar. CookieJar()
handler = urllib . request.HTTPCookieProcesso r (cookie)
opener = urllib.request . build opener(handle r )
response = opener. open (’ http://www.baidu.com')
于or item in cookie:
print(item.name+”=”+i tem.value)
```



### 2 urllib.parse

1 urllib.parse.urlencode
```python
urllib.parse.urlencode({'word ’:’ hello'})    # 将字典转化为字符串

data = bytes(urllib.parse.urlencode({'word ’:’ hello'}), encoding ＝’ utf-8')
# 转字节流采用了bytes （）方法
# 该方法的第一个参数需要是str （字符串）类型，需要用urllib.parse 模块里的urlencode （）方法来将参数字典转化为字符串；
# 第二个参数指定编码格式，这里指定为utf8

response= urllib.request.urlopen('http://httpbin.org/post ’, data=data)
# 添加该参数，必须传bytes（字节流）类型的,则它的请求方式是POST 方式。
```

2 urllib.parse.urlparse
```python
result＝ urllib.parse.urlparse （urlstring, scheme =”, allow_fragments=True)
result＝ urllib.parse.urlparse （’ http://www.baidu . com/index .htr比u ser?id=S#comment ’）
print(type(result), result)
# <class ’ urllib.parse.ParseResult ’>
# ParseResult(scheme=’ http ’, netloc= p 刷w. baidu. com ', path=' /index. html ’, params='user', query='id=S',
# fragment='comment ' )  返回结果是一个ParseResult 类型的元组对象

```

3 urllib.parse.urlunparse()

URL 的构造

4 urllib.parse.urlsplit()

5 urllib.parse.urlunsplit()

6 urllib.parse.urljoin()

7 urllib.parse.parse_qs()

8 urllib.parse.parse_qsl()

9  quote

10 unquote

11 urllib.robotparser


### 3 urllib.error

```
e = urllib.error.URLError   #: <Urlope n error timed out>
e.reason                    # 属性
error. HTTPError       # 是URL Error 的子类
e.reason, e.code, e.headers   # 属性

因为URLError 是HTTP Error 的父类，所以可以先选择捕获子类的错误，再去捕获父类的错误，所
以上述代码更好的写法如下：
于rom urllib import request, error
try:
response = request.urlopen(’ https://cuiqingcai.com/index.htm ’)
except error.HTTPError as e:
print(e.reason, e.code, e.headers, sep=’\ n’)
exce pt error.URLError as e:
print(e . reason)
else:
print (’ Request Successfully')
这样就可以做到先捕获HTTP Error ，获取它的错误状态码、原因、h eaders 等信息。如果不是
HTTP Error 异常，就会捕获URLError 异常，输出错误原因。最后，用else 来处理正常的逻辑。这是一
个较好的异常处理写法。


```

### 4 urllib.robotparse

### 附
有些网站在打开时就会弹出提示框，直接提示你输入用户名和密码

build_opener(auth_handler).open(url)
