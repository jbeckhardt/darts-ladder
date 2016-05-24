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

    finally:
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
 
    finally:
        cursor.close()
        conn.close()

# def get_cleaned_records(records):
#     '''cleans the record data by taking the individual records out of tuples
#     and leaving it as strings

#     Note: only pertains to records from a single column'''
    
#     cleaned_records = []
#     for record in records:
#         cleaned_record = str(record)[3:-3]
#         cleaned_records.append(cleaned_record)
#     return cleaned_records


   