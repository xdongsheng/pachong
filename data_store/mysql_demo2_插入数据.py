import pymysql

# 链接数据库
conn = pymysql.connect(host='localhost',user='root',password='xdsxdsxds',database='pymysql_demo',port=3306)
# 添加光标
cursor =conn.cursor()
# 执行sql语句
# sql = """
# insert into user(id,username,age,password) values(2,'bbb',20,'22222')
# """
# cursor.execute(sql)
# conn.commit()


sql = """
insert into user(id,username,age,password) values(null,%s,%s,%s)
"""

username = 'spider'
age = 21
password = '12345'
cursor.execute(sql,(username,age,password))
conn.commit()

conn.close()