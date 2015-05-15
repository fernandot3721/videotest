# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import MXPlayerUtil
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class MXPlayerMemTestTask(AbstractVideoTask):
    urlList = Conf.MX_MEMORY_URL

    def __init__(self):
        super(MXPlayerMemTestTask, self).__init__()
        self.loopCount = Conf.LOOP_TIME_MX_M
        self.setTitle(Conf.TASK_TYPE[5])
        self.keyevents = Conf.MX_MEMORY_KEYEVENT
        self.ignore = False
        self.logMemory = False
        self.testTime = 600

    def doTest(self):
        MXPlayerUtil.closeBrowser()
        print("STARTUP MXPLAYER")
        self.dataRecord.\
            onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', Conf.TASK_TYPE[5])
        self.logMemory = True
        MXPlayerUtil.launchBrowser()

        sleep(Conf.WAIT_TIME)

        TaskLogger.normalLog("PLAY VIDEO:")
        TaskLogger.detailLog(self.urlList[self.currentCategory])
        MXPlayerUtil.openURI(self.urlList[self.currentCategory])

        myloop = 0
        while True:
            sleep(1)
            if self.hasStartPlay is True:
                break
            elif myloop > 50:
                self.logMemory = False
                raise Exception('Can not play video')
            myloop += 1

        # 等待视频播起来
        myloop = 0
        TaskLogger.detailLog('play sucess')
        # self.logMemory = True
        TaskLogger.detailLog('test run for %s seconds' % self.testTime)
        while True:
            sleep(1)
            if myloop > self.testTime:
                TaskLogger.detailLog('play complete')
                break
            myloop += 1

        self.logMemory = False
        print("SHUTDOWN MXPLAYER")
        MXPlayerUtil.closeBrowser()
        sleep(Conf.WAIT_TIME)

    def onTimingKeyDetected(self, key, value, type=None):
        if self.logMemory:
            self.dataRecord.onData(self, DataRecord.TYPE_TIMING, self.currentCategory+key, value, type)
        pass

    def onEventDetected(self, event, time):
        if self.hasStartPlay:
            return
        TaskLogger.debugLog('###########onEventDetected: %s %s' % (event, time))
        if 'start' in event:
            self.hasStartPlay = True

    def getKeyevents(self):
        return self.keyevents.values()