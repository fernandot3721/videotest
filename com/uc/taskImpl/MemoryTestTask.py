# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.utils import AndroidUtil


class MemoryTestTask(AbstractVideoTask):
    urlList = Conf.MEMEROY_URL

    def __init__(self):
        super(MemoryTestTask, self).__init__()
        self.setTitle(Conf.TASK_TYPE[2])
        self.keywords = Conf.MEMORY_KEYWORD
        self.logMemory = False

    def doTest(self):
        print("STARTUP UC")
        if not AndroidUtil.testMemfree():
            return
        self.logMemory = True
        BrowserUtils.launchBrowser()

        sleep(Conf.WAIT_TIME)

        print("CLEAR HISTROY")
        BrowserUtils.clearVideoCache()
        sleep(Conf.WAIT_TIME)

        TaskLogger.normalLog("PLAY VIDEO:")
        TaskLogger.detailLog(self.urlList[self.currentCategory])
        BrowserUtils.openURI(self.urlList[self.currentCategory])

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
        # sleep(Conf.WAIT_TIME)

        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()
        sleep(Conf.WAIT_TIME)

    def getKeywords(self):
        return self.keywords

    def onTimingKeyDetected(self, key, value):
        if self.logMemory and self.playerVersion != "":
            # TaskLogger.debugLog('onTimingKeyDetected %s %s' % (key, value))
            # if key in self.keywords:
            self.dataRecord.onData(self.title, self.currentCategory+key, value)
        pass
