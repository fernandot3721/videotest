#!/usr/bin/python
# coding=utf-8


from os.path import sys

sys.path.append('/home/tangjp/work/videotest')

from com.uc.task.TaskManager import TaskManager
from com.uc.taskImpl.CoreT1TestTask import CoreT1TestTask
from com.uc.taskImpl.ErrorBeforePlayTestTask import ErrorBeforePlayTestTask
from com.uc.taskImpl.NotFirstT1TestTask import NotFirstT1TestTask
from com.uc.taskImpl.T1TestTask import T1TestTask
from com.uc.taskImpl.T2TestTask import T2TestTask
from com.uc.utils.ColorUtil import *



if __name__ == '__main__':
    
    print ingreen("===========ADD TASK===========")
    manager = TaskManager()
    t1task = CoreT1TestTask()
    manager.addTask(t1task)
#   playResultTask = ErrorBeforePlayTestTask()
#     t2task = T2TestTask()
#     NFt1task = NotFirstT1TestTask()
#     manager.addTask(playResultTask1)

#    manager.addTask(playResultTask)
#     manager.addTask(t2task)
#     manager.addTask(NFt1task)
    
    result = manager.startTest()
     
    if result == 0:
        print ingreen('===========TEST COMPLETE===========')
        pass 
    else:
        print inred('===========TEST FAILED===========')
    manager.stopTest()

