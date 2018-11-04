import pandas as pd
import pymysql
mysql_cn= pymysql.connect(host='localhost', port=3306,user='root', passwd='root', db='demodjango')
sql="select * from message_usermessage;"
df = pd.read_sql(sql, con=mysql_cn)
mysql_cn.close()

df.to_csv('demo.csv', encoding='utf-8', index=False)
#index=False表示导出时去掉行名称，如果数据中含有中文，一般encoding指定为‘utf-8’