#Runs continusouly, scanning slack for new messages and logging results in database

import DatabaseManager as db
from Slacker import get_messages
from MessageParser import get_parsed_messages



last_match_time = db.get_last_match_time()

messages = get_messages(oldest_time=last_match_time)

parsed_messages = get_parsed_messages(messages)

for parsed_message in parsed_messages:
    if parsed_message['message_type'] == 'match_result':
        winner_darter_id = parsed_message['parsed_message']['winner_darter_id']
        loser_darter_id = parsed_message['parsed_message']['loser_darter_id']
        reported_at = parsed_message['parsed_message']['reported_at']
        db.log_result(winner_darter_id,loser_darter_id,reported_at)
        print winner_darter_id
    else:
        pass


#TODO 1) get last_matcht_time working, 2) figure out cursor closing issue