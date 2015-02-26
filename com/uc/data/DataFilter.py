

from com.uc.utils.ColorUtil import *


class DataFilter(object):
    def processData(self, data):
        # debugLog('PROCESS DATA ' + str(self.__class__))
        pass

    # @abstractmethod
    # def getFilterInfo(self):
    #     pass


class EmptyFilter(DataFilter):
    def __init__(self, filter):
        if isinstance(filter, DataFilter):
            self.filter = filter
        else:
            raise Exception("A filter should be used make a new one")


class CutPeak(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        data.printData()
        debugLog('PROCESS DATA ' + str(self.__class__))
        # do cut peak
        cases = data.getCase()
        for case in cases:
            single = data.getData(case)
            # debugLog("=======%s" % (single))
            maxValue = max(single)
            minValue = min(single)
            data.addCaseExtra(case, 'CUT-MAX', maxValue)
            data.addCaseExtra(case, 'CUT-MIN', minValue)
            single.remove(maxValue)
            single.remove(minValue)
        data.printData()
        pass


class Normalize(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        debugLog('PROCESS DATA ' + str(self.__class__))
        # do normal distribution
        pass


class Average(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        data.printData()
        debugLog('PROCESS DATA ' + str(self.__class__))
        # do average
        cases = data.getCase()
        for case in cases:
            total = 0
            single = data.getData(case)
            # debugLog("=======%s" % (single))
            for value in single:
                total += float(value)
            data.addCaseExtra(case, 'AVG', total/len(single))
        data.printData()
        pass


class InvalidData(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        debugLog('PROCESS DATA ' + str(self.__class__))
        # do invalid
        pass
