# encoding: utf-8

from time import sleep

from com.uc.conf import GConf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class CoreT1TestTask(AbstractVideoTask):

    def __init__(self):
        super(CoreT1TestTask, self).__init__()
        self.urlList = GConf.getUrlList()
        self.tasktype = GConf.getCase('TASK_TYPE')
        self.setTitle(self.tasktype)
        self.keywords = {'`tl=': 'ms'}

    def doTest(self):
        print("STARTUP UC")
        self.dataRecord.\
            onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', self.tasktype)
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
            elif myloop > 7:
                TaskLogger.errorLog('play time out')
                break
            myloop += 1

        BrowserUtils.openURIInCurrentWindow("http://www.baidu.com")

        sleep(GConf.getCaseInt('WAIT_TIME'))

        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()

    def onKeywordDetected(self, key, t1):
        if key in self.__keywords:
            self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex], t1)

    def getKeywords(self):
        return self.keywords
