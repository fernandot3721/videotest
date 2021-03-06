# encoding: utf-8
from os.path import sys
from com.uc.monitor.AndroidLogcat import AndroidLogcat
from com.uc.monitor.AdbTimingMonitor import AdbTimingMonitor
from com.uc.utils.TaskLogger import TaskLogger
import traceback
import os
from com.uc.conf import GConf
from time import sleep


class TaskManager:
    taskList = []
    logcatThread = AndroidLogcat()
    meminfoThread = AdbTimingMonitor()

    def __init__(self):
        os.system('adb logcat -c')
        self.logcatThread.start()
        self.meminfoThread.start()
        pass

    def shouldTerminate(self):
        if self.logcatThread.isRunning:
            return False
        else:
            TaskLogger.debugLog("logcatThread failed")
            return True

    def addTask(self, task):
        self.taskList.append(task)
        task.setManager(self)
        pass

    def startTest(self):
        try:
            TaskLogger.infoLog("===========EXECUTE TASK===========")
            for task in self.taskList:
                self.logcatThread.setHandler(task)
                self.meminfoThread.setHandler(task)
                self.logcatThread.init()
                self.meminfoThread.init()
                self.meminfoThread.setActivity(task.getActivity())
                self.meminfoThread.setPackage(task.getPackage())
                task.run()
            return 0
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            TaskLogger.errorLog("Exception: {}".format(exc_value))
            TaskLogger.errorLog("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
            return 0

    def stopTest(self):
        self.logcatThread.stop()
        sleep(GConf.getCaseInt('WAIT_TIME'))
        self.meminfoThread.stop()
        sleep(GConf.getCaseInt('WAIT_TIME'))
        self.logcatThread.join()
        sleep(GConf.getCaseInt('WAIT_TIME'))
        self.meminfoThread.join()
