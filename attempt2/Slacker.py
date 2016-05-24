#Say hello to slack

#interfaces with Slack

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







def get_slack_users():
    # returns users in  dictionary form
    sc = SlackClient(TOKEN)

    members = sc.api_call("users.list")['members']

    slack_users = []

    for member in members:
        slack_id = member['id']
        slack_deleted = member['deleted']
        slack_name = member['name']
        slack_status = member['status']
        slack_first_name = member['profile']['first_name']
        slack_last_name = member['profile']['last_name']
        slack_real_name = member['profile']['real_name']
        slack_real_name_normalized = member['profile']['real_name_normalized']
        slack_email = member['profile']['email']


        slack_user = {'slack_id': slack_id, 
                    'slack_deleted': slack_deleted, 
                    'slack_name': slack_name,
                    'slack_status': slack_status,
                    'slack_first_name': slack_first_name,
                    'slack_last_name': slack_last_name,
                    'slack_real_name': slack_real_name,
                    'slack_real_name_normalized': slack_real_name_normalized,
                    'slack_email': slack_email}

        slack_users.append(slack_user)

    return slack_users