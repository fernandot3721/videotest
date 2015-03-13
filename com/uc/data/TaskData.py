
import thread
from com.uc.utils.TaskLogger import TaskLogger


class TaskData():

    def __init__(self):
        self.timingData = {}
        self.normalData = {}
        self.timingKeys = []
        self.normalKeys = []
        self.extra = {}
        self.lock = thread.allocate_lock()
        self.title = ''

    def getTimingDataByCase(self, case):
        if case in self.timingData:
            return self.timingData[case]

    def getNormalDataByCase(self, case):
        if case in self.normalData:
            return self.normalData[case]

    def getAllExtra(self):
        return self.extra

    def getExtra(self, key):
        return self.extra[key]

    def getTimingKeys(self):
        return self.timingKeys

    def getNormalKeys(self):
        return self.normalKeys

    def addTimingData(self, key, value):
        self.lock.acquire()
        if key not in self.timingData:
            self.timingKeys.append(key)
            self.timingData[key] = CaseData()
        self.timingData[key].data.append(value)
        self.lock.release()
        pass

    def addNormalData(self, key, value):
        self.lock.acquire()
        if key not in self.normalData:
            self.normalKeys.append(key)
            self.normalData[key] = CaseData()
        self.normalData[key].data.append(value)
        self.lock.release()
        pass

    def addExtra(self, key, value):
        self.lock.acquire()
        if key not in self.extra:
            self.extra[key] = value
        self.lock.release()

    def addTimingExtra(self, key, extra, value):
        self.lock.acquire()
        if key in self.timingData:
            self.timingData[key].extra[extra] = value
        pass

    def addNormalExtra(self, key, extra, value):
        self.lock.acquire()
        if key in self.normalData:
            self.normalData[key].extra[extra] = value
        pass

    def setTimingData(self, key, values):
        self.lock.acquire()
        if key not in self.timingData:
            self.timingKeys.append(key)
        self.timingData[key] = values
        self.lock.release()

    def setNormalData(self, key, values):
        self.lock.acquire()
        if key not in self.normalData:
            self.normalKeys.append(key)
        self.normalData[key] = values
        self.lock.release()

    def setTitle(self, title):
        self.title = title

    def printData(self):
        print('')
        TaskLogger.infoLog('=====TASK DATA:=====')
        print(self.title)

        # extras
        TaskLogger.infoLog('EXTRA')
        for extra in self.extra:
            print('KEY: %s, VALUE: %s' % (extra, self.extra[extra]))

        # normal data
        TaskLogger.infoLog('NORMAL DATA')
        for key in self.normalData:
            caseData = self.normalData[key]
            print('CASE: %s, VALUE: %s' % (key, self.normalData[key]))

            for extra in caseData.extra:
                print('EXTRA: %s, VALUE: %s' % extra, caseData.extra[extra])

        # timing data
        TaskLogger.infoLog('TIMING DATA')
        for key in self.timingData:
            caseData = self.timingData[key]
            print('CASE: %s, VALUE: %s' % (key, self.timingData[key]))

            for extra in caseData.extra:
                print('EXTRA: %s, VALUE: %s' % extra, caseData.extra[extra])

        TaskLogger.infoLog('===================')
        print('')

    def __str__(self):
        return self.title


class CaseData():

    def __init__(self):
        self.data = []
        self.extra = {}
