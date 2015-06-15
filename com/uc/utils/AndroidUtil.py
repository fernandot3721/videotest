# encoding: utf-8

import os
from com.uc.conf import GConf
from com.uc.utils import BrowserUtils
from time import sleep
from com.uc.utils.TaskLogger import TaskLogger


def execCmd(cmd, wait):
    TaskLogger.debugLog(cmd)
    os.system(cmd)
    sleep(wait)


def doSwitch(pathFrom, pathTo, name, wait):
    pathTmp = '/sdcard/UCDownloads/'

    pushCmd = "adb push %s%s %s%s" % (pathFrom, name, pathTmp, name)
    execCmd(pushCmd, wait)
    mvCmd = "adb shell su -c \"cat %s%s > %s%s\"" % (pathTmp, name, pathTo, name)
    execCmd(mvCmd, wait)
    chCmd = "adb shell su -c \"chmod 777 %s%s\"" % (pathTo, name)
    execCmd(chCmd, wait)


def doSwitchApollo(pathFrom, pathTo, wait):

    libffmpeg = 'libffmpeg.so'
    libu3player = 'libu3player.so'
    librender = 'librenderer.so'
    libomx40 = 'libomxdr_40.so'
    libomx42 = 'libomxdr_42.so'
    libomx44 = 'libomxdr_44.so'

    doSwitch(pathFrom, pathTo, libffmpeg, wait)
    doSwitch(pathFrom, pathTo, libu3player, wait)
    doSwitch(pathFrom, pathTo, librender, wait)
    doSwitch(pathFrom, pathTo, libomx40, wait)
    doSwitch(pathFrom, pathTo, libomx42, wait)
    doSwitch(pathFrom, pathTo, libomx44, wait)

def switchApollo(pathFrom, target='uc', wait=None, package=None):
    if pathFrom == "":
        TaskLogger.errorLog("apollo path null")
        return

    if package is None:
        package = GConf.getCase('PACKAGE_NAME')

    if wait is None:
        wait = GConf.getCaseInt('WAIT_TIME')

    TaskLogger.normalLog("switchApollo")
    BrowserUtils.closeBrowser()
    sleep(wait)

    if target == 'uc':
        if package is None:
            package = 'com.UCMobile'
        pathTo = '/data/data/%s/apollo2/' % package
        pathTo2 = '/data/data/%s/apollo1/' % package
        doSwitchApollo(pathFrom, pathTo2, wait)
        pass
    elif target == 'hc':
        if package is None:
            package = 'com.UCMobile'
        pathTo = '/data/data/%s/lib/' % package
        pass
    elif target == 'vt':
        pathTo = '/data/data/com.example.videoviewtest/lib/'
        pass
    else:
        TaskLogger.infoLog("not need to switch apollo")
        return

    doSwitchApollo(pathFrom, pathTo, wait)


def getPid(package=None):
    if package is None:
        package = GConf.getCase('PACKAGE_NAME')
    cmd = 'adb shell ps | tr \"\\r\\n\" \"\\n\" | grep "%s$" | awk \'{print $2}\'' % package
    # TaskLogger.debugLog(cmd)
    return os.popen(cmd).read().strip()


def getCpuUsage(pid):
    cmd = 'adb shell su -c \'top -d 0 -n 1\' | grep \'%s\\s\'' % pid
    # TaskLogger.debugLog(cmd)
    return os.popen(cmd).read().strip()

def getCpu(package=None):
    if package is None:
        # TaskLogger.errorLog('package not set')
        package = GConf.getCase('PACKAGE_NAME')
    cmd = 'adb shell su -c \'top -d 0 -n 1\' | tr \"\\r\\n\" \"\\n\" | grep %s$ | awk \'{print $3}\' | tr -d \'%%\'' % package
    # TaskLogger.debugLog(cmd)
    return int(os.popen(cmd).read().strip())

def getPrivateDirty(package):
    if package is None:
        package = GConf.getCase('PACKAGE_NAME')
    cmd = 'adb shell dumpsys meminfo %s | grep TOTAL | awk \'{print $3}\'' % package
    # TaskLogger.infoLog(cmd)
    return os.popen(cmd).read().strip()


def getPrivateClean(package):
    if package is None:
        package = GConf.getCase('PACKAGE_NAME')
    cmd = 'adb shell dumpsys meminfo %s | grep TOTAL | awk \'{print $4}\'' % package
    # TaskLogger.infoLog(cmd)
    return os.popen(cmd).read().strip()


def getUss(package):
    if package is None:
        package = GConf.getCase('PACKAGE_NAME')
    cmd = 'adb shell dumpsys meminfo %s | grep TOTAL | awk \'{total = $3 + $4; print total}\'' % package
    # TaskLogger.infoLog(cmd)
    return os.popen(cmd).read().strip()


def getMemFree():
    cmd = 'adb shell \'cat /proc/meminfo\' | grep MemFree | awk \'{print $2}\''
    return os.popen(cmd).read().strip()


def getBuffers():
    cmd = 'adb shell \'cat /proc/meminfo\' | grep Buffers | awk \'{print $2}\''
    return os.popen(cmd).read().strip()


def getCached():
    cmd = 'adb shell \'cat /proc/meminfo\' | grep Cached | awk \'NR==1 {print $2}\''
    # TaskLogger.debugLog(cmd)
    return os.popen(cmd).read().strip()


def getRealMemfree():
    cmd = 'adb shell \'cat /proc/meminfo\' | awk \'/MemFree|Buffers|Cached/ {if (NR<5) {total += $2}} END {print total}\''
    return os.popen(cmd).read().strip()


def testMemfree():
    cmd = 'adb shell \'cat /proc/meminfo\' | awk \'BEGIN {total = 0} /MemFree|Buffers|Cached/ {if (NR<5) {total += 1}} END {print total}\''
    result = os.popen(cmd).read().strip()
    # TaskLogger.debugLog('result is [%s]' % result)
    if (result == '3'):
        TaskLogger.debugLog('MemFree detection is reliable!')
        return True
    else:
        TaskLogger.errorLog('MemFree detection is NOT reliable!')
        return False
