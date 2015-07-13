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
            'play': 'XOXO'
            }
        self.loging = 0

        # caculate frame info
        self.r2 = 0
        self.f2 = 0
        self.total = 0
        self.dropframe = 0
        self.FPS = 15
        self.FRAMEDUR = 1000000/self.FPS
        self.renderlist = []
        self.standardlist = []
        self.match = False

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

        if key == 'rendertime=':
            self.match = True
            self.rendertime = time
            return

        if key == 'frameTime=' and self.match is True:
            self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex] + '| rendertime', self.rendertime)
            self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex] + '| frameTime', time)
            self.match = False
            self.frametime = time

            if self.r2 != 0 and self.f2 != 0:
                realrenderdur = self.rendertime - self.r2
                baseframedur = self.frametime - self.f2

                self.total += 1
                if baseframedur/self.FRAMEDUR > 1000:
                    # it is impossible in normal situation, so drop all the data before
                    self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex] + '| clear by', self.frametime)
                    self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex] + '| drop count', self.total)
                    self.renderlist = []
                    self.standardlist = []
                    self.total = 0
                else:
                    self.renderlist.append(realrenderdur)
                    self.standardlist.append(baseframedur)
                    self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex] + '| render interval', realrenderdur)
                    # self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex] + '| standard interval', baseframedur)


                    framedelta = int(realrenderdur/self.FRAMEDUR - 1)
                    if framedelta >= 1:
                        self.dropframe += framedelta
                        self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex] + '| dropframe by', realrenderdur)
                        self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.urlList[self.caseIndex] + '| dropframe count', framedelta)

            self.r2 = self.rendertime
            self.f2 = self.frametime

    def onEventDetected(self, event, time):
        # TaskLogger.debugLog('###########onEventDetected: %s %s' % (event, time))
        if event == self.keyevents['logstart']:
            TaskLogger.debugLog('log start')
            self.loging = 1
        elif event == self.keyevents['logend']:
            TaskLogger.debugLog('log end')
            self.loging = 2
            self.calculateFrame()
        elif event == self.keyevents['play']:
            TaskLogger.debugLog('play')
            self.hasStartPlay = True

    def getKeywords(self):
        return self.keywords

    def getKeyevents(self):
        return self.keyevents.values()

    def calculateFrame(self):
        TaskLogger.debugLog('========================calculateFrame=======================')
        # TaskLogger.debugLog('total: %s' % self.total)
        TaskLogger.debugLog('dropframe: %s' % self.dropframe)
        self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, self.urlList[self.caseIndex] + '| total frames', self.total)
        self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, self.urlList[self.caseIndex] + '| dropframe', self.dropframe)
        total = 0
        base = 0
        num = 0
        for base, num in zip(self.standardlist, self.renderlist):
            total += (num - base)**2

        # TaskLogger.debugLog('base %s' % type(base))
        # TaskLogger.debugLog('num %s' % type(num))
        # TaskLogger.debugLog('total %s' % type(total))

        # TaskLogger.debugLog('frame duration: %s' % (base/1000))
        # TaskLogger.debugLog('std duration: %s' % round((total/len(self.renderlist))**(1.0/2)/1000,2))
        # TaskLogger.debugLog('fps: %s' % round(1.0/base*10**6))
        # TaskLogger.debugLog('total: %s' % total)

        self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, self.urlList[self.caseIndex] + '-std duration', round((total/len(self.renderlist))**(1.0/2)/1000,2))
        self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, self.urlList[self.caseIndex] + '-last frame fps', round(1.0/base*10**6))
        self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, self.urlList[self.caseIndex] + '-last frame duration', base/1000)
        self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, self.urlList[self.caseIndex] + '=========STANDAR FPS', self.FPS)
        self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, self.urlList[self.caseIndex] + '=========STANDAR FRAMEDUR', self.FRAMEDUR)