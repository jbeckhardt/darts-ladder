import os
import ConfigParser

CONFIG_PATH = 'config.ini'

def get_config_value(key):
		"""returns a requested value from the config file"""
		
		config = ConfigParser.ConfigParser()
		config.read(CONFIG_PATH)
		return config.get('all', key)





	