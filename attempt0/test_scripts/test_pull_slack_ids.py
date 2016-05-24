#get sql ids
import time
from slackclient import SlackClient


TOKEN  = "xoxp-35254464561-35239114516-35279347939-a100834ee7"


sc = SlackClient(TOKEN)


users = sc.api_call("users.list")['members']

names = {}

for i in range(len(users)):
    slack_name = (users[i]['name'])
    real_name = (users[i]['profile']['real_name'])
    
    names[slack_name] = real_name 

print names


# print users['members'][0]['name']