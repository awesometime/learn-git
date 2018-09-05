-[Django2.1 官方中文文档](https://docs.djangoproject.com/zh-hans/2.1/)

-[Django2.1 新手图文入门教程](http://www.liujiangblog.com/blog/36/)

-[Django-MySQL数据库使用](https://www.cnblogs.com/demo-deng/p/7801966.html)

## 顺序
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
