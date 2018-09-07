-[Django2.1 官方中文文档](https://docs.djangoproject.com/zh-hans/2.1/)

-[Django2.1 新手图文入门教程](http://www.liujiangblog.com/blog/36/)

-[Django-MySQL数据库使用](https://www.cnblogs.com/demo-deng/p/7801966.html)

### 写在前边

-[python web 框架](https://wiki.python.org/moin/WebFrameworks)

Django:    1个重武器，包含了web开发中常用的功能、组件的框架；（ORM、Session、Form、Admin、分页、中间件

、信号、缓存、ContenType....）；

Tornado:   2大特性就是异步非阻塞、原生支持WebSocket协议；

Flask：    功能和性能虽然不及Django和Tornado，但是Flask的第三方开源组件比丰富；http://flask.pocoo.org/extensions/

Bottle：   比较简单；

总结：

都不是我写的！！！不论优劣，不同的工具而已；

小型web应用设计的功能点不多使用Flask；

大型web应用设计的功能点比较多使用的组件也会比较多，使用Django（自带功能多不用去找插件）；

如果追求性能可以考虑Tornado；

### 一些思想

    django的设计专注于代码的高度可重用，信奉DRY原则，一切面向对象。

网站程序基本有三部分组成，业务逻辑代码(Python),静态文件(js/css),模板(Python中的 jinja,mako,nodejs

中有jade), 用户向webserver发起请求之后，server程序找到当前url对应的模板，填充模板变量(输出成字符串

形式的html源码),返回给浏览器，浏览器渲染页面。一般模板语言都有继承(extend),插入(include)等特性，

来提高页面的复用率。

　   django将页面上所有元素模块化，网页中一些常见元素，表单，表格，标签页，全部封装成Python类，
    
每个组件有自己对应的一小块html模板.当渲染整个页面的时候,Horizon先找到当前页面有多少组件，将各个

组件分别进行渲染变成一段html片段，最后拼装成一 个完整的html页面，返回浏览器。

## 1 顺序
```
G:\PyCharm\PythonProjects\Django> python manage.py runserver

$ python manage.py runserver          # 启动开发服务器
$ python manage.py startapp polls     # 创建投票应用(app)
$ models.py
$ views.py
$ urls.py
$ templates
$ settings.py

$ app_polls/admin.py文件，加入下面的内容：
from django.contrib import admin
from .models import Question

admin.site.register(Question) 
# 在admin中注册投票应用

$ python manage.py makemigrations app_polls      # 产生 migrations/0001_initial.py 文件
Migrations for 'app_polls':
  app_polls\migrations\0001_initial.py
    - Create model Choice
    - Create model Question
    - Add field question to choice
    
$ python manage.py migrate   
Operations to perform:
  Apply all migrations: admin, app1, app_polls, auth, contenttypes, sessions
Running migrations:
  Applying app_polls.0001_initial... OK
```
### Part 2：模型与管理后台------四、使用模型的API
```
G:\PyCharm\PythonProjects\Django>python manage.py shell
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from app1.models import UserInfo

In [2]: UserInfo.objects.all()
Out[2]: <QuerySet [<UserInfo: UserInfo object (1)>, <UserInfo: UserInfo object (2)>, <UserInfo: UserInfo object (3)>]>

In [3]:
```

### Part 2：模型与管理后台------五、admin后台管理站点
```
G:\PyCharm\PythonProjects\Django>python manage.py createsuperuser
Username: root
Email address: 243@qq
Password:1-6
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

### 编写你的第一个 Django 应用，第 5 部分
```
G:\PyCharm\PythonProjects\Django>py manage.py test polls

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "G:\PyCharm\PythonProjects\Django\polls\tests.py", line 18, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.080s

FAILED (failures=1)
Destroying test database for alias 'default'...


```

### python命令创建 模型对象
```
G:\PyCharm\PythonProjects\Django>python manage.py shell
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

>>> from polls.models import Question
>>> q = Question.objects.get(pk=1)
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Choice object>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: Choice object>
>>> q.choice_set.create(choice_text='Just hacking again', votes=0)
<Choice: Choice object>
```
## 项目

```
一、在 pycharm 中建立虚拟环境
结果是：
在目录中 G:\PyCharm\PythonProjects\python_virtualenv_for_django  隔离出最基本的 python 环境，和干净的基本没有第三方库在site-packages中。


二、安装django
cmd 下 在 G:\PyCharm\PythonProjects\python_virtualenv_for_django\Scripts 运行 activate 命令，激活该虚拟环境，
之后的命令行提示符将以(python_virtualenv_for_django)开头

(python_virtualenv_for_django) G:\PyCharm\PythonProjects\python_virtualenv_for_django\Scripts>pip install django
Collecting django
  Cache entry deserialization failed, entry ignored
  Downloading https://files.pythonhosted.org/packages/ca/7e/fc068d164b32552ae3a8f8d5d0280c083f2e8d553e71ecacc21927564561/Django-2.1.1-py3-none-any.whl (7.3MB)
    100% |████████████████████████████████| 7.3MB 80kB/s
Collecting pytz (from django)
  Cache entry deserialization failed, entry ignored
  Cache entry deserialization failed, entry ignored
  Downloading https://files.pythonhosted.org/packages/30/4e/27c34b62430286c6d59177a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl (510kB)
    100% |████████████████████████████████| 512kB 74kB/s
Installing collected packages: pytz, django
Successfully installed django-2.1.1 pytz-2018.5
You are using pip version 9.0.1, however version 18.0 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

退出虚拟环境，可以使用deactive命令


三、创建工程
进入Pycharm，File->new Project 创建 django 新工程，此时 create virtual env 也行
Location  G:\PyCharm\PythonProjects\mysite，与python解释器 G:\PyCharm\PythonProjects\python_virtualenv_for_django在
同级目录下
建好后会自动出现manage.py等django需要的包和环境

四、创建app
在cmd 终端需要 activate 

在pycharm 的终端里直接start app
(python_virtualenv_for_django) G:\PyCharm\PythonProjects\mysite>python manage.py startapp login


五、设置settings 时区 语言
六、启动一下开发服务器
设置127.0.0.1:8000 ，>>>py manage.py runserver 


```

问题解决

```
一、
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?

pycharm 安装 mysqlclient
报error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": 
http://landinghub.visualstudio.com/visual-cpp-build-tools

去官方下载 mysqlclient 相关文件，并自行百度下载后如何使其可用 
或者从系统python site-packages 包(前提是已经有mysqlclient包及相关py文件)中复制mysqlclient包及相关py文件到当前目录下

```

