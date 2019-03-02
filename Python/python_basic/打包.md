```
G:\PyCharm\PythonProjects\django-polls>python setup.py sdist

running sdist
running egg_info
creating django_polls.egg-info
writing django_polls.egg-info\PKG-INFO
writing dependency_links to django_polls.egg-info\dependency_links.txt
writing top-level names to django_polls.egg-info\top_level.txt
writing manifest file 'django_polls.egg-info\SOURCES.txt'
reading manifest file 'django_polls.egg-info\SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no files found matching '*' under directory 'docs'
writing manifest file 'django_polls.egg-info\SOURCES.txt'
running check
creating django-polls-0.1
creating django-polls-0.1\django_polls.egg-info
creating django-polls-0.1\polls
creating django-polls-0.1\polls\migrations
creating django-polls-0.1\polls\static
creating django-polls-0.1\polls\static\polls
creating django-polls-0.1\polls\static\polls\images
creating django-polls-0.1\polls\templates
creating django-polls-0.1\polls\templates\polls
copying files to django-polls-0.1...
copying LICENSE -> django-polls-0.1
copying MANIFEST.in -> django-polls-0.1
copying README.rst -> django-polls-0.1
copying setup.py -> django-polls-0.1
copying django_polls.egg-info\PKG-INFO -> django-polls-0.1\django_polls.egg-info
copying django_polls.egg-info\SOURCES.txt -> django-polls-0.1\django_polls.egg-info
copying django_polls.egg-info\dependency_links.txt -> django-polls-0.1\django_polls.egg-info
copying django_polls.egg-info\top_level.txt -> django-polls-0.1\django_polls.egg-info
copying polls\__init__.py -> django-polls-0.1\polls
copying polls\admin.py -> django-polls-0.1\polls
copying polls\apps.py -> django-polls-0.1\polls
copying polls\models.py -> django-polls-0.1\polls
copying polls\tests.py -> django-polls-0.1\polls
copying polls\urls.py -> django-polls-0.1\polls
copying polls\views.py -> django-polls-0.1\polls
copying polls\migrations\0001_initial.py -> django-polls-0.1\polls\migrations
copying polls\migrations\__init__.py -> django-polls-0.1\polls\migrations
copying polls\static\polls\style.css -> django-polls-0.1\polls\static\polls
copying polls\static\polls\images\background.png -> django-polls-0.1\polls\static\polls\images
copying polls\templates\polls\detail.html -> django-polls-0.1\polls\templates\polls
copying polls\templates\polls\index.html -> django-polls-0.1\polls\templates\polls
copying polls\templates\polls\results.html -> django-polls-0.1\polls\templates\polls
Writing django-polls-0.1\setup.cfg
creating dist
Creating tar archive
removing 'django-polls-0.1' (and everything under it)

G:\PyCharm\PythonProjects\django-polls>

```
##### 打包后目录成如下
```
django-polls/
    dist/
        django-polls-0.1.tar.gz          # 核心文件  tar.gz
    django_polls.egg-info/
        dependency_links.txt
        PKG-INFO
        SOURCES.txt
        top_level.txt
    polls/
        __init__.py
        admin.py
        migrations/
            __init__.py
            0001_initial.py
        models.py
        static/
            polls/
                images/
                    background.gif
                style.css
        templates/
            polls/
                detail.html
                index.html
                results.html
        tests.py
        urls.py
        views.py
    docs
    LICENSE
    MANIFEST.in
    README.rst
    setup.py        
```
