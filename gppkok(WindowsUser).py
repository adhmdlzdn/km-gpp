# encoding: utf-8
# (c) 2021-2022, ev All rights reserved

# 1 - Import all modules we need
from datetime import datetime
import time, os, sys

# 2 - Data, list, etc
N = '\x1b[0m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m'
C = '\x1b[1;36m'
P = '\x1b[1;37m'
now = datetime.now()
clear = lambda : os.system('cls')

# 3 - Menu, Function, etc
# 3.1 - Restart program
def restart_program():
	python = sys.executable
	os.execl(python, python, *sys.argv)
	curdir = os.getcwd()

# 3.2 - Start menu
def start():
	clear()
	b1()

# 4 - Banner
# 4.1 - Start banner
def b1():
	print('                   _         _    ')
	print('                  | |       | |   ')
	print('  __ _ _ __  _ __ | | _____ | | __')
	print(' / _` | \'_ \\| \'_ \\| |/ / _ \\| |/ /')
	print('| (_| | |_) | |_) |   < (_) |   < ')
	print(' \\__, | .__/| .__/|_|\\_\\___/|_|\\_\\ ')
	print('  __/ | |   | |__________________ ')
	print(' |___/|_|   |____________________|')

# Start
start()