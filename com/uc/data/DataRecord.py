

from abc import abstractmethod


class DataRecord():
    @abstractmethod
    def onData(self, group, data):
        pass

    @abstractmethod
    def onComplete(self):
        pass

    @abstractmethod
    def getData(self):
        pass
