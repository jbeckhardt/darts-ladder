import LadderManager as lm
from ConfigManager import get_message
from ConfigManager import get_config_value


PUBLIC_CHANNEL = get_config_value('public_channel')
LOG_CHANNEL = get_config_value('log_channel')



def accept_match_result(winner_darter_id,loser_darter_id,notifier_darter_id):
    """ accepts the result of a match """

    if notifier_darter_id == winner_darter_id
        confirmation_message = get_message('confirm_win')
        informing_message = get_message('inform_loss')
    else:  
        confirmation_message = get_message('confirm_loss')
        informing_message = get_message('inform_win')

    announcement_message = get_message('match_result')

    send_message(notifier_darter_id,confirmation_message)

    send_message()

    lm.log_result(winner_darter_id,loser_darter_id)
    

def accept_match_dispute(disputer_darter_id,disputee_darter_id):
    
    announcement_message = get_message('match_dispute')

    players = [disputee_darter_id,disputee_darter_id]

    lm.get_most_recent_match_id([players])

    lm.log_result(winner_darter_id,loser_darter_id)



