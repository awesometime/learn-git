MySQL安装及使用配置

##  1 下载
https://dev.mysql.com/downloads/mysql/

选择ZIP Archive 版（简单、干净、免安装）的适合系统位数的版本进行下载

这里建议安装压缩包版本，需要**手动配置**点东西，不过会比较好用。

## 2 解压到某个目录G:\MySQL\mysql5.7\下

## 3 添加环境变量（可选）--
#### 配置环境变量的目的是：不用每次启动mysql时都将目录切换到G:\MySQL\mysql5.7\bin目录下，只需在C:\Users\linuix>下输入mysql -u root -p 即可登录。
    操作如下：
    1）右键单击我的电脑->属性->高级系统设置(高级)->环境变量
      点击系统变量下的新建按钮
      输入变量名：MYSQL_HOME
      输入变量值：D:\java\mysql
      #即为mysql的自定义解压目录。
    2）选择系统变量中的Path
      点击编辑按钮
      在变量值中添加变量值：%MYSQL_HOME%\bin
      注意是在原有变量值后面加上这个变量，用;隔开，不能删除原来的变量值
      
      
## 4 配置文件

我下载的版本解压后没有默认配置文件my-default.ini，所以自己新建my.ini配置文件，具体内容如下，按照菜鸟教程http://www.runoob.com/mysql/mysql-install.html
```
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
 
[mysqld]
# 设置3306端口
port = 3306
# 设置mysql的安装目录
basedir=G:\MySQL\mysql5.7
# 设置mysql数据库的数据的存放目录 , 注意先不要手动新建data文件夹，不然后面net　start　mysql 会出错，
后面采用mysqld --initialize进行初始化后会自动帮我们新建data文件夹。
datadir=G:\MySQL\mysql5.7\data  
# 允许最大连接数
max_connections=20
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
```

### 5 启动 MySQL 数据库

以**管理员身份**否则会出[安装mysql Install/Remove of the Service Denied!错误的解决办法](https://blog.csdn.net/lxpbs8851/article/details/14161935/)打开 cmd 命令行工具，切换到目录G:\MySQL\mysql5.7\bin下：

 ` mysqld install`         如果提示成功，说明安装成功了

 `mysqld --initialize`    注意: 在 5.7 需要初始化 data 目录,否则会出现[mysql服务无法启动 服务没有报告任何错误解决方法](https://blog.csdn.net/liyangyang0528/article/details/54233632)

总之先初始化再启动。

**启动mysql服务有两种方法**

  1 初始化后再运行 net start mysql 即可启动 mysql。

  2 计算机图标上右键-->管理-->服务和应用程序-->服务，找到mysql的服务，点击启动即可。

## 6 修改mysql临时密码为自己设置的密码
输入：mysqld–initialize，初始化data文件这一步会生成一个mysql临时登录密码。在data文件夹下生成有一个err为后缀的文件。

用记事本打开，临时密码位于文件的最后一行，[Note] A temporary password is generated for root@localhost: E7203xxdQ.FP

将此密码复制保存(一会改密码时需要这个密码登录)

在cmd输入：

`C:\Users\linuix>mysql -u root -p`                                     登录MySQL修改改密码,将刚才复制的密码E7203xxdQ.FP粘贴进去，回车。
 `Enter password:*******`
 `mysql>`

然后MySQL欢迎界面后，接着输入：

`mysql>set password =password('用户自己设置的密码，比如root');`           单引号中的内容就是自己的密码，可以改成自己想要的密码。
 
`mysql>exit;`

用新密码重新登录
```
C:\Users\linuix>mysql -u root -p
Enter password: ****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.22 MySQL Community Server (GPL)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```
