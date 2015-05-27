# encoding: utf-8

from time import sleep

from com.uc.conf import GConf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import MXPlayerUtil
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class MXPlayerMemTestTask(AbstractVideoTask):

    def __init__(self):
        super(MXPlayerMemTestTask, self).__init__()
        self.urlList = GConf.getUrlList()
        self.loopCount = GConf.getCaseInt('LOOP_TIME')
        self.tasktype = GConf.getCase('TASK_TYPE')
        self.setTitle(self.tasktype)
        self.keyevents = {'start_time': 'start_time'}
        self.ignore = False
        self.logMemory = False
        self.testTime = 600

    def doTest(self):
        MXPlayerUtil.closeBrowser()
        print("STARTUP MXPLAYER")
        self.dataRecord.\
            onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', self.tasktype)
        self.logMemory = True
        MXPlayerUtil.launchBrowser()

        sleep(GConf.getCaseInt('WAIT_TIME'))

        TaskLogger.normalLog("PLAY VIDEO:")
        caseUrl = GConf.getUrl(self.urlList[self.caseIndex])
        TaskLogger.detailLog(caseUrl)
        MXPlayerUtil.openURI(caseUrl)

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
        sleep(GConf.getCaseInt('WAIT_TIME'))

    def onTimingKeyDetected(self, key, value, type=None):
        if self.logMemory:
            self.dataRecord.onData(self, DataRecord.TYPE_TIMING, self.urlList[self.caseIndex]+key, value, type)
        pass

    def onEventDetected(self, event, time):
        if self.hasStartPlay:
            return
        TaskLogger.debugLog('###########onEventDetected: %s %s' % (event, time))
        if 'start' in event:
            self.hasStartPlay = True

    def getKeyevents(self):
        return self.keyevents.values()