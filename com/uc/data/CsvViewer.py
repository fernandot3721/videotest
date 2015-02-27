from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.ColorUtil import *
import csv
import traceback


class CsvViewer(ResultViewer):

    def __init__(self):
        self.dataCount = 0
        self.lineInfo = {}
        self.reportPath = '{}report.csv'\
            .format(Conf.REPORT_DIR)
        # self.reportPath = '{}report-{}.csv'\
        #     .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])

    def showResult(self):
        # self.init()
        csvfile = file(self.reportPath, 'w')
        try:
            writer = csv.writer(csvfile)
            for task in self.lineInfo:
                writer.writerow([task])
                writer.writerows(self.lineInfo[task])
                writer.writerow('')
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(inred("Exception: {}".format(exc_value)))
            print(inred("#######STACK TRACE:"))
            traceback.print_tb(exc_traceback)
        finally:
            csvfile.close()
            print(inblue("view Report: file://%s" % self.reportPath))
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
        self.dataCount = 0
        for case in data.getCase():
            lineContent = data.getData(case)
            count = len(lineContent)
            if count > self.dataCount:
                self.dataCount = count
                lineHead = [n for n in range(1, self.dataCount+1)]
                lineHead.insert(0, 'AVG')
                lineHead.insert(0, 'CASE')
                # debugLog(lineHead)

            caseExtras = data.getCaseExtra(case)
            lineContent.insert(0, caseExtras['AVG'])
            lineContent.insert(0, case)
            taskInfo.append(lineContent)

        # header
        taskInfo.insert(lineHeadPos, lineHead)
        # debugLog(lineHead)
        pass
