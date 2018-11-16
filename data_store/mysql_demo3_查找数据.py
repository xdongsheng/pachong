import pymysql

# 链接数据库
conn = pymysql.connect(host='localhost',user='root',password='xdsxdsxds',database='pymysql_demo',port=3306)
# 添加光标
cursor =conn.cursor()

sql = """
select * from user
"""
cursor.execute(sql)
result = cursor.fetchone()
print(result)
results = cursor.fetchall()
print(results)
resultm = cursor.fetchmany(2)
print(resultm)

conn.close()