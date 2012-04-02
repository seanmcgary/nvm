#!/usr/bin/python
import sys
sys.path.append('./lib')

import requests
import json
import data_loader 
import colors

def known():

	req = json.loads(requests.get(tags_url).text)
	versions = []
	for i in req:
		if i['name'][0] == 'v':
			versions.append(i['name'])

	versions.sort()

	data = data_loader.load_data()
	
	for i in versions:
		try:
			data['installed_versions'].index(i)
			
			if i == data['current_version']:
				print colors.green(i)
			else:
				print colors.yellow(i)

		except:
			print i
	

available_args = {
	'known': known
}

tags_url = 'https://api.github.com/repos/joyent/node/tags'

if __name__ == '__main__':

	args = sys.argv[1:len(sys.argv)]

	if(len(args) == 0):
		# list installed versions of node as well as the current
		print "foobar"
	elif len(args) == 1:
		if(args[0] in available_args):
			available_args[args[0]]()
	else:
		print "unknown command"
