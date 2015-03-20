from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import Conf
from com.uc.utils import ChartUtils
import time
import os


class MultiChartViewer(ResultViewer):

    def __init__(self):
        self.dataCount = 0
        self.data = {}
        self.reportPath = '{}report-{}'\
            .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])
            # .format(Conf.REPORT_DIR, 'test')

    def addData(self, data):
        self.dataCount = 0
        for case in data.getCase():
            i = 0
            if 'uss' in case:
                i = case.find('uss')
                name = case[0:i-1] + '#'+ str(data)
                if not name in self.data:
                    self.data[name] = []
                self.data[name].append(data.getData(case))
                TaskLogger.debugLog('add uss %s-%s' % (name, len(self.data[name][0])))
            elif 'MemFree' in case:
                i = case.find('MemFree')
                name = case[0:i-1] + '#' + str(data)
                if not name in self.data:
                    self.data[name] = []
                self.data[name].append(data.getData(case))
                TaskLogger.debugLog('add MemFree %s-%s' % (name, len(self.data[name][0])))
        pass

    def showResult(self):
        if not os.path.exists(self.reportPath):
            os.mkdir(self.reportPath)
        i = 1
        for taskInfo in self.data:
            # path
            saveFile = '%s/%s.png' % (self.reportPath, i)
            i = i + 1
            TaskLogger.detailLog('file://%s' % saveFile)
            TaskLogger.debugLog(len(self.data[taskInfo]))
            ChartUtils.createstripeschart(saveFile, taskInfo, None, self.data[taskInfo])
