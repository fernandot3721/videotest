import threading
import traceback
import sys
from abc import abstractmethod
from com.uc.utils.TaskLogger import TaskLogger


class LogMonitor(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.isRunning = True
        self.handler = None
        self.isStop = False

    def isRunning(self):
        return self.__isRunning

    def setHandler(self, handler):
        self.handler = handler

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

    @abstractmethod
    def doMonitor(self):
        pass

    @abstractmethod
    def init(self):
        pass
