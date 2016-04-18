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
	3. opens match
	4. Asks other party if accepts within window of time (e.g. 48 hours)
	5a. If other party does not accept, closes match and informs challenger of win.
	5b. Confirms match with both parties  and informs of deadline.
	"""

	def follow_up_on_match_result():
	"""follows up on results of open matches

	"""

	def accept_match_result():
	"""accepts a match result"""

	def add_new_user(slack_name):
	"""adds new user to the ladder and adjusts rankings accordingly"""

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


Class Translator(object):
"""Translates slack messages into key terms"""

	def translate(self,message):
	"translates message into key terms"


Class Messager(object):
"""Communicates specific messages"""
	
	def __init__(self,message_path):
		self.config_path = config_path

	def announce_new_challenge():
	"""announces a challenge publicly"""

	def express_nonunderstanding():
	"""tells user that it does not understand message"""

	def confirm_message():
	"""confirms a request from an individual"""

	def express_acceptable_messages():
	"""provide a list of acceptable inbound messages"""

	def accept_match_
	"informs a challenged users of the match, gives them the window of time to respond \
	and expresses how to say that they confirm"



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



Class SlackWrapper(object):
	"""Wrapper for Slack API. Contains no business logic"""

	def sendPublicMessage(message_body):

	def send_private_message(message_body, recipients):

	def send_group_message(message_body, recipients):

	def recieve_message(sender, message_body)


Class DatabaseConnector(Object):
	"""Wrapper for database connection"""

	def __init___(self,host=False,db=False,user=False,password=False):
		self.host = host
		self.db = db
		self.user = user
		self.password = password
	
	def read(self,query):

	def insert(self,query):


Class ConfigManager(object):
	"""makes it easy to get values from a config file"""

	def __init__(self,config_path):
		self.config_path = config_path

	def get_value(self, key):
	""" returns a requested value from the config file"""



	

