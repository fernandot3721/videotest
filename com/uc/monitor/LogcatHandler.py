from abc import abstractmethod


class LogcatHandler(object):

    @abstractmethod
    def onKeywordDetected(self, key, value):
        pass

    @abstractmethod
    def onEventDetected(self, event, value):
        pass

    @abstractmethod
    def onVideoStartPlayer(self):
        pass

    @abstractmethod
    def onPlayerVersion(version):
        pass

    @abstractmethod
    def getKeywords(self):
        pass

    @abstractmethod
    def getKeyevents(self):
        pass
