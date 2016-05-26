# handles phonology, morphology, syntax, semantics, and reasonings steps for understanding as shown in this pipeline architecture
# here http://stackoverflow.com/questions/9706769/any-tutorials-for-developing-chatbots

from collections import Counter
from ConfigManager import get_message_type_value
from DatabaseManager import get_darter_info


def get_parsed_messages(messages):
    '''iterates through a list or raw messages and returns a list of parsed_messages

    will only parse message (and return into list of parsed messages) if message_type is identifiable

    '''

    parsed_messages = []

    for message in messages:
        message_type = get_message_type(message)
        if message_type == 'match_result':
            parsed_message = get_parsed_match_result_message(message)
            parsed_messages.append(parsed_message)
        else:
            pass

    return parsed_messages



def get_message_type(message):
    '''identifies what type of message is sent

    uses rough business logic to determine the message type
    '''

    if 'i beat' in message['text'].lower():
        message_type = 'match_result'
    else:
        message_type = None 

    return message_type



def get_parsed_match_result_message(message):
    '''parses a match_result message

    Message must end with the mentioned individual. For example "I beat @jim"

    returns a dict of the form:
    {"message_type":message_type,
    "parsed_message":
        {'winner_darter_id': winner_darter_id, 
        'loser_darter_id', loser_darter_id,
        'reported_at': timestamp}}'''
    
    winner_slack_id = message['user']
    winner_darter_id = get_darter_info('darter_id', 'slack_id', winner_slack_id)

    loser_slack_id = message['text'][-10:-1]
    loser_darter_id = get_darter_info('darter_id', 'slack_id', loser_slack_id)

    timestamp = int(float(message['ts']))

    parsed_message = {'message_type': 'match_result',
                    'parsed_message':
                        {'winner_darter_id': winner_darter_id,
                        'loser_darter_id': loser_darter_id,
                        'reported_at':timestamp}}

    return parsed_message

