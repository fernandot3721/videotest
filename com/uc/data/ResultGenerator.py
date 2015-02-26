
import importlib
from com.uc.conf import Conf
from com.uc.data.DataFilter import DataFilter
from com.uc.utils.ColorUtil import *


class ResultGenerator():

    def __init__(self):
        self.loadConfig()
        self.data = []
        pass

    def loadConfig(self):
        # read conf to determin which filters to use
        pass

    def generateResult(self, dataRecord):
        # read data record and filter the data
        self.data = dataRecord.getData()
        pass

    def processT1Result(self, data):
        # use spcific config to make filter the data
        t1Filter = DataFilter()
        filters = Conf.T1_FILTER
        for filter in filters:
            debugLog('create filter: ' + str(filter))
            t1Filter = self.generateFilter(filter, t1Filter)

        debugLog('call %s procssData' % t1Filter)
        t1Filter.processData(data)
        pass

    def generateFilter(self, key, filter):
        # produce corresponding filter according to keyword
        # NOTE the key is the name of filter class
        module = importlib.import_module("com.uc.data.DataFilter")
        #print str(module)
        filterClass = getattr(module, key)
        filterObject = filterClass(filter)
        # filterObject.procssData(None)
        return filterObject
        pass
