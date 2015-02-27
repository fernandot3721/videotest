from abc import abstractmethod
from com.uc.utils.ColorUtil import *
import time


class ResultViewer():

    @abstractmethod
    def addData(self, data):
        pass

    @abstractmethod
    def showResult(self):
        pass
