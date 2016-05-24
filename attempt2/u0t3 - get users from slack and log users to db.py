from Slacker import get_slack_users 
from DatabaseManager import add_darters


slack_users = get_slack_users()

darters = []

for slack_users in slack_users:
    real_name = slack_users['slack_real_name']
    slack_name = slack_users['slack_name']
    darter = (slack_name,real_name)
    darters.append(darter)

add_darters(darters)