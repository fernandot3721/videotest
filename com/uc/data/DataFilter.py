

from com.uc.utils.ColorUtil import *


class DataFilter(object):
    def processData(self, data):
        debugLog('PROCESS DATA ' + str(self.__class__))
        pass

    # @abstractmethod
    # def getFilterInfo(self):
    #     pass


class EmptyFilter(DataFilter):
    def __init__(self, filter):
        if isinstance(filter, DataFilter):
            debugLog('CREATE %s FROM %s' % (self.__class__, filter.__class__))
            self.filter = filter
        else:
            raise Exception("A filter should be used make a new one")


class CutPeak(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        debugLog('PROCESS DATA ' + str(self.__class__))
        # do cut peak
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
        debugLog('PROCESS DATA ' + str(self.__class__))
        # do average
        pass


class InvalidData(EmptyFilter):
    def processData(self, data):
        self.filter.processData(data)
        debugLog('PROCESS DATA ' + str(self.__class__))
        # do invalid
        pass
