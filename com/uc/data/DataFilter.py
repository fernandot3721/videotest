
from abc import abstractmethod
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.TaskData import TaskData


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
        # do normal distribution
        pass


class Average(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        TaskLogger.debugLog('PROCESS DATA ' + str(self.__class__))
        # TaskLogger.debugLog('before==========')
        # data.printData()
        # do average
        self.avgData(data, TaskData.DATA_TYPE_TIMING)
        self.avgData(data, TaskData.DATA_TYPE_NORMAL)
        # cases = data.getCase()
        # for case in cases:
        #     total = 0
        #     single = data.getData(case)
        #     for value in single:
        #         total += float(value)
        #     data.addCaseExtra(case, 'AVG', total/len(single))
        # TaskLogger.debugLog('after==========')
        # data.printData()
        pass

    def avgData(self, data, dataType):
        for key in data.getKeysByType(dataType):
            caseData = data.getDataByTypeAndKey(dataType, key)
            total = 0
            for value in caseData.data:
                total += float(value)
            data.addDataExtra(dataType, key, 'AVG', total/len(caseData.data))

class InvalidData(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        TaskLogger.debugLog('PROCESS DATA ' + str(self.__class__))
        # do invalid
        pass
