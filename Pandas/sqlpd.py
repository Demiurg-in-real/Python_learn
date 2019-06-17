import pandas as pd
import mysql.connector as sql

db_connection=sql.connect(host='hostname',database='db_name', user='username', password='password')
df=pd.read_sql('SELECT * FROM table_name', con=db_connection)


#Less efficient 
#db_cursor=db_connection.cursor()
#db.cursor.execute('SELECT * FROM table_name')
#table_rows=db_cursor.fetchall()
#df=pd.DataFrame(table_rows)

import MySQLdb
mysql_cn= MySQLdb.connect(host='myhost',
                port=3306,user='myusername', passwd='mypassword',
                db='information_schema')
df_mysql = pd.read_sql('select * from VIEWS;', con=mysql_cn)
print 'loaded dataframe from MySQL. records:', len(df_mysql)
mysql_cn.close()
