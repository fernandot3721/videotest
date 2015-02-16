# encoding: utf-8

import os
from com.uc.conf import Conf
from com.uc.utils import BrowserUtils
from time import sleep

def switchApollo(pathFrom):
	print "SHUTDOWN UC"
	BrowserUtils.closeBrowser()
	sleep(Conf.WAIT_TIME)

	libffmpeg = 'libffmpeg.so'
	libu3player = 'libu3player.so'
	# pathFrom = ' /home/tangjp/work/vr/apolloso/2.8.8.888/'
	pathTmp = '/sdcard/UCDownloads/'
	pathTo = 'data/data/{}/apollo1/'.format(Conf.PACKAGE_NAME)

	pushffInCmd = "adb push {}{} {}{}".format(pathFrom, libffmpeg, pathTmp, libffmpeg)
	pushu3InCmd = "adb push {}{} {}{}".format(pathFrom, libu3player, pathTmp, libu3player)
	mvffInCmd = "adb shell su -c \"cat {}{} > {}{}\"".format(pathTmp, libffmpeg, pathTo, libffmpeg)
	mvu3InCmd = "adb shell su -c \"cat {}{} > {}{}\"".format(pathTmp, libu3player, pathTo, libu3player)

	print pushffInCmd
	os.system(pushffInCmd)
	print pushu3InCmd
	os.system(pushu3InCmd)
	print mvffInCmd
	os.system(mvffInCmd)
	print mvu3InCmd
	os.system(mvu3InCmd)
	pass

# def testApollo():
# 	videoPath = Conf.SEVER_ADDRESS + "t1_200k/test_video_short.html"
# 	BrowserUtils.launchBrowser()
# 	sleep(Conf.WAIT_TIME)
# 	BrowserUtils.openURI(self.urlList[self.currentCategory])
# 	sleep(Conf.WAIT_TIME)
# 	checkApolloCmd = "adb logcat"
