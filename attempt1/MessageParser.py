
def get_parsed_message(message):
    
    message_type = identify_message_type(message)
    
    if message_type == 'match_result'
        parsed_message = parse_match_result_message(message)

    return parsed_message

def identify_message_type(message):



def parse_match_result_message(message):

    message_type = 
    winner_darter_id =
    loser_darter_id = 
    notifier_darter_id = 

    parsed_message = {'message_type' = message_type,
                    'winner_darter_id' = winner_darter_id,
                    'loser_darter_id'= loser_darter_id,
                    'notifier_darter_id' = notifier_darter_id}

    return parsed_message


