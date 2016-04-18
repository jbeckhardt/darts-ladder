#Say hello to slack
import time
from slackclient import SlackClient


TOKEN  = "xoxp-35254464561-35239114516-35279347939-a100834ee7"


sc = SlackClient(TOKEN)

print "checks api calling code"
print sc.api_call("api.test")


print "lists all users"
print sc.api_call("users.list")


print "list of all channels in the team"
print sc.api_call("channels.list")


print "gets info on channel" 
print sc.api_call("channels.info", channel='C117B1MUP')

print "posts message to channel"
print sc.api_call(
    "chat.postMessage", channel="#general", text="Hello world :tada:",
    username='Darts Commissioner Bot', icon_emoji=':robot_face:')

