import pymysql

# 链接数据库
conn = pymysql.connect(host='localhost',user='root',password='xdsxdsxds',database='pymysql_demo',port=3306)
# 指定光标
cursor = conn.cursor()
# 这个是更新数据的sql
# sql = """
# delete from user where id=1
# """
# 这个是删除数据的sql
sql = """
update user set username='aaa' where id=1
"""

cursor.execute(sql)
# 插入、删除、更新都需要执行commit操作
conn.commit()




conn.close()