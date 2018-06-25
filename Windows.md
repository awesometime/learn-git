### 1 修改CMD中显示的 C:\Users\ 后的用户名

参考https://www.jb51.net/diannaojichu/417162.html

在 Windows 安装的时候会输入一个用户名，电脑店装的一般都会给你设置成Admin之类的。

这个时候你想要改成自己的，一般都是直接在 控制面板 > 用户帐户和家庭安全 > 用户帐户 > 更改账户名称 这里修改。

改完之后开始菜单上显示的用户名是你自己的了，但是 C:\Users 文件夹下面的主账户文件夹还是原来的名字，

打开Win+R，输入cmd，回车，上面的用户名还是原来的名字。想要改掉这些地方，就要用下面的方法了。

Win+R，输入regedit，回车；

定位到HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList；

选中下面名字最长的项，双击右侧的ProfileImagePath，修改 C:\Users\ 后的用户名，点击确定；

**注销并重新登录**；此时会以TEMP用户登录，可能有些文件会看不到，别慌，接着下一步。

在C盘中打开 C:\User\，将新的用户名文件夹删除，再将原来的的用户名文件夹重命名为新的用户名；

**再次注销并重新登录**。

修改完以后打开Win+R，输入cmd，回车，输入python会提示不是内部命令，需要将python加入**环境变量Path**中

具体解决如下：

参考：如何通过cmd（命令提示符）来启动python？https://jingyan.baidu.com/article/b0b63dbf1edef64a48307024.html

解决后输入python显示
```
C:\Users\linuix>python
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```
### 2 pip相关问题
python是可以安装到C盘以外的盘的

pip是一个安装和管理 Python 包的工具

**修改python及pip环境变量后仍然有如下问题**

pip ipython 路径C:\Users\linuix\AppData\Local\Programs\Python\Python35\Scripts

AppData  为隐藏文件夹，查看勾选后可以看到

```
C:\Users\linuix>pip
Fatal error in launcher: Unable to create process using '"'
```
**解决**
```
C:\Users\linuix>python -m pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/0f/74/ecd13431bcc456ed390b44c8a6e917c1820365cbebcb6a8974d1cd045ab4/pip-10.0.1-py2.py3-none-any.whl (1.3MB)
    100% |████████████████████████████████| 1.3MB 140kB/s
Installing collected packages: pip
  Found existing installation: pip 9.0.1
    Uninstalling pip-9.0.1:
      Successfully uninstalled pip-9.0.1
Successfully installed pip-10.0.1
```
```
C:\Users\linuix>pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to
                              WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup,
                              (a)bort).
  --trusted-host <hostname>   Mark this host as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the
                              certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for
                              download. Implied with --no-index.
  --no-color                  Suppress colored output
```
```
C:\Users\linuix>pip list
Package    Version
---------- -------
pip        10.0.1
pygame     1.9.3
setuptools 38.4.0
```
ipython安装
```
C:\Users\linuix>pip install ipython
C:\Users\linuix>ipython
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```
查看通过pip安装ipython的安装路径

C:\Users\linuix\AppData\Local\Programs\Python\Python35\Lib\site-packages
```
C:\Users\linuix>pip install ipython
Requirement already satisfied: ipython in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (6.4.0)
Requirement already satisfied: decorator in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (4.3.0)
Requirement already satisfied: backcall in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (0.1.0)
Requirement already satisfied: win-unicode-console>=0.5; sys_platform == "win32" and python_version < "3.6" in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (0.5)
Requirement already satisfied: pickleshare in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (0.7.4)
Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.15 in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (1.0.15)
Requirement already satisfied: traitlets>=4.2 in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (4.3.2)
Requirement already satisfied: simplegeneric>0.8 in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (0.8.1)
Requirement already satisfied: colorama; sys_platform == "win32" in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (0.3.9)
Requirement already satisfied: jedi>=0.10 in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (0.12.0)
Requirement already satisfied: pygments in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (2.2.0)
Requirement already satisfied: setuptools>=18.5 in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from ipython) (38.4.0)
Requirement already satisfied: wcwidth in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from prompt-toolkit<2.0.0,>=1.0.15->ipython) (0.1.7)
Requirement already satisfied: six>=1.9.0 in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from prompt-toolkit<2.0.0,>=1.0.15->ipython) (1.11.0)
Requirement already satisfied: ipython-genutils in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from traitlets>=4.2->ipython) (0.2.0)
Requirement already satisfied: parso>=0.2.0 in c:\users\linuix\appdata\local\programs\python\python35\lib\site-packages (from jedi>=0.10->ipython) (0.2.1)
```
### 3 cmd中从C盘切到D盘
```
Win+R cmd 回车
C:\Users\linuix>D:
D:\>
D:\>dir  查看D盘文件夹
D:\>cd filename  切到D盘下某个文件夹内
```
### 4 win10如何将txt文件设置为默认从Notepad++打开

[notepad++设置默认打开txt文件失效的解决方法](https://www.cnblogs.com/zsy/p/5951680.html)
