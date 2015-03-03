# encoding: utf-8

import os
from com.uc.conf import Conf
from com.uc.utils import BrowserUtils
from time import sleep
from com.uc.utils.TaskLogger import TaskLogger


def switchApollo(pathFrom):
    TaskLogger.normalLog("SHUTDOWN UC")
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
    TaskLogger.normalLog(mvffInCmd1)
    os.system(mvu3InCmd1)
    TaskLogger.normalLog(mvffInCmd2)
    os.system(mvffInCmd2)
    TaskLogger.normalLog(mvu3InCmd2)
    os.system(mvu3InCmd2)
    pass

# def testApollo():
#   videoPath = Conf.SEVER_ADDRESS + "t1_200k/test_video_short.html"
#   BrowserUtils.launchBrowser()
#   sleep(Conf.WAIT_TIME)
#   BrowserUtils.openURI(self.urlList[self.currentCategory])
#   sleep(Conf.WAIT_TIME)
#   checkApolloCmd = "adb logcat"
