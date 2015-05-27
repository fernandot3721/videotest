from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.TaskData import TaskData
from com.uc.conf import GConf
from com.uc.utils import MatplotUtil
import time
import os


class VsChartViewer(ResultViewer):

    def __init__(self):
        self.data = {}
        self.caseSeq = []
        self.reportPath = '{}report-{}'\
            .format(GConf.getGlobal('REPORT_DIR'), 'chart')
        self.saveFile = time.strftime('%Y%m%d%H%M')[2:]
        # self.saveFile = 'test'

    def addData(self, data):
        self.parseDataType(data, TaskData.DATA_TYPE_TIMING)
        self.parseDataType(data, TaskData.DATA_TYPE_NORMAL)
        pass

    def parseDataType(self, data, dataType):
        for key in data.getKeysByType(dataType):
            caseData = data.getDataByTypeAndKey(dataType, key)

            if not key in self.data:
                self.data[key] = []
                self.caseSeq.append(key)
            self.data[key].append((data.getTitle(), caseData.data))

    def showResult(self):
        if not os.path.exists(self.reportPath):
            os.mkdir(self.reportPath)
        # path
        saveFile = '%s/%s.svg' % (self.reportPath, self.saveFile)
        # saveFile = '%s/%s.png' % (self.reportPath, taskInfo)
        MatplotUtil.createChrat(saveFile, self.data, self.caseSeq, 3, 2)
        TaskLogger.detailLog('view Report: file://%s ' % saveFile)
        # TaskLogger.detailLog('view Report: http://100.84.44.238/videotest/report-test/test1.svg')
        return saveFile
