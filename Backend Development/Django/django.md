### todo 

> django + [vue](https://vuejs.bootcss.com/) 前后端分离

> Django RESTful framework
  

目录

  * [1 django部署实践](#1-django部署实践)
      * [1.1 写在前边](#1.1-写在前边)
      * [1.2 一些思想](#1.2-一些思想)
      * [1.3 顺序](#1.3-顺序)
   * [2 django具体知识model](#2-django具体知识model)




-[Django2.1 官方中文文档](https://docs.djangoproject.com/zh-hans/2.1/)

-[Django2.1 新手图文入门教程](http://www.liujiangblog.com/blog/36/)

-[Django-MySQL数据库使用](https://www.cnblogs.com/demo-deng/p/7801966.html)

## 1 django部署实践

### 1.1 写在前边

- [python web 框架](https://wiki.python.org/moin/WebFrameworks)

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

### 1.2 一些思想

    django的设计专注于代码的高度可重用，信奉DRY原则，一切面向对象。

网站程序基本有三部分组成，业务逻辑代码(Python),静态文件(js/css),模板(Python中的 jinja,mako,nodejs

中有jade), 用户向webserver发起请求之后，server程序找到当前url对应的模板，填充模板变量(输出成字符串

形式的html源码),返回给浏览器，浏览器渲染页面。一般模板语言都有继承(extend),插入(include)等特性，

来提高页面的复用率。

　   django将页面上所有元素模块化，网页中一些常见元素，表单，表格，标签页，全部封装成Python类，
    
每个组件有自己对应的一小块html模板.当渲染整个页面的时候,Horizon先找到当前页面有多少组件，将各个

组件分别进行渲染变成一段html片段，最后拼装成一 个完整的html页面，返回浏览器。

### 1.3 顺序
```
G:\PyCharm\PythonProjects\Django> django-admin startproject project_name
G:\PyCharm\PythonProjects\Django> python manage.py runserver

$ python manage.py runserver          # 启动开发服务器
$ python manage.py startapp app_name     # 创建投票应用(app)
$ models.py
$ views.py
$ urls.py
$ templates

以上写好轮廓以后修改settings
$ settings.py
主要修改  INSTALLED_APPS   TEMPLATES_DIR  DATABASES

$ app_name/admin.py文件，加入下面的内容：
from django.contrib import admin
from .models import name_of_class_in_models

admin.site.register(name_of_class_in_models) 
# 在admin中注册投票应用

$ python manage.py makemigrations app_name      # 产生 migrations/0001_initial.py 文件
Migrations for 'app_name':
  app_name\migrations\0001_initial.py
    - Create model CPU
    - Create model Disk
    - Create model EventLog
    - Create model IDC
    - Create model Manufacturer
    - Create model NetworkDevice
    - Create model NewAssetApprovalZone
    - Create model NIC
    - Create model RAM
    - Create model SecurityDevice
    - Create model Server
    - Create model Software
    - Create model StorageDevice
    - Create model Tag
    - Add field new_asset to eventlog
    - Add field user to eventlog
    - Add field business_unit to asset
    - Add field contract to asset
    - Add field idc to asset
    - Add field manufacturer to asset
    - Add field tags to asset
    - Alter unique_together for ram (1 constraint(s))
    - Alter unique_together for nic (1 constraint(s))
    - Alter unique_together for disk (1 constraint(s))

    
$ python manage.py migrate   
Operations to perform:
  Apply all migrations: admin, app_name, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying assets.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK

  
$ py manage.py createsuperuser

$ mysql> show tables;  # 数据库变化
+-----------------------------+
| Tables_in_django_99         |
+-----------------------------+
| assets_asset                |   # app assets 的
| assets_asset_tags           |
| assets_businessunit         |
| assets_contract             |
| assets_cpu                  |
| assets_disk                 |
| assets_eventlog             |
| assets_idc                  |
| assets_manufacturer         |
| assets_networkdevice        |
| assets_newassetapprovalzone |
| assets_nic                  |
| assets_ram                  |
| assets_securitydevice       |
| assets_server               |
| assets_software             |
| assets_storagedevice        |
| assets_tag                  |
| auth_group                  |        # django自己的
| auth_group_permissions      |
| auth_permission             |
| auth_user                   |
| auth_user_groups            |
| auth_user_user_permissions  |
| django_admin_log            |
| django_content_type         |
| django_migrations           |
| django_session              |
+-----------------------------+
28 rows in set (0.00 sec)

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
### 项目

```
一、在 pycharm 中建立虚拟环境virtualenv

C:\Users\lx>pip install virtualenv
Requirement already satisfied: virtualenv in g:\python\python-3.6.5\lib\site-packages (16.0.0)

C:\Users\lx> 切换到想要存放虚拟环境的目录下

G:\PyCharm\PythonProjects>virtualenv --no-site-packages python_virtualenv_for_django
Using base prefix 'g:\\python\\python-3.6.5'
New python executable in G:\PyCharm\PythonProjects\my_virtual_env\Scripts\python.exe
Installing setuptools, pip, wheel...done.

或者指定Python版本
G:\PyCharm\PythonProjects>virtualenv --python=path of python.exe  python_virtualenv_for_django

结果是：
出现目录 G:\PyCharm\PythonProjects\python_virtualenv_for_django  其中隔离出最基本的 python 环境，和干净的基本没有第三方库在site-packages中。


二、安装django

cmd 下 在 G:\PyCharm\PythonProjects\python_virtualenv_for_django\Scripts 运行 activate 命令，激活该虚拟环境，
之后的命令行提示符将以(python_virtualenv_for_django)开头

(python_virtualenv_for_django) G:\PyCharm\PythonProjects\python_virtualenv_for_django\Scripts>pip install django -i https://pypi.douban.com/simple/
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

进入PyCharm，File->new Project 创建 django 新工程，此时 会用到前面create 好的virtual env 
Location  填 G:\PyCharm\PythonProjects\mysite，(与要用的python Iterpreter  G:\PyCharm\PythonProjects\python_virtualenv_for_django在
同级目录下)
在Iterpreter 右侧点击三个点，选中G:\PyCharm\PythonProjects\python_virtualenv_for_django\Scripts\python.exe，然后就选定了虚拟好的python
解释器
建好后会自动出现manage.py等django需要的包和环境

四、创建app

在cmd 终端需要 activate 

在pycharm 的终端里直接start app
(python_virtualenv_for_django) G:\PyCharm\PythonProjects\mysite>py manage.py startapp app_name
注意G:\PyCharm\PythonProjects\mysite目录里才有manage.py文件，才能执行py manage.py startapp app_name

五、设置settings 时区 语言

六、启动一下开发服务器

在Pycharm的Run-->Edit Configurations...--> Run/Debug Configurations配置界面里，将HOST设置为127.0.0.1，Port保持原样的8000，
确定后，点击OK
设置127.0.0.1:8000 ，>>>py manage.py runserver 
写好models等文件后
$ python manage.py makemigrations app_name      
$ python manage.py migrate   

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
**virtualenvwrapper-win**
```
pip install virtualenvwrapper-win
添加环境变量  WORK0N_HOME    想存放虚拟环境的目录
cmd workon   显示你的环境变量中指定的虚拟环境的目录中的envs
C:\Users\lx>workon

Pass a name to activate one of the following virtualenvs:
==============================================================================

C:\Users\lx>mkvirtualenv django
Using base prefix 'c:\\linuix\\python37'
New python executable in F:\Python\virtualenvs\django\Scripts\python.exe
Installing setuptools, pip, wheel...
done.

(django) C:\Users\lx>pip list
Package    Version
---------- -------
pip        18.1
setuptools 40.5.0
wheel      0.32.2

(django) C:\Users\lx>
```

## 2 django具体知识model
```
"""
   1 模型
   
   查看生成sql语句 用>python manage.py sqlmigrate
"""

"""
   2 字段

    ForeignKey(User)     导入Django内置的User表
    ManyToManyField('xxx') 关联xxx模型
    OneToOneField
"""

"""
   3 字段参数

    choices= 下拉多选框
    default= 数据库中为默认值
    max_length
    verbose_name 为字段设置一个人类可读，更加直观的别名
    unique 独一无二
    null=True 数据库填NULL
    blank=true 浏览器中就显示为浅色，非必填项
    on_delete=models.CASCADE  模拟SQL语言中的ON DELETE CASCADE约束，将定义有外键的模型对象同时删除
    related_name= '用于关联对象反向引用模型的名称'
    auto_now_add=True  自动加今天
    auto_now=True    自动加今天
"""
```
