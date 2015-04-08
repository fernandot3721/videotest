# encoding: utf-8
from abc import abstractmethod

from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import Conf
from com.uc.utils import AndroidUtil
from com.uc.utils.BrowserUtils import setCDParams
from com.uc.monitor.LogcatHandler import LogcatHandler
from com.uc.monitor.TimingHandler import TimingHandler
from com.uc.data.DataRecord import DataRecord
import re
import datetime

__author__ = 'Administrator'


class AbstractVideoTask(LogcatHandler, TimingHandler):

    def setDataRecord(self, dataRecord):
        self.dataRecord = dataRecord

    def setManager(self, manager):
        self.manager = manager

    def setPlayerPath(self, playPath):
        self.playPath = playPath

    def getCurrentReultList(self):
        return self.keyValue.get(self.currentCategory)

    def setTitle(self, titleStr):
        self.title = titleStr

    def __init__(self):
        self.loopCount = Conf.LOOP_TIME
        self.currentLoopIndex = 0
        self.hasComplatePlay = False
        self.hasStartPlay = False
        self.valueCount = 0
        self.currentCategory = ""
        self.currentCategoryIndex = 0
        self.title = ""
        self.keyValue = {}
        self.cdkey = {}
        self.manager = None
        self.playerVersion = ""
        self.playDetected = False
        self.playPath = ""
        self.dataRecord = None
        self.playerVersion = ""

    def initTest(self, i):
        # 每次测试之前做一下初始化
        if self.manager is not None and self.manager.shouldTerminate():
            TaskLogger.errorLog('ERROR: manager Terminate')
            return False

        self.hasComplatePlay = False
        self.hasStartPlay = False
        self.currentCategoryIndex = i
        self.currentCategory = self.urlList.keys()[i]
        return True

    def dataInit(self):
        TaskLogger.infoLog("===========SWITCH PLAYER LIB===========")
        TaskLogger.normalLog("player path is: %s" % self.playPath)
        if Conf.HARDCODE_APOLLO:
            AndroidUtil.switchHardCodeApollo(self.playPath)
        else:
            AndroidUtil.switchApollo(self.playPath)
        match = re.search(r'\d\.\d+', self.playPath)
        libName = match.group(0)
        TaskLogger.errorLog('&&&&&&&&&&&&&&&&&libName: {}'.format(libName))
        # self.setTitle('{}-{}'.format(libName, self.title))
        for key in self.urlList.keys():
            self.keyValue[key] = []

        TaskLogger.infoLog("===========SET CD PARAM===========")
        for key in self.cdkey:
            setCDParams(key, self.cdkey[key])

    def run(self):
        self.dataInit()
        TaskLogger.infoLog("%s TEST START for %s times" % (self.title, str(self.loopCount)))
        for i in range(0, self.loopCount):
            self.currentLoopIndex = i
            for j in range(0, len(self.urlList)):
                TaskLogger.infoLog("----------------Loop %s Case %s is running" % (i, j))
                if self.initTest(j):
                    starttime = datetime.datetime.now()
                    self.doTest()
                    endtime = datetime.datetime.now()
                    TaskLogger.infoLog("----------------Loop %s Case %s run for %s and ends" % (i, j, str(endtime-starttime)))

    @abstractmethod
    def doTest(self):
        pass

    def onVideoEndPlay(self):
        self.hasComplatePlay = True

    def setCD(self, key, value):
        self.cdkey[key] = value
        TaskLogger.errorLog('set param %s to %s' % (key, value))
        self.setTitle('%s_%s_%s' % (self.title, key, value))

    def setPlayerVersion(self, version):
        if not self.playDetected:
            self.playerVersion = version
            self.playDetected = True
            self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, 'PLAYER_VERSION', version)
            TaskLogger.errorLog('player version is: %s' % self.playerVersion)
            self.setTitle('{}_{}'.format(self.title, self.playerVersion))

    def onVideoStartPlay(self):
        self.hasStartPlay = True

    def onPlayerVersion(self, version):
        self.setPlayerVersion(version)

    def getKeywords(self):
        return []

    def getKeyevents(self):
        return []

    def onKeywordDetected(self, key, value):
        pass

    def onEventDetected(self, event, value):
        pass
