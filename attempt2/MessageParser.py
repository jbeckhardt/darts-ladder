# handles phonology, morphology, syntax, semantics, and reasonings steps for understanding as shown in this pipeline architecture
# here http://stackoverflow.com/questions/9706769/any-tutorials-for-developing-chatbots

from ConfigManager import get_message_type_value
from collections import Counter

def get_parsed_message(message):
    '''pulls together other functions to return meaning of message

    returns a json object of the form:
    {"message_type":message_type,
    "parsed_message":parsed_message}'''


    message_type = identify_message_type(message)
    
    if message_type == 'match_result':
        parsed_message = parse_match_result_message(message)
    else:
        parsed_message = None

    data_nugget = {"message_type":message_type,
                    "parsed_message":parsed_message}

    return parsed_message



def identify_message_type(message):
    '''identifies what type of message is sent

    iterates through each word, matches words to message_types, returns most common message_type'''

    words = message.split(' ')
    
    potential_message_types = []

    for word in words:
        message_type_value = get_message_type_value(word)
        potential_message_types.append(message_type_value)

    message_types = dict(Counter(potential_message_types))

    message_type = max(message_types, key=message_types.get) #http://stackoverflow.com/questions/14091636/get-dict-key-by-max-value

    return message_type



def parse_match_result_message(message):
    '''parses a match_result message

    returns dict of form {'winner_darter_id': winner_darter_id, 'loser_darter_id', loser_darter_id}'''

    

    match_result = {'winner_darter_id' = winner_darter_id,
                    'loser_darter_id'= loser_darter_id}

    return parsed_message