
import time
from com.uc.utils.ColorUtil import *
import traceback
from com.uc.conf import Conf
import csv
from com.uc.data.DataRecord import DataRecord
from com.uc.data.TaskData import TaskData
import sys


class CSVRecorder(DataRecord):

    TAG_START = 'TASK-DATA-START'
    TAG_END = 'TASK-DATA-END'
    TAG_TASK = 'TASK-NAME'
    TAG_CASE = 'TASK-CASE'
    TAG_EXTRA = 'TASK-EXTRA'

    def __init__(self):
        self.init()
        self.recordPath = '{}report-{}.csv'\
            .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])

    def init(self):
        self.taskData = {}

    def getData(self):
        return self.taskData

    def onData(self, task, case, data):
        print inblue('onData: {}, {}, {}'.format(task, case, data))
        if task not in self.taskData:
            self.taskData[task] = TaskData()
        self.taskData[task].addData(case, data)

    def onComplete(self):
        self.saveData()
        pass

    def getRecordPath(self):
        return self.recordPath

    def loadData(self):
        debugLog('loadData from /Users/tangjp/work/test/test.csv')
        self.init()
        try:
            csvfile = file('/Users/tangjp/work/test/test.csv', 'rb')
            reader = csv.reader(csvfile)

            tempData = None
            for line in reader:
                if (line[0] == self.TAG_START):
                    tempData = TaskData()
                if (line[0] == self.TAG_TASK):
                    self.taskData[line[0]] = tempData # WARNING: see if after added tempData work or not
                if (line[0] == self.TAG_CASE):
                    tempData.setData(line[1], line[2:])
                if (line[0] == self.TAG_EXTRA):
                    tempData.addExtra(line[1], line[2])
                if (line[0] == self.TAG_END):
                    tempData.printData() # DEBUG ONLY
                    tempData = None
            debugLog('loadData end')
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print inred("Exception: {}".format(exc_value))
            print inred("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
        finally:
            csvfile.close()
        pass

    def saveData(self):
        # cvsfile = file('/opt/lampp/htdocs/test/test.csv', 'w')
        cvsfile = file('/Users/tangjp/work/test/test.csv', 'w')
        try:
            dataToWrite = []
            for task in self.taskData.keys():
                debugLog('saveData')
                debugLog(self.taskData[task])
                self.taskData[task].printData() #DEBUG ONLY
                dataToWrite.append([self.TAG_START])
                dataToWrite.append([self.TAG_TASK, task])
                cases = self.taskData[task].getCase()
                for case in cases:
                    value = self.taskData[task].getData(case)
                    value.insert(0, case)
                    value.insert(0, self.TAG_CASE)
                    dataToWrite.append(value)
                extras = self.taskData[task].getExtra()
                for extra in extras:
                    value = [extra, extras[extra]]
                    value.index(0, self.TAG_EXTRA)
                    dataToWrite.append(value)
                dataToWrite.append([self.TAG_END])
            writer = csv.writer(cvsfile)
            writer.writerows(dataToWrite)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print inred("Exception: {}".format(exc_value))
            print inred("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
        finally:
            cvsfile.close()
            print inblue("view Record: file:///opt/lampp/htdocs/test/test.csv")
            print inblue("view Record: http://100.84.44.238//test/test.csv")

    def testWrite(self):
        list1 = ['1', '2', '3', '4', '5']
        list2 = ['5', '6', '7', '8', '9']
        listall = [list1, list2]
        cvsfile = file('/opt/test.csv', 'wb')
        writer = csv.writer(cvsfile)
        # writer.writeheader()
        # writer.writerow(['a'] + list1)
        # writer.writerow(['b'] + list2)
        writer.writerows(listall)
