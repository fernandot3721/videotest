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
from com.uc.taskImpl.MemoryTestTask import MemoryTestTask
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import Conf
import datetime

from com.uc.data.CSVRecorder import CSVRecorder
from com.uc.data.ResultGenerator import ResultGenerator
from com.uc.data.DataFilter import DataFilter
from com.uc.utils import AndroidUtil
from com.uc.utils.BrowserUtils import setCDParams
from com.uc.utils.BrowserUtils import launchBrowser
from com.uc.utils.BrowserUtils import openURI
from com.uc.utils import BrowserUtils

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    TaskLogger.init()
    # recorder = CSVRecorder()

    # recorder.loadData()
    # recorder.testWrite()
    # recorder.onData('2.25-CORE-T1-TEST', '50_l', '2230.0')
    # recorder.onData('2.25-CORE-T1-TEST', '100_l', '2230.0')
    # recorder.onData('2.25-CORE-T1-TEST', '200_l', '2230.0')
    # recorder.onData('2.26-CORE-T1-TEST', '50_l', '2230.0')
    # recorder.onData('2.26-CORE-T1-TEST', '100_l', '2230.0')
    # recorder.onData('2.26-CORE-T1-TEST', '200_l', '2230.0')

    recorder = CSVRecorder()
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '50_l', '22550.0')
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '50_l', '22551.0')
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '50_l', '22552.0')
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '50_l', '22553.0')

    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '100_l', '225101.0')
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '100_l', '225102.0')
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '100_l', '225103.0')
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '100_l', '225104.0')

    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '200_l', '225200.0')
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '200_l', '225201.0')
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '200_l', '225202.0')
    # recorder.onData('{}#2.25'.format(Conf.TASK_TYPE[0]), '200_l', '225203.0')

    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '50_l', '22651.0')
    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '50_l', '22652.0')
    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '50_l', '22653.0')
    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '50_l', '22654.0')

    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '100_l', '226100.0')
    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '100_l', '226101.0')
    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '100_l', '226102.0')
    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '100_l', '226103.0')

    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '200_l', '226201.0')
    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '200_l', '226202.0')
    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '200_l', '226203.0')
    # recorder.onData('{}#2.26'.format(Conf.TASK_TYPE[0]), '200_l', '226204.0')

    # recorder.onComplete()

    # recorder.loadData('/opt/lampp/htdocs/videotest/origin/record-test1.csv')
    # recorder.loadData('/opt/lampp/htdocs/videotest/origin/record-1504101833.csv')

    # filter = DataFilter()
    # # memtask = MemoryTestTask()
    # recorder.onData(memtask, CSVRecorder.TYPE_EXTRA, 'PLAYER_VERSION', '2.2.2.123')
    # recorder.onData(memtask, CSVRecorder.TYPE_EXTRA, 'TASK_TYPE', Conf.TASK_TYPE[0])
    # recorder.onData(memtask, CSVRecorder.TYPE_EXTRA, 'cd key', 'apollo_str:12345')
    # recorder.onData(memtask, CSVRecorder.TYPE_NORMAL, '50k', '235.3')
    # recorder.onData(memtask, CSVRecorder.TYPE_NORMAL, '50k', '335.3')
    # recorder.onData(memtask, CSVRecorder.TYPE_NORMAL, '50k', '435.3')
    # recorder.onData(memtask, CSVRecorder.TYPE_NORMAL, '50k', '535.3')
    # recorder.onData(memtask, CSVRecorder.TYPE_NORMAL, '500k', '235.3')
    # recorder.onData(memtask, CSVRecorder.TYPE_NORMAL, '500k', '335.3')
    # recorder.onData(memtask, CSVRecorder.TYPE_NORMAL, '500k', '435.3')
    # recorder.onData(memtask, CSVRecorder.TYPE_NORMAL, '500k', '535.3')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'memfree', '5000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'memfree', '5020')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'memfree', '5100')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'memfree', '5000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'memfree', '7000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'memfree', '4000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'memfree', '3000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'memfree', '2000')

    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'privateDirty', '5000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'privateDirty', '5020')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'privateDirty', '5100')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'privateDirty', '5000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'privateDirty', '7000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'privateDirty', '4000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'privateDirty', '3000')
    # recorder.onData(memtask, CSVRecorder.TYPE_TIMING, 'privateDirty', '2000')
    # recorder.onComplete()
    # rg = ResultGenerator()
    # rg.generateResult(recorder)
    # raise Exception("end")

    # AndroidUtil.switchApollo('/home/tangjp/work/vr/apolloso/2.2.0.128/')
    # result = AndroidUtil.getPrivateDirty()
    # TaskLogger.debugLog(result)
    # BrowserUtils.launchBrowser()
    # BrowserUtils.openURI('http://192.168.0.4/t1Test/mp4/t1Test_1203Kbps.html')
    # setCDParams('u3js_video_proxy', '0')
    # setCDParams('apollo_str', 'mov_seg_dur=120')
    # TaskLogger.errorLog(AndroidUtil.getUss())
    # if AndroidUtil.testMemfree():
    #     TaskLogger.debugLog('true')
    # else:
    #     TaskLogger.debugLog('false')


    manager = TaskManager()

    playerCount = Conf.PLAYER_COUNT
    if Conf.PLAYER_COUNT > len(Conf.PLAYER_LIB):
        playerCount = len(Conf.PLAYER_LIB)
    for i in range(playerCount):
        TaskLogger.infoLog("===========ADD TASK {}===========".format(0))
        # t2task = ApolloT2TestTask()
        # t2task.setPlayerPath(Conf.PLAYER_LIB[i])
        # t2task.setDataRecord(recorder)
        # manager.addTask(t2task)
 
#t2task = ApolloT2AndMemoryTestTask()
        t2task = ApolloT1TestTask()
        t2task.setPlayerPath(Conf.PLAYER_LIB[i])
        t2task.setDataRecord(recorder)
        manager.addTask(t2task)

        t2task = None

    # cdCount = Conf.CD_COUNT
    # if Conf.CD_COUNT > len(Conf.CD_PARAM):
    #     cdCount = len(Conf.CD_PARAM)
    # for i in range(cdCount):
    #     TaskLogger.infoLog("===========ADD TASK {}===========".format(i))
    #     t1task = ApolloT1TestTask()
    #     t1task.setCD('u3js_video_proxy', '0')
    #     t1task.setCD('apollo_str', Conf.CD_PARAM[i])
    #     t1task.setPlayerPath(Conf.PLAYER_LIB[0])
    #     t1task.setDataRecord(recorder)
    #     manager.addTask(t1task)
    #     t1task = None

    # playerCount = Conf.PLAYER_COUNT
    # if Conf.PLAYER_COUNT > len(Conf.PLAYER_LIB):
    #     playerCount = len(Conf.PLAYER_LIB)
    # TaskLogger.debugLog('playerCount: %s' % playerCount)
    # for i in range(playerCount):
    #     TaskLogger.infoLog("===========ADD TASK {}===========".format(i))
    #     memtask = MemoryTestTask()
    #     # t1task.setCD('u3js_video_proxy', '0')
    #     # t1task.setCD('apollo_str', Conf.CD_PARAM[i])
    #     memtask.setPlayerPath(Conf.PLAYER_LIB[i])
    #     memtask.setDataRecord(recorder)
    #     manager.addTask(memtask)
    #     memtask = None

    try:
        TaskLogger.infoLog('===========TEST START===========')
        result = manager.startTest()
    except:
        TaskLogger.errorLog('===========TEST ABOART===========')
    finally:
        if result == 0:
            TaskLogger.infoLog('===========SAVE DATA===========')
            recorder.onComplete()
            TaskLogger.infoLog('===========GENERATE RESULT===========')
            rg = ResultGenerator()
            rg.generateResult(recorder)
            pass
        else:
            TaskLogger.errorLog('===========TEST FAILED===========')
        manager.stopTest()
        endtime = datetime.datetime.now()
        duration = endtime-starttime
        TaskLogger.infoLog("TEST COSTS %s" % str(duration))
        TaskLogger.detailLog("Log file: file://%s" % TaskLogger.logfile)
