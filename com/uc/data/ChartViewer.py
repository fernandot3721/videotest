from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import Conf
from com.uc.utils import ChartUtils
import time
import os


class ChartViewer(ResultViewer):

    def __init__(self):
        self.dataCount = 0
        self.data = {}
        self.reportPath = '{}report-{}'\
            .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])
            # .format(Conf.REPORT_DIR, 'test')

    def addData(self, data):
        taskInfo = {}
        self.data[str(data)] = taskInfo

        #  case data & head
        self.dataCount = 0
        taskInfo['case'] = []
        for case in data.getCase():
            lineContent = data.getData(case)
            count = len(lineContent)
            if count > self.dataCount:
                self.dataCount = count
            taskInfo['case'].append(lineContent)
        pass

    def showResult(self):
        if not os.path.exists(self.reportPath):
            os.mkdir(self.reportPath)
        countLine = [n for n in range(1, self.dataCount+1)]
        i = 1
        for taskInfo in self.data:
            # path
            saveFile = '%s/%s.png' % (self.reportPath, i)
            i = i + 1
            TaskLogger.detailLog('file://%s' % saveFile)
            ChartUtils.createstripeschart(saveFile, taskInfo, countLine, self.data[taskInfo]['case'])
