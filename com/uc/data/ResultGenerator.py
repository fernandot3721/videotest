
import importlib
from com.uc.data.CsvViewer import CsvViewer
from com.uc.data.HtmlViewer import HtmlViewer
from com.uc.data.ChartViewer import ChartViewer
from com.uc.data.DataFilter import DataFilter
from com.uc.conf import Conf
from com.uc.utils.TaskLogger import TaskLogger


class ResultGenerator():

    def __init__(self):
        self.loadConfig()
        self.data = []
        # self.viewer = CsvViewer()
        # self.viewer = HtmlViewer()
        self.viewer = ChartViewer()
        pass

    def loadConfig(self):
        # read conf to determin which filters to use
        pass

    def generateResult(self, dataRecord):
        # read data record and filter the data
        self.data = dataRecord.getData()
        for data in self.data:
            self.processData(data)

        #  show result
        for data in self.data:
            TaskLogger.debugLog('addData %s' % data)
            self.viewer.addData(data)
        self.viewer.showResult()
        pass

    def processData(self, data):
        # use spcific config to make filter the data
        dataFilter = DataFilter()
        filters = Conf.FILTERS[data.getExtra('TASK_TYPE')]
        for filterName in filters:
            dataFilter = self.generateFilter(filterName, dataFilter)
        dataFilter.processData(data)
        pass

    def generateFilter(self, key, filter):
        # produce corresponding filter according to keyword
        # NOTE the key is the name of filter class
        module = importlib.import_module("com.uc.data.DataFilter")
        filterClass = getattr(module, key)
        filterObject = filterClass(filter)
        return filterObject
        pass
