#!/usr/bin/python

import argparse
import sys
import os

def use(args):
	exec_args = ['./nvm-use.py'] + args
	os.execvp(exec_args[0], exec_args)

def install(args):
	exec_args = ['./nvm-install.py'] + args
	os.execvp(exec_args[0], exec_args)

def npm(args):
	print "npm"

def list(args):
	exec_args = ['./nvm-list.py'] + args
	os.execvp(exec_args[0], exec_args)

args = {
	'use': use,
	'install': install,
	'npm': npm,
	'list': list
}

if __name__ == "__main__":
	
	if(sys.argv[1] in args):
		args[sys.argv[1]](sys.argv[2:len(sys.argv)])
	else:
		print "bad command"

