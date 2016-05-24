#Runs continusouly, scanning slack for new messages and logging results in database

import Slacker
import DatabaseManager as db

def get_last_match_time():
    """gets the time the last match was logged"""

last_match_time = get_last_match_time

messages = Slacker.get_messages(oldest_time=last)

parsed_messages = get_parsed_messages()

for parsed_message in parsed_messages:
    if parsed_message['message_type'] == 'match_result':
        winner_darter_id = parsed_message['parsed_message']['winner_darter_id']
        loser_darter_id = parsed_message['parsed_message']['loser_darter_id']
        db.log_result(1,3)