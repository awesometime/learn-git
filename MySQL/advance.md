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

### 工程1 mysql生成千万级的测试数据--利用MYSQL存储过程

[mysql生成千万级的测试数据](https://blog.csdn.net/dennis211/article/details/78076399)
