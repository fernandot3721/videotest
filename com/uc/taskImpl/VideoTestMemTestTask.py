# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import VideoTestUtil
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.DataRecord import DataRecord


class VideoTestMemTestTask(AbstractVideoTask):
    urlList = Conf.VT_MEMORY_URL

    def __init__(self):
        super(VideoTestMemTestTask, self).__init__()
        self.loopCount = Conf.LOOP_TIME_VT_M
        self.setTitle(Conf.TASK_TYPE[6])
        self.ignore = False
        self.logMemory = False
        self.keyevents = Conf.APOLLO_T1_KEYWORD

    def doTest(self):
        print("STARTUP MXPLAYER")
        self.dataRecord.\
            onData(self, DataRecord.TYPE_EXTRA, 'TASK_TYPE', Conf.TASK_TYPE[6])
        self.logMemory = True
        # MXPlayerUtil.launchBrowser()

        # sleep(Conf.WAIT_TIME)

        TaskLogger.normalLog("PLAY VIDEO:")
        TaskLogger.detailLog(self.urlList[self.currentCategory])
        VideoTestUtil.openURI(self.urlList[self.currentCategory])

        myloop = 0
        while True:
            sleep(1)
            if self.hasStartPlay is True:
                break
            elif myloop > 50:
                self.logMemory = False
                raise Exception('Can not play video')
            myloop += 1

        # 等待视频播起来
        myloop = 0
        TaskLogger.detailLog('play sucess')
        self.logMemory = True
        while True:
            sleep(1)
            if myloop > 180:
                TaskLogger.detailLog('play complete')
                break
            myloop += 1

        self.logMemory = False
        print("SHUTDOWN MXPLAYER")
        VideoTestUtil.closeBrowser()
        sleep(Conf.WAIT_TIME)

    def onTimingKeyDetected(self, key, value, type=None):
        if self.logMemory:
            self.dataRecord.onData(self, DataRecord.TYPE_TIMING, self.currentCategory+key, value, type)
        pass

    def onEventDetected(self, event, time):
        if self.hasStartPlay:
            return
        TaskLogger.debugLog('###########onEventDetected: %s %s' % (event, time))
        if 'mov_seg_dur' in event:
            self.hasStartPlay = True

    def getKeyevents(self):
        return self.keyevents.values()