from abc import abstractmethod


class TimingHandler(object):

    @abstractmethod
    def onTimingKeyDetected(self, key, value, type=None):
        pass
