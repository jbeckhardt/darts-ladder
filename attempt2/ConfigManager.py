import os
import ConfigParser



CONFIG_PATH = 'config_files/config.ini'
MESSAGE_TYPE_PATH = 'config_files/message_types.ini'

def get_config_value(key):
		"""returns a requested value from the config file"""
		
		config = ConfigParser.ConfigParser()
		config.read(CONFIG_PATH)
		return config.get('all', key)


def get_message_type_value(key):
        """returns a requested value from the messaage typefile"""
        try:
            config = ConfigParser.ConfigParser()
            config.read(MESSAGE_TYPE_PATH)
            return config.get('all', key)
        except:
            return None

