# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord
from com.uc.utils import AndroidUtil


class ApolloSeekTestTask(AbstractVideoTask):
    urlList = Conf.APOLLO_SEEK_URL

    def __init__(self):
        super(ApolloSeekTestTask, self).__init__()
        self.setTitle(Conf.TASK_TYPE[7])
        self.loopCount = Conf.LOOP_TIME_SEEK
        self.keyevents = Conf.APOLLO_SEEK_KEYEVENT
        self.timeStart = None

    def doTest(self):
        print("STARTUP UC")
        self.dataRecord.\
            onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', Conf.TASK_TYPE[3])
        BrowserUtils.launchBrowser()

        sleep(Conf.WAIT_TIME)

        print("CLEAR HISTROY")
        BrowserUtils.clearVideoCache()
        sleep(Conf.WAIT_TIME)

        TaskLogger.normalLog("PLAY VIDEO:")
        TaskLogger.detailLog(self.urlList[self.currentCategory])
        BrowserUtils.openURI(self.urlList[self.currentCategory])

        sleep(10)
        AndroidUtil.pressplaybutton()
        myloop = 0
        while True:
            sleep(1)
            if self.hasStartPlay is True:
                break
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

        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()
        sleep(Conf.WAIT_TIME)

    def onEventDetected(self, event, time):
        TaskLogger.debugLog('###########onEventDetected: %s %s' % (event, time))

        if event == self.keyevents['seek']:
            self.timeStart = time
        elif event == self.keyevents['play']:
            if self.timeStart is None:
                TaskLogger.detailLog('log time failed, skip')
                self.timeStart = None
                return
            deltaTime = time - self.timeStart
            # millisecond delta
            deltaMilli = deltaTime.seconds*1000 + deltaTime.microseconds/1000
            self.timeStart = None
            self.dataRecord.onData(self, DataRecord.TYPE_NORMAL, self.currentCategory, deltaMilli, 'SEEK')

    def getKeyevents(self):
        return self.keyevents.values()
