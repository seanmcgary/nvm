#!/usr/bin/python
import sys
import os
import subprocess
import shlex
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

	clone = "git clone https://github.com/joyent/node " + clone_path
	if(subprocess.call(clone, shell=True) != 0):
		print colors.red("Failed to clone repository")
		exit()
	
	print colors.green("Checking out tag " + tag + "...") + "\n"

	checkout = "cd " + clone_path + " && git checkout " + tag
	if(subprocess.call(checkout, shell=True) != 0):
		print colors.red("Failed to checkout tag " + tag)
		exit()

	print colors.green("Building Nodejs...") + "\n"

	make = "cd " + clone_path + " && ./configure && make"
	if(subprocess.call(make, shell=True) != 0):
		print colors.red("Failed to configure and make")
		exit()
	
	symlink = ''
	

	if len(data['current_version']) > 0:
		symlink = "cd " + os.environ['NVM_VERSIONS'] + " && rm -rf current; ln -s " + tag + " current"
	else:
		symlink = "cd " + os.environ['NVM_VERSIONS'] + " && ln -s " + tag + " current"
	print symlink
	if(subprocess.call(symlink, shell=True) != 0):
		print colors.red("Failed to make tag " + tag + " current")
		exit()
	
	# add a directory for the modules and symlink it if it doesnt already exist
	if(os.path.exists(os.environ['NVM_MODULES'] + '/' + tag) != True):
		subprocess.call("cd " + os.environ['NVM_MODULES'] + ' && mkdir ' + tag, shell=True)
	
	module_symlink = ''

	if(os.path.exists(os.environ['NVM_MODULES'] + '/current') != True):
		module_symlink = "cd " + os.environ['NVM_MODULES'] + ' && ln -s ' + tag + ' current'
	else:
		module_symlink = "cd " + os.environ['NVM_MODULES'] + ' && rm -rf current; ln -s ' + tag + ' current'
	
	subprocess.call(module_symlink, shell=True)

	data['installed_versions'].append(tag)
	data['current_version'] = tag

	data_loader.save_data(data)
	
