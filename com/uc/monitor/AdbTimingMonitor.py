from com.uc.utils.TaskLogger import TaskLogger
from com.uc.monitor.LogMonitor import LogMonitor
from time import sleep
from com.uc.utils import AndroidUtil


class AdbTimingMonitor(LogMonitor):

    def __init__(self):
        super(AdbTimingMonitor, self).__init__()
        self.keywords = []

    def doMonitor(self):
        self.setName('AdbTimingMonitor')
        TaskLogger.\
            infoLog("===========THREAD %s start===========" % self.getName())
        # open target file
        while not self.isStop:
            try:
                # monito uss
                # uss = float(AndroidUtil.getPrivateDirty())/1024  # N4
                uss = float(AndroidUtil.getPrivateClean())/1024  # SAMSUM
                # monitor memfree
                MemFree = float(AndroidUtil.getRealMemfree())/1024

                self.handler.onTimingKeyDetected('uss', uss)
                self.handler.onTimingKeyDetected('MemFree', MemFree)
            except:
                TaskLogger.debugLog('parse uss failed')
                TaskLogger.debugLog('parse MemFree failed')
                pass

            sleep(5)
        pass

    def init(self):
        pass
    pass
