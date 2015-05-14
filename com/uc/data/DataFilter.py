
from abc import abstractmethod
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.TaskData import TaskData
import numpy as np


class DataFilter(object):
    @abstractmethod
    def processData(self, data):
        # debugLog('PROCESS DATA ' + str(self.__class__))
        pass


class EmptyFilter(DataFilter):
    def __init__(self, filter):
        if isinstance(filter, DataFilter):
            self.filter = filter
        else:
            raise Exception("A filter should be used make a new one")


class Count(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        TaskLogger.debugLog('PROCESS DATA ' + str(self.__class__))
        # TaskLogger.debugLog('before==========')
        # data.printData()
        self.countData(data, TaskData.DATA_TYPE_TIMING)
        self.countData(data, TaskData.DATA_TYPE_NORMAL)
        # TaskLogger.debugLog('after==========')
        # data.printData()
        pass

    def countData(self, data, dataType):
        for key in data.getKeysByType(dataType):
            caseData = data.getDataByTypeAndKey(dataType, key)
            count = len(caseData.data)
            data.addDataExtra(dataType, key, 'COUNT', count)


class CutPeak(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        TaskLogger.debugLog('PROCESS DATA ' + str(self.__class__))
        # TaskLogger.debugLog('before==========')
        # data.printData()
        # do cut peak
        self.cutData(data, TaskData.DATA_TYPE_TIMING)
        self.cutData(data, TaskData.DATA_TYPE_NORMAL)
        # TaskLogger.debugLog('after==========')
        # data.printData()
        pass

    def cutData(self, data, dataType):
        for key in data.getKeysByType(dataType):
            caseData = data.getDataByTypeAndKey(dataType, key)
            if len(caseData.data) < 3:
                TaskLogger.debugLog('too few data, do not cut peak')
                data.addDataExtra(dataType, key, 'CUT-MAX', None)
                data.addDataExtra(dataType, key, 'CUT-MIN', None)
                continue
            maxValue = max(caseData.data)
            minValue = min(caseData.data)
            data.addDataExtra(dataType, key, 'CUT-MAX', maxValue)
            data.addDataExtra(dataType, key, 'CUT-MIN', minValue)
            caseData.data.remove(maxValue)
            caseData.data.remove(minValue)
            count = len(caseData.data)
            data.addDataExtra(dataType, key, 'COUNT', count)


class Normalize(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        TaskLogger.debugLog('PROCESS DATA ' + str(self.__class__))
        self.normalizeData(data, TaskData.DATA_TYPE_TIMING)
        self.normalizeData(data, TaskData.DATA_TYPE_NORMAL)
        # do normal distribution
        pass

    def normalizeData(self, data, dataType):
        for key in data.getKeysByType(dataType):
            caseData = data.getDataByTypeAndKey(dataType, key)
            testData = map(float, caseData.data)
            avg = np.mean(testData)
            sdev = np.std(testData)
            maxValue = avg + sdev
            minValue = avg - sdev
            data.addDataExtra(dataType, key, 'avg', avg)

            removeList = []
            count = 0
            for value in caseData.data:
                floatValue = float(value)
                if floatValue > maxValue or floatValue < minValue:
                    removeList.append(value)
                    count += 1
            for value in removeList:
                caseData.data.remove(value)
            data.addDataExtra(dataType, key, 'NOR', count)


class Average(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        TaskLogger.debugLog('PROCESS DATA ' + str(self.__class__))
        # do average
        self.avgData(data, TaskData.DATA_TYPE_TIMING)
        self.avgData(data, TaskData.DATA_TYPE_NORMAL)
        pass

    def avgData(self, data, dataType):
        for key in data.getKeysByType(dataType):
            caseData = data.getDataByTypeAndKey(dataType, key)
            total = 0
            for value in caseData.data:
                try:
                    total += float(value)
                except:
                    caseData.data.remove(value)
            data.addDataExtra(dataType, key, 'AVG', total/len(caseData.data))

class InvalidData(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        TaskLogger.debugLog('PROCESS DATA ' + str(self.__class__))
        # do invalid
        pass
