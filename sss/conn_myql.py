import pymysql
conn = pymysql.Connection(
    host="localhost",
    port=3306,
    user="root",
    password="ABdo15::",
    autocommit=True
)
cursor = conn.cursor()
conn.select_db("db_stu")
cursor.execute("select * from user; ")
result = cursor.fetchall()
print(result)
