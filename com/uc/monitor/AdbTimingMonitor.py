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
            # monito privateDirty
            privateDirty = AndroidUtil.getPrivateDirty().strip()
            try:
                self.handler.onTimingKeyDetected('PrivateDirty', float(privateDirty)/1024)
            except:
                TaskLogger.errorLog('parse PrivateDirty failed [%s]' % privateDirty)
                pass

            # monitor privateClean
            privateClean = AndroidUtil.getPrivateClean().strip()
            try:
                self.handler.onTimingKeyDetected('PrivateClean', float(privateClean)/1024)
            except:
                TaskLogger.errorLog('parse PrivateClean failed [%s]' % privateClean)
                pass

            # monitor memfree
            MemFree = AndroidUtil.getMemFree().strip()
            try:
                self.handler.onTimingKeyDetected('MemFree', float(MemFree)/1024)
            except:
                TaskLogger.errorLog('parse MemFree failed [%s]' % MemFree)
                pass

            # monitor memfree
            Buffers = AndroidUtil.getBuffers().strip()
            try:
                self.handler.onTimingKeyDetected('Buffers', float(Buffers)/1024)
            except:
                TaskLogger.errorLog('parse Buffers failed [%s]' % Buffers)
                pass

            # monitor memfree
            Cached = AndroidUtil.getCached().strip()
            try:
                self.handler.onTimingKeyDetected('Cached', float(Cached)/1024)
            except:
                TaskLogger.errorLog('parse Cached failed [%s]' % Cached)
                pass

            sleep(5)
        pass

    def init(self):
        pass
    pass
