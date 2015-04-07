

from abc import abstractmethod


class DataRecord():

    TAG_START = 'TASK-DATA-START'
    TAG_END = 'TASK-DATA-END'
    TAG_TASK = 'TASK-NAME'
    TAG_EXTRA = 'TASK-EXTRA'
    TAG_NORMAL_DATA = 'NORMAL-DATA'
    TAG_NORMAL_EXTRA = 'NORMAL-EXTRA'
    TAG_TIMING_DATA = 'TIMING-DATA'
    TAG_TIMING_EXTRA = 'TIMING-EXTRA'
    TYPE_NORMAL = 'TYPE_NORMAL'
    TYPE_TIMING = 'TYPE_TIMING'
    TYPE_EXTRA = 'TYPE_EXTRA'

    @abstractmethod
    def onData(self, task, dtype, key, value, rtype=None):
        pass

    @abstractmethod
    def onComplete(self):
        pass

    @abstractmethod
    def getData(self):
        pass
