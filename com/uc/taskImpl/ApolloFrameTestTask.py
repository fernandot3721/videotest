# encoding: utf-8

from time import sleep

from com.uc.conf import GConf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class ApolloFrameTestTask(AbstractVideoTask):

    def __init__(self):
        super(ApolloFrameTestTask, self).__init__()
        self.urlList = GConf.getUrlList()
        self.loopCount = GConf.getCaseInt('LOOP_TIME')
        self.tasktype = GConf.getCase('TASK_TYPE')
        self.setTitle(self.tasktype)
        self.keywords = {
            'rendertime=': ',',
            'frameTime=': '',
            }
        self.keyevents = {'logstart': 'start dump time info',
            'logend': 'end dump time info',
            'play': 'XOXO'}
        self.loging = 0

    def doTest(self):
        print("SHUTDOWN")
        BrowserUtils.closeBrowser()
        sleep(GConf.getCaseInt('WAIT_TIME'))
        
        print("STARTUP")
        self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', self.tasktype)
        # BrowserUtils.launchBrowser()

        sleep(GConf.getCaseInt('WAIT_TIME'))

        print("CLEAR HISTROY")
        BrowserUtils.clearVideoCache()

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
            if myloop > 30:
                TaskLogger.detailLog('play complete')
                break
            myloop += 1
        sleep(GConf.getCaseInt('WAIT_TIME'))
        print("go back")
        BrowserUtils.goback()

        myloop = 0
        while True:
            sleep(1)
            if self.loging == 2 or myloop > 60:
                TaskLogger.debugLog('exit task %s' % self.loging)
                break
            myloop += 1
            # TaskLogger.infoLog(myloop)

        print("SHUTDOWN")
        BrowserUtils.closeBrowser()
        sleep(GConf.getCaseInt('WAIT_TIME'))

    def onKeywordDetected(self, key, time):
        # TaskLogger.debugLog('###########onKeywordDetected: %s %s' % (key, time))
        if self.loging != 1:
            return

        if key in self.keywords:
            self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex] + key, time)

    def onEventDetected(self, event, time):
        # TaskLogger.debugLog('###########onEventDetected: %s %s' % (event, time))
        if event == self.keyevents['logstart']:
            TaskLogger.debugLog('log start')
            self.loging = 1
        elif event == self.keyevents['logend']:
            TaskLogger.debugLog('log end')
            self.loging = 2
        elif event == self.keyevents['play']:
            TaskLogger.debugLog('play')
            self.hasStartPlay = True

    def getKeywords(self):
        return self.keywords

    def getKeyevents(self):
        return self.keyevents.values()