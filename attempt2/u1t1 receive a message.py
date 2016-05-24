#Say hello to slack
import time
from slackclient import SlackClient
from ConfigManager import get_config_value

TOKEN = get_config_value('token')

sc = SlackClient(TOKEN)
message = sc.api_call("im.history",channel = 'D11713D2Q')['messages'][0]['text']

print message
