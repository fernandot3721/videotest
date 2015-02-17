#!/usr/bin/python
# coding=utf-8


import os, sys

sys.path.append(os.getcwd())

from com.uc.task.TaskManager import TaskManager
from com.uc.taskImpl.CoreT1TestTask import CoreT1TestTask
from com.uc.taskImpl.ErrorBeforePlayTestTask import ErrorBeforePlayTestTask
from com.uc.taskImpl.NotFirstT1TestTask import NotFirstT1TestTask
from com.uc.taskImpl.T1TestTask import T1TestTask
from com.uc.taskImpl.T2TestTask import T2TestTask
from com.uc.utils.ColorUtil import *
from com.uc.conf import Conf
import datetime

from com.uc.data.CSVRecorder import CSVRecorder

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    recorder = CSVRecorder()
    # recorder.testWrite()
    # recorder.onData('2.25-CORE-T1-TEST', '50_l', '2230.0')
    # recorder.onData('2.25-CORE-T1-TEST', '100_l', '2230.0')
    # recorder.onData('2.25-CORE-T1-TEST', '200_l', '2230.0')
    # recorder.onData('2.26-CORE-T1-TEST', '50_l', '2230.0')
    # recorder.onData('2.26-CORE-T1-TEST', '100_l', '2230.0')
    # recorder.onData('2.26-CORE-T1-TEST', '200_l', '2230.0')
    # recorder.onComplete()
    # raise Exception("end")

    manager = TaskManager()

    playerCount = Conf.PLAYER_COUNT
    if Conf.PLAYER_COUNT > len(Conf.PLAYER_LIB):
        playerCount = len(Conf.PLAYER_LIB)
    for i in range(playerCount):
        print ingreen("===========ADD TASK {}===========".format(i))
        t1task = CoreT1TestTask()
        t1task.setPlayerPath(Conf.PLAYER_LIB[i])
        t1task.setDataRecord(recorder)
        manager.addTask(t1task)
        t1task = None

    result = manager.startTest()
     
    if result == 0:
        print ingreen('===========TEST COMPLETE===========')
        recorder.onComplete()
        pass 
    else:
        print inred('===========TEST FAILED===========')
    manager.stopTest()
    endtime = datetime.datetime.now()
    print ingreen("TEST COSTS {} seconds".format((endtime-starttime).seconds))

