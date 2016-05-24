#connect to mysqwl
import mysql.connector
from mysql.connector import Error
#http://www.mysqltutorial.org/python-connecting-mysql-databases/




HOST = '23.236.54.228' #see above link for better handling of this configuration
DATABASE = 'darts'
USER = 'root'
PASSWORD = 'GI4FAOjq510dut2q'

conn = mysql.connector.connect(host=HOST,database=DATABASE,user=USER,password=PASSWORD)


def query_with_fetchall(query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
    	cursor.close()
        conn.close()

query_with_fetchall("select * from darters")



# def insert_many(query, values):
#     try:
#         cursor = conn.cursor()
#         cursor.executemany(query, values)
#         conn.commit()
#     except Error as e:
#         print('Error:', e)
 
#     finally:
#         cursor.close()
#         conn.close()
 


# query = "INSERT INTO darters(slack_alias,name) VALUES(%s, %s)"
# values = [('kbeckhar', 'kevin G'),
# 		('jbec','Jim Beck'),
# 		('ikske','Jolly Ben')]

# insert_many(query,values)