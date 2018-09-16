
- [Sbulime Text 3 官网](http://www.sublimetext.com/)
- [Sublime Text 3 全程指南](http://lucida.me/blog/sublime-text-complete-guide/)
- [Sublime Text 3 使用方法](https://www.cnblogs.com/zhaowy/p/8400443.html)
- [Sublime Text 3 配置Python3开发环境](https://www.cnblogs.com/leopython/p/7589181.html)
- [Sublime text 3 搭建Python开发环境](https://blog.csdn.net/sinat_32596537/article/details/78156562)




## 1.安装 Package Control（插件管理器）

Sublime Text支持大量插件，如何找到并管理这些插件就成了一个问题，Package Control正是为了解决这个问题而出现的，

利用它我们可以很方便的浏览、安装和卸载Sublime Text中的插件。

1.按下快捷键： ctrl + shift + p 打开命令行

2 然后在输入框中输入install ，然后选中install package control

3 等待 安装，出现 success 表示成功安装，此时在Preferences中看到package control这一项


## 2 各种插件 (https://packagecontrol.io/)

- [1 Colorsublime 集合了许多主题](https://packagecontrol.io/packages/Colorsublime)

Installing
```
With Package Control (recommended)
Install Package Control
Run “Package Control: Install Package” command
Find and install the Colorsublime plugin.
Restart Sublime Text if there are issues.
```
Usage
```
Press ctl+shift+p (Windows/Linux) or ⇧+⌘+p (OSX) to open up Sublime Text's command menu
Select Colorsublime: Install Theme
Use the arrow keys to run through the themes (“color schemes”) and see your current tab change in realtime!
```

- [2 Boxy Theme](https://packagecontrol.io/packages/Boxy%20Theme)

 3-6 参考了https://blog.csdn.net/sinat_32596537/article/details/78156562

- [3 SublimeREPL 交互式调试程序]



详细步骤见 https://www.cnblogs.com/JackyXu2018/p/8821482.html

找到 C:\Users\linuix\AppData\Roaming\Sublime Text 3\Packages\SublimeREPL\config\Python\Main.sublime-menu 文件，

然后用Sublime Text 3 打开，找到id 为 repl_python行，修改 "cmd": ["python", "-i", "-u","$file_basename"]，保存。

这样相当于将SublimeREPL的python交互环境的命令改为运行当前文件的交互环境。

- [4 SublimeCodeIntel代码自动补全配置]
```
自动提示/补全python代码

选择 Perference-Package Settings-SublimeCodeIntel-Settings-User,复制以下配置:

{
    "codeintel_language_settings": {
        "Python3": {
            "python3": "E:/Program Files/python/python.exe",
            "codeintel_scan_extra_dir": [
                "E:/Program Files/python/DLLs",
                "E:/Program Files/python/Lib",
                "E:/Program Files/python/Lib/site-packages",
                "E:/Program Files/python/Lib/idlelib",
                "E:/Program Files/python/",
                "E:/Program Files/python/Lib/*",
            ],
            "codeintel_scan_files_in_project": true,
            "codeintel_selected_catalogs": []
        },
    }
}
追踪函数、查看系统函数
配置快捷键使其同eclipse,实现ctrl+鼠标左键追踪函数,alt+left/right跳转,alt+/自动提示代码

选择 Perference-package Settings-SublimeCodeIntel-Key Bindings-User

//自动提示代码
{ "keys": ["alt+/"], "command": "code_intel_auto_complete" },
//跳转到函数定义
{ "keys": ["alt+right"], "command": "goto_python_definition"},
//返回到跳转位置
{ "keys": ["alt+left"], "command": "back_to_python_definition"}
```
- [5 Anaconda：代码提示等许多功能，必备  和SublimeCodeIntel功能重叠]()

- [6 SublimeTmpl：新建文件模板插件，可以支持多种语言例如Python、PHP等，下面的代码是我在配置文件中的配置信息]()


- [7 ]()
