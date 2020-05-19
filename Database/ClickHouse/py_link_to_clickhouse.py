# 该模块实现功能：将csv文件通过tcp连接方式导入到clickhouse

import datetime
import time
import pandas as pd
from clickhouse_driver import Client

start_time = time.time()
# connect ClickHouse
client = Client(host="10.x.x.x", port=8000, database="ln", user='default', password='')
# database 中应该事先建立对应的table表
# client.execute("select 1")
print("linked")

insert_sql = "insert into ln.log (log_date, name, house, model, role, num, arm_num) values"

csv_name = "aa.csv"  # todo
df = pd.read_csv(csv_name, sep='|', header=None)
# print(df)

csv_total_list = []
for row in df.itertuples():
    row_list = []
    date = datetime.datetime.strptime(row[1], '%Y-%m-%d').date()
    ip = row[2]
    warehouse = row[3]
    role = row[4]
    model = row[5]
    s = row[6]
    w = row[7]
    row_list.append(date)
    row_list.append(ip)
    row_list.append(warehouse)
    row_list.append(model)
    row_list.append(role)
    row_list.append(s)
    row_list.append(w)
    # print(row_list)
    csv_total_list.append(row_list)

# print(len(csv_total_list))
# print(csv_total_list)
try:
    result = client.execute(insert_sql, csv_total_list, types_check=True)
    print(result)
except Exception as e:
    print(e)
end_time = time.time()
print("save to clickhouse cost " + str(end_time - start_time))
