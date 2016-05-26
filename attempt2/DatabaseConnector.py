# from http://www.mysqltutorial.org/python-connecting-mysql-databases/

from ConfigManager import get_config_value
import mysql.connector
from mysql.connector import Error

HOST = get_config_value('host')
DATABASE = get_config_value('database')
USER = get_config_value('user')
PASSWORD = get_config_value('password')


conn = mysql.connector.connect(host=HOST,database=DATABASE,user=USER,password=PASSWORD)

    
def read(query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()


        records = []
        for row in rows:
            records.append(row)
            
        return records 

    except Error as e:
        print(e)

    cursor.close()
    conn.close()


def insert(query, values):
    """
    example:
    query = "INSERT INTO darters(slack_alias,name) VALUES(%s, %s)"
    values = [('kbeckhar', 'kevin G'), ('bill', 'bill schmidt')]"""
    
    try:
        cursor = conn.cursor()
        cursor.executemany(query, values)
        conn.commit()
    except Error as e:
        print('Error:', e)
 

    cursor.close()
    conn.close()


   