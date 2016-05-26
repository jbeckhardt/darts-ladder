import time
from slackclient import SlackClient
from ConfigManager import get_config_value

TOKEN = get_config_value('token')
GENERAL_CHANNEL = get_config_value('general_channel')



def print_recursive():
    print 1
    print_recursive()

print_recursive()