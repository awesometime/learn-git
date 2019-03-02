### 1

如果把网页比作一个人的话， HTML 相当于骨架， JavaScript 相当于肌肉， css 相当于皮肤，三者结合起来才能形成一个完善的网页

在HTML中，只需要用link 标签即可引人写好的css 文件

JavaScript 通常也是以单独的文件形式加载的，后缀为js ，在HTML 中通过script 标签即可引人

HTML 定义了网页的内容和结构， css 描述了网页的布局， JavaScript 定义了网页的行为。


### 2 css 选择器

1 id

div 节点的id 为conta in er ，那么就可以表示为＃ co ntainer ，其中＃开头代表选择id ，其后紧跟id 的名称

2 class

选择class为wrapper 的节点，便可以使用.wrapper ，这里以点（．）开头代表选择class ，其后紧跟class 的名称

3 根据标签名筛选

例如想选择二级标题，直接用h2 即可

### 3

如何采集JavaScrip t 渲染的网页

可以分析其后台Ajax 接口，也可使用Selenium 、Splash 这样的库来实现模拟JavaScript 渲染。


### 4 保持HTTP 连接状态

会话和Cookies 

会话在服务端，也就是网站的服务器，用来保存用户的会话信息； Cookies 在客户端，也可以理解为浏览器端，有了

Cookies ，浏览器在下次访问网页时会自动附带上它发送给服务器，服务器通过识别Cookjes 并鉴定出

是哪个用户，然后再判断用户是否是登录状态，然后返回对应的响应。

爬虫中，有时候处理需要登录才能访问的页面时，我们一般会直接将登录成功后获取的

Cookies 放在请求头里面直接请求，而不必重新模拟登录。

### 代理

403 Forbidden ， 这时候打开网页一看，可能会看到“您的IP 访问频率太高”这
