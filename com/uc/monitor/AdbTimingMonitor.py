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
            if privateDirty != '':
                self.handler.onTimingKeyDetected('PrivateDirty', float(privateDirty)/1024)

            # monitor memfree
            MemFree = AndroidUtil.getMemFree().strip()
            if MemFree != '':
                self.handler.onTimingKeyDetected('MemFree', float(MemFree)/1024)

            sleep(5)
        pass

    def init(self):
        pass
    pass
