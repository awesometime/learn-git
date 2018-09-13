linux常用命令总结

**rpm**
rpm -qal |grep mysql  查看mysql所有安装包的文件存储位置
rpm -ql               列出软件包安装的文件


<p align="center">
   一、Linux常用命令符
</p>


```
ctrl+alt+t                                                    调出终端
gsettings set com.canonical.Unity.Launcher launcher-position Bottom   应用程序启动器置底
gsettings set com.canonical.Unity.Launcher launcher-position Left      应用程序启动器置左
ctrl + shift + =                    放大终端字体
ctrl + -                          缩小终端字体
apt-get update
apt-get upgrade
ls  /(ls  -lha)
pwd                            查看当前所在目录路径
cd                             切换路径
grep  关键词  文件名           从文件中找到关键词输出
grep  ‘^[a-z]’文件名           从文件中输出所有字母 
tail -30 文件名  |  grep "关键词"   从文件的后30行中找出含有关键词的内容输出
cat                            查看文件具体内容
touch                          新建文件
mkdir
rm                            删除文件
clear                          清屏
tree                           目录
cp                             复制
mv                            修改文件名字
more
echo > [文件内容] [目标文件]      覆盖>，追加>>文件
|                              管道
shutdown                       关机
reboot                         重启
ifconfig  (| grep inet)             网卡配置信息  (抓取关键字inet并用管道输出)
ping  目标主机IP地址           是否与目标主机连接  (Ctrl+C退出)      
ping  -c  n 目标IP              输出n行内容
ssh                            远程登录
scp                            远程复制文件
tar  -xvzf  xxx.tar.gz  -C  ~                   解压缩安装
chgrp ［选项］ group filename                改变文件或目录所属的组
chmod ［ugoa］(+/-)r/w/x  [文件名]           修改文件和目录都有访问许可权限
which   python3                            查python3所在路径
ps  -aux                                    列出进程
\      >                                   换行输入命令
history                     查看历史操作命令记录，保存于.bash_history隐藏文件中
history  -c     清除历史操作命令记录，/etc/profile文件中可以配置是否记录历史操作命令
sudo  su  root                                   切换到root用户登录
sudo  su  用户名                                 切换到用户登录
su 用户名 / 直接输入exit  / Ctrl+D退出        root用户切换回普通用户
hostname或uname –n                        查看机主名
hostname永久修改                           编辑/etc/hostname的内容，重启reboot
/etc/hostname                                /etc/hostname存放的是主机名
/etc/hosts                                    /etc/hosts存放的是域名与ip的对应关系
sudo ufw status                               查看防火墙状态
brctl show                                    查询网桥信息
ifconfig eth1 promisc                           设置网卡混杂模式
ifconfig eth1 -promisc                           取消网卡混杂模式
root@controller                               用户名@虚拟机名
# lsb_release -a                             查看ubuntu版本
# uname -ar                                  查看linux内核版本
# libvirtd --version
# kvm --version
# wget  URL 

```

<p align="center">
   二、VI/VIM命令
</p> 

```
Vi  进入命令模式，i进入输入模式，    vi进入，  ：wq保存退出
   

输入模式                             vi中按i进入，ESC键退出

底线命令模式  命令模式下按下:（英文冒号）就进入了底线命令模式。ESC键退出
q 退出程序w 保存文件
vim  .bashrc 进去可以自定义配置
alias  cl="clear"
alias  gh="cd ~"
alias  ..="cd ../"
alias  ...="cd ../.."
alias  ....="cd ../../.."
alias q="exit"

Vim .vimrc 进去可以自定义配置
参考资料https://github.com/VundleVim/Vundle.vim
也可参考CSDN的类似文章[vim设置(非常全面)，即.vimrc文件的配置]s
1.先下载插件管理Vundle插件  (Vundle is short for Vim bundle and is a Vim plugin manager)
git clone  https://github.com/VundleVim/Vundle.vim.git     ~/.vim/bundle/Vundle.vim
git clone下来Vundle插件，并保存于.vim/bundle/Vundle.vim中。
2.按需要编辑.vimrc内容
接着配置或者安装以下插件
set  nu
set  ruler
set  cmdheight=1
set  encoding=utf-8
Set  foldmethod=indent
set  fileencodings=ucs-bom,utf-8,cp936,gb18030,big5,euc-jp,euc-kr,latin1

Plugin  'VundleVim/Vundle.vim'
Plugin  'Yggdroot/indentLine'
Plugin  'scrooloose/nerdtree'
Plugin  'fholgado/minibufexpl.vim'
Plugin  'majutsushi/tagbar'
Plugin  'altercation/vim-colors-solarized'             背景配色
Plugin  'davidhalter/jedi'
Plugin  'scrooloose/syntastic'
Plugin  'Raimondi/delimitMate'
Plugin  'Valloric/YouCompleteMe'

Plugin indentLine settings
Plugin nerdtree settings
Plugin minibufexpl settings
Plugin Tagbar settings
Plugin theme
3.To install from command line:   vim +PluginInstall +qall

Vim(中这几个用的较少)
Ctrl + i              进入下一级
+--------------  z + o/c  显示/折叠收起的内容
Ctrl + o             右边显示在总进度中的占比
Ctrl + g/h/j/k         窗口间切换
Vim(常用的命令)
:wq                                         保存退出
：set nu/nonu                                vim中(不)设置行号
：60,120  w！  >>  文件名                   将60-120行追加到文件末尾
：60,120  w！  文件名                       将60-120行复制到文件中(将文件替换？)
? ？？？？?                                          将60-120行追加到文件指定行
：1                                         跳到文件首
：$                                   跳到文件尾
：行号                                跳到某行
：/关键词                             关键词向下查找，n向下继续查找；N向上继续
：？关键词                            关键词向上查找，n向下继续查找；
Vim中退出insert               yy复制一行，p粘到指针下一行
Vim中退出insert       dd删除一整行；ndd代表删除n行(光标放在前面删除后n行？？？)
Vim中退出insert               D删除行尾到光标处(含光标)内容
```

<p align="center">
   三、虚拟机常用命令
</p>

```
Mysql -u root -p                 进入mysql
Mysql语句                     以；结束。Exit退出
. (source)  文件名                     ？加载/执行文件

/etc/network/interfaces           网络
/etc/apt/sources.list               修改更新、文件下载源
/etc/ssh/sshd_config              PermitRootLogin=yes
/etc/hosts
/etc/nova/nova.conf              配置my_ip=192.168.20.131
/var/log
Service network restart             
Service httpd   restart
/etc/resolv.conf                    DNS信息（Domain Name System，域名系统），域名和IP地址相互映射的一个分布式数据库
do-release-upgrade                 to upgrade to New release '16.04.4 LTS'
批量删除行首
批量取消注释
检查CPU是否支持安装KVM：
egrep -o '(vmx|svm)' /proc/cpuinfo

sudo apt-get install qemu-kvm qemu-system libvirt-bin virt-manager bridge-utils vlan   
  安装KVM，参考cloudman
  命令 virsh         管理虚机
```

<p align="center">
   四、虚拟机安装完以后的configuration可以ping通外网步骤 Ubuntu-16.04
</p>

```
ip  r                                  查看当前ip      
设置可以远程登录(就可以用SecureCRT软件远程登录进行操作了)
sudo apt-get install openssh-server
sudo passwd root
su - root或者sudo su root
vim /etc/ssh/sshd_config
PermitRootLogin=yes 
sudo service ssh restart   或者(systemctl restart ssh 、systemctl restart sshd.service)
另：修改host。可以把root@ubuntu改为root@controller，方法如下
Host name             查看机主名
Hostname修改   修改/etc/sysconfig/network?和/etc/hosts中的hostname，重启reboot

Edit the /etc/hosts file to contain the following:
# controller
10.0.0.11       controller
# compute1
10.0.0.31       compute1

/etc/network/interfaces   重启，手动设置好IP后用ping命令测试可以ping通   
sudo   /etc/init.d/networking  restart  (ubuntu16.04)重启网络服务


/etc/apt/sources.list
sudo  cp  /etc/apt/sources.list   /etc/apt/sources.list.backup   备份
中国科学技术大学源
deb https://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse

阿里云源
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse

sudo apt- get update               更新源列表,换源后必须执行(如果更新速度非常慢请更换源 sudo gedit /etc/apt/sources.list ) 
sudo apt-get dist-upgrade           更新软件
Reboot the system to activate the changes     重启虚拟机

以下两项可根据需要自行配置，非必须项
vim  .bashrc 进去可以自定义配置  .(source)  ~/.bashrc生效
vim  .vimrc 进去可以自定义配置
initial configuration完以后做个SnapShot
```

<p align="center">
   五、Ubuntu 14.04
</p>

```
Ubuntu 14.04
普通用户需要加sudo，root用户不用
Eject弹出  Ubuntu 14.04.5 LTS amd64 iso

# /etc/network/interfaces     重启，可以上网
可以用sudo gedit /etc/network/interfaces比vi好用
需要sudo 不然不能保存
修改/etc/hosts   和
#sudo apt-get install openssh-server   
sudo passwd root
su - root或者sudo su root
gedit或者vi  /etc/ssh/sshd_config
PermitRootLogin yes
sudo service ssh restart
虚拟机先关机以root登录
接着可以用SecureCRT远程以root登录

安装vim
#sudo apt-get install vim 

改源
#sudo  cp  /etc/apt/sources.list   /etc/apt/sources.list.backup   备份源
# vim /etc/apt/sources.list
# sudo apt-get update
# sudo apt-get upgrade

#vim  .bashrc 
#source  ~/.bashrc
# apt-get install git
不执行apt-get update 的话会出现E: Unable to locate package git
#git  clone  https://github.com/VundleVim/Vundle.vim.git    ~/.vim/bundle/Vundle.vim
   configured repository to   ~/.vim/bundle/Vundle.vim   by default
#vim  .vimrc  将 https://github.com/VundleVim/Vundle.vim 内容粘贴过来
按需要配置，有空研究一下每一项的作用。。。。。
#vim +PluginInstall +qall
root@openstack-compute1:~# vim +PluginInstall +qall
运行如下  " Installing plugins to /root/.vim/bundle                                       
. Plugin 'VundleVim/Vundle.vim'                                                 
+ Plugin 'tpope/vim-fugitive'                                                    
+ Plugin 'git://git.wincent.com/command-t.git'                                   
! Plugin 'file:///home/gmarik/path/to/plugin'  (未安)                                    
+ Plugin 'rstacruz/sparkup'                                                       
+ Plugin 'Yggdroot/indentLine'                                                    
+ Plugin 'scrooloose/nerdtree'                                                    
+ Plugin 'fholgado/minibufexpl.vim'                                               
+ Plugin 'majutsushi/tagbar'                                                      
+ Plugin 'altercation/vim-colors-solarized'                                       
+ Plugin 'davidhalter/jedi'                                                       
+ Plugin 'scrooloose/syntastic'                                                   
+ Plugin 'Raimondi/delimitMate'                                                   
* Helptags  
#source  ~/.vimrc
以下error以后再说
-bash:  set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
: No such file or directory
-bash: call vundle#begin('~/some/path/here')

: No such file or directory
Plugin: command not found
 The following are examples of different formats supported.
: command not found
-bash:  plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
: No such file or directory
 Plugin 'L9'
: command not found
Plugin: command not found
-bash:  git repos on your local machine (i.e. when working on your own plugin)
Plugin 'file:///home/gmarik/path/to/plugin'
: No such file or directory
-bash: /root/.vimrc: line 84: unexpected EOF while looking for matching `''
-bash: /root/.vimrc: line 109: syntax error: unexpected end of file


安装KVM
#sudo apt-get install qemu-kvm qemu-system libvirt-bin virt-manager bridge-utils vlan
qemu-kvm 和 qemu-system 是 KVM 和 QEMU 的核心包，提供 CPU、内存和 IO 虚拟化功能
libvirt-bin 就是 libvirt，用于管理 KVM 等 Hypervisor
virt-manager 是 KVM 图形化管理工具
bridge-utils 和 vlan，主要是网络虚拟化需要，KVM 网络虚拟化的实现是基于 linux-bridge 和 VLAN。

SnapShot保存
     
```

<p align="center">
   六、Python命令
</p>

```
python                         打开python2.7.12
python3                        打开python3.5.2
exit()或ctrl + d                  退出python
print()
type()                          查看数据类型
input() 
Dir(函数，变量，数据，标识符等对象)      查看(对象)的所有属性，方法
```

<p align="center">
   七、PyCharm命令
</p>
  
```
Ctrl+d                               向下复制一行
鼠标放在方法上点击Ctrl+q             查看帮助信息
print("xxx", end="")                    不换行打印
"""    """    或ctrl+/                多行注释
{"name": "jasds","qq": "123456"}         字典格式
for aaa in ttt:        print(aaa)         遍历
Str [开始索引：结束索引：步长]        str、list、tuple的切片slice
TODO                               注释，提示待完成的工作
break                               跳出循环
continue                            
return      返回函数执行结果；下方代码不会执行，返回调用函数处并执行它下面的代码
dict["name"]                         通过key输出字典的value
光标放上去+enter                    一个引号输出的内容变成两个引号
id(xxx)                              查看地址
%d                                 十进制
%x                                 十六进制
__类名/方法名                       私有类名/方法名
is/is not                             看地址是否相同/不同
==                                 看内容是否相同
__name__属性                      测试代码，其他模块导入时就不会立即执行一遍了



关键字
Del
Global                               修改全局变量
Def                                  定义
Not  
函数
Len()
Del()
Max()
Min()


方法
Index()
Count()
Strip()                  去除字符串中的空白字符
Center()                 居中显示文本   
Ljust()                  居左显示
Rjust()                  居右显示  
Split()                     分割
Join()                     拼接 
Sort/Sort（reverse=True）  升序/降序排列【注】reverse为缺省参数，必须为最后一个参数

【注意1】
str、list、tuple都支持slice
str、list、tuple都支持 * / +  等运算符
str、list、tuple、dict都支持in / not in 成员运算符
List                                    extend / append / +
不可变类型   str    数字    tuple      [dict中的key只能是str，tuple，数字]
可变类型     list    dict 

【注意2】
代码结构  shebang  import模块  全局变量  函数定义  执行代码

【注意3】
函数返回值为tuple时可以使用多个变量一次性接收相同个数个返回值
交换两个数              a，b = b，a   右边为一个tuple，省略了括号
【注意4】
无论给函数传递的参数是可变类型还是不可变类型，在函数内部使用赋值语句修改了数据内容，外部数据不会改变

若给函数传递的参数是可变类型，在函数内部使用方法（例如append，pop）修改了数据内容，外部数据也会随之修改 

多值参数（num，*args，**kwargs）=（num，*arguments，**keyword args）=（数字，tuple，dict）         拆包语法tuple变量前加*，dict变量前加**
【注意5】
类            具有属性和方法
对象
```

#### 8 ubuntu 物理机备份 恢复

- [Ubuntu全盘备份与恢复，亲自总结，实测可靠](https://blog.csdn.net/sinat_27554409/article/details/78227496)
- [Ubuntu14.04如何备份和恢复系统](https://blog.csdn.net/liuzane/article/details/79715914)

root@cloudlet:~# cd /
root@cloudlet:/# ls
bin   etc         initrd.img.old  lib64       mnt   root  srv  usr      vmlinuz.old
boot  home        lib             lost+found  opt   run   sys  var
dev   initrd.img  lib32           media       proc  sbin  tmp  vmlinuz
root@ubuntu:/# tar cvpzf backup913.tgz --exclude=/proc --exclude=/lost+found --exclude=/backup913.tgz --exclude=/sys --exclude=/media /

