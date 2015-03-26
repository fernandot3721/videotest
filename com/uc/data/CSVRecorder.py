
import time
from com.uc.utils.TaskLogger import TaskLogger
import traceback
from com.uc.conf import Conf
import csv
from com.uc.data.DataRecord import DataRecord
from com.uc.data.TaskData import TaskData
import sys


class CSVRecorder(DataRecord):

    def __init__(self):
        self.init()
        self.recordPath = '{}record-{}.csv'\
            .format(Conf.DATA_DIR, 'test1')
            # .format(Conf.DATA_DIR, time.strftime('%Y%m%d%H%M')[2:])

    def init(self):
        self.taskData = {}

    def getData(self):
        return self.taskData.values()

    def onData(self, task, dtype, key, value):
        TaskLogger.\
            detailLog('onData: %s, %s, %s, %s' % (task, dtype, key, value))
        if task not in self.taskData:  # init
            TaskLogger.debugLog('record: %s' % task)
            self.taskData[task] = TaskData()
            self.taskData[task].setTitle(task)

        if dtype == DataRecord.TYPE_EXTRA:  # extra
            self.taskData[task].addExtra(key, value)
        elif dtype == DataRecord.TYPE_NORMAL:  # normal data
            self.taskData[task].addData(TaskData.DATA_TYPE_NORMAL, key, value)
        elif dtype == DataRecord.TYPE_TIMING:  # timing data
            self.taskData[task].addData(TaskData.DATA_TYPE_TIMING, key, value)

    def onComplete(self):
        self.saveData()
        pass

    def getRecordPath(self):
        return self.recordPath

    def loadData(self, path=None):
        self.init()
        try:
            csvfile = ''
            if (path is None):
                # TODO you may choose the most recent one to load
                csvfile = open(self.recordPath, 'rb')
                TaskLogger.debugLog('loadData from %s' % self.recordPath)
            else:
                csvfile = open(path, 'rb')
                TaskLogger.debugLog('loadData from file://%s' % path)
            reader = csv.reader(csvfile)

            tempData = None
            for line in reader:
                if (line[0] == DataRecord.TAG_START):
                    tempData = TaskData()
                if (line[0] == DataRecord.TAG_TASK):
                    self.taskData[line[1]] = tempData
                    tempData.setTitle(line[1])
                if (line[0] == DataRecord.TAG_NORMAL_DATA):
                    tempData.\
                        setData(TaskData.DATA_TYPE_NORMAL, line[1], line[2:])
                if (line[0] == DataRecord.TAG_TIMING_DATA):
                    tempData.\
                        setData(TaskData.DATA_TYPE_TIMING, line[1], line[2:])
                if (line[0] == DataRecord.TAG_NORMAL_EXTRA):
                    tempData.addDataExtra(TaskData.DATA_TYPE_NORMAL, line[1], line[2])
                if (line[0] == DataRecord.TAG_TIMING_EXTRA):
                    tempData.addDataExtra(TaskData.DATA_TYPE_TIMING, line[1], line[2])
                if (line[0] == DataRecord.TAG_EXTRA):
                    tempData.addExtra(line[1], line[2])
                if (line[0] == DataRecord.TAG_END):
                    tempData.printData()  # DEBUG ONLY
                    tempData = None
            TaskLogger.debugLog('loadData end')
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            TaskLogger.errorLog("Exception: {}".format(exc_value))
            TaskLogger.errorLog("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
        finally:
            csvfile.close()
        pass

    def saveData(self):
        cvsfile = open(self.recordPath, 'w')

        try:
            dataToWrite = []
            for task in self.taskData.keys():
                TaskLogger.debugLog('saveData: %s' % task)
                TaskLogger.debugLog(self.taskData[task])
                self.taskData[task].printData()  # DEBUG ONLY

                dataToWrite.append([DataRecord.TAG_START])  # TASK-DATA-START
                # TASK-NAME
                dataToWrite.\
                    append([DataRecord.TAG_TASK, self.taskData[task]])

                # extras
                extras = self.taskData[task].getAllExtra()
                for extra in extras:
                    value = list([extra, extras[extra]])
                    value.insert(0, DataRecord.TAG_EXTRA)  # TASK-EXTRA
                    dataToWrite.append(value)

                # normal data
                normalKeys = self.taskData[task].\
                    getKeysByType(TaskData.DATA_TYPE_NORMAL)
                for key in normalKeys:
                    caseData = self.taskData[task].\
                        getDataByTypeAndKey(TaskData.DATA_TYPE_NORMAL, key)
                    # NORMAL DATA
                    value = list(caseData.data)
                    value.insert(0, key)
                    value.insert(0, DataRecord.TAG_NORMAL_DATA)
                    dataToWrite.append(value)

                    for extra in caseData.extra:
                        dataToWrite.append([DataRecord.TAG_NORMAL_EXTRA, extra, caseData[extra]])

                # timing data
                timingKeys = self.taskData[task].\
                    getKeysByType(TaskData.DATA_TYPE_TIMING)
                for key in timingKeys:
                    caseData = self.taskData[task].\
                        getDataByTypeAndKey(TaskData.DATA_TYPE_TIMING, key)
                    # TIMING DATA
                    value = list(caseData.data)
                    value.insert(0, key)
                    value.insert(0, DataRecord.TAG_TIMING_DATA)
                    dataToWrite.append(value)
                    for extra in caseData.extra:
                        dataToWrite.append([DataRecord.TAG_TIMING_EXTRA, extra, caseData[extra]])

                dataToWrite.append([DataRecord.TAG_END])  # TASK-END
            writer = csv.writer(cvsfile)
            writer.writerows(dataToWrite)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            TaskLogger.errorLog("Exception: {}".format(exc_value))
            TaskLogger.errorLog("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
        finally:
            cvsfile.close()
            TaskLogger.detailLog("view Record: file://%s" % self.recordPath)
