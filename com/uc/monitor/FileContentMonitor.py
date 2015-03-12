from com.uc.utils.TaskLogger import TaskLogger
from com.uc.monitor.LogMonitor import LogMonitor
from com.uc.conf import Conf
from time import sleep

import traceback
import sys


class FileContentMonitor(LogMonitor):

    def __init__(self):
        super(FileContentMonitor, self).__init__()
        self.keywords = []
        self.targetFile = '/proc/meminfo'

    def doMonitor(self):
        self.setName('FileContentMonitor')
        TaskLogger.\
            infoLog("===========THREAD %s start===========" % self.getName())
        # open target file
        while not self.isStop:
            fileHandle = open(self.targetFile, 'rb')
            for line in fileHandle:
                # TaskLogger.debugLog(line)
                self.onRead(line)
                pass
            fileHandle.close()

            sleep(5)
        pass

    def init(self):
        # self.keywords = self.handler.getContents()
        self.keywords = {'MemFree:': 'kB'}
        pass

    def onRead(self, line):
        # filt out keyword and pass it to hanelder
        for key in self.keywords:
            if key in line:
                value = self.parseLog(line, key, self.keywords[key])
                self.handler.onContentKeyDetected(key, value)
        pass
    pass
