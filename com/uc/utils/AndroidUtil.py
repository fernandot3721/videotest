# encoding: utf-8

import os
from com.uc.conf import Conf
from com.uc.utils import BrowserUtils
from time import sleep
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.utils import VideoTestUtil


def switchApollo(pathFrom):
    if pathFrom == "":
        TaskLogger.errorLog("apollo path null")
        return
    TaskLogger.normalLog("switchApollo")
    BrowserUtils.closeBrowser()
    sleep(Conf.WAIT_TIME)

    libffmpeg = 'libffmpeg.so'
    libu3player = 'libu3player.so'
    # pathFrom = ' /home/tangjp/work/vr/apolloso/2.8.8.888/'
    pathTmp = '/sdcard/UCDownloads/'
    pathTo1 = '/data/data/{}/apollo1/'.format(Conf.PACKAGE_NAME)
    pathTo2 = '/data/data/{}/apollo2/'.format(Conf.PACKAGE_NAME)

    pushffInCmd = "adb push %s%s %s%s" % \
        (pathFrom, libffmpeg, pathTmp, libffmpeg)
    pushu3InCmd = "adb push %s%s %s%s" % \
        (pathFrom, libu3player, pathTmp, libu3player)
    mvffInCmd1 = "adb shell su -c \"cat %s%s > %s%s\"" % \
        (pathTmp, libffmpeg, pathTo1, libffmpeg)
    mvu3InCmd1 = "adb shell su -c \"cat %s%s > %s%s\"" % \
        (pathTmp, libu3player, pathTo1, libu3player)
    mvffInCmd2 = "adb shell su -c \"cat %s%s > %s%s\"" % \
        (pathTmp, libffmpeg, pathTo2, libffmpeg)
    mvu3InCmd2 = "adb shell su -c \"cat %s%s > %s%s\"" % \
        (pathTmp, libu3player, pathTo2, libu3player)

    TaskLogger.normalLog(pushffInCmd)
    os.system(pushffInCmd)
    TaskLogger.normalLog(pushu3InCmd)
    os.system(pushu3InCmd)
    TaskLogger.normalLog(mvffInCmd1)
    os.system(mvffInCmd1)
    sleep(Conf.WAIT_TIME)
    TaskLogger.normalLog(mvu3InCmd1)
    os.system(mvu3InCmd1)
    sleep(Conf.WAIT_TIME)
    TaskLogger.normalLog(mvffInCmd2)
    os.system(mvffInCmd2)
    sleep(Conf.WAIT_TIME)
    TaskLogger.normalLog(mvu3InCmd2)
    os.system(mvu3InCmd2)
    pass


def switchHardCodeApollo(pathFrom):
    if pathFrom == "":
        TaskLogger.errorLog("apollo path null")
        return
    TaskLogger.normalLog("switchHardCodeApollo")
    BrowserUtils.closeBrowser()
    sleep(Conf.WAIT_TIME)

    libffmpeg = 'libffmpeg.so'
    libu3player = 'libu3player.so'
    # pathFrom = ' /home/tangjp/work/vr/apolloso/2.8.8.888/'
    pathTmp = '/sdcard/UCDownloads/'
    pathTo = '/data/data/{}/lib/'.format(Conf.PACKAGE_NAME)

    pushffInCmd = "adb push %s%s %s%s" % \
        (pathFrom, libffmpeg, pathTmp, libffmpeg)
    pushu3InCmd = "adb push %s%s %s%s" % \
        (pathFrom, libu3player, pathTmp, libu3player)
    mvffInCmd = "adb shell su -c \"cat %s%s > %s%s\"" % \
        (pathTmp, libffmpeg, pathTo, libffmpeg)
    mvu3InCmd = "adb shell su -c \"cat %s%s > %s%s\"" % \
        (pathTmp, libu3player, pathTo, libu3player)

    TaskLogger.normalLog(pushffInCmd)
    os.system(pushffInCmd)
    TaskLogger.normalLog(pushu3InCmd)
    os.system(pushu3InCmd)
    TaskLogger.normalLog(mvffInCmd)
    os.system(mvffInCmd)
    sleep(Conf.WAIT_TIME)
    TaskLogger.normalLog(mvu3InCmd)
    os.system(mvu3InCmd)
    pass


def switchVideoTestApollo(pathFrom):
    if pathFrom == "":
        TaskLogger.errorLog("apollo path null")
        return
    TaskLogger.normalLog("switchVideoTestApollo")
    VideoTestUtil.closeBrowser()
    sleep(Conf.WAIT_TIME)

    libffmpeg = 'libffmpeg.so'
    libu3player = 'libu3player.so'
    # pathFrom = ' /home/tangjp/work/vr/apolloso/2.8.8.888/'
    pathTmp = '/sdcard/UCDownloads/'
    pathTo = '/data/data/com.example.videoviewtest/lib/'

    pushffInCmd = "adb push %s%s %s%s" % \
        (pathFrom, libffmpeg, pathTmp, libffmpeg)
    pushu3InCmd = "adb push %s%s %s%s" % \
        (pathFrom, libu3player, pathTmp, libu3player)
    mvffInCmd = "adb shell su -c \"cat %s%s > %s%s\"" % \
        (pathTmp, libffmpeg, pathTo, libffmpeg)
    mvu3InCmd = "adb shell su -c \"cat %s%s > %s%s\"" % \
        (pathTmp, libu3player, pathTo, libu3player)

    TaskLogger.normalLog(pushffInCmd)
    os.system(pushffInCmd)
    TaskLogger.normalLog(pushu3InCmd)
    os.system(pushu3InCmd)
    TaskLogger.normalLog(mvffInCmd)
    os.system(mvffInCmd)
    sleep(Conf.WAIT_TIME)
    TaskLogger.normalLog(mvu3InCmd)
    os.system(mvu3InCmd)
    pass


def getPid(package):
    if package is None:
        package = Conf.PACKAGE_NAME
    # cmd = 'adb shell ps | tr \"\\r\\n\" \"\\n\" | grep "%s\%"' % Conf.PACKAGE_NAME
    cmd = 'adb shell ps | tr \"\\r\\n\" \"\\n\" | grep "%s$" | awk \'{print $2}\'' % package
    # TaskLogger.debugLog(cmd)
    return os.popen(cmd).read().strip()


def getCpuUsage(pid):
    cmd = 'adb shell su -c \'top -d 0 -n 1\' | grep \'%s\\s\'' % pid
    # TaskLogger.debugLog(cmd)
    return os.popen(cmd).read().strip()

def getCpu(package):
    if package is None:
        # TaskLogger.errorLog('package not set')
        package = Conf.PACKAGE_NAME
    cmd = 'adb shell su -c \'top -d 0 -n 1\' | tr \"\\r\\n\" \"\\n\" | grep %s$ | awk \'{print $3}\' | tr -d \'%%\'' % package
    # TaskLogger.debugLog(cmd)
    return int(os.popen(cmd).read().strip())

def getPrivateDirty(package):
    if package is None:
        package = Conf.PACKAGE_NAME
    cmd = 'adb shell dumpsys meminfo %s | grep TOTAL | awk \'{print $3}\'' % package
    # TaskLogger.infoLog(cmd)
    return os.popen(cmd).read().strip()


def getPrivateClean(package):
    if package is None:
        package = Conf.PACKAGE_NAME
    cmd = 'adb shell dumpsys meminfo %s | grep TOTAL | awk \'{print $4}\'' % package
    # TaskLogger.infoLog(cmd)
    return os.popen(cmd).read().strip()


def getUss(package):
    if package is None:
        package = Conf.PACKAGE_NAME
    cmd = 'adb shell dumpsys meminfo %s | grep TOTAL | awk \'{total = $3 + $4; print total}\'' % package
    # cmd = 'adb shell dumpsys meminfo %s | grep TOTAL | awk \'{total = $3 + $4; print total; print $3; print $4}\'' % Conf.PACKAGE_NAME
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

# def testApollo():
#   videoPath = Conf.SEVER_ADDRESS + "t1_200k/test_video_short.html"
#   BrowserUtils.launchBrowser()
#   sleep(Conf.WAIT_TIME)
#   BrowserUtils.openURI(self.urlList[self.currentCategory])
#   sleep(Conf.WAIT_TIME)
#   checkApolloCmd = "adb logcat"
