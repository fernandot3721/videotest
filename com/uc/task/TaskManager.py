# encoding: utf-8
from os.path import sys
from com.uc.log.AndroidLogcat import AndroidLogcat
from com.uc.utils.TaskLogger import TaskLogger
import traceback
import os


class TaskManager:
    taskList = []
    monitorThread = AndroidLogcat()

    def __init__(self):
        os.system('adb logcat -c')
        self.monitorThread.start()
        pass

    def shouldTerminate(self):
        if self.monitorThread.isRunning:
            return False
        else:
            TaskLogger.debugLog("monitorThread failed")
            return True

    def addTask(self, task):
        self.taskList.append(task)
        task.setManager(self)
        pass

    def startTest(self):
        try:
            TaskLogger.infoLog("===========EXECUTE TASK===========")
            for task in self.taskList:
                self.monitorThread.setHandler(task)
                self.monitorThread.init()
                task.run()
            return 0
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            TaskLogger.errorLog("Exception: {}".format(exc_value))
            TaskLogger.errorLog("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
            return -1

    def stopTest(self):
        self.monitorThread.stop()
        self.monitorThread.join()
