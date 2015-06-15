import sys
from com.uc.utils import AndroidUtil
from com.uc.utils import BrowserUtils

from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import GConf
from time import sleep

PROG = 'TOOLBOX'

def printHelp():
    global PROG
    print('usage: %s [-c | -l | -s | -u | -t | -cpu]' % PROG)
    print('-c: change so')
    print('-l: launch app')
    print('-s: shutdown app')
    print('-u: browse a url')
    print('-t: start a test')

def printHelpChange():
    print('usage: %s -c path target [package]' % PROG)
    print(' target: uc/hc(hardcode)/vt(videotest)')
    print(' NOTE: target videotest needs no package')


def printHelpLaunch():
    print('usage: %s -l [package] [activity]' % PROG)
    print(' package: defaults to com.UCMobile, uc/vt can be used for short')
    print(' package: uc/vt can be used for short')
    print(' NOTE: uc/vt(videotest) activity is preconfig')


def printHelpShutdown():
    print('usage: %s -s [package]' % PROG)
    print(' package dfaults to com.UCMobile, uc/vt can be used for short')


def printHelpBrowseUrl():
    print('usage: %s -u url [package] [activity]' % PROG)
    print(' package dfaults to com.UCMobile, uc/vt can be used for short')
    print(' NOTE: uc/vt(videotest) activity is preconfig')


def printHelpCPU():
    print('usage: %s -cpu time' % PROG)
    print(' NOTE: time represent how long each command')


def printHelpTest():
    print('usage: %s -t test [config]' % PROG)
    print(' test: t1/t2/t2mc/mem/seek/frame/vmc/vframe')
    print(' NOTE: confg default to global config')


def parseCommand(args):
    if len(args) == 2:
        printHelp()
        return

    GConf.initConfig()
    TaskLogger.init()
    command = args[1]
    if command == '-h':
        printHelp()
    elif command == '-c':
        parseCommandC(args)
    elif command == '-l':
        parseCommandL(args)
    elif command == '-s':
        parseCommandS(args)
    elif command == '-u':
        parseCommandU(args)
    elif command == '-t':
        parseCommandT(args)
    elif command == '-cpu':
        parseCommandCPU(args)
    else:
        print('###command unreconized!!!')
        printHelp()


def parseCommandCPU(args):
    if args[2] == '-h':
        printHelpCPU()
        return

    length = len(args[2:])
    if length > 1:
        print('###too many args!!!')
        printHelpCPU()
        return
    if length < 1:
        print('###not enough args!!!')
        printHelpCPU()
    else:
        while True:
            cpu = AndroidUtil.getCpu('com.UCMobile')
            TaskLogger.debugLog(cpu)
            sleep(float(args[2]))
    pass


def parseCommandL(args):
    if args[2] == '-h':
        printHelpLaunch()
        return
    length = len(args[2:])
    packageUC = 'com.UCMobile'
    activityUC = 'com.UCMobile.main.UCMobile'
    packageVT = 'com.example.videoviewtest'
    activityVT = '.MainActivity'
    if length > 2 :
        print('###too many args!!!')
        printHelpLaunch()
    elif length == 0:
        BrowserUtils.launchBrowser(packageUC, activityUC)
    elif length == 1:
        if args[2] == 'uc':
            BrowserUtils.launchBrowser(packageUC, activityUC)
        elif args[2] == 'vt':
            BrowserUtils.launchBrowser(packageVT, activityVT)
        else:
            print('###not enough args!!!')
            printHelpLaunch()
    elif length == 2:
        if args[3] == 'uc':
            BrowserUtils.launchBrowser(args[2], activityUC)
        elif args[3] == 'vt':
            BrowserUtils.launchBrowser(args[2], activityVT)
        else:
            BrowserUtils.launchBrowser(args[2], args[3])
    pass

def parseCommandS(args):
    if args[2] == '-h':
        printHelpShutdown()
        return
    length = len(args[2:])
    packageUC = 'com.UCMobile'
    packageVT = 'com.example.videoviewtest'
    if length > 1 :
        print('###too many args!!!')
        printHelpShutdown()
    elif length == 0:
        BrowserUtils.closeBrowser(packageUC)
    else:
        if args[2] == 'uc':
            BrowserUtils.closeBrowser(packageUC)
        if args[2] == 'vt':
            BrowserUtils.closeBrowser(packageVT)
        else:
            BrowserUtils.closeBrowser(args[2])
    pass

def parseCommandU(args):
    if args[2] == '-h':
        printHelpBrowseUrl()
        return
    length = len(args[2:])
    packageUC = 'com.UCMobile'
    packageVT = 'com.example.videoviewtest'
    activityUC = 'com.UCMobile.main.UCMobile'
    activityVT = '.MainActivity'
    if length < 2:
        print('###not enough args!!!')
        printHelpBrowseUrl()
        return
    elif length > 3 :
        print('###too many args!!!')
        printHelpBrowseUrl()
        return
    elif length == 2:
        if args[3] == 'uc':
            BrowserUtils.openURI(args[2], packageUC, activityUC)
        elif args[3] == 'vt':
            BrowserUtils.openURI(args[2], packageVT, activityVT)
        else:
            print('###not enough args!!!')
            printHelpBrowseUrl()
    elif length == 3:
        if args[4] == 'uc':
            BrowserUtils.openURI(args[2], args[3], activityUC)
        elif args[4] == 'vt':
            BrowserUtils.openURI(args[2], args[3], activityVT)
        else:
            BrowserUtils.openURI(args[2], args[3], args[4])
    pass

def parseCommandT(args):
    if args[2] == '-h':
        printHelpTest()
        return
    length = len(args[2:])
    config = 'confg.ini'
    if length < 1:
        print('###not enough args!!!')
        printHelpTest()
    elif length > 2:
        print('###too many args!!!')
        printHelpTest()
    elif length == 2:
        config = args[3]
        pass
    print config
    # task = args[2]

    # TODO put task to taskRunner and run a test by config
    pass

def parseCommandC(args):
    if args[2] == '-h':
        printHelpChange()
        return
    length = len(args[2:])
    if length < 2:
        print('###not enough args!!!')
        printHelpChange()
        return
    elif length > 3 :
        print('###too many args!!!')
        printHelpChange()
        return
    elif length == 2:
        callChangeLib(args[2], args[3])
    else:
        callChangeLib(args[2], args[3], args[4]) 

def callChangeLib(path, target, package=None):
    if package is None:
        package = 'com.UCMobile'

    
    if target == 'uc' or target == 'hc' or target == 'vt':
        AndroidUtil.switchApollo(path, target, 0, package)
    else:
        print('###target (%s) incorrect!!!' % target)
        printHelpChange()



if __name__ == '__main__':
    PROG = sys.argv[0]
    parseCommand(sys.argv)