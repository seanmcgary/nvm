import sys
import data_loader
import os
from subprocess import call

import colors

def write_rc():
	data = data_loader.load_data()

	#open the file
	rc_path = os.environ['NVM_PATH'] + '/.nvmrc'

	rc = open(rc_path, 'w+')

	#create some global environment variables
	rc.write("export NVM_VERSIONS=" + os.environ['NVM_PATH'] + "/versions\n")
	rc.write("export NVM_MODULES=" + os.environ['NVM_PATH'] + "/modules\n")
	
	rc.write("export NODE_PATH=" + os.environ['NVM_PATH'] + "/modules/current\n")
	rc.write("export NVM_NODE_PATH=" + os.environ['NVM_PATH'] + "/modules/current\n")

	rc.write("PATH=$PATH:" + os.environ['NVM_PATH'] + "/bin:$NVM_VERSIONS/current:$NVM_VERSIONS/current/tools\n")

	print colors.yellow("Please source your shells rc file to apply changes.")


	
