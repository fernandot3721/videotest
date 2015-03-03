
from abc import abstractmethod
from com.uc.utils.TaskLogger import TaskLogger


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
        for case in data.getCase():
            count = len(data.getData(case))
            data.addCaseExtra(case, 'COUNT', count)
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
