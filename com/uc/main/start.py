#!/usr/bin/python
# coding=utf-8


import os
import sys

sys.path.append(os.getcwd())

from com.uc.task.TaskManager import TaskManager
from com.uc.taskImpl.CoreT1TestTask import CoreT1TestTask
from com.uc.taskImpl.ApolloT1TestTask import ApolloT1TestTask
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import Conf
import datetime

from com.uc.data.CSVRecorder import CSVRecorder
from com.uc.data.ResultGenerator import ResultGenerator
from com.uc.data.DataFilter import DataFilter
from com.uc.utils import AndroidUtil
from com.uc.utils.BrowserUtils import setCDParams

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

    # recorder.loadData('/opt/lampp/htdocs/videotest/origin/record-1503011113.csv')

    # filter = DataFilter()
    # rg = ResultGenerator()
    # rg.generateResult(recorder)

    # AndroidUtil.switchApollo('/home/tangjp/work/vr/apolloso/2.13/')
    # setCDParams('u3js_video_proxy', '0')
    # setCDParams('apollo_str', 'mov_seg_dur=120')
    # raise Exception("end")

    manager = TaskManager()

    # playerCount = Conf.PLAYER_COUNT
    # if Conf.PLAYER_COUNT > len(Conf.PLAYER_LIB):
    #     playerCount = len(Conf.PLAYER_LIB)
    # for i in range(playerCount):
    #     TaskLogger.infoLog("===========ADD TASK {}===========".format(i))
    #     t1task = CoreT1TestTask()
    #     t1task.setPlayerPath(Conf.PLAYER_LIB[i])
    #     t1task.setDataRecord(recorder)
    #     manager.addTask(t1task)
    #     t1task = None

    cdCount = Conf.CD_COUNT
    if Conf.CD_COUNT > len(Conf.CD_PARAM):
        cdCount = len(Conf.CD_PARAM)
    for i in range(cdCount):
        TaskLogger.infoLog("===========ADD TASK {}===========".format(i))
        t1task = ApolloT1TestTask()
        t1task.setCD('u3js_video_proxy', '0')
        t1task.setCD('apollo_str', Conf.CD_PARAM[i])
        t1task.setPlayerPath(Conf.PLAYER_LIB[0])
        t1task.setDataRecord(recorder)
        manager.addTask(t1task)
        t1task = None

    result = manager.startTest()
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
    duration = (endtime-starttime).seconds
    TaskLogger.infoLog("TEST COSTS %s seconds" % duration)
    TaskLogger.detailLog("Log file: file://%s" % TaskLogger.logfile)
