#!/usr/bin/python
# coding=utf-8


import os
import sys

sys.path.append(os.getcwd())

from com.uc.task.TaskManager import TaskManager
from com.uc.taskImpl.CoreT1TestTask import CoreT1TestTask
from com.uc.taskImpl.ApolloT1TestTask import ApolloT1TestTask
from com.uc.taskImpl.ApolloT2TestTask import ApolloT2TestTask
from com.uc.taskImpl.ApolloT2AndMemoryTestTask import ApolloT2AndMemoryTestTask
from com.uc.taskImpl.MXPlayerMemTestTask import MXPlayerMemTestTask
from com.uc.taskImpl.VideoTestMemTestTask import VideoTestMemTestTask
from com.uc.taskImpl.MemoryTestTask import MemoryTestTask
from com.uc.taskImpl.ApolloFrameTestTask import ApolloFrameTestTask
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import GConf
import datetime

from com.uc.data.CSVRecorder import CSVRecorder
from com.uc.data.ResultGenerator import ResultGenerator
from com.uc.data.DataFilter import DataFilter
from com.uc.utils import AndroidUtil
from com.uc.utils.BrowserUtils import setCDParams
from com.uc.utils.BrowserUtils import launchBrowser
from com.uc.utils.BrowserUtils import openURI
from com.uc.utils import BrowserUtils
import traceback

if __name__ == '__main__':
    GConf.initConfig()
    # raise Exception("debug")
    starttime = datetime.datetime.now()
    TaskLogger.init()
    recorder = CSVRecorder()

    # recorder.loadData('/opt/lampp/htdocs/videotest/origin/record-test.csv')
    # recorder.loadData('/opt/lampp/htdocs/videotest/origin/record-1505112125.csv')
    # recorder.loadData('/opt/lampp/htdocs/videotest/origin/record-1505121614.csv')
    # recorder.loadData('/opt/lampp/htdocs/videotest/origin/record-1505131039.csv')

    try:
        path = GConf.getGlobal('REPORT_DIR')
        print path
        recorder.loadData('/home/tangjp/work/vr/test/wangjb-cache-mem-t2-record-1507012121.csv')
        # recorder.loadData('/opt/lampp/htdocs/videotest/origin/vt-vs-mx-mem-record-1506251042.csv')
        # recorder.loadData('/home/tangjp/work/vr/test/241_vs_231_for_T1-record-1506241915.csv')
        rg = ResultGenerator()
        rg.generateResult(recorder)
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        TaskLogger.errorLog("Exception: {}".format(exc_value))
        TaskLogger.errorLog("#######STACK TRACE:")
        traceback.print_tb(exc_traceback)
    finally:
        raise Exception("end")


    manager = TaskManager()
    # mxtask = MXPlayerMemTestTask()
    # mxtask.setPackage('com.mxtech.videoplayer.ad')
    # mxtask.setActivity('.ActivityScreen')
    # mxtask = VideoTestMemTestTask()
    # mxtask.setPackage('com.example.videoviewtest')
    # mxtask.setActivity('.MainActivity')
    # mxtask.setDataRecord(recorder)
    # manager.addTask(mxtask)

    playerCount = GConf.getGlobalInt('PLAYER_COUNT')
    libStr = GConf.getGlobal('PLAYER_LIB')
    libList = libStr.splitlines()
    if playerCount > len(libList):
        playerCount = len(libList)
    for i in range(playerCount):
        TaskLogger.infoLog("===========ADD TASK {}===========".format(i))
        mxtask = ApolloFrameTestTask()
        mxtask.setPlayerPath(libList[i])
        # mxtask.setPackage('com.example.videoviewtest')
        # mxtask.setActivity('.MainActivity')
        mxtask.setPlayerType(GConf.getGlobalInt('LIBPOS'))
        mxtask.setDataRecord(recorder)
        manager.addTask(mxtask)

    # cdCount = GConf.getGlobalInt('CD_COUNT')
    # cdStr = GConf.getGlobal('CD_PARAM')
    # cdList = cdStr.splitlines()
    # if GConf.getGlobalInt('CD_COUNT') > len(cdList):
    #     cdCount = len(cdList)
    # for i in range(cdCount):
    #     TaskLogger.infoLog("===========ADD TASK {}===========".format(i))
    #     t1task = ApolloT1TestTask()
    #     t1task.setCD('u3js_video_proxy', '0')
    #     t1task.setCD('apollo_str', cdList[i])
    #     t1task.setPlayerPath(GConf.getGlobal('PLAYER_LIB').splitlines()[0])
    #     t1task.setDataRecord(recorder)
    #     manager.addTask(t1task)
    #     t1task = None

    result = 1
    try:
        TaskLogger.infoLog('===========TEST START===========')
        result = manager.startTest()
    except:
        TaskLogger.errorLog('===========TEST ABOART===========')
    finally:
        # if False:
        if result == 0:
            TaskLogger.infoLog('===========SAVE DATA===========')
            recorder.onComplete()

            TaskLogger.infoLog('===========GENERATE RESULT===========')
            TaskLogger.debugLog(recorder.getRecordPath())
            ret = CSVRecorder()
            ret.loadData(recorder.getRecordPath())
            rg = ResultGenerator()
            rg.generateResult(ret)
            pass
        else:
            TaskLogger.errorLog('===========TEST FAILED===========')
        TaskLogger.infoLog('===========STOP TEST===========')
        manager.stopTest()
        endtime = datetime.datetime.now()
        duration = endtime-starttime
        TaskLogger.infoLog("TEST COSTS %s" % str(duration))
        TaskLogger.detailLog("Log file: file://%s" % TaskLogger.instance.logfile)
