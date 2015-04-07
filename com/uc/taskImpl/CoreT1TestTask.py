# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class CoreT1TestTask(AbstractVideoTask):
    urlList = Conf.CORE_T1_URL

    def __init__(self):
        self.setTitle(Conf.TASK_TYPE[0])
        self.__keywords = Conf.CORE_T1_KEYWORD

    def doTest(self):
        print("STARTUP UC")
        self.dataRecord.\
            onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', Conf.TASK_TYPE[0])
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
            elif myloop > 7:
                TaskLogger.errorLog('play time out')
                break
            myloop += 1

        BrowserUtils.openURIInCurrentWindow("http://www.baidu.com")

        sleep(Conf.WAIT_TIME)

        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()

    def onKeywordDetected(self, key, t1):
        if key in self.__keywords:
            self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.currentCategory, t1)

    def getKeywords(self):
        return self.__keywords
