import json
import os

data_path = os.environ['NVM_PATH'] + '/src/.nvm-data'

def load_data():

	data = open(data_path, 'r').read()
	return json.loads(data)
