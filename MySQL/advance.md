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
