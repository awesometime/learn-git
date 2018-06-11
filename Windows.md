### 1 修改 C:\Users\ 后的用户名

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
