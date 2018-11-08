- [Python3.6+Django2.0+Xadmin2.0环境搭建](https://www.cnblogs.com/v88v/p/8858853.html)

基于原版xadmin修改，修复原版已知bug，适配Python3.X+Django2.1/2.0

### python3 不是虚拟环境安装  关键先得到  修改后的xadmin.zip

https://github.com/sshwsfc/xadmin  下载官方原版xadmin

可通过 git clone -b django2 https://github.com/sshwsfc/xadmin.git 下载django2 分支到 git 默认的目录，我这是C:/users/lx

或者直接下载他的zip文件


https://github.com/vip68/xadmin_bugfix 下载修复版，将其中的xadmin文件夹替换复制到官方xadmin下的xadmin文件夹(包含19个文件)

替换后，压缩整个替换后的官方xadmin文件夹成xadmin.zip

切换到xadmin.zip所在目录下pip install xadmin.zip 此方法将xadmin安装到了python3下dist-packages中

(附)虚拟环境中安装时 直接找到python3下dist-packages中 **xadmin**  和 **xadmin-2.0.1-py3.7.egg-info**复制到虚拟环境中也行

```shell
D:\>pip install xadmin.zip
Processing d:\xadmin.zip
Requirement already satisfied: setuptools in c:\linuix\python37\lib\site-packages (from xadmin==2.0.1) (39.0.1)
Requirement already satisfied: django>=2 in c:\linuix\python37\lib\site-packages (from xadmin==2.0.1) (2.1.2)
Collecting django-crispy-forms>=1.6.0 (from xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/9a/05/6bad05742d185ec2fabfa4deab05cafde286eb3f383fba24b3674340aca2/django_crispy_forms-1.7.2-py2.py3-none-any.whl (105kB)
    100% |████████████████████████████████| 112kB 152kB/s
Collecting django-reversion>=2.0.0 (from xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/3d/83/9ad46218b282c18b45dc8c05a92d8214146cb204ee65d1084f3f13256132/django_reversion-3.0.2-py2.py3-none-any.whl (81kB)
    100% |████████████████████████████████| 81kB 225kB/s
Collecting django-formtools>=1.0 (from xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/97/3f/b8e04c41c028d5cdad651393abea1f686d846c717d8ab5d5ebe2974f711c/django_formtools-2.1-py2.py3-none-any.whl (132kB)
    100% |████████████████████████████████| 133kB 214kB/s
Collecting django-import-export>=0.5.1 (from xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/5d/36/98fbfaa069f35aa8f2d3637bf91824edbc73b022f5a15294e028baddaca5/django_import_export-1.1.0-py2.py3-none-any.whl (73kB)
    100% |████████████████████████████████| 81kB 225kB/s
Collecting httplib2==0.9.2 (from xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/ff/a9/5751cdf17a70ea89f6dde23ceb1705bfb638fd8cee00f845308bf8d26397/httplib2-0.9.2.tar.gz (205kB)
    100% |████████████████████████████████| 215kB 68kB/s
Collecting future (from xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/90/52/e20466b85000a181e1e144fd8305caf2cf475e2f9674e797b222f8105f5f/future-0.17.1.tar.gz (829kB)
    100% |████████████████████████████████| 829kB 44kB/s
Requirement already satisfied: six in c:\linuix\python37\lib\site-packages (from xadmin==2.0.1) (1.11.0)
Requirement already satisfied: pytz in c:\linuix\python37\lib\site-packages (from django>=2->xadmin==2.0.1) (2018.6)
Collecting diff-match-patch (from django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/22/82/46eaeab04805b4fac17630b59f30c4f2c8860988bcefd730ff4f1992908b/diff-match-patch-20121119.tar.gz (54kB)
    100% |████████████████████████████████| 61kB 31kB/s
Collecting tablib (from django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/e4/9f/cba4e1145ca9ec84d9326f7ce38c6b5f37d9be8bc1af1bd8b19c20374095/tablib-0.12.1.tar.gz (63kB)
    100% |████████████████████████████████| 71kB 43kB/s
Collecting odfpy (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/01/0f/c9971c99d0d06024a1652f467427ff3f1a1136237e5740da715c5b208a48/odfpy-1.3.6.tar.gz (691kB)
    100% |████████████████████████████████| 696kB 73kB/s
Collecting openpyxl (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/04/18/64737cc6c5233e15374d21b4958a5600be52359e71063b4d4e7a604a1387/openpyxl-2.5.9.tar.gz (1.9MB)
    100% |████████████████████████████████| 1.9MB 112kB/s
Collecting unicodecsv (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/6f/a4/691ab63b17505a26096608cc309960b5a6bdf39e4ba1a793d5f9b1a53270/unicodecsv-0.14.1.tar.gz
Collecting xlrd (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/07/e6/e95c4eec6221bfd8528bcc4ea252a850bffcc4be88ebc367e23a1a84b0bb/xlrd-1.1.0-py2.py3-none-any.whl (108kB)
    100% |████████████████████████████████| 112kB 62kB/s
Collecting xlwt (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/44/48/def306413b25c3d01753603b1a222a011b8621aed27cd7f89cbc27e6b0f4/xlwt-1.3.0-py2.py3-none-any.whl (99kB)
    100% |████████████████████████████████| 102kB 90kB/s
Collecting pyyaml (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/bf/96/d02ef8e1f3073e07ffdc240444e5041f403f29c0775f9f1653f18221082f/PyYAML-3.13-cp37-cp37m-win_amd64.whl (206kB)
    100% |████████████████████████████████| 215kB 96kB/s
Collecting jdcal (from openpyxl->tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/a0/38/dcf83532480f25284f3ef13f8ed63e03c58a65c9d3ba2a6a894ed9497207/jdcal-1.4-py2.py3-none-any.whl
Collecting et_xmlfile (from openpyxl->tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Downloading https://files.pythonhosted.org/packages/22/28/a99c42aea746e18382ad9fb36f64c1c1f04216f41797f2f0fa567da11388/et_xmlfile-1.0.1.tar.gz
Installing collected packages: django-crispy-forms, django-reversion, django-formtools, diff-match-patch, odfpy, jdcal, et-xmlfile, openpyxl, unicodecsv, xlrd, xlwt, pyyaml, tablib, django-import-export, httplib2, future, xadmin
  Running setup.py install for diff-match-patch ... done
  Running setup.py install for odfpy ... done
  Running setup.py install for et-xmlfile ... done
  Running setup.py install for openpyxl ... done
  Running setup.py install for unicodecsv ... done
  Running setup.py install for tablib ... done
  Running setup.py install for httplib2 ... done
  Running setup.py install for future ... done
  Running setup.py install for xadmin ... done
Successfully installed diff-match-patch-20121119 django-crispy-forms-1.7.2 django-formtools-2.1 django-import-export-1.1.0 django-reversion-3.0.2 et-xmlfile-1.0.1 future-0.17.1 httplib2-0.9.2 jdcal-1.4 odfpy-1.3.6 openpyxl-2.5.9 pyyaml-3.13 tablib-0.12.1 unicodecsv-0.14.1 xadmin-2.0.1 xlrd-1.1.0 xlwt-1.3.0
```
pip list 检验


### 虚拟环境中安装

若要安装到虚拟环境中还需要进入虚拟环境    (将xadmin.zip先放到虚拟环境所在目录中 不需要貌似)

```shell
C:\Users\lx>workon django
(django) C:\Users\lx>pip install xadmin.zip
Processing f:\python\virtualenvs\django\lib\site-packages\xadmin.zip
Requirement already satisfied: setuptools in f:\python\virtualenvs\django\lib\site-packages (from xadmin==2.0.1) (40.5.0)
Requirement already satisfied: django>=2 in f:\python\virtualenvs\django\lib\site-packages (from xadmin==2.0.1) (2.1.3)
Collecting django-crispy-forms>=1.6.0 (from xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/9a/05/6bad05742d185ec2fabfa4deab05cafde286eb3f383fba24b3674340aca2/django_crispy_forms-1.7.2-py2.py3-none-any.whl
Collecting django-reversion>=2.0.0 (from xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/3d/83/9ad46218b282c18b45dc8c05a92d8214146cb204ee65d1084f3f13256132/django_reversion-3.0.2-py2.py3-none-any.whl
Collecting django-formtools>=1.0 (from xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/97/3f/b8e04c41c028d5cdad651393abea1f686d846c717d8ab5d5ebe2974f711c/django_formtools-2.1-py2.py3-none-any.whl
Collecting django-import-export>=0.5.1 (from xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/5d/36/98fbfaa069f35aa8f2d3637bf91824edbc73b022f5a15294e028baddaca5/django_import_export-1.1.0-py2.py3-none-any.whl
Collecting httplib2==0.9.2 (from xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/ff/a9/5751cdf17a70ea89f6dde23ceb1705bfb638fd8cee00f845308bf8d26397/httplib2-0.9.2.tar.gz
Collecting future (from xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/90/52/e20466b85000a181e1e144fd8305caf2cf475e2f9674e797b222f8105f5f/future-0.17.1.tar.gz
Requirement already satisfied: six in f:\python\virtualenvs\django\lib\site-packages (from xadmin==2.0.1) (1.11.0)
Requirement already satisfied: pytz in f:\python\virtualenvs\django\lib\site-packages (from django>=2->xadmin==2.0.1) (2018.7)
Collecting tablib (from django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/e4/9f/cba4e1145ca9ec84d9326f7ce38c6b5f37d9be8bc1af1bd8b19c20374095/tablib-0.12.1.tar.gz
Collecting diff-match-patch (from django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/22/82/46eaeab04805b4fac17630b59f30c4f2c8860988bcefd730ff4f1992908b/diff-match-patch-20121119.tar.gz
Collecting odfpy (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/01/0f/c9971c99d0d06024a1652f467427ff3f1a1136237e5740da715c5b208a48/odfpy-1.3.6.tar.gz
Collecting openpyxl (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/04/18/64737cc6c5233e15374d21b4958a5600be52359e71063b4d4e7a604a1387/openpyxl-2.5.9.tar.gz
Collecting unicodecsv (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/6f/a4/691ab63b17505a26096608cc309960b5a6bdf39e4ba1a793d5f9b1a53270/unicodecsv-0.14.1.tar.gz
Collecting xlrd (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/07/e6/e95c4eec6221bfd8528bcc4ea252a850bffcc4be88ebc367e23a1a84b0bb/xlrd-1.1.0-py2.py3-none-any.whl
Collecting xlwt (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/44/48/def306413b25c3d01753603b1a222a011b8621aed27cd7f89cbc27e6b0f4/xlwt-1.3.0-py2.py3-none-any.whl
Collecting pyyaml (from tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/bf/96/d02ef8e1f3073e07ffdc240444e5041f403f29c0775f9f1653f18221082f/PyYAML-3.13-cp37-cp37m-win_amd64.whl
Collecting jdcal (from openpyxl->tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/a0/38/dcf83532480f25284f3ef13f8ed63e03c58a65c9d3ba2a6a894ed9497207/jdcal-1.4-py2.py3-none-any.whl
Collecting et_xmlfile (from openpyxl->tablib->django-import-export>=0.5.1->xadmin==2.0.1)
  Using cached https://files.pythonhosted.org/packages/22/28/a99c42aea746e18382ad9fb36f64c1c1f04216f41797f2f0fa567da11388/et_xmlfile-1.0.1.tar.gz
Building wheels for collected packages: xadmin, httplib2, future, tablib, diff-match-patch, odfpy, openpyxl, unicodecsv, et-xmlfile
  Running setup.py bdist_wheel for xadmin ... done
  Stored in directory: C:\Users\lx\AppData\Local\Temp\pip-ephem-wheel-cache-oipi41qg\wheels\21\ca\aa\28dd42866d322426dcb9341bc6679ed5703c3b9ab34e402ee3
  Running setup.py bdist_wheel for httplib2 ... done
  Stored in directory: C:\Users\lx\AppData\Local\pip\Cache\wheels\36\f2\49\5adbf90fba31e02a7784e1147d7f8b6c4af3718739e568c8cb
  Running setup.py bdist_wheel for future ... done
  Stored in directory: C:\Users\lx\AppData\Local\pip\Cache\wheels\0c\61\d2\d6b7317325828fbb39ee6ad559dbe4664d0896da4721bf379e
  Running setup.py bdist_wheel for tablib ... done
  Stored in directory: C:\Users\lx\AppData\Local\pip\Cache\wheels\ea\e4\b9\9eb46eaf91476d5dd88a5cf6f76f0884114eafe0b2ef24e2df
  Running setup.py bdist_wheel for diff-match-patch ... done
  Stored in directory: C:\Users\lx\AppData\Local\pip\Cache\wheels\f2\72\a3\8c2adafbe9afc22a1e65cfc412982e0061199c0092b1be11d9
  Running setup.py bdist_wheel for odfpy ... done
  Stored in directory: C:\Users\lx\AppData\Local\pip\Cache\wheels\da\af\f6\a0b436814a73a88125b8fa82acc73ae96de511bc1faa62b7cc
  Running setup.py bdist_wheel for openpyxl ... done
  Stored in directory: C:\Users\lx\AppData\Local\pip\Cache\wheels\57\41\b9\3765af8bda4a8d4b6aaf4957d7214984c3332348713e85cf36
  Running setup.py bdist_wheel for unicodecsv ... done
  Stored in directory: C:\Users\lx\AppData\Local\pip\Cache\wheels\a6\09\e9\e800279c98a0a8c94543f3de6c8a562f60e51363ed26e71283
  Running setup.py bdist_wheel for et-xmlfile ... done
  Stored in directory: C:\Users\lx\AppData\Local\pip\Cache\wheels\2a\77\35\0da0965a057698121fc7d8c5a7a9955cdbfb3cc4e2423cad39
Successfully built xadmin httplib2 future tablib diff-match-patch odfpy openpyxl unicodecsv et-xmlfile
Installing collected packages: django-crispy-forms, django-reversion, django-formtools, odfpy, jdcal, et-xmlfile, openpyxl, unicodecsv, xlrd, xlwt, pyyaml, tablib, diff-match-patch, django-import-export, httplib2, future, xadmin
Successfully installed diff-match-patch-20121119 django-crispy-forms-1.7.2 django-formtools-2.1 django-import-export-1.1.0 django-reversion-3.0.2 et-xmlfile-1.0.1 future-0.17.1 httplib2-0.9.2 jdcal-1.4 odfpy-1.3.6 openpyxl-2.5.9 pyyaml-3.13 tablib-0.12.1 unicodecsv-0.14.1 xadmin-2.0.1 xlrd-1.1.0 xlwt-1.3.0

(django) C:\Users\lx>pip list
```
