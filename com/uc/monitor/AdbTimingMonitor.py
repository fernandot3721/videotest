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
                uss = float(AndroidUtil.getUss(self.package))/1024  # N4
                #uss = float(AndroidUtil.getPrivateDirty(self.package))/1024  # N4
                # uss = float(AndroidUtil.getPrivateClean(self.package))/1024  # SAMSUM
                # monitor memfree
                MemFree = float(AndroidUtil.getRealMemfree())/1024

                self.handler.onTimingKeyDetected('uss', uss, 'MEMORY')
                self.handler.onTimingKeyDetected('MemFree', MemFree, 'MEMORY')
            except:
                # TaskLogger.debugLog('parse memory failed')
                pass

            try:
                # monitor cpu
                cpu = AndroidUtil.getCpu(self.package)
                self.handler.onTimingKeyDetected('Cpu', cpu, 'CPU')
            except:
                # TaskLogger.debugLog('parse cpu failed')
                pass

            sleep(5)
        pass

    def init(self):
        pass
    pass
