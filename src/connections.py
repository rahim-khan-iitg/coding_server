import pymysql as mysql

def connect():
    conn=mysql.connect(host="localhost",user="rahim",password="rahim123",database="codeverse")
    # cur.execute("select * from user")
    # for i in cur:
    #     print(i)
    # conn.close()
    return conn
