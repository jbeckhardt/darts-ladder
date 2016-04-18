# this script takes the ladder and finds two players to play against one
# it is based on a test script of similar name

import mysql.connector
from mysql.connector import Error
from random import choice



HOST = '23.236.54.228' #see above link for better handling of this configuration
DATABASE = 'darts'
USER = 'root'
PASSWORD = 'GI4FAOjq510dut2q'

conn = mysql.connector.connect(host=HOST,database=DATABASE,user=USER,password=PASSWORD)

max_threshold = 4 # eg user cant be more than 4 spots above. If i am seed 7 the max seed is 11 
min_threshold = 2 # eg user must be at least 2 steps above. If I am see 7 it can't be seed 6


def query_with_fetchall(query):
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

query = "select slack_name from darters order by current_seed"
records = query_with_fetchall(query)


def get_player_indices(records):
    '''Gets two indices based on the threshold criteria that can then be applied
    against list from response to identify players

    It does this by:
    1) creating a list of indexes from records
    2) Choosing an index at random - this is "index  of player a"
    3) iterating through rest of list and determining if accepted
    4) Choosing a random index from the list of accepted indexes - this is "index of player b'''
    
    indices = range(len(records))
    index_a = choice(indices)
    accepted_indices = []
    
    for index in indices:
        distance = abs(index_a - index)
        if distance >= min_threshold and distance <= max_threshold:
            accepted_indices.append(index)
        else:
            pass

    index_b = choice(accepted_indices) 
    player_indices = [index_a,index_b] 
    
    return player_indices


def get_cleaned_records(records):
    '''cleans the record data by taking the individual records out of tuples
    and leaving it as strings

    Note: only pertains to records from a single column'''
    
    cleaned_records = []
    for record in records:
        cleaned_record = str(record)[3:-3]
        cleaned_records.append(cleaned_record)
    return cleaned_records

player_indices = get_player_indices(records)
cleaned_records = get_cleaned_records(records)
players = [cleaned_records[i] for i in player_indices]

print players



# get users
# order users
# choose one user
# find all other users with in accepted ranges
# find