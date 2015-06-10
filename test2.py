import sys
from com.uc.utils import AndroidUtil

from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import GConf

PROG = 'TOOLBOX'

def printHelp():
	global PROG
	print('usage: %s [-c | -l | -s | -u | -t]' % PROG)
	print('-c: change so')
	print('-l: launch app')
	print('-s: shutdown app')
	print('-u: browse a url')
	print('-t: start a test')

def printHelpChange():
	print('usage: %s -c path target [package]' % PROG)
	print('	target: uc/hardcode/videotest')
	print('	NOTE: target videotest needs no package')


def printHelpLaunch():
	print('usage: %s -l [package] [activity]' % PROG)
	print('	package dfaults to com.UCMobile')
	print('	NOTE: uc/videotest activity is preconfig')


def printHelpShutdown():
	print('usage: %s -s package' % PROG)
	print('	target: uc/hardcode/videotest')
	print('	NOTE: target videotest needs no package')


def printHelpBrowseUrl():
	print('usage: %s -c path target [package]' % PROG)
	print('	target: uc/hardcode/videotest')
	print('	NOTE: target videotest needs no package')


def printHelpTest():
	print('usage: %s -c path target [package]' % PROG)
	print('	target: uc/hardcode/videotest')
	print('	NOTE: target videotest needs no package')


def parseCommand(args):
	if len(args) == 1:
		printHelp()
		return

	GConf.initConfig()
	TaskLogger.init()
	command = args[1]
	if command == '-h':
		printHelp()
	elif command == '-c':
		parseCommandC(args)
	else:
		print('###command unreconized!!!')
		printHelp()


def parseCommandL(args):
	pass

def parseCommandS(args):
	pass

def parseCommandU(args):
	pass

def parseCommandT(args):
	pass

def parseCommandC(args):
	length = len(args[2:])
	if length < 2:
		print('###not enough args!!!')
		printHelpChange()
		return
	if length > 3 :
		print('###too many args!!!')
		printHelpChange()
		return
	if length == 2:
		callChangeLib(args[2], args[3])
	else:
		callChangeLib(args[2], args[3], args[4]) 

def callChangeLib(path, target, package=None):
	if package is None:
		package = 'com.UCMobile'

	if target == 'uc':
		AndroidUtil.switchApollo(path, package)
		pass
	elif target == 'hardcode':
		AndroidUtil.switchApollo(path, package)
		pass
	elif target == 'videotest':
		AndroidUtil.switchVideoTestApollo(path)
		pass
	else:
		print('###target (%s) incorrect!!!' % target)
		printHelpChange()



if __name__ == '__main__':
	PROG = sys.argv[0]
	parseCommand(sys.argv)