数据库部分
CREATE TABLE walle_log_afs
(
    `log_date` Date, 
    `switch_name` String, 
    `switch_warehouse` String, 
    `switch_model` String, 
    `switch_role` String, 
    `syslog_num` Int32, 
    `alarm_num` Int32
)
ENGINE = MergeTree(log_date, (switch_name, log_date), 8192)

ClickHouse深度揭秘 
https://www.sohu.com/a/361343972_100253472


clickhouse-driver
https://github.com/mymarilyn/clickhouse-driver
