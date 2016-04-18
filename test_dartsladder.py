import os
import ConfigParser

CONFIG_PATH = 'config.ini'

class ConfigManager(object):
	"""creates a wrapper for getting config values"""

	def __init__(self):
		self.config_path = CONFIG_PATH

	def get_value(self, key):
		"""returns a requested value from the config file"""
		
		config = ConfigParser.ConfigParser()
		config.read(self.config_path)
		return config.get('all', key)

print ConfigManager().get_value('token')
