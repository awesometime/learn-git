```
SELECT语句的完整语法为： 
SELECT[ALL|DISTINCT|DISTINCTROW|TOP] 
{*|talbe.*|[table.]field1[AS alias1][,[table.]field2[AS alias2][,…]]} 
FROM tableexpression[,…][IN externaldatabase] 
[WHERE…] 
[GROUP BY…] 
[HAVING…] 
[ORDER BY…] 
[WITH OWNERACCESS OPTION] 
说明： 
用中括号([])括起来的部分表示是可选的，用大括号({})括起来的部分是表示必须从中选择其中的一个。
```
### 去重
数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行

select  distinct  name  from  student
### group by

```
mysql> select product_color,count(product_color) from jd_bar group by product_color;
+---------------+----------------------+
| product_color | count(product_color) |
+---------------+----------------------+
| 灰色          |                 2439 |
| 白色          |                  612 |
| 粉色          |                 1440 |
| 紫色          |                 3150 |
| 红色          |                  763 |
| 肤色          |                 8612 |
| 蓝色          |                 1402 |
| 黑色          |                 4902 |
+---------------+----------------------+
8 rows in set (0.06 sec)

mysql> select * from jd_bar where product_color='香槟色';
Empty set (0.05 sec)

mysql> select * from jd_bar where product_color='肤色';
有结果......

mysql> select product_size,count(product_size) from jd_bar group by product_size;
+--------------+---------------------+
| product_size | count(product_size) |
+--------------+---------------------+
| NULL         |                   0 |
| A            |                4346 |
| B            |               12592 |
| C            |                3165 |
| D            |                 377 |
+--------------+---------------------+
5 rows in set (0.10 sec)

**注意此处   group by product_color
mysql> select product_size,count(product_size) from jd_bar group by product_color;
+--------------+---------------------+
| product_size | count(product_size) |
+--------------+---------------------+
| C            |                2342 |
| A            |                 347 |
| B            |                1424 |
| B            |                3140 |
| C            |                 654 |
| B            |                6930 |
| B            |                1294 |
| A            |                4349 |
+--------------+---------------------+
8 rows in set (0.06 sec)

```
### order by

order by执行流程
```
CREATE TABLE `t` (
  `id` int(11) NOT NULL,
  `city` varchar(16) NOT NULL,
  `name` varchar(16) NOT NULL,
  `age` int(11) NOT NULL,
  `addr` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `city` (`city`)
) ENGINE=InnoDB;

select city,name,age from t where city='杭州' order by name limit 1000  ;


初始化sort_buffer，确定放入name、city、age这三个字段； # MySQL会给每个线程分配一块内存用于排序，称为sort_buffer。
从索引city找到第一个满足city='杭州’条件的主键id，也就是图中的ID_X；
到主键id索引取出整行，取name、city、age三个字段的值，存入sort_buffer中；
从索引city取下一个记录的主键id；
重复步骤3、4直到city的值不满足查询条件为止，对应的主键id也就是图中的ID_Y；
对sort_buffer中的数据按照字段name做快速排序；     全字段排序
按照排序结果取前1000行返回给客户端。
```
```
mysql> select * from table1 order by age asc limit 0,3;   # limit 偏移量，每页显示个数
+------+-----+--------+--------+
| name | age | gender | work   |
+------+-----+--------+--------+
| wwe  |   3 | NULL   | school |
| li   |  12 | 男     | NULL   |
| fhh  |  12 | NULL   | NULL   |
+------+-----+--------+--------+
3 rows in set

mysql> select * from table1 order by age asc limit 3,3;
+-------+-----+--------+-------+
| name  | age | gender | work  |
+-------+-----+--------+-------+
| sk    |  14 | NULL   | ibm   |
| apple |  23 | NULL   | Apple |
| ajjd  |  34 | 女     | core  |
+-------+-----+--------+-------+
3 rows in set

mysql> select * from table1 order by age asc limit 6,3;
+--------+-----+--------+------+
| name   | age | gender | work |
+--------+-----+--------+------+
| banaba |  67 | 男     | NULL |
+--------+-----+--------+------+
1 row in set
```
### inner join、left join、right join、full outer join、union、union all

[图解SQL的inner join、left join、right join、full outer join、union、union all的区别](https://www.cnblogs.com/logon/p/3748020.html)

### 工程1 mysql 生成千万级的测试数据--利用MYSQL存储过程

[mysql生成千万级的测试数据](https://blog.csdn.net/dennis211/article/details/78076399)

### 工程2 mysql 生成十万条量的，三张关联表，并查询

```mysql
mysql 生成十万条量的，三张关联表，并查询
参考https://blog.csdn.net/simplexingfupeng/article/details/79474214
https://www.cnblogs.com/liangwh520/p/8299744.html
--------------------------------------
不用内存MEMORY    实测10万条数据用5min
通过内存MEMORY    实测10万条数据用1秒
--------------------------------------
学生表
--------------------------------------
create table students_memory(
 sid int primary key auto_increment,
 sname varchar(100) not null,
 age int,
 address varchar(100),
 courseid int
 )ENGINE = MEMORY AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;



create table students(
 sid int primary key auto_increment,
 sname varchar(100) not null,
 age int,
 address varchar(100),
 courseid int
 )ENGINE = INNODB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;


DELIMITER //
CREATE FUNCTION `rand_string`(n INT) RETURNS varchar(255) CHARSET latin1
BEGIN 
DECLARE chars_str varchar(100) DEFAULT 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'; 
DECLARE return_str varchar(255) DEFAULT '' ;
DECLARE i INT DEFAULT 0; 
WHILE i < n DO 
SET return_str = concat(return_str,substring(chars_str , FLOOR(1 + RAND()*62 ),1)); 
SET i = i +1; 
END WHILE; 
RETURN return_str; 
END //



DELIMITER //
CREATE  PROCEDURE `add_students_memory`(IN n int)
BEGIN  
  DECLARE i INT DEFAULT 1;
    WHILE (i <= n ) DO
      INSERT into students_memory  (sname,age,address,courseid ) VALUEs (rand_string(20),FLOOR(RAND() * 100),10000+FLOOR(RAND() * 10) ,1000+FLOOR(RAND() * 10) );
			set i=i+1;
    END WHILE;
END //


DELIMITER ;
CALL add_students_memory(100000);

select count(*) from students_memory;
INSERT into students SELECT * from  students_memory;
select count(*) from students;
delete from students_memory;

mysql> select * from students limit 10,20;
+-----+----------------------+------+---------+----------+
| sid | sname                | age  | address | courseid |
+-----+----------------------+------+---------+----------+
|  11 | nyuDxDoUb1rZpYsbncGE |   91 | 10000   |     1006 |
|  12 | n9vSGF6lg6ByOeyWTrmk |   24 | 10007   |     1009 |
|  13 | ymYFdVPevDxAc5DKIavU |   66 | 10000   |     1004 |
|  14 | 1dQog1aBmOQEwvQuMgN2 |   48 | 10007   |     1004 |
|  15 | f6DIwgCaMgO4OGNNqzri |   84 | 10008   |     1006 |
|  16 | Ox7Ow1pPJ0GdSBfeizQm |   95 | 10001   |     1009 |
|  17 | DvwUOcm30LCD9IYyHEZP |   83 | 10001   |     1004 |
|  18 | TttPy7NqDHqSVSph0357 |   99 | 10000   |     1004 |
|  19 | d5AvEzKSY5mnDTpcAd6L |   17 | 10000   |     1007 |
|  20 | LVc0jnOK8hRgC6xcfrj5 |   17 | 10000   |     1008 |
|  21 | mviLOAkHpKkiitiSkThy |   65 | 10000   |     1003 |
|  22 | JZCUyTEpVhq79gJFYJxo |   99 | 10002   |     1004 |
|  23 | Ee09Bp4Xq4WjyJPK8gMV |   98 | 10006   |     1002 |
|  24 | icZcRwQy3t2zCcZdXWIB |   53 | 10003   |     1001 |
|  25 | NWaSGDXKG1Wqaoh6w7QI |   72 | 10009   |     1005 |
|  26 | 8mf19yaYgbZgbVXSjOW5 |   30 | 10007   |     1008 |
|  27 | 10NPzdcdlSb7V5xdlVo2 |   72 | 10009   |     1005 |
|  28 | fPhHwn8mh8EKBzWO6TZ5 |   20 | 10002   |     1004 |
|  29 | A5u1wl0R8TVLTZ7uUUFq |   81 | 10002   |     1000 |
|  30 | iO2CP4Knuado9prOzhxI |   59 | 10003   |     1008 |
+-----+----------------------+------+---------+----------+
20 rows in set (0.00 sec)

-------------------------------------------
老师表 |  不用内存  实测10万条数据用5min   |
-------------------------------------------
create table teachers(
tid int(5) primary key auto_increment,
tname varchar(100) not null,
age int(4),
address varchar(100),
courseid int
)engine=innodb auto_increment=101 DEFAULT CHARSET = utf8;


DELIMITER //
CREATE  PROCEDURE `add_teachers`(IN n int)
BEGIN  
  DECLARE i INT DEFAULT 1;
    WHILE (i <= n ) DO
      INSERT into teachers  (tname,age,address,courseid ) VALUEs (rand_string(5),FLOOR(RAND() * 100),10000+FLOOR(RAND() * 10) ,1000+FLOOR(RAND() * 10) );
			set i=i+1;
    END WHILE;
END //


DELIMITER ;
CALL add_teachers(100000);

select count(*) from teachers;

mysql> select * from teachers limit 10,20;
+-----+-------+------+---------+----------+
| tid | tname | age  | address | courseid |
+-----+-------+------+---------+----------+
| 111 | w3wiI |   40 | 10003   |     1005 |
| 112 | Imuco |    2 | 10004   |     1001 |
| 113 | wAc5H |   87 | 10007   |     1001 |
| 114 | E8AnX |   32 | 10002   |     1001 |
| 115 | nJkjo |   70 | 10008   |     1001 |
| 116 | e7Lkb |   57 | 10008   |     1003 |
| 117 | qrPBp |   90 | 10007   |     1002 |
| 118 | 2MELG |   81 | 10005   |     1000 |
| 119 | 09Dwz |   93 | 10004   |     1005 |
| 120 | ztyb3 |   43 | 10004   |     1000 |
| 121 | 7HYEb |   64 | 10001   |     1006 |
| 122 | gC9HU |   15 | 10005   |     1000 |
| 123 | 2icWW |   60 | 10006   |     1004 |
| 124 | p676Z |   34 | 10002   |     1000 |
| 125 | EALWf |   11 | 10002   |     1000 |
| 126 | CffjF |   11 | 10000   |     1007 |
| 127 | UA6zn |   87 | 10007   |     1009 |
| 128 | AxOiS |   16 | 10006   |     1008 |
| 129 | jsduG |   63 | 10006   |     1001 |
| 130 | TuAjF |    4 | 10007   |     1004 |
+-----+-------+------+---------+----------+
20 rows in set (0.00 sec)

-------------------------------------------
课程表
-------------------------------------------
create table courses(
cid int primary key auto_increment,
cname varchar(100) not null,
xuefen int,
tid int
)engine=innodb auto_increment = 1001 DEFAULT CHARSET = utf8;

create table courses_memory(
cid int primary key auto_increment,
cname varchar(100) not null,
xuefen int,
tid int
)engine=memory auto_increment = 1001 DEFAULT CHARSET = utf8;


DELIMITER //
CREATE  PROCEDURE `add_courses_memory`(IN n int)
BEGIN  
  DECLARE i INT DEFAULT 1;
    WHILE (i <= n ) DO
      INSERT into courses_memory  (cname,xuefen,tid ) VALUEs (1000+FLOOR(RAND() * 10),FLOOR(RAND() * 10),FLOOR(RAND() * 100000) );
			set i=i+1;
    END WHILE;
END //


DELIMITER ;
CALL add_courses_memory(100000);

select count(*) from courses_memory;
INSERT into courses SELECT * from  courses_memory;
select count(*) from courses;
delete from courses_memory;

mysql> select * from courses limit 10,20;
+------+-------+--------+-------+
| cid  | cname | xuefen | tid   |
+------+-------+--------+-------+
| 1011 | 1002  |      1 | 96697 |
| 1012 | 1004  |      2 |  1661 |
| 1013 | 1002  |      4 | 22084 |
| 1014 | 1008  |      5 | 21899 |
| 1015 | 1004  |      5 | 55662 |
| 1016 | 1000  |      5 | 61758 |
| 1017 | 1004  |      3 | 37740 |
| 1018 | 1008  |      2 | 51790 |
| 1019 | 1009  |      9 | 24251 |
| 1020 | 1002  |      4 | 41743 |
| 1021 | 1008  |      8 | 84691 |
| 1022 | 1006  |      6 | 48255 |
| 1023 | 1003  |      3 | 73781 |
| 1024 | 1005  |      7 | 99653 |
| 1025 | 1007  |      5 | 80164 |
| 1026 | 1002  |      7 | 22492 |
| 1027 | 1007  |      1 | 34991 |
| 1028 | 1003  |      8 | 92018 |
| 1029 | 1001  |      1 | 16671 |
| 1030 | 1004  |      5 | 49257 |
+------+-------+--------+-------+
20 rows in set (0.00 sec)

----------------------------
学生修了哪些课程
----------------------------
select s.sname,c.cid,c.cname
from students s left join courses c
on s.courseid = c.cid;
+----------------------+------+-------+
| sname                | cid  | cname |
+----------------------+------+-------+
| Tcccfuy7MqAuvW05eKT5 | 1008 | 1006  |
| ZCZUrj6npOCwBgmPUVHA | 1009 | 1003  |
| Vec7OBp2QURqnu82CO1z | 1001 | 1001  |
| jq1F6ovckTkKEQ7U1fYZ | NULL | NULL  |
| cgzUElF9x8SOgIDUqgRp | 1003 | 1009  |
| AkIt2DRhEhhmQW05gTxO | 1007 | 1007  |
| ffjHmzCd2oG6gTuAlORG | 1001 | 1001  |
| CRhHvetvW3gZ1ZKzqj5j | 1003 | 1009  |
| PsFOQGIoDP3EUsmknKtV | 1007 | 1007  |
| MWbZbQuJ4Xq8ctAmUjEa | 1005 | 1007  |
| nyuDxDoUb1rZpYsbncGE | 1006 | 1004  |
| n9vSGF6lg6ByOeyWTrmk | 1009 | 1003  |
| ymYFdVPevDxAc5DKIavU | 1004 | 1009  |
| 1dQog1aBmOQEwvQuMgN2 | 1004 | 1009  |
| f6DIwgCaMgO4OGNNqzri | 1006 | 1004  |

100000 rows in set (0.22 sec)
----------------------------
学生修的课程有哪些老师教
----------------------------
select s.sname,c.cid,c.cname,t.tname
from students s,courses c,teachers t
where s.courseid = c.cid and c.tid = t.tid;
+----------------------+------+-------+-------+
| sname                | cid  | cname | tname |
+----------------------+------+-------+-------+
| Tcccfuy7MqAuvW05eKT5 | 1008 | 1006  | A1cIR |
| ZCZUrj6npOCwBgmPUVHA | 1009 | 1003  | J51Ku |
| Vec7OBp2QURqnu82CO1z | 1001 | 1001  | UzXWD |
| cgzUElF9x8SOgIDUqgRp | 1003 | 1009  | YzJPK |
| AkIt2DRhEhhmQW05gTxO | 1007 | 1007  | nJoCJ |
| ffjHmzCd2oG6gTuAlORG | 1001 | 1001  | UzXWD |
| CRhHvetvW3gZ1ZKzqj5j | 1003 | 1009  | YzJPK |
| PsFOQGIoDP3EUsmknKtV | 1007 | 1007  | nJoCJ |
| MWbZbQuJ4Xq8ctAmUjEa | 1005 | 1007  | SkQ5H |
| nyuDxDoUb1rZpYsbncGE | 1006 | 1004  | 3sU1c |
| n9vSGF6lg6ByOeyWTrmk | 1009 | 1003  | J51Ku |
| ymYFdVPevDxAc5DKIavU | 1004 | 1009  | hkE5l |
| 1dQog1aBmOQEwvQuMgN2 | 1004 | 1009  | hkE5l |
| f6DIwgCaMgO4OGNNqzri | 1006 | 1004  | 3sU1c |
+----------------------+------+-------+-------+
90095 rows in set (0.27 sec)



select s.sname,c.cid,c.cname,t.tname
from students s inner join courses c inner join teachers t
on  s.courseid = c.cid and c.tid = t.tid;


----------------------------
truncate table 表名;   # 删除表数据  新建一个表头一样的表
max_heap_table_size=4000M
```
