#manages interactions with database

from ConfigManager import get_config_value
import DatabaseConnector as db
import time


CURRENT_EPOCH_TIME = int(time.time())


def log_result(winner_darter_id, loser_darter_id,reported_at):
    """logs a match result"""
    
    query = "INSERT INTO matches(winner_darter_id,loser_darter_id,reported_at, created_at, updated_at) VALUES(%s,%s,%s,%s,%s)"
    value = [(winner_darter_id, loser_darter_id, reported_at, CURRENT_EPOCH_TIME, CURRENT_EPOCH_TIME)]
    
    db.insert(query,value)



def get_darter_info(desired_info, current_identifier_column, current_identifier):
    '''gets a value from the darter table given another value (identifiers such as 'slack_id', 'slack_name', 'desired_id')'''

    query = '''SELECT %s FROM darters WHERE %s = "%s"''' % (desired_info, current_identifier_column,current_identifier)

    record = db.read(query)
    darter_info = record[0][0]
    
    return darter_info


def get_last_match_time():
    """gets the time the last match was logged"""

    query = '''SELECT max(reported_at) FROM matches'''

    record = db.read(query)
    last_match_time = record[0][0]

    return last_match_time



def add_darters(darters):
    """adds user(s) to database

    darters should be list of tuples of the form"""

    values = []
    for darter in darters:
        darter +=  (CURRENT_EPOCH_TIME, CURRENT_EPOCH_TIME)
        values.append(darter)

    query = "INSERT INTO darters(slack_name,slack_id,real_name, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)"

    db.insert(query, values)




