import threading
import traceback
import sys
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

    def doMonitor(self):
        pass

    def init(self):
        pass
