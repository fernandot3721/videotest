
import time
from com.uc.utils.ColorUtil import *
import traceback
from com.uc.conf import Conf
import csv
from com.uc.data.DataRecord import DataRecord
from com.uc.data.TaskData import TaskData
import sys


class CSVRecorder(DataRecord):

    def __init__(self):
        self.taskData = {}
        self.data = {}
        self.recordPath = '{}report-{}.csv'\
            .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])

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
        pass

    def saveData(self):
        cvsfile = file('/opt/lampp/htdocs/test/test.csv', 'w')
        try:
            dataToWrite = []
            for key in self.taskData.keys():
                dataToWrite.append(key)
                cases = self.taskData[key].getCase
                for case in cases:
                    value = self.taskData[key].getData(case)
                    value.insert(0, case)
                    dataToWrite.append(value)
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
        cvsfile = file('/opt/test.csv', 'w')
        writer = csv.writer(cvsfile)
        # writer.writeheader()
        # writer.writerow(['a'] + list1)
        # writer.writerow(['b'] + list2)
        writer.writerows(listall)
