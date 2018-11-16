import pymysql

# 链接数据库
conn = pymysql.connect(host='localhost',user='root',password='xdsxdsxds',database='pymysql_demo',port=3306)
# 添加光标
cursor =conn.cursor()
# 执行sql语句
cursor.execute("select * from user")
# 得到结果
result = cursor.fetchall()

print(result)
conn.close()