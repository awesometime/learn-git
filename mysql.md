- [一千行 MySQL 学习笔记](https://shockerli.net/post/1000-line-mysql-note/)

- [ mysql-5.1-zh ](http://tool.oschina.net/apidocs/apidoc?api=mysql-5.1-zh)

MySQL语法   更多详细语法直接查[菜鸟教程](http://www.runoob.com/mysql/mysql-tutorial.html)

注意库名  表名

大小写不敏感？？

### python 连接数据库
```python

    # 连接数据库
    conn = pymysql.Connect(
        host='localhost',  # mysql服务器地址
        port=3306,  # mysql服务器端口号
        user='root',  # 用户名
        passwd='root',  # 密码
        db='ip_test_628',  # 数据库名
        charset='utf8'  # 连接编码
    )
    print('数据库已连接，对象为：{}'.format(conn))

    # 获取游标
    cursor = conn.cursor()

    
    # 创建表     *注意最好新建一个不存在的表
    sql = """CREATE TABLE IF NOT EXISTS jobbole_article (
                 TITLE  VARCHAR(200) NOT NULL,
                 CREATE_DATE  DATE,
                 URL VARCHAR(300) NOT NULL,
                 URL_OBJECT_ID  VARCHAR(50)  NOT NULL  PRIMARY KEY,
                 FRONT_IMAGE_URL VARCHAR(300), 
                 FRONT_IMAGE_PATH VARCHAR(200), 
                 COMMENT_NUMS INT(11), 
                 FAV_NUMS  INT(11), 
                 PRAISE_NUMS  INT(11), 
                 TAGS  varchar(200), 
                 CONTENT LONGTEXT
            )"""
    # Mysql中经常用来存储日期的数据类型有三种：Date、Datetime、Timestamp。
    # Date      数据类型：用来存储没有时间的日期。Mysql获取和显示这个类型的格式为“YYYY-MM-DD”。支持的时间范围为“1000-00-00”到“9999-12-31”。
    # Datetime  类型：存储既有日期又有时间的数据。存储和显示的格式为 “YYYY-MM-DD HH:MM:SS”。支持的时间范围是“1000-00-00 00:00:00”到“9999-12-31 23:59:59”。
    # Timestamp 类型：也是存储既有日期又有时间的数据。存储和显示的格式跟Datetime一样。支持的时间范围是“1970-01-01 00:00:01”到“2038-01-19 03:14:07”。
    
    
    
    cursor.execute(sql)
    print('已创建tabels')

    
    # SQL 表里插入
    sql = """INSERT INTO jobbole_article(title, url, tags, content)
             VALUES ('ip', %s, %s, %s)"""
    cursor.execute(sql, (url, tags, content))
    cursor.executemany(sql, (url, tags, content))
    # 提交到数据库执行
    conn.commit()
    # 如果发生错误则回滚
    # conn.rollback()
    print('mysql数据表已插入')

    
    # 查询表里有啥
    sql = """
            select * FROM ip_my
            """
    cursor.execute(sql)
    fetch_ip = cursor.fetchall()          # 返回元组
    cursor.close()


```


### 创建数据库
```
mysql> create database 'database-name';                      创建数据库
mysql> drop database 'database-name';                        删除数据库
mysql> GRANT ALL PRIVILEGES ON 'database-name'.* TO 'root'@'localhost' IDENTIFIED BY '密码';         Grant proper access to the 'database-name' database:
mysql> show databases;                                       查看显示所有数据库
mysql> use 'database-name' (此处貌似不需要分号)                选择某个数据库
mysql> select database();                                    查看当前使用的数据库
```

### 创建tables
```
mysql> CREATE TABLE 'table-name' (           创建table
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )；
mysql> drop table 'table-name'；              删除table
mysql> show tables;                           查看数据库的表名
mysql> describe 'table-name'；                查看表头及其参数的类型等信息
```
### SQL 插入操作 增 INSERT
```
示例  mysql> INSERT INTO 'table-name'(表头各项) VALUES ( 表头各项的具体内容);
mysql> INSERT INTO 'table-name'(id,name,sex,birthday) VALUES ( 1,'小明', '男', '2015-11-02');        
```
mysql> select * from 'table-name';                查看数据
mysql> select count(列名) from 表名;               统计某列有多少数据


mysql> truncate table 'table-name';               清空数据

mysql> select * from information_schema.tables where table_schema='databasename';          查看某个数据库的表信息。

mysql> select * from information_schema.tables where table_name ='table_name'              查看某种具体表的信息

?                                                                                    查看当前数据库大小

?                                                                                     查看数据所占的空间大小


### SQL 删除语句 删 DELETE
```
删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
```
### SQL 查询操作 查 query
```
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
见select 
```
### SQL 更新语句 改 UPDATE
```
将 TESTDB 的EMPLOYEE表中 SEX 为 'M' 的 AGE 字段递增 1
mysql>  "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'"  % ('M')
```
### 事务
对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。每一个方法都开始了一个新的事务。

commit()方法提交游标的所有更新操作，

rollback（）方法回滚当前游标的所有操作。

### 其他
```
mysql> select * from mysql.user                           查看所有用户
mysql> status;
mysql> SELECT VERSION();                                  查看数据库的安装版本
mysql> show variables  like 'port';                       查看数据库使用端口
mysql> show variables like 'character%';                  查看数据库编码
mysql> select distinct concat('user: ''',user,'''@''',host,''';') as query from mysql.user;   查看数据库的所有用户信息
mysql> show grants for 'root'@'localhost';                查看某个具体用户的权限
mysql>  show variables like '%max_connections%';          查看数据库的最大连接数
mysql> show status like 'Threads%';                       查看数据库当前连接数，并发数。
mysql> show variables like '%datadir%';                   查看数据文件存放路径
```


MySQL安装及使用配置

##  1 下载
https://dev.mysql.com/downloads/mysql/

选择ZIP Archive 版（简单、干净、免安装）的适合系统位数的版本进行下载

这里建议安装压缩包版本，需要**手动配置**点东西，不过会比较好用。

## 2 解压到某个目录G:\MySQL\mysql5.7\下

## 3 添加环境变量（可选）
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
输入：mysqld–initialize，初始化data文件这一步会生成一个mysql临时登录密码。在data文件夹下生成有一个lerr为后缀的文件。

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
