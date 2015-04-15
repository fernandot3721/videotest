from abc import abstractmethod


class ResultViewer():

    @abstractmethod
    def addData(self, data):
        pass

    @abstractmethod
    def showResult(self, subPath=None):
        pass
