import json
import os
data_path = os.environ['NVM_PATH'] + '/src/.nvm-data'

def load_data():

	data = open(data_path, 'r').read()
	return json.loads(data)

def save_data(data):
	json_string = json.dumps(data)

	d = open(data_path, 'w+')

	d.write(json_string)
