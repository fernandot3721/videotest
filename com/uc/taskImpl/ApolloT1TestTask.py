# encoding: utf-8

from time import sleep

from com.uc.conf import GConf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class ApolloT1TestTask(AbstractVideoTask):

    def __init__(self):
        super(ApolloT1TestTask, self).__init__()
        self.urlList = GConf.getUrlList()
        self.loopCount = GConf.getCaseInt('LOOP_TIME')
        self.tasktype = GConf.getCase('TASK_TYPE')
        self.setTitle(self.tasktype)
        self.keywords = {'mov_seg_dur T1 ': 'ms'}

    def doTest(self):
        print("STARTUP UC")
        self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', self.tasktype)
        BrowserUtils.launchBrowser()

        sleep(GConf.getCaseInt('WAIT_TIME'))

        print("CLEAR HISTROY")
        BrowserUtils.clearVideoCache()

        TaskLogger.normalLog("PLAY VIDEO:")
        caseUrl = GConf.getUrl(self.urlList[self.caseIndex])
        TaskLogger.detailLog(caseUrl)
        BrowserUtils.openURI(caseUrl)

        # 等待视频播起来
        myloop = 0
        while True:
            sleep(1)
            if self.hasStartPlay is True:
                TaskLogger.detailLog('play sucess')
                break
            elif myloop > 70:
                TaskLogger.errorLog('play time out')
                break
            myloop += 1

        sleep(GConf.getCaseInt('WAIT_TIME'))

        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()
        sleep(GConf.getCaseInt('WAIT_TIME'))

    def onKeywordDetected(self, key, t1):
        TaskLogger.debugLog('###########onKeywordDetected: %s %s' % (key, t1))
        if key in self.keywords:
            self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex], t1)

    def getKeywords(self):
        return self.keywords
