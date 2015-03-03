# encoding: utf-8
from os.path import sys
import time
from com.uc.html.HtmlBuilder import HtmlBuilder
from com.uc.log.LogcatMonitor import LogcatMonitor
from com.uc.utils.TaskLogger import TaskLogger
import traceback
from com.uc.conf import Conf
import os


class TaskManager:
    taskList = []
    monitorThread = LogcatMonitor()
    htmlBuilder = HtmlBuilder()

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
        self.htmlBuilder.addNode(task)
        task.setManager(self)
        pass

    def startTest(self):
        try:
            TaskLogger.infoLog("===========EXECUTE TASK===========")
            for task in self.taskList:
                self.monitorThread.setLogListener(task)
                task.run()

            TaskLogger.infoLog("===========GERNERATE REPORT===========")
            htmlcode = self.htmlBuilder.generatingRepors()
            timelog = time.strftime('%Y%m%d%H%M')[2:]
            resultFile = '{}report-{}.html'.format(Conf.DATA_DIR, timelog)
            f1 = open(resultFile, 'w')
            TaskLogger.detailLog("view result: file://{}".format(resultFile))
            f1.write(htmlcode)
            f1.close()

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
