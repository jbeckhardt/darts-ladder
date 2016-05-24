from ConfigManager import get_config_value
import DatabaseConnector as db
import time


CURRENT_EPOCH_TIME = int(time.time())


def log_result(winner_darter_id, loser_darter_id):
    """logs a match result"""
    
    query = "INSERT INTO matches(winner_darter_id,loser_darter_id,created_at,updated_at) VALUES(%s,%s,%s,%s)"
    value = [(winner_darter_id, loser_darter_id, CURRENT_EPOCH_TIME, CURRENT_EPOCH_TIME)]
    
    db.insert(query,value)




def get_darter_id(slack_name):
    query = '''SELECT darter_id FROM darters WHERE slack_name = "%s"''' % (slack_name)
    record = db.read(query)
    darter_id = record[0][0]
    return darter_id



def get_slack_name(darter_id):
    query = '''SELECT slack_name FROM darters WHERE darter_id = %d''' % (darter_id)
    record = db.read(query)
    slack_name = record[0][0]
    return slack_name



# def lookup_id(current_id={}, desired_id=()):
#     #looks up ids between darter_id, real name, slack id, slack name
#     #provide the name of the id in current
    
#     #TODO
#     current_table = desired_id.key()[0]
#     current_value = desired_id[current_table]
#     # desired_table = 


#     query = '''SELECT %s from %s where'''

def add_darters(darters):
    """adds user(s) to database

    darters should be list of tuples of the form ("""

    values = []
    for darter in darters:
        print darter
        darter +=  (CURRENT_EPOCH_TIME, CURRENT_EPOCH_TIME)
        values.append(darter)

    query = "INSERT INTO darters(slack_name,real_name, created_at, updated_at) VALUES(%s, %s, %s, %s)"

    db.insert(query, values)

print get_darter_id('andres')


