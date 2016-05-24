import time
from slackclient import SlackClient
from ConfigManager import get_config_value

TOKEN = get_config_value('token')
GENERAL_CHANNEL = get_config_value('general_channel')



def get_messages(channel=GENERAL_CHANNEL,oldest_time=0):
    """gets messages from public channels

    channel: name of public channel
    oldest_time: time of oldest message. note: it is not inclusive of messages at this time"""

    sc = SlackClient(TOKEN)
    messages = sc.api_call("channels.history",channel = channel)['messages']

    return messages

print get_messages()