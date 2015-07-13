
import importlib
from com.uc.data.CsvViewer import CsvViewer
from com.uc.data.HtmlViewer import HtmlViewer
from com.uc.data.ChartViewer import ChartViewer
from com.uc.data.VsChartViewer import VsChartViewer
from com.uc.data.DataFilter import DataFilter
from com.uc.conf import GConf
from com.uc.utils.TaskLogger import TaskLogger
from os.path import sys
import traceback


class ResultGenerator():

    def __init__(self):
        self.loadConfig()
        self.data = []
        # self.viewer = CsvViewer()
        self.viewer = HtmlViewer()
        self.subViewer = VsChartViewer()
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
            self.subViewer.addData(data)
            self.viewer.addData(data)
        try:
            if GConf.getCaseBool('RESULT_IMG') is True:
                TaskLogger.debugLog('do generate img')
                path = self.subViewer.showResult()
                self.viewer.showResult(path)
            else:
                TaskLogger.debugLog('do not generate img')
                self.viewer.showResult()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            TaskLogger.errorLog("Exception: {}".format(exc_value))
            TaskLogger.errorLog("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
        pass

    def processData(self, data):
        # use spcific config to make filter the data
        dataFilter = DataFilter()
        filters = GConf.getCase('FILTERS').splitlines()
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
