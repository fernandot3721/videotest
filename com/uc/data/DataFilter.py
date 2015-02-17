


from abc import ABCMeta, abstractmethod

class  DataFilter(object):
    @abstractmethod
    def processData(self, data):
        pass

    @abstractmethod
    def getFilterInfo(self):
        pass
