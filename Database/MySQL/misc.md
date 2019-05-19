①②

- [索引](#索引)
- [锁](#锁)
- [事务](#事务)
- [执行流程](#执行流程)
- [存储引擎](#存储引擎)
- [视图](#视图)
- [MySQL优化系列](#MySQL优化系列)
- [misc](#misc)


## 执行流程

> 架构

[![架构](https://github.com/awesometime/learn-git/blob/master/Database/MySQL/mysql_architecture.png)](https://github.com/awesometime/learn-git/blob/master/Database/MySQL/mysql_architecture.png)

> Server层

连接器

查询缓存

分析器
 
优化器 选择索引是优化器的工作

执行器 


> 存储引擎




## 存储引擎

> InnoDB

- 支持行锁，采用MVCC(Multi-Version Concurrency Control, 多版本并发控制)来支持高并发，有可能死锁
- 支持事务(Transaction):ACID(Atomicity、Consistency、Isolation、Durability, 即原子性、一致性、隔离性、持久性)
- 支持外键
- 支持崩溃后的安全恢复
- 不支持全文索引

> MyISAM

- **不支持行锁(MyISAM只有表锁)**,读取时对需要读到的所有表加锁，写入时则对表加排他锁；
- **不支持事务**
- **不支持外键**
- **不支持崩溃后的安全恢复**
- 在表有读取查询的同时，支持往表中插入新纪录
- 支持BLOB和TEXT的前500个字符索引，支持**全文索引**
- **支持延迟更新索引**，极大地提升了写入性能
- 对于不会进行修改的表，支持**压缩表** ，极大地减少了磁盘空间的占用
- MyISAM 索引文件和数据文件是分离的，索引文件仅保存数据记录的地址。

> MEMORY

支持Hash索引，内存表，Memory引擎将数据存储在内存中，表结构不是存储在内存中的，查询时不需要执行磁盘I/O操作，

所以要比MyISAM和InnoDB快很多倍，但是数据库断电或是重启后，表中的数据将会丢失，表结构不会丢失。

> 常见对比

1) count运算上的区别： 因为MyISAM缓存有表meta-data（行数等），因此在做COUNT(\*)
时对于一个结构很好的查询是不需要消耗多少资源的。而对于InnoDB来说，则没有这种缓存。

2) 是否支持事务和崩溃后的安全恢复： 
MyISAM 强调的是性能，每次查询具有原子性,其执行数度比InnoDB类型更快，但是不提供事务支持。
InnoDB 提供事务支持事务，外部键等高级数据库功能。 具有事务(commit)、回滚(rollback)和崩溃修复能力(crash recovery capabilities)的事务安全(transaction-safe (ACID compliant))型表。

3)是否支持外键： MyISAM不支持，而InnoDB支持。

4)MyISAM更适合读密集的表，而InnoDB更适合写密集的的表。 在数据库做主从分离的情况下，经常选择MyISAM作为主库的存储引擎。

1) 存储结构 
MyISAM：每个MyISAM在磁盘上存储成三个文件。第一个文件的名字以表的名字开始，扩展名指出文件类型。.frm文件存储表定义。数据文件的扩展名为.MYD (MYData)。索引文件的扩展名是.MYI (MYIndex)。 
InnoDB：所有的表都保存在同一个数据文件中（也可能是多个文件，或者是独立的表空间文件），InnoDB表的大小只受限于操作系统文件的大小，一般为2GB。

2) 存储空间 
MyISAM：可被压缩，存储空间较小。支持三种不同的存储格式：静态表(默认，但是注意数据末尾不能有空格，会被去掉)、动态表、压缩表。 
InnoDB：需要更多的内存和存储，它会在主内存中建立其专用的缓冲池用于高速缓冲数据和索引。

3.可移植性、备份及恢复 
MyISAM：数据是以文件的形式存储，所以在跨平台的数据转移中会很方便。在备份和恢复时可单独针对某个表进行操作。 
InnoDB：免费的方案可以是拷贝数据文件、备份 binlog，或者用 mysqldump，在数据量达到几十G的时候就相对痛苦了。

4.事务支持 
MyISAM：强调的是性能，每次查询具有原子性,其执行速度比InnoDB类型更快，但是不提供事务支持。 
InnoDB：提供事务支持事务，外部键等高级数据库功能。 具有事务(commit)、回滚(rollback)和崩溃修复能力(crash recovery capabilities)的事务安全(transaction-safe (ACID compliant))型表。

5.AUTO_INCREMENT 
MyISAM：可以和其他字段一起建立联合索引。引擎的自动增长列必须是索引，如果是组合索引，自动增长可以不是第一列，他可以根据前面几列进行排序后递增。 
InnoDB：InnoDB中必须包含只有该字段的索引。引擎的自动增长列必须是索引，如果是组合索引也必须是组合索引的第一列。

6.表锁差异 
MyISAM：只支持表级锁，用户在操作myisam表时，select，update，delete，insert语句都会给表自动加锁，如果加锁以后的表满足insert并发的情况下，可以在表的尾部插入新的数据。 
InnoDB：支持事务和行级锁，是innodb的最大特色。行锁大幅度提高了多用户并发操作的新能。但是InnoDB的行锁，只是在WHERE的主键是有效的，非主键的WHERE都会锁全表的。

7.全文索引 
MyISAM：支持 FULLTEXT类型的全文索引 
InnoDB：不支持FULLTEXT类型的全文索引，但是innodb可以使用sphinx插件支持全文索引，并且效果更好。

8.表主键 
MyISAM：允许没有任何索引和主键的表存在，索引都是保存行的地址。 
InnoDB：如果没有设定主键或者非空唯一索引，就会自动生成一个6字节的主键(用户不可见)，数据是主索引的一部分，附加索引保存的是主索引的值。

9.表的具体行数 
MyISAM：保存有表的总行数，如果select count(*) from table;会直接取出出该值。 
InnoDB：没有保存表的总行数，如果使用select count(*) from table；就会遍历整个表，消耗相当大，但是在加了wehre条件后，myisam和innodb处理的方式都一样。

10.CURD操作 
MyISAM：如果执行大量的SELECT，MyISAM是更好的选择。 
InnoDB：如果你的数据执行大量的INSERT或UPDATE，出于性能方面的考虑，应该使用InnoDB表。DELETE 从性能上InnoDB更优，但DELETE FROM table时，InnoDB不会重新建立表，而是一行一行的删除，在innodb上如果要清空保存有大量数据的表，最好使用truncate table这个命令。



> misc

InnoDB的redo log写满了。这时候系统会停止所有更新操作，把checkpoint往前推进，redo log留出空间可以继续写。



## 索引

> Mysql索引使用的数据结构主要有B+Tree索引和Hash索引

索引可以加快数据库的检索速度,索引需要占物理和数据空间。

表经常进行INSERT/UPDATE/DELETE操作就不要建立索引了，换言之：索引会降低插入、删除、修改等维护任务的速度。

Mysql索引使用的数据结构主要有**B+Tree索引**和**Hash索引** 

在有大量重复键值情况下，哈希索引的效率也是极低的---->哈希碰撞问题

(**二分查找**O(log<sub>2</sub>n)要求被检索数据有序，而**二叉树查找**O(log<sub>2</sub>n)只能应用于二叉查找树上)

> **B+Tree**

> [索引的物理存储](https://www.jianshu.com/p/1775b4ff123a)

MySql  InnoDB的数据是按数据页为单位来读写的。也就是说，当需要读一条记录的时候，并不是

将这个记录本身从磁盘读出来，而是以页为单位，将其整体读入内存。在InnoDB中，每个

数据页的大小默认是16KB。各个数据页可以组成一个双向链表 每个数据页中的记录又可以组成一个单向链表

我们假设一个非页子节点是 16kb，每个索引，即主键是 bigint，即 8b，指针为 8b。那么每页能存储大约 1000 个索引（16kb/ 8b + 8b）.

大约能够存储 10 亿个索引。通常 B+ 树的高度在 2-4 层，由于 MySql 在运行时，**根节点是常驻内存的**，因此每次查找只需要大约 2 -3 次 IO。

可以说，B+ 树的设计，就是根据机械磁盘的特性来进行设计的。每一页中可使用二分查找,前提有序。

> Mysql的BTree索引使用的是B数中的B+Tree，但对于主要的两种存储引擎的实现方式是不同的。

- MyISAM: 

MyISAM，索引文件和数据文件是分离的，B+Tree叶节点的data域存放的是数据记录的地址。在索引检索的时候，

首先按照B+Tree搜索算法搜索索引，如果指定的Key存在，则取出其 data 域的值，然后以 data 域的值为地址读取相应的数据记录。

- InnoDB: 

InnoDB数据文件本身就是索引文件,表数据文件本身就是按B+Tree组织的一个索引结构，树的叶节点data域保存了完整的数据记录。

这个索引的key是数据表的主键，因此InnoDB表数据文件本身就是主索引。这被称为**聚集索引）**。

而其余的索引都作为**非聚集索引**，辅助索引的data域存储相应记录主键的值。

**在根据聚集索引搜索时，直接找到key所在的节点即可取出数据；**

**在根据非聚集索引查找时，则需要先取出主键的值，再走一遍主索引,也就是回表。**

因此，在设计表的时候，不建议使用过长的字段作为主键，也不建议使用非单调的字段作为主键，这样会造成主索引频繁分裂。

聚集索引就是以主键创建的索引

非聚集索引就是以非主键创建的索引

> 索引分类 

- 普通索引：最基本的索引，没有任何约束。
- 唯一索引：与普通索引类似，但具有唯一性约束。
- 主键索引：特殊的唯一索引，不允许有空值。
- 复合索引：将多个列组合在一起创建索引，可以覆盖多个列。
- 外键索引：只有InnoDB类型的表才可以使用外键索引，保证数据的一致性、完整性和实现级联操作。
- 全文索引：MySQL 自带的全文索引只能用于 InnoDB、MyISAM ，并且只能对英文进行全文检索，一般使用全文索引引擎（ES，Solr）。

> 索引最左匹配原则

> 索引优化

1) 最左前缀匹配原则。这是非常重要、非常重要、非常重要（重要的事情说三遍）的原则，MySQL会一直向右匹配直到遇到范围查询（>,<,BETWEEN,LIKE）就停止匹配。
2) 尽量选择区分度高的列作为索引，区分度的公式是 COUNT(DISTINCT col) / COUNT(\*)。表示字段不重复的比率，比率越大我们扫描的记录数就越少。
3) 索引列不能参与计算，尽量保持列“干净”。比如，FROM_UNIXTIME(create_time) = '2016-06-06' 就不能使用索引，原因很简单，B+树中存储的都是数据表中的字段值，但是进行检索时，需要把所有元素都应用函数才能比较，显然这样的代价太大。所以语句要写成 ： create_time = UNIX_TIMESTAMP('2016-06-06')。
4) 尽可能的扩展索引，不要新建立索引。比如表中已经有了a的索引，现在要加（a,b）的索引，那么只需要修改原来的索引即可。
5) 单个多列组合索引和多个单列索引的检索查询效果不同，因为在执行SQL时，MySQL只能使用一个索引，会从多个单列索引中选择一个限制最为严格的索引。


> misc

唯一索引用不上change buffer的优化机制，因此如果业务可以接受，从性能角度出发我建议你优先考虑普通索引。

主键 键 索引是自己指定的
但使用哪个索引是由MySQL来确定的
覆盖索引


- 前缀索引
直接创建完整索引，这样可能比较占用空间；

创建前缀索引，节省空间，但会增加查询扫描次数，并且不能使用覆盖索引；

倒序存储，再创建前缀索引，用于绕过字符串本身前缀的区分度不够的问题；

创建hash字段索引，查询性能稳定，有额外的存储和计算消耗，跟第三种方式一样，都不支持范围扫描。


## 锁

[![锁分类](https://github.com/awesometime/learn-git/blob/master/Database/MySQL/mysql_lock.jpg)](https://github.com/awesometime/learn-git/blob/master/Database/MySQL/mysql_lock.jpg)

> 全局锁

主要用在逻辑备份过程中

> 表锁

Mysql的行锁和表锁（ 锁是计算机协调多个进程或纯线程并发访问某一资源的机制）

表级锁： 每次操作锁住整张表。开销小，加锁快；不会出现死锁；锁定粒度大，发生锁冲突的概率最高，并发度最低；

> 行锁

行级锁： 每次操作锁住一行数据。开销大，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低，并发度也最高；

> 事务隔离级别

SQL标准的事务隔离级别包括：读未提交（read uncommitted）、读提交（read committed）、**可重复读（repeatable read）**和串行化（serializable ）

- 读未提交是指，一个事务还没提交时，它做的变更就能被别的事务看到。

- 读提交是指，一个事务提交之后，它做的变更才会被其他事务看到。

- **可重复读**是指，一个事务执行过程中看到的数据，总是跟这个事务在启动时看到的数据是一致的。当然在可重复读隔离级别下，未提交变更对其他事务也是不可见的。

**mysql的默认级别。整个事务过程中，对同一笔数据的读取结果是相同的，不管其他事务是否在对共享数据进行更新，也不管更新提交与否。**

- 串行化，顾名思义是对于同一行记录，“写”会加“写锁”，“读”会加“读锁”。当出现读写锁冲突的时候，后访问的事务必须等前一个事务执行完成，才能继续执行。

> 不同事务级别带来的并发问题

当数据库上有多个事务同时执行的时候，就可能出现脏读（dirty read）、不可重复读（non-repeatable read）、幻读（phantom read）的问题，

为了解决这些问题，就有了“隔离级别”的概念。隔离得越严实，效率就会越低。因此很多时候，我们都要在二者之间寻找一个平衡点。

- 脏读：一个事务读取到另外一个事务未提交的数据

- 不可重复读：一个事务读取到另外一个事务已经提交的数据，也就是说一个事务可以看到其他事务所做的修改(重复读到的数据不一致即对于我们来说是不可重复读)

- 幻读：是指在一个事务内读取到了别的事务插入的数据，导致前后读取不一致。

||dirty read|non-repeatable read|phantom read|
|-|-|-|-|
|read uncommitted|√|√|√|
|read committed|×|√|√|
|repeatable read|×|×|√|
|serializable|×|×|×|


当内存数据页跟磁盘数据页内容不一致的时候，我们称这个内存页为“脏页”。内存数据写入到磁盘后，内存和磁盘上的数据页的内容就一致了，称为“干净页”。
不论是脏页还是干净页，都在内存中。

如果要收缩一个表，只是delete掉表里面不用的数据的话，表文件的大小是不会变的，你还要通过alter table命令重建表，才能达到表文件变小的目的。






## mysql优化系列

[mysql优化系列](https://blog.csdn.net/Jack__Frost/article/details/72571540)



## misc
```
------------------------------
建一个表，表里有a、b两个字段，并分别建上索引
CREATE TABLE `table_3` (
  `id` int(11) NOT NULL,
  `a` int(11) DEFAULT NULL,
  `b` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `a` (`a`),
  KEY `b` (`b`)
) ENGINE=InnoDB;

用存储过程来插入数据
delimiter ;;
create procedure idata_001()
begin
  declare i int;
  set i=1;
  while(i<=100000)do
    insert into table_3 values(i, i, i);
    set i=i+1;
  end while;
end;;
delimiter ;
call idata_001();
Query OK, 1 row affected (24 min 28.31 sec)


select * from t where a between 10000 and 20000;
explain select * from t where a between 10000 and 20000;

show index from table;
alter table SUser add index index1(email);

select count(distinct email) as L from SUser;
select 
  count(distinct left(email,4)）as L4,
  count(distinct left(email,5)）as L5,
  count(distinct left(email,6)）as L6,
  count(distinct left(email,7)）as L7,
from SUser;
```
