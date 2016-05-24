#Say hello to slack
import time
from slackclient import SlackClient
from ConfigManager import get_config_value

TOKEN = get_config_value('token')

sc = SlackClient(TOKEN)
data_nugget = sc.api_call("im.history",channel = 'D11713D2Q')
message = data_nugget['messages'][2]['text']
print data_nugget



def get_darter_id(known_id, desired_id):


    table = 'darters'
    known_column = known_id.keys()[0]
    known_value = known_id[known_column]
    desired_column = None


    query = '''SELECT %s from %s where %s = %s''' % (table, known_column, known_value,desired_column)

    


lookup_id({'id':'U119ZAYP9'}, 'slack_name')
