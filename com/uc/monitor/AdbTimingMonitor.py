from com.uc.utils.TaskLogger import TaskLogger
from com.uc.monitor.LogMonitor import LogMonitor
from time import sleep
from com.uc.utils import AndroidUtil


class AdbTimingMonitor(LogMonitor):

    def __init__(self):
        super(AdbTimingMonitor, self).__init__()
        self.keywords = []

    def doMonitor(self):
        self.setName('FileContentMonitor')
        TaskLogger.\
            infoLog("===========THREAD %s start===========" % self.getName())
        # open target file
        while not self.isStop:
            try:
                # monito privateDirty
                privateDirty = float(AndroidUtil.getPrivateDirty().strip())/1024

                # monitor privateClean
                privateClean = float(AndroidUtil.getPrivateClean().strip())/1024

                # monitor memfree
                memFree = float(AndroidUtil.getMemFree().strip())/1024

                # monitor memfree
                buffers = float(AndroidUtil.getBuffers().strip())/1024

                # monitor memfree
                cached = float(AndroidUtil.getCached().strip())/1024

                self.handler.onTimingKeyDetected('PrivateDirty', privateDirty)
                self.handler.onTimingKeyDetected('PrivateClean', privateClean)
                self.handler.onTimingKeyDetected('MemFree', memFree)
                self.handler.onTimingKeyDetected('Buffers', buffers)
                self.handler.onTimingKeyDetected('Cached', cached)
            except:
                TaskLogger.debugLog('parse meminfo failed')
                pass

            sleep(5)
        pass

    def init(self):
        pass
    pass
