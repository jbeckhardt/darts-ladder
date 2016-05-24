#Say hello to slack
import time
from slackclient import SlackClient


TOKEN  = "xoxp-35254464561-35239114516-35279347939-a100834ee7"


sc = SlackClient(TOKEN)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="1234567890")
print sc.api_call(
    "chat.postMessage", channel="#general", text="Hello world :tada:",
    username='Darts Commissioner Bot', icon_emoji=':robot_face:')