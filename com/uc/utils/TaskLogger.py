# encoding: utf-8
from com.uc.conf import GConf
import time
import threading


def inred(s):
    return"%s[1;31;40m%s%s[0m" % (chr(27), s, chr(27))


def ingreen(s):
    return"%s[1;32;40m%s%s[0m" % (chr(27), s, chr(27))


def inyellow(s):
    return"%s[1;33;40m%s%s[0m" % (chr(27), s, chr(27))


def inblue(s):
    return"%s[1;34;40m%s%s[0m" % (chr(27), s, chr(27))


class TaskLogger():

    instance = None

    @staticmethod
    def debugLog(s):
        if GConf.getGlobal('DEBUG_LOG'):
            print(inyellow(s))
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    @staticmethod
    def errorLog(s):
        if GConf.getGlobal('ERROR_LOG'):
            print(inred(threading.currentThread()))
            print(inred(s))
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    @staticmethod
    def infoLog(s):
        if GConf.getGlobal('INFO_LOG'):
            print(ingreen(s))
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    @staticmethod
    def detailLog(s):
        if GConf.getGlobal('DETAIL_LOG'):
            print(inblue(s))
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    @staticmethod
    def normalLog(s):
        if GConf.getGlobal('NORMAL_LOG'):
            print(s)
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    def __init__(self):
        if GConf.getGlobal('FILE_LOG'):
            self.logfile = '%s%s.log' % (GConf.getGlobal('TASK_LOG_PATH'), time.strftime('%Y%m%d%H%M')[2:])
            self.__fileHandle = open(self.logfile, 'wb')
            pass
        self.__instance = None

    def __del__(self):
        self.__fileHandle.close()

    def writeLog(self, s):
        if GConf.getGlobal('FILE_LOG'):
            self.__fileHandle.write(s)

    @staticmethod
    def init():
        if TaskLogger.instance is None:
            TaskLogger.instance = TaskLogger()
