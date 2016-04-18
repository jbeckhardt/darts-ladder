#This script comes from a test (it is exaclty the same as test_pull_slack_users_put_names_seeds_in_db at first creation)


import time
from slackclient import SlackClient
import mysql.connector
from mysql.connector import Error
from random import shuffle

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


def randomize_seeds(list):
    '''creates a list of randomly sorted integers same lenght as user list'''
    seeds = [i+1 for i in range(len(list))]
    shuffle(seeds)
    return seeds


def get_names():
    '''gets usernames and real names from of all slack users'''
    sc = SlackClient(TOKEN)

    users = sc.api_call("users.list")['members']

    seeds = randomize_seeds(users)
    names = []

    for i in range(len(users)):
        slack_name = (users[i]['name'])
        real_name = (users[i]['profile']['real_name'])
        seed = seeds[i] 
        name = (slack_name,real_name,seed)
        names.append(name)

    return names


query = "INSERT INTO darters(slack_name,real_name,current_seed) VALUES(%s, %s,%s)"
names = get_names()


insert_many(query,names)