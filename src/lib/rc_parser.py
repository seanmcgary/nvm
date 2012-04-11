import sys
import data_loader
import os
import subprocess

import colors

def write_rc():
	data = data_loader.load_data()

	#open the file
	rc_path = os.environ['NVM_PATH'] + '/.nvmrc'

	rc = open(rc_path, 'w+')

	#create some global environment variables
	#rc.write("export NVM_VERSIONS=" + os.environ['NVM_PATH'] + "/versions\n")
	#rc.write("export NVM_MODULES=" + os.environ['NVM_PATH'] + "/modules\n")
	
	rc.write("export NVM_INSTALL=/usr/local/nvm\n")

	#put everything globally in /usr/local/nvm
	rc.write("export NVM_VERSIONS=$NVM_INSTALL/versions\n")
	rc.write("export NVM_MODULES=$NVM_INSTALL/modules\n")
	rc.write("export NVM_BIN=$NVM_INSTALL/bin\n")
	rc.write("export NVM_NODE_PATH=NVM_INSTALL/modules/current\n")

	rc.write("PATH=$NVM_BIN:$NVM_PATH/bin:$PATH\n")


	rc.write("export NODE_PATH=$NVM_MODULES/current/lib/node_modules\n")
	
