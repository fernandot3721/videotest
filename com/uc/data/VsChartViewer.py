from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import Conf
from com.uc.utils import MatplotUtil
import time
import os


class VsChartViewer(ResultViewer):

    def __init__(self):
        self.dataCount = 0
        self.data = {}
        self.caseSeq = []
        self.reportPath = '{}report-{}'\
            .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])
            # .format(Conf.REPORT_DIR, 'test')

    def addData(self, data):
        self.dataCount = 0
        for case in data.getCase():
            if not case in self.data:
                self.data[case] = []
                self.caseSeq.append(case)
            self.data[case].append((data, data.getData(case)))
        pass

    def showResult(self):
        if not os.path.exists(self.reportPath):
            os.mkdir(self.reportPath)
        # path
        # saveFile = '%s/%s.png' % (self.reportPath, taskInfo)
        MatplotUtil.createChrat(None, self.data, self.caseSeq, 3, 2)
