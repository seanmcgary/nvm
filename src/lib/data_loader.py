import json

data_path = '.nvm-data'

def load_data():

	data = open(data_path, 'r').read()
	return json.loads(data)
