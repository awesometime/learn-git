
注意：同MySQL使用Python的pymysql模块进行操作要先安装MySQL软件一样

MongoDB使用Python的pymongo模块时也需要先安装Mongo软件

### 1 NoSQL 简介

NoSQL(NoSQL = Not Only SQL )，意即"不仅仅是SQL"。

早期使用较多的是`关系数据库管理系统`（Relational Database Management System,RDBMS）。 

NoSQL 作为`非关系型的数据存储`是一项全新的数据库革命性运动，该词最早出现于1998年，发展至`2009年`趋势越发高涨。

NoSQL用于超大规模数据的存储。（例如谷歌或Facebook每天为他们的用户收集万亿比特的数据）。现在已经有很多公司使用了 NoSQL：Google Facebook  Adobe  LinkedIn

这些类型的数据存储不需要固定的模式，无需多余操作就可以横向扩展。

[NoSQL 简介](http://www.runoob.com/mongodb/nosql.html)

```
RDBMS vs NoSQL
RDBMS 
- 高度组织化结构化数据 
- 结构化查询语言（SQL） (SQL) 
- 数据和关系都存储在单独的表中。 
- 数据操纵语言，数据定义语言 
- 严格的一致性
- 基础事务transaction(ACID属性：A (Atomicity) 原子性  C (Consistency) 一致性  I (Isolation) 独立性  D (Durability) 持久性)
  [关系型数据库遵循ACID规则](http://www.runoob.com/mongodb/nosql.html)
NoSQL 
- 代表着不仅仅是SQL
- 没有声明性查询语言
- 没有预定义的模式
- 键 - 值对存储，列存储，文档存储，图形数据库
- 最终一致性，而非ACID属性，BASE原则
- 非结构化和不可预知的数据
- CAP定理 
- 高性能，高可用性和可伸缩性
```
```
NoSQL 数据库分类

列存储
**文档存储**               **MongoDB**
key-value存储
图存储
对象存储
xml数据库
```


### 2 MongoDB 引入

MongoDB 是一个基于`分布式文件存储`的`数据库`。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能`数据存储`解决方案。

MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是`非关系数据库`当中功能最丰富，最像关系数据库的。

`mysql`     关系数据库  由数据库（database）、表（table）、记录（record）三个层次概念组成，

`MongoDB`              由数据库（database）、集合（collection）、文档对象（document）三个层次组成。

[SQL  MongoDB  术语/概念类比](http://www.runoob.com/mongodb/mongodb-databases-documents-collections.html)

[MySQL与MongoDB的区别](https://blog.csdn.net/see__you__again/article/details/51995956)

[mongodb与mysql区别（超详细](https://blog.csdn.net/gjc_csdn/article/details/80419997)

### 3 MongoDB 语法      数据库层面  集合层面  文档层面
**连接、创建、删除数据库**
```
mongodb://localhost(:27017/)              使用默认端口来连接 MongoDB 的服务
mongodb://admin:123456@localhost/test     使用用户 admin 密码 123456 连接到本地localhost的 MongoDB 服务的指定数据库test上
> show dbs                                显示所有数据库的列表；注意：刚创建的数据库并不显示在数据库的列表中， 要显示它，我们需要向新建的数据库插入一些数据
> use 'db-name'                           如果数据库不存在，则创建数据库；存在则连接到一个指定的数据库
> db                                      显示当前数据库对象或**集合**
> db.dropDatabase()                       删除数据库
> db.'db-name'.insert({"name":"菜鸟教程"})
```
**集合**
```
> db.createCollection(" 'collection-name' ")        创建集合 
> show collections                                  显示集合
> db.'collection-name'.drop()                       删除集合
```
**文档----增删改查**
```
> db.COLLECTION_NAME.insert(document)                     如果集合COLLECTION_NAME不在该数据库中， MongoDB 会自动创建该集合；再插入文档document
> db.COLLECTION_NAME.find()                               查看已插入文档
> db.COLLECTION_NAME.save(document)                       可以指定 _id 字段。如果不指定 _id 字段 save() 方法类似于 insert() 方法。

> db.collection.remove(
   <query>,
   <justOne>
)

> db.collection.update(
    <query>,
    <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)

> db.collection.find(query, projection)
```
















