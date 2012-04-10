import sys
import os
import subprocess

import data_loader
import colors


def set_version(ver):
	data = data_loader.load_data()

	if(len(data['current_version']) == 0):
		print colors.yellow("You need to install a version of NodeJS first.")
		exit()
	
	try:
		data['installed_versions'].index(ver)
	except:
		print colors.yellow(ver + " is not installed")
		exit()
	
	
	#remove the current binaries
	subprocess.call("cd $NVM_BIN && rm *", shell=True)


	# symlink node binary
	installed_ver = os.environ['NVM_INSTALL'] + "/versions/current"
	subprocess.call("ln -s $NVM_INSTALL/versions/current/node $NVM_BIN/node", shell=True)
	
	# now for npm 
	subprocess.call("ln -s $NVM_INSTALL/versions/current/deps/npm/bin/npm $NVM_BIN/npm", shell=True)


def create_env(tag, data):
	
	nvm_ver = os.environ['NVM_VERSIONS']
	nvm_mod = os.environ['NVM_MODULES']
	nvm_install = os.environ['NVM_INSTALL']
	
	# symlink the new tag to current in nvm_versions
	if len(data['current_version']) > 0:
		symlink = "cd " + nvm_ver + " && rm -rf current; ln -s " + tag + " current"
	else:
		symlink = "cd " + nvm_ver + " && ln -s " + tag + " current"
	
	if(subprocess.call(symlink, shell=True) != 0):
		print colors.red("Failed to make tag " + tag + " current")
		exit()
	
	
	if(os.path.exists(nvm_install + '/bin') != True):
		subprocess.call("cd $NVM_INSTALL && mkdir bin", shell=True)

	# add a directory for the modules and symlink it if it doesnt already exist
	if(os.path.exists(nvm_mod + '/' + tag) != True):
		subprocess.call("cd " + nvm_mod + ' && mkdir ' + tag, shell=True)
	
	module_symlink = ''

	if(os.path.exists(nvm_mod + '/current') != True):
		module_symlink = "cd " + nvm_mod + ' && ln -s ' + tag + ' current'
	else:
		module_symlink = "cd " + nvm_mod + ' && rm -rf current; ln -s ' + tag + ' current'
	
	subprocess.call(module_symlink, shell=True)
	
	node_lib_path = nvm_mod + '/current/lib';
	if(os.path.exists(node_lib_path) != True):
		subprocess.call('cd ' + nvm_mod + '/current && mkdir lib', shell=True)

	#create modules/current/node_modules and modules/current/node
	node_mod_path = node_lib_path + '/node_modules'
	if(os.path.exists(node_mod_path) != True):
		subprocess.call('cd ' + node_lib_path + ' && mkdir node_modules', shell=True)
	
	node_path = node_lib_path + '/node'
	if(os.path.exists(node_path) != True):
		subprocess.call('cd ' + node_lib_path + ' && mkdir node', shell=True)


	# check to see if /usr/local/lib/node_modules exists
	lib_node_modules = '/usr/local/lib/node_modules'
	sym_link_node_mod = 'sudo ln -s ' + node_mod_path + ' ' + lib_node_modules
	if(os.path.exists(lib_node_modules) == True):
		sym_link_node_mod = 'sudo rm -rf ' + lib_node_modules + '; ' + sym_link_node_mod
	
	subprocess.call(sym_link_node_mod, shell=True)

	# check to see if /usr/local/lib/node exists
	#lib_node = '/usr/local/lib/node'
	#sym_link_node = 'sudo ln -s ' + node_path + ' ' + lib_node
	#if(os.path.exists(lib_node) == True):
	#	sym_link_node = 'sudo rm -rf ' + lib_node + '; ' + sym_link_node

	#subprocess.call(sym_link_node, shell=True)

	
	data['current_version'] = tag
