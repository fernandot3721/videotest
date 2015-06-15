# encoding: utf-8
from abc import abstractmethod

from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import GConf
from com.uc.utils import AndroidUtil
from com.uc.utils.BrowserUtils import setCDParams
from com.uc.monitor.LogcatHandler import LogcatHandler
from com.uc.monitor.TimingHandler import TimingHandler
from com.uc.data.DataRecord import DataRecord
import datetime

__author__ = 'Administrator'


class AbstractVideoTask(LogcatHandler, TimingHandler):

    def setDataRecord(self, dataRecord):
        self.dataRecord = dataRecord

    def setManager(self, manager):
        self.manager = manager

    def setPlayerPath(self, playPath):
        self.playPath = playPath

    def setPlayerType(self, pType):
        self.playerType = pType
        # 0 for uc
        # 1 for hardcode uc
        # 2 for use default
        # 3 for videotest

    def setActivity(self, activity):
        self.activity = activity

    def setPackage(self, package):
        self.package = package

    def getActivity(self):
        return self.activity

    def getPackage(self):
        return self.package

    def getCurrentReultList(self):
        return self.urlList

    def setTitle(self, titleStr):
        self.title = titleStr

    def __init__(self):
        self.loopCount = GConf.getCaseInt('LOOP_TIME')
        self.currentLoopIndex = 0
        self.hasComplatePlay = False
        self.hasStartPlay = False
        self.valueCount = 0
        self.caseIndex = 0
        self.title = ""
        self.keyValue = {}
        self.cdkey = {}
        self.manager = None
        self.playerVersion = ""
        self.playDetected = False
        self.playPath = ""
        self.dataRecord = None
        self.playerVersion = ""
        self.playerType = 0
        self.activity = None
        self.package = None

    def initTest(self, i):
        # 每次测试之前做一下初始化
        if self.manager is not None and self.manager.shouldTerminate():
            TaskLogger.errorLog('ERROR: manager Terminate')
            return False

        self.hasComplatePlay = False
        self.hasStartPlay = False
        self.caseIndex = i
        return True

    def dataInit(self):
        TaskLogger.infoLog("===========SWITCH PLAYER LIB===========")
        TaskLogger.normalLog("player path is: %s" % self.playPath)
        if self.playerType == 0:
            AndroidUtil.switchApollo(self.playPath)
        elif self.playerType == 1:
            AndroidUtil.switchApollo(self.playPath, 'hc')
        elif self.playerType == 2:
            # switch for video test
            AndroidUtil.switchApollo(self.playPath, 'vt')
            pass

        for key in self.urlList:
            self.keyValue[key] = []

        TaskLogger.infoLog("===========SET CD PARAM===========")
        for key in self.cdkey:
            setCDParams(key, self.cdkey[key])

    def run(self):
        self.dataInit()
        TaskLogger.infoLog("%s TEST START for %s times" % (self.title, str(self.loopCount)))
        for i in range(0, self.loopCount):
            self.currentLoopIndex = i
            TaskLogger.infoLog("----------------run %s cases" % len(self.urlList))
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
        TaskLogger.detailLog('set param %s to %s' % (key, value))
        self.setTitle('%s_%s_%s' % (self.title, key, value))

    def setPlayerVersion(self, version):
        if not self.playDetected:
            self.playerVersion = version
            self.playDetected = True
            self.dataRecord.onData(self, DataRecord.TYPE_EXTRA, 'PLAYER_VERSION', version)
            TaskLogger.detailLog('player version is: %s' % self.playerVersion)
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
