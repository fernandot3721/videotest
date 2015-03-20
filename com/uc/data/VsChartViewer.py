from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import Conf
from com.uc.utils import ChartUtils
import time
import os


class VsChartViewer(ResultViewer):

    def __init__(self):
        self.dataCount = 0
        self.data = {}
        self.reportPath = '{}report-{}'\
            .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])
            # .format(Conf.REPORT_DIR, 'test')

    def addData(self, data):
        self.dataCount = 0
        for case in data.getCase():
            TaskLogger.infoLog(case)
            if not case in self.data:
                self.data[case] = []
            self.data[case].append(data.getData(case))
        pass

    def showResult(self):
        if not os.path.exists(self.reportPath):
            os.mkdir(self.reportPath)
        for taskInfo in self.data:
            # path
            saveFile = '%s/%s.png' % (self.reportPath, taskInfo)
            TaskLogger.detailLog('file://%s' % saveFile)
            ChartUtils.createstripeschart(saveFile, taskInfo, None, self.data[taskInfo])
