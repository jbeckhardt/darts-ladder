from Slacker import get_slack_users 
from DatabaseManager import add_darters


slack_users = get_slack_users()

darters = []

for slack_user in slack_users:
    slack_id = slack_user['slack_id']
    real_name = slack_user['slack_real_name']
    slack_name = slack_user['slack_name']
    darter = (slack_name,slack_id, real_name)
    darters.append(darter)

add_darters(darters)