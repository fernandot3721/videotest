from abc import abstractmethod


class ContentHandler(object):

    @abstractmethod
    def onContentKeyDetected(self, key, value):
        pass

    @abstractmethod
    def getContents(self):
        pass
