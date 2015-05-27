# encoding: utf-8

from time import sleep

from com.uc.conf import GConf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class ApolloT2AndMemoryTestTask(AbstractVideoTask):

    def __init__(self):
        super(ApolloT2AndMemoryTestTask, self).__init__()
        self.urlList = GConf.getUrlList()
        self.loopCount = GConf.getCaseInt('LOOP_TIME')
        self.tasktype = GConf.getCase('TASK_TYPE')
        self.setTitle(self.tasktype)
        self.keyevents = {
            't1': '>>> nativeCreateInstance',
            'seek': 'jni nativeSeekTo',
            't2': 'MediaPlayerInstance::onBufferingStateUpdate() 1',
            'play': 'play(). isPlaying = 0',
        }
        self.ignore = False
        self.timeStart = None
        self.logMemory = False

    def doTest(self):
        print("STARTUP UC")
        self.dataRecord.\
            onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', self.tasktype)
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
            elif myloop == 60:
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
            if myloop > 100:
                TaskLogger.detailLog('play complete')
                break
            myloop += 1

        self.logMemory = False
        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()
        sleep(GConf.getCaseInt('WAIT_TIME'))

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
            self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex], deltaMilli, 'T2')

    def onTimingKeyDetected(self, key, value, type=None):
        if self.logMemory and self.playerVersion != "":
            # TaskLogger.debugLog('onTimingKeyDetected %s %s' % (key, value))
            # if key in self.keywords:
            self.dataRecord.onData(self, DataRecord.TYPE_TIMING, self.urlList[self.caseIndex]+key, value, 'MEMORY')
        pass

    def getKeyevents(self):
        return self.keyevents.values()

