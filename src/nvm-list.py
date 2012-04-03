#!/usr/bin/python
import sys
import os
sys.path.append(os.environ['NVM_PATH'] + '/src/lib')

import data_loader 
import colors
import github

def known():

	req = github.get_tags()
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
	
def current():
	data = data_loader.load_data()

	if len(data['current_version']) > 0:
		print "Current installed version:"
		print "\t" + colors.green(data['current_version'])
	else:
		print colors.red("No current version installed")
		print "Use " + colors.yellow("nvm install <version>") + " to install"

def installed():
	data = data_loader.load_data()

	if len(data['installed_versions']) > 0:
		for i in data['installed_versions']:
			if i == data['current_version']:
				print colors.green(i)
			else:
				print colors.yellow(i)
	else:
		print colors.red("No versions installed")
		print "Use " + colors.yellow("nvm install <version>") + " to install"
		

available_args = {
	'known': known,
	'installed': installed,
	'current': current
}

tags_url = 'https://api.github.com/repos/joyent/node/tags'

if __name__ == '__main__':

	args = sys.argv[1:len(sys.argv)]

	if(len(args) == 0):
		# list installed versions of node as well as the current
		installed()
	elif len(args) == 1:
		if(args[0] in available_args):
			available_args[args[0]]()
	else:
		print "unknown command"
