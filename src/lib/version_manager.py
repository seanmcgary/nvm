import sys
import os
import subprocess

import data_loader
import colors


def set_version(tag, data):
	
	nvm_ver = os.environ['NVM_VERSIONS']
	nvm_mod = os.environ['NVM_MODULES']
	
	# symlink the new tag to current in nvm_versions
	if len(data['current_version']) > 0:
		symlink = "cd " + nvm_ver + " && rm -rf current; ln -s " + tag + " current"
	else:
		symlink = "cd " + nvm_ver + " && ln -s " + tag + " current"
	
	if(subprocess.call(symlink, shell=True) != 0):
		print colors.red("Failed to make tag " + tag + " current")
		exit()
	

	# add a directory for the modules and symlink it if it doesnt already exist
	if(os.path.exists(nvm_mod + '/' + tag) != True):
		subprocess.call("cd " + nvm_mod + ' && mkdir ' + tag, shell=True)
	
	module_symlink = ''

	if(os.path.exists(nvm_mod + '/current') != True):
		module_symlink = "cd " + nvm_mod + ' && ln -s ' + tag + ' current'
	else:
		module_symlink = "cd " + nvm_mod + ' && rm -rf current; ln -s ' + tag + ' current'
	
	subprocess.call(module_symlink, shell=True)

	#create modules/current/node_modules and modules/current/node
	node_mod_path = nvm_mod + '/current/node_modules'
	if(os.path.exists(node_mod_path) != True):
		subprocess.call('cd ' + nvm_mod + '/current && mkdir node_modules', shell=True)
	
	node_path = nvm_mod + '/current/node'
	if(os.path.exists(node_path) != True):
		subprocess.call('cd ' + nvm_mod + '/current && mkdir node', shell=True)

	# check to see if /usr/local/lib/node_modules exists
	lib_node_modules = '/usr/local/lib/node_modules'
	sym_link_node_mod = 'sudo ln -s ' + node_mod_path + ' ' + lib_node_modules
	if(os.path.exists(lib_node_modules) == True):
		sym_link_node_mod = 'sudo rm -rf ' + lib_node_modules + '; ' + sym_link_node_mod
	
	subprocess.call(sym_link_node_mod, shell=True)

	# check to see if /usr/local/lib/node exists
	lib_node = '/usr/local/lib/node'
	sym_link_node = 'sudo ln -s ' + node_path + ' ' + lib_node
	if(os.path.exists(lib_node) == True):
		sym_link_node = 'sudo rm -rf ' + lib_node + '; ' + sym_link_node

	subprocess.call(sym_link_node, shell=True)



	data['current_version'] = tag
