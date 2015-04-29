# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class ApolloT2AndMemoryTestTask(AbstractVideoTask):
    urlList = Conf.APOLLO_T2_M_URL

    def __init__(self):
        super(ApolloT2AndMemoryTestTask, self).__init__()
        self.loopCount = Conf.LOOP_TIME_T2_M
        self.setTitle(Conf.TASK_TYPE[4])
        self.keyevents = Conf.APOLLO_T2_KEYEVENT
        self.ignore = False
        self.timeStart = None
        self.keywords = Conf.MEMORY_KEYWORD
        self.logMemory = False

    def doTest(self):
        print("STARTUP UC")
        self.dataRecord.\
            onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', Conf.TASK_TYPE[3])
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
            if myloop > 1800:
                TaskLogger.detailLog('play complete')
                break
            myloop += 1

        self.logMemory = False
        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()
        sleep(Conf.WAIT_TIME)

    def onEventDetected(self, event, time):
        TaskLogger.debugLog('###########onEventDetected: %s %s' % (event, time))

        if event == self.keyevents['t1'] or event == self.keyevents['seek']:
            self.ignore = True
        elif event == self.keyevents['t2']:
            self.timeStart = time
        elif event == self.keyevents['play']:
            if self.ignore is True or self.timeStart is None:
                # only if t2 without t1 or seek that counts
                TaskLogger.detailLog('Not a t2 play, skip')
                self.ignore = False
                self.timeStart = None
                return
            deltaTime = time - self.timeStart
            # millisecond delta
            deltaMilli = deltaTime.seconds*1000 + deltaTime.microseconds/1000
            self.ignore = False
            self.timeStart = None
            self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.currentCategory, deltaMilli, 'T2')

    def onTimingKeyDetected(self, key, value, type=None):
        if self.logMemory and self.playerVersion != "":
            # TaskLogger.debugLog('onTimingKeyDetected %s %s' % (key, value))
            # if key in self.keywords:
            self.dataRecord.onData(self, DataRecord.TYPE_TIMING, self.currentCategory+key, value, 'MEMORY')
        pass

    def getKeyevents(self):
        return self.keyevents.values()

    def getKeywords(self):
        return self.keywords
