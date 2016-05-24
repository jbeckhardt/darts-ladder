#get sql ids
import time
from slackclient import SlackClient
import mysql.connector
from mysql.connector import Error

HOST = '23.236.54.228' #see above link for better handling of this configuration
DATABASE = 'darts'
USER = 'root'
PASSWORD = 'GI4FAOjq510dut2q'

TOKEN  = "xoxp-35254464561-35239114516-35279347939-a100834ee7"

conn = mysql.connector.connect(host=HOST,database=DATABASE,user=USER,password=PASSWORD)

def insert_many(query, values):
    '''inserts many values into mysql from: http://www.mysqltutorial.org/python-mysql-insert/'''
    
    try:
        cursor = conn.cursor()
        cursor.executemany(query, values)
        conn.commit()
    except Error as e:
        print('Error:', e)
 
    finally:
        cursor.close()
        conn.close()




def get_names():
    '''gets usernames and real names from of all slack users'''
    sc = SlackClient(TOKEN)

    users = sc.api_call("users.list")['members']

    names = []

    for i in range(len(users)):
        slack_name = (users[i]['name'])
        real_name = (users[i]['profile']['real_name'])
        name = (slack_name,real_name)
        names.append(name)

    return names


query = "INSERT INTO darters(slack_name,real_name) VALUES(%s, %s)"
names = get_names()

insert_many(query,names)