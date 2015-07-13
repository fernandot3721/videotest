# encoding: utf-8

from time import sleep

from com.uc.conf import GConf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.utils import AndroidUtil
from com.uc.data.DataRecord import DataRecord


class MemoryTestTask(AbstractVideoTask):

    def __init__(self):
        super(MemoryTestTask, self).__init__()
        self.urlList = GConf.getUrlList()
        self.tasktype = GConf.getCase('TASK_TYPE')
        self.setTitle(self.tasktype)
        self.logMemory = False

    def doTest(self):
        print("STARTUP UC")
        self.dataRecord.\
            onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', tasktype)
        if not AndroidUtil.testMemfree():
            return
        self.logMemory = True
        BrowserUtils.launchBrowser()

        sleep(GConf.getCaseInt('WAIT_TIME'))

        print("CLEAR HISTROY")
        BrowserUtils.clearVideoCache()
        sleep(GConf.getCaseInt('WAIT_TIME'))

        TaskLogger.normalLog("PLAY VIDEO:")
        caseUrl = GConf.getUrl(self.urlList[self.caseIndex])
        TaskLogger.detailLog(caseUrl)
        BrowserUtils.openURI(caseUrl)

        myloop = 0
        while True:
            sleep(1)
            if self.hasStartPlay is True:
                break
            elif myloop == 20 or myloop == 40 or myloop == 60:
                BrowserUtils.fresh()
                TaskLogger.detailLog('refresh')
            elif myloop > 100:
                self.logMemory = False
                raise Exception('Can not play video')
            myloop += 1

        # 等待视频播起来
        myloop = 0
        TaskLogger.detailLog('play sucess')
        while True:
            sleep(1)
            if myloop > 2700:
                TaskLogger.detailLog('play complete')
                break
            myloop += 1

        self.logMemory = False
        # sleep(GConf.getCaseInt('WAIT_TIME'))

        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()
        sleep(GConf.getCaseInt('WAIT_TIME'))

    def onTimingKeyDetected(self, key, value, type=None):
        if self.logMemory and self.playerVersion != "":
            # TaskLogger.debugLog('onTimingKeyDetected %s %s' % (key, value))
            # if key in self.keywords:
            self.dataRecord.onData(self, DataRecord.TYPE_TIMING, self.urlList[self.caseIndex]+key, value)
        pass
