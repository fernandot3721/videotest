# encoding: utf-8
from com.uc.conf import Conf
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
    logfile = '%s%s.log' % (Conf.TASK_LOG_PATH, time.strftime('%Y%m%d%H%M')[2:])

    @staticmethod
    def debugLog(s):
        if Conf.DEBUG_LOG:
            print(inyellow(s))
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    @staticmethod
    def errorLog(s):
        if Conf.ERROR_LOG:
            print(inred(threading.currentThread()))
            print(inred(s))
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    @staticmethod
    def infoLog(s):
        if Conf.INFO_LOG:
            print(ingreen(s))
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    @staticmethod
    def detailLog(s):
        if Conf.DETAIL_LOG:
            print(inblue(s))
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    @staticmethod
    def normalLog(s):
        if Conf.NORMAL_LOG:
            print(s)
            if TaskLogger.instance is not None:
                TaskLogger.instance.writeLog('%s\n' % s)

    def __init__(self):
        if Conf.FILE_LOG:
            self.__fileHandle = open(TaskLogger.logfile, 'wb')
            pass
        self.__instance = None

    def __del__(self):
        self.__fileHandle.close()

    def writeLog(self, s):
        if Conf.FILE_LOG:
            self.__fileHandle.write(s)

    @staticmethod
    def init():
        if TaskLogger.instance is None:
            TaskLogger.instance = TaskLogger()
