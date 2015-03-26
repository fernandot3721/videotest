
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
        # debugLog('PROCESS DATA ' + str(self.__class__))
        # debugLog('before==========')
        # data.printData()
        for key in data.getKeysByType(TaskData.DATA_TYPE_TIMING):
            caseData = data.getDataByTypeAndKey(TaskData.DATA_TYPE_TIMING, key)
            count = len(caseData.data)
            data.addDataExtra(TaskData.DATA_TYPE_TIMING, key, 'COUNT', count)
        for key in data.getKeysByType(TaskData.DATA_TYPE_TIMING):
            caseData = data.getDataByTypeAndKey(TaskData.DATA_TYPE_NORMAL, key)
            count = len(caseData.data)
            data.addDataExtra(TaskData.DATA_TYPE_NORMAL, key, 'COUNT', count)
        # debugLog('after==========')
        # data.printData()
        pass


class CutPeak(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        # debugLog('PROCESS DATA ' + str(self.__class__))
        # debugLog('before==========')
        # data.printData()
        # do cut peak
        # for key in data.getKeysByType(TaskData.DATA_TYPE_TIMING):
        #     caseData = data.getDataByTypeAndKey(TaskData.DATA_TYPE_TIMING, key)
        #     # self.cutPeakAndChangeCount(data, caseData)
        #     if len(caseData.data) < 3:
        #         TaskLogger.debugLog('too few data, do not cut peak')
        #         continue
        #     maxValue = max(caseData.data)
        #     minValue = min(caseData.data)
        #     data.addDataExtra(TaskData.DATA_TYPE_TIMING, key, 'CUT-MAX', maxValue)
        #     data.addDataExtra(TaskData.DATA_TYPE_TIMING, key, 'CUT-MIN', minValue)
        #     caseData.remove(maxValue)
        #     caseData.remove(minValue)
        #     count = len(data.getData(case))

        cases = data.getCase()
        for case in cases:
            single = data.getData(case)
            # check count
            if len(single) < 3:
                TaskLogger.debugLog('too few data, do not cut peak')
                continue

            # debugLog("=======%s" % (single))
            maxValue = max(single)
            minValue = min(single)
            data.addCaseExtra(case, 'CUT-MAX', maxValue)
            data.addCaseExtra(case, 'CUT-MIN', minValue)
            single.remove(maxValue)
            single.remove(minValue)
            count = len(data.getData(case))
            data.addCaseExtra(case, 'COUNT', count)
        # debugLog('after==========')
        data.printData()
        pass


class Normalize(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        TaskLogger.debugLog('PROCESS DATA ' + str(self.__class__))
        # do normal distribution
        pass


class Average(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        # debugLog('PROCESS DATA ' + str(self.__class__))
        # debugLog('before==========')
        # data.printData()
        # do average
        cases = data.getCase()
        for case in cases:
            total = 0
            single = data.getData(case)
            for value in single:
                total += float(value)
            data.addCaseExtra(case, 'AVG', total/len(single))
        # debugLog('after==========')
        # data.printData()
        pass


class InvalidData(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        TaskLogger.debugLog('PROCESS DATA ' + str(self.__class__))
        # do invalid
        pass
