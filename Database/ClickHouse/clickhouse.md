### 知识
```
ClickHouse深度揭秘 
https://www.sohu.com/a/361343972_100253472

clickhouse-driver
https://github.com/mymarilyn/clickhouse-driver
```

### 操作


> 创建数据库
```
CREATE TABLE log
(
    `log_date` Date, 
    `sw_name` String, 
    `a_num` Int32
)
ENGINE = MergeTree(log_date, (sw_name, log_date), 8192)

CREATE TABLE log (log_date Date, sw_name String, a_num Int32) ENGINE=MergeTree(log_date, (sw_name, log_date), 8192)
```


> 写入数据库shell命令方式    将log.csv写入clickhouse
cat log.csv | clickhouse-client --format_csv_delimiter="|" --query="INSERT INTO database_name.table_name FORMAT CSV";


> 写入数据库python    将log.csv写入clickhouse
```
>>> from clickhouse_driver import Client
>>> import datetime
>>> client = Client(host="10.64.28.64", port=9000, database="lx")
client.execute('CREATE TABLE test (x Int32) ENGINE = Memory')
>>> client.execute("select 1")
>>> client.execute("select * from log")
[(datetime.date(2010, 3, 23), u'10.14.1.13', u'H', u'H-2304', u'DCore', 200, 30)]

>>> client.execute("""insert into lx.log (log_date, sw_name, sw_model, sw_role, log_num, alarm_num) VALUES""", [[datetime.datetime.strptime('2020-03-17', "%Y-%m-%d").date(), 'dog', 'H-04', 'ore', 200, 30]])

>>> insert_sql = "insert into lx.log (log_date, switch_name, sww, switch_model, switch_role, log_num, alarm_num) values"

>>> somedata = [
 [datetime.datetime.strptime('2010-03-23', '%Y-%m-%d').date(), '10.11.10.123', 'HB', 'H-04', 'T-DEV', 200, 30],
 [datetime.datetime.strptime('2010-03-21', '%Y-%m-%d').date(), '10.14.1.13', 'HD', 'H-2304', 'DEV', 4, 0]]

>>> insert_sql = "insert into lx.log (log_date, switch_name, sww, switch_model, switch_role, log_num, alarm_num) values"

>>> somedata_02 = [
[datetime.datetime.strptime('2010-03-23', '%Y-%m-%d').date(), '10.11.10.123', 'HZ', 'C-04', 'Core', 500, 30],

>>> client.execute(insert_sql, somedata, types_check=True)
```






