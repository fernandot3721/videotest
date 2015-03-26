# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class MemoryTestTask(AbstractVideoTask):
    urlList = Conf.MEMEROY_URL

    def __init__(self):
        super(MemoryTestTask, self).__init__()
        self.setTitle(Conf.TASK_TYPE[2])
        self.keywords = Conf.MEMORY_KEYWORD
        self.logMemory = False

    def doTest(self):
        print("STARTUP UC")
        self.dataRecord.\
            onData(self, DataRecord.TAG_EXTRA, 'TASK_TYPE', Conf.TASK_TYPE[2])
        BrowserUtils.launchBrowser()

        sleep(Conf.WAIT_TIME)
        self.logMemory = True

        print("CLEAR HISTROY")
        BrowserUtils.clearVideoCache()

        TaskLogger.normalLog("PLAY VIDEO:")
        TaskLogger.detailLog(self.urlList[self.currentCategory])
        BrowserUtils.openURI(self.urlList[self.currentCategory])

        myloop = 0
        refresh = False
        while True:
            sleep(1)
            if self.hasStartPlay is True:
                TaskLogger.detailLog('play sucess')
                break
            elif not refresh and myloop > 20:
                BrowserUtils.fresh()
                TaskLogger.detailLog('refresh')
                refresh = True
            elif myloop > 60:
                raise Exception('Can not play video')
            myloop += 1

        # 等待视频播起来
        myloop = 0
        while True:
            sleep(1)
            if myloop > 60:
                TaskLogger.detailLog('play complete')
                break
            myloop += 1

        sleep(Conf.WAIT_TIME)
        self.logMemory = False

        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()
        sleep(Conf.WAIT_TIME)

    def getKeywords(self):
        return self.keywords

    def onTimingKeyDetected(self, key, value):
        if self.logMemory and self.playerVersion != "":
            # TaskLogger.debugLog('onTimingKeyDetected %s %s' % (key, value))
            # if key in self.keywords:
            self.dataRecord.onData(self.title, key, value)
        pass
