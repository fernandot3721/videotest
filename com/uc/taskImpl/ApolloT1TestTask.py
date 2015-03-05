# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger


class ApolloT1TestTask(AbstractVideoTask):
    urlList = Conf.APOLLO_T1_URL

    def __init__(self):
        super(ApolloT1TestTask, self).__init__()
        self.setTitle(Conf.TASK_TYPE[0])
        self.keywords = Conf.APOLLO_T1_KEYWORD

    def doTest(self):
        print("STARTUP UC")
        BrowserUtils.launchBrowser()

        sleep(Conf.WAIT_TIME)

        print("CLEAR HISTROY")
        BrowserUtils.clearVideoCache()

        TaskLogger.normalLog("PLAY VIDEO:")
        TaskLogger.detailLog(self.urlList[self.currentCategory])
        BrowserUtils.openURI(self.urlList[self.currentCategory])

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

        sleep(Conf.WAIT_TIME)

        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()
        sleep(Conf.WAIT_TIME)

    def onKeywordDetected(self, key, t1):
        TaskLogger.debugLog('###########onKeywordDetected: %s %s' % (key, t1))
        if key in self.keywords:
            self.dataRecord.onData(self.title, self.currentCategory, t1)

    def getKeywords(self):
        return self.keywords
