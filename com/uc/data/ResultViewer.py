from abc import abstractmethod
from com.uc.utils.ColorUtil import *
import time


class ResultViewer():

    def __init__(self):
        self.lineInfo = {}
        self.reportPath = '{}report-{}'\
            .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])
        pass

    def addData(self, data):
        taskInfo = []
        self.lineInfo[str(data)] = taskInfo
        #  extra info
        taskInfo.append(['Task Info:'])
        extras = data.getAllExtra()
        for extra in extras:
            taskInfo.append([extra, extras[extra]])

        #  case data & head
        lineHead = []
        lineHeadPos = len(taskInfo)
        maxCount = 0
        for case in data.getCase():
            lineContent = data.getData(case)
            count = len(lineContent)
            if count > maxCount:
                maxCount = count
                lineHead = [n for n in range(1, maxCount+1)]
                lineHead.insert(0, 'AVG')
                lineHead.insert(0, '')
                # debugLog(lineHead)

            caseExtras = data.getCaseExtra(case)
            lineContent.insert(0, caseExtras['AVG'])
            lineContent.insert(0, case)
            taskInfo.append(lineContent)

        # header
        taskInfo.insert(lineHeadPos, lineHead)
        # debugLog(lineHead)
        pass

    @abstractmethod
    def ShowResult(self):
        pass
