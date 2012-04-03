import sys
import os
import subprocess

import data_loader
import colors


def set_version(tag, data):
	
	if len(data['current_version']) > 0:
		symlink = "cd " + os.environ['NVM_VERSIONS'] + " && rm -rf current; ln -s " + tag + " current"
	else:
		symlink = "cd " + os.environ['NVM_VERSIONS'] + " && ln -s " + tag + " current"
	
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

	data['current_version'] = tag
