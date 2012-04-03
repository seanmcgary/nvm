#!/usr/bin/python
import sys
import os
sys.path.append(os.environ['NVM_PATH'] + '/src/lib')

import data_loader
import colors
import github

if __name__ == '__main__':

	if len(sys.argv) < 2:
		print 'Useage: ' + colors.yellow('nvm-install <tag>')
		exit()

	tag = sys.argv[1]
	data = data_loader.load_data()

	#check to see if its install already
	try:
		data['installed_versions'].index(tag)

		print colors.yellow(tag + " is already installed")
		exit()
	except:
		# not installed
		pass
	
	#check to see if its a valid tag
	if github.is_valid_tag(tag) != True:
		print colors.red(tag + ' is not a valid tag')
		exit()
	
	#install the version
	
	#create the right dir
	#os.system("mkdir " + os.environ['NVM_VERSIONS'] + '/' + tag)
	clone_path = os.environ['NVM_VERSIONS'] + '/' + tag

	print colors.green("Cloning node.js to " + clone_path + "...") + "\n"

	os.system("git clone https://github.com/joyent/node " + clone_path)
	
	print colors.green("Checking out tag " + tag + "...") + "\n"

	os.system("cd " + clone_path + " && git checkout " + tag)

	print colors.green("Building Nodejs...") + "\n"

	os.system("cd " + clone_path + " && ./configure && make")

	if len(data['current_version']) > 0:
		os.system("cd " + clone_path + " && rm -rf current; ln -s " + tag + " current")
	else:
		os.system("cd " + clone_path + " && ln -s " + tag + " current")
