import os
import ConfigParser


CONFIG_PATH = 'config.ini'


Class FunCaptain(object):
"""facilitates darts ladder"""

	def propose_new_match():
	"""finds two eligible opponents and 

	1. Finds eligible oppponents
	2. Announces match publicly
	3. Logs an open match"""

	def accept_new_match():
	"""Accepts a new match proposal

	1. Confirms match proposal
	2. Evaluates if match is eligible
	3. Opens match
	4. Asks other party if accepts within window of time (e.g. 48 hours)
	5a. If other party does not accept, closes match and informs challenger of win.
	5b. Confirms match with both parties  and informs of deadline.
	"""

	def follow_up_on_match_result():
	"""follows up on results of open matches

	1. based on set followup time, identifies matches to follow up on
	2. asks both users who won and informs them how to communicate back to them, and informs time period to get back to them
	3. Upon receipt, Confirms results with other party
	4a. If consensus, logs match and confirms with other party
	4b. If no consensus, asks them to figure it out and get back, otherwise it will call it a forfeit """

	def receive_match_result():
	"""receives an unprompted match result

	1. Confirms there is an open match
	2a.If open match, confirms with user message and that they need to confirm with other party
	2b.If not open, informs user there is no open match
    3. Confirms result with other party
    4a. If consensus, logs match and confirms with other party
    4b. If no consensus, asks them to figure it out and get back,"""

	def add_new_user(slack_name):
	"""adds new user to the ladder and adjusts rankings accordingly

	1. Adds new user as bottom seed
	2. Determines random seed for user
	3. Adjusts ladder
	4. Informs individual of their seed
	5. Announces additional user and seed publicly"""

	def opt_out_user(slack_name):
	"""opts a user out of ladder

	1.puts them to bottom of ladder
	2.Adjusts ladder
	3.sets ranking to None
	4.sets opt_out=1  
	5.confirms with users they have been opted out and instructions for reinstating"""

	def reinstate_user(slack_name):
	""" reinstates a user to ladder

	1. sets opt_out  = 0
	2. puts them at lowest seed.
	"""


Class Dispatcher(object):
"""dispatches inbound messages to FunCaptain"""

Class Translator(object):
"""Translates slack messages into key terms"""

	def translate(self,message):
	"translates message into key terms"


Class Messager(object):
"""Communicates specific messages"""
	
	def __init__(self,message_path):
		self.message_path = message_path

	def announce_new_challenge():
	"""announces a challenge publicly"""

	def express_nonunderstanding():
	"""tells user that it does not understand message"""

	def confirm_message():
	"""confirms a request from an individual"""

	def express_acceptable_messages():
	"""provide a list of acceptable inbound messages"""

	def accept_match_challenge():
	"informs a challenged users of the match, gives them the window of time to respond \
	and expresses how to say that they confirm"

	def express_ineligible_match():
	"informs a user that their match challenge is not eligible"


Class LadderManager(object):

	def adjust_ladder(darter_id, new_position):
	"""moves individual to new position and adjust """

	def get_ranking(identifier):
	"""gets the ranking of a darter"""

	def open_match(slack_name,slack_name):
	
	def	close_match(match_id):
	"""closes a match and adjusts the seeds accordingly

		1. Calls the match closed. 
		2. Sets the winners seed to the seed of whichever player has a higher ranking
		3. Adjusts ladder accordingly"""

	def get_eligible_opponents():
	"""finds two eligible opponents for computer suggested matches"""

	def is_eligible():
	"""determines if two users are eligible"""



Class Slacker(object):
	"""Wrapper for Slack API. Contains no business logic"""

	def ___init__(self):
		self.public_channel = ConfigManager().get_value('public_channel')
		self.token = ConfigManager().get_value('token')

	def send_public_message(message_body):

	def send_private_message(message_body, recipients):

	def send_group_message(message_body, recipients):

	def receive_message(sender, message_body):


class DatabaseConnector(object):
	"""Wrapper for database connection"""

	def __init___(self):
		self.host = ConfigManager().get_value('host')
		self.db = ConfigManager().get_value('database')
		self.user = ConfigManager().get_value('user')
		self.password = ConfigManager().get_value('password')
	
	def read(self,query):

	def insert(self,query):

   
class ConfigManager(object):
	"""creates a wrapper for getting config values"""

	def __init__(self):
		self.config_path = CONFIG_PATH

	def get_value(self, key):
		"""returns a requested value from the config file"""
		
		config = ConfigParser.ConfigParser()
		config.read(self.config_path)
		return config.get('all', key)

	

