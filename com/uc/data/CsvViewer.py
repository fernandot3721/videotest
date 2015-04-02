from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.TaskData import TaskData
from com.uc.conf import Conf
import sys
import csv
import traceback


class CsvViewer(ResultViewer):

    def __init__(self):
        self.dataCount = 0
        self.lineInfo = {}
        # self.reportPath = '{}report.csv'\
            # .format(Conf.REPORT_DIR)
        self.reportPath = '{}report-{}.csv'\
            .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])

    def showResult(self):
        # self.init()
        csvfile = file(self.reportPath, 'w')
        try:
            writer = csv.writer(csvfile)
            for task in self.lineInfo:
                writer.writerow([task])
                writer.writerows(self.lineInfo[task])
                writer.writerow('')
            return self.reportPath
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            TaskLogger.errorLog("Exception: {}".format(exc_value))
            TaskLogger.errorLog("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
        finally:
            csvfile.close()
            TaskLogger.detailLog("view Report: file://%s" % self.reportPath)
        pass

    def addData(self, data):
        data.printData()
        taskInfo = []
        self.lineInfo[str(data)] = taskInfo
        #  extra info
        taskInfo.append(['Task Info:'])
        extras = data.getAllExtra()
        for extra in extras:
            taskInfo.append([extra, extras[extra]])

        #  case data & head
        self.parseDataType(data, TaskData.DATA_TYPE_TIMING, taskInfo)
        self.parseDataType(data, TaskData.DATA_TYPE_NORMAL, taskInfo)
        pass

    def parseDataType(self, data, dataType, taskInfo):
        lineHead = []
        lineHeadPos = len(taskInfo)
        dataCount = 0
        for key in data.getKeysByType(dataType):
            caseData = data.getDataByTypeAndKey(dataType, key)
            lineContent = caseData.data
            extras = data.getDataExtra(dataType, key)

            count = len(lineContent)
            if count > dataCount:
                dataCount = count
                lineHead = [n for n in range(1, dataCount+1)]
                # lineHead.insert(0, 'AVG')
                for extra in extras:
                    lineHead.insert(0, extra)
                lineHead.insert(0, 'CASE')
                # debugLog(lineHead)

            for extra in extras:
                lineContent.insert(0, extras[extra])
            lineContent.insert(0, key)
            taskInfo.append(lineContent)
        # header
        taskInfo.insert(lineHeadPos, lineHead)
