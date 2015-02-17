

from abc import ABCMeta, abstractmethod

class  DataRecord(object):
    @abstractmethod
    def onData(self, group, data, head=False):
        pass

    @abstractmethod
    def onComplete(self):
        pass
