import threading
import traceback
import sys
import datetime
import time
from abc import abstractmethod
from com.uc.utils.TaskLogger import TaskLogger


class LogMonitor(threading.Thread):

    def __init__(self, package=None, activity=None):
        threading.Thread.__init__(self)
        self.isRunning = True
        self.handler = None
        self.isStop = False
        self.package = package
        self.activity = activity

    def isRunning(self):
        return self.__isRunning

    def setHandler(self, handler):
        self.handler = handler

    def setActivity(self, activity):
        self.activity = activity

    def setPackage(self, package):
        self.package = package

    def run(self):
        self.isRunning = True
        try:
            self.doMonitor()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            TaskLogger.errorLog("Exception: {}".format(exc_value))
            TaskLogger.errorLog("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
        finally:
            TaskLogger.\
                errorLog('==========THREAD %s end==========' % self.getName())
            self.isRunning = False

    def stop(self):
        self.isStop = True

    def parseLog(self, lineStr, prefix, suffix):
        start = lineStr.find(prefix)
        if start >= 0:
            if len(suffix) > 0:
                end = lineStr.find(suffix, start + len(prefix))
            else:
                end = len(lineStr)
            result = float(lineStr[start + len(prefix):end].strip())
            return result

    def parseLogStr(self, lineStr, prefix, suffix):
        start = lineStr.find(prefix)
        if start >= 0:
            if len(suffix) > 0:
                end = lineStr.find(suffix, start + len(prefix))
            else:
                end = len(lineStr)
            result = lineStr[start + len(prefix):end].strip()
            return result

    def parseTime(self, lineStr):
        _year = time.localtime(time.time())[0]
        _month, _day = lineStr.split()[0].split('-')
        _time, _micro = lineStr.split()[1].split('.')
        _hour, _minute, _second = _time.split(':')
        return datetime.datetime(int(_year), int(_month), int(_day), int(_hour), int(_minute), int(_second), long(_micro)*1000)
        pass

    @abstractmethod
    def doMonitor(self):
        pass

    @abstractmethod
    def init(self):
        pass
