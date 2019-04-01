- [一千行 MySQL 学习笔记](https://shockerli.net/post/1000-line-mysql-note/)

- [ mysql-5.1-zh 中文文档](http://tool.oschina.net/apidocs/apidoc?api=mysql-5.1-zh)

MySQL语法   更多详细语法直接查[菜鸟教程](http://www.runoob.com/mysql/mysql-tutorial.html)

注意库名  表名

大小写不敏感？？

### SQLALchemy-----ORM  (Object Relational Mapping)   python 通过 ORM 操作 mysql

```python
# 需要在 cmd 中
# ipython
# In [1]: from sql1 import Table2

# In [2]: from sql1 import engine

# In [3]: Table2.metadata.create_all(engine)



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import pymysql


engine = create_engine('mysql+pymysql://用户名:密码@localhost:3306/数据库名')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Table2(Base):
	"""docstring for ClassName"""
	__tablename__ = "table2"      # table名
	id = Column(Integer, primary_key=True)
	name = Column(String(10), nullable=False)    #Column类创建一个字段
	age = Column(Integer, nullable=False)    
	gender = Column(String(5), )
	work = Column(String(10), )
    

class OrmTest(object):
	def __init__(self):
		self.session = Session()

	
	def add_one(self):
		"""新增一条记录"""
		new_obj = Table2(
            name = "wzw",
            age = "24",
            gender ="男",
            work = "student",
			)
		self.session.add(new_obj)
		self.session.commit()
		return new_obj


	def get_one(self):
		return self.session.query(Table2).get(1)


	def get_more(self):
		return self.session.query(Table2).filter_by(gender="男")


	def updata_data(self, id):
		"""修改单条数据"""
		new_obj = self.session.query(Table2).get(id)
		if new_obj:
			new_obj.name = "neinei"
			self.session.add(new_obj)
			self.session.commit()
			return True
		return False
    

	def updata_more_data(self):    
		# 修改多条数据
		data_list = self.session.query(Table2).filter_by(gender="男")
		for item in data_list:
		    item.name = "nei"
		    self.session.add(item)
		self.session.commit()
		return True


	def delete_data(self, id):
		new_obj = self.session.query(Table2).get(id)
		self.session.delete(new_obj)
		self.session.commit()


def main():
	obj = OrmTest()
	# result = obj.add_one()
	# print(result.id)

	# result = obj.get_one()
	# if result:
	#    print('name :{0} , age :{1}'.format(result.name, result.age))
	# else:
	#    print("not exist")

	# result = obj.get_more()
	# print(result.count())
	# for obj in result:
	# 	print('name :{0} , age :{1}'.format(obj.name, obj.age))

	# print(obj.updata_data(2))
	# print(obj.updata_more_data())
	
	obj.delete_data(3)


if __name__ == "__main__":
	main()
```
### pymysql  python 操作 mysql
```python
import pymysql


class Mysql(object):

    def __init__(self):
        self.get_connect()


    def get_connect(self):
        try:
            self.conn = pymysql.Connect(
                host='localhost',  # mysql服务器地址
                port=3306,  # mysql服务器端口号
                user='root',  # 用户名
                passwd='root',  # 密码
                db='awesome',  # 数据库名
                charset='utf8'  # 连接编码
            )
            # print('数据库已连接，对象为：{}'.format(self.conn))
        except pymysql.Error as e:
            print("Error:  {}".format(e))


    def close_connect(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print("Error:  {}".format(e))


    def get_one_data(self):
        """查询一条数据
        """
        sql = """select * from table1;"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        # self.conn.commit()  # 查询的话不需要commit
        # print(dir(cursor))
        # print(cursor.rowcount)
        # print(cursor.description)
        # result = cursor.fetchone()
        result = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # print(result)
        cursor.close()
        self.close_connect()
        return result


    def get_more_data(self):
        """查询多条数据
        """
        sql = """select * from table1;"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        
        # for row in cursor.fetchall():
        #     print(row)
        # ('li', 12, '男', None)
        # ('sk', 14, None, 'ibm')
        # ('ajjd', 34, '女', 'core')
        # ('fhh', 12, None, None)
        # ('wwe', 3, None, 'school')

        result = [dict(zip([k[0] for k in cursor.description], row))
                 for row in cursor.fetchall()]
        # print(result)
        cursor.close()
        self.close_connect()
        return result


    def get_more_by_page(self, page, page_size):
        """分页查询数据
        """
        offset = (page - 1) * page_size

        sql = """select * from table1 order by age asc limit %s, %s;"""
        cursor = self.conn.cursor()
        cursor.execute(sql, (offset, page_size))
        result = [dict(zip([k[0] for k in cursor.description], row))
                 for row in cursor.fetchall()]
        # print(result)
        cursor.close()
        self.close_connect()
        return result


    def insert_mysql(self):
        """insert数据
        """
        try:
            sql = """insert into table1 (name, age, gender, work) value (%s ,%s ,%s ,%s);"""
            cursor = self.conn.cursor()
            cursor.execute(sql, ('byr', 123, '男', 'station'))
            cursor.execute(sql, ('descr', 53, '女', 'space'))
            self.conn.commit()         # 别错写成self.cursor.commit()
            cursor.close()
        except:
            print("Error")
            self.cursor.callback()       
        self.close_connect()


def main():
    obj = Mysql()
    # result = obj.get_one_data()
    # print(result)
    
    # result = obj.get_more_data()
    # print(result)

    # result = obj.get_more_by_page(2, 3)   #  每页显示3个，查询第2页（页码从1开始，如果有7个数据，有123页，第三页只有1个数据）
    # for item in result: 
    #     print(item)

    obj.insert_mysql()

if __name__ == '__main__':
    main()
```
### python 连接数据库
```python

    # 连接数据库
    conn = pymysql.Connect(
        host='localhost',  # mysql服务器地址
        port=3306,  # mysql服务器端口号
        user='xxx',  # 用户名
        passwd='xxx',  # 密码
        db='xxx',  # 数据库名
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


MySQL 8.0.12 安装及使用配置

##  1 下载
https://dev.mysql.com/downloads/mysql/

选择ZIP Archive 版（简单、干净、免安装）的适合系统位数的版本进行下载

这里建议安装压缩包版本，需要**手动配置**点东西，不过会比较好用。

## 2 解压到某个目录c:\lxinstall\MySQL\mysql下

## 3 添加环境变量（可选）
#### 配置环境变量的目的是：不用每次启动mysql时都将目录切换到c:\lxinstall\MySQL\mysql\bin目录下，只需在C:\Users\linuix>下输入mysql -u root -p 即可登录。
    操作如下：
      右键单击我的电脑->属性->高级系统设置(高级)->环境变量
      点击系统变量下的新建按钮
      添加 c:\lxinstall\MySQL\mysql\bin
      
      
## 4 c:\lxinstall\MySQL\mysql 新建配置文件 my.ini

我下载的版本解压后没有默认配置文件my-default.ini，所以自己新建 `my.ini` 配置文件，具体内容如下，按照菜鸟教程http://www.runoob.com/mysql/mysql-install.html

不用新建 C:\lxinstall\MySQL\mysql\data 文件夹
```
[mysqld]
# 设置3306端口
port=3306

# 设置mysql的安装目录                     # 注意修改这两处地方
basedir=C:\lxinstall\MySQL\mysql
# 设置mysql数据库的数据的存放目录
datadir=C:\lxinstall\MySQL\mysql\data     # 此文件夹data 不用自己新建，后续初始化时自动建，不然会出错


# 允许最大连接数
max_connections=200
# 允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统
max_connect_errors=10
# 服务端使用的字符集默认为UTF8
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# 默认使用“mysql_native_password”插件认证
default_authentication_plugin=mysql_native_password

[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8

[client]
# 设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8
```

### 5 启动 MySQL 数据库

以**管理员身份** 切到 `C:\lxinstall\MySQL\mysql\bin` 否则会出[安装mysql Install/Remove of the Service Denied!错误的解决办法](https://blog.csdn.net/lxpbs8851/article/details/14161935/)打开 cmd 命令行工具，切换到目录C:\lxinstall\MySQL\mysql\bin下：

 ` mysqld install`         如果提示成功，说明安装成功了，若提示找不到msvcp140.dll
 
 [原因是没有安装VC++2015的版本库。下载地址：](https://www.microsoft.com/en-us/download/details.aspx?id=53587)

 `mysqld --initialize`    注意: 在 5.7 需要初始化 data 目录,否则会出现[mysql服务无法启动 服务没有报告任何错误解决方法](https://blog.csdn.net/liyangyang0528/article/details/54233632)

总之先初始化再启动。

**启动mysql服务有两种方法**

  1 初始化后再运行 `net start mysql` 即可启动 mysql。

  2 计算机图标上右键-->管理-->服务和应用程序-->服务，找到mysql的服务，点击启动即可。

## 6 修改mysql临时密码为自己设置的密码
`输入：mysqld–initialize，初始化data文件`这一步骤中会生成一个mysql临时登录密码。在data文件夹下生成有一个`电脑名.lerr`为后缀的文件。

用记事本打开，临时密码位于文件的最后一行，[Note] A temporary password is generated for root@localhost: E7203xxdQ.FP

将此密码复制保存(一会改密码时需要这个密码登录)

在cmd输入：

`C:\Users\linuix>mysql -u root -p`                                     登录MySQL修改改密码,将刚才复制的密码E7203xxdQ.FP粘贴进去，回车。

`Enter password:*******`

`mysql>`

然后MySQL欢迎界面后，接着输入：

`mysql>set password =password('用户自己设置的密码，比如root');`           单引号中的内容就是自己的密码，可以改成自己想要的密码。

或者

`alter user 'root'@'localhost' identified with mysql_native_password by 'newpassword';`
 
`mysql>exit;`

用新密码重新登录
```
C:\Users\linuix>mysql  -u root -p
Enter password: ****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.12 MySQL Community Server - GPL

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

