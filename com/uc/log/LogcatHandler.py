from abc import abstractmethod


class LogcatHandler(object):

    @abstractmethod
    def onKeywordDetected(key, value):
        pass

    @abstractmethod
    def onVideoStartPlayer():
        pass

    @abstractmethod
    def onPlayerVersion(version):
        pass

    @abstractmethod
    def getKeywords():
        pass
