MyBatis 知识体系
总链接 https://www.cnblogs.com/ashleyboy/category/1246107.html
- 入门简介   https://www.cnblogs.com/ashleyboy/p/9255153.html
- Mapper映射文件
- 动态SQL
- Mapper接口动态代理
- 关联查询
- 延迟加载
- 缓存机制

```
一、入门简介

MyBatis简介
Mybatis是Apache的一个Java开源项目，是一个支持动态Sql语句的持久层框架。Mybatis可以将Sql语句配置在
XML文件中，避免将Sql语句硬编码在Java类中。与JDBC相比：
Mybatis通过参数映射方式，可以将参数灵活的配置在SQL语句中的配置文件中，避免在Java类中配置参数（JDBC）
Mybatis通过输出映射机制，将结果集的检索自动映射成相应的Java对象，避免对结果集手工检索（JDBC）
Mybatis可以通过Xml配置文件对数据库连接进行管理。


MyBatis整体架构及运行流程
Mybatis整体构造由 数据源配置文件、Sql映射文件、会话工厂、会话、执行器和底层封装对象组成。

1.数据源配置文件
SqlMapConfig.xml

2.Sql映射文件
Mapper.xml

3.会话工厂与会话
Mybatis中会话工厂SqlSessionFactory类可以通过加载资源文件，读取数据源配置SqlMapConfig.xml
信息，从而产生一种可以与数据库交互的会话实例SqlSession，会话实例SqlSession根据Mapper.xml
文件中配置的sql,对数据库进行操作。

4.运行流程
会话工厂SqlSessionFactory通过加载资源文件获取SqlMapConfig.xml配置文件信息，然后生成可以与
数据库交互的会话实例SqlSession。会话实例可以根据Mapper配置文件中的Sql配置去执行相应的增删改
查操作。在SqlSession会话实例内部，通过执行器Executor对数据库进行操作，Executor依靠封装对象
Mappered Statement，它分装了从mapper.xml文件中读取的信息（sql语句，参数，结果集类型）。
Mybatis通过执行器与Mappered Statement的结合实现与数据库的交互。
执行流程图：



三、动态SQL

```
