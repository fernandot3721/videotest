
import thread
from com.uc.utils.TaskLogger import TaskLogger


class TaskData():

    DATA_TYPE_TIMING = 'TimingData'
    DATA_TYPE_NORMAL = 'NormalData'

    def __init__(self):
        self.timingData = {}
        self.normalData = {}
        self.timingKeys = []
        self.normalKeys = []
        self.extra = {}
        self.lock = thread.allocate_lock()
        self.title = ''

    def getTimingDataByKey(self, key):
        if key in self.timingData:
            return self.timingData[key]

    def getNormalDataByKey(self, key):
        if key in self.normalData:
            return self.normalData[key]

    def getDataByTypeAndKey(self, type, key):
        TaskLogger.debugLog('getDataByTypeAndKey: %s | %s' % (type, key))
        if type == self.DATA_TYPE_NORMAL and key in self.normalData:
            return self.normalData[key]
        elif type == self.DATA_TYPE_TIMING and key in self.timingData:
            return self.timingData[key]
        return None

    def getAllExtra(self):
        return self.extra

    def getExtra(self, key):
        return self.extra[key]

    def getTimingKeys(self):
        return self.timingKeys

    def getNormalKeys(self):
        return self.normalKeys

    def getKeysByType(self, type):
        if type == self.DATA_TYPE_NORMAL:
            return self.normalKeys
        elif type == self.DATA_TYPE_TIMING:
            return self.timingKeys
        return None

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

    def addData(self, type, key, value):
        self.lock.acquire()
        if type == self.DATA_TYPE_NORMAL:
            if key not in self.normalData:
                self.normalKeys.append(key)
                self.normalData[key] = CaseData()
            self.normalData[key].data.append(value)
        elif type == self.DATA_TYPE_TIMING:
            if key not in self.timingData:
                self.timingKeys.append(key)
                self.timingData[key] = CaseData()
            self.timingData[key].data.append(value)
        self.lock.release()

    def setTimingData(self, key, values):
        self.lock.acquire()
        if key not in self.timingData:
            self.timingKeys.append(key)
            self.timingData[key] = CaseData()
        self.timingData[key].data = values
        self.lock.release()

    def setNormalData(self, key, values):
        self.lock.acquire()
        if key not in self.normalData:
            self.normalKeys.append(key)
            self.normalData[key] = CaseData()
        self.normalData[key].data = values
        self.lock.release()

    def setData(self, type, key, values):
        self.lock.acquire()
        if type == self.DATA_TYPE_NORMAL:
            if key not in self.normalData:
                self.normalKeys.append(key)
                self.normalData[key] = CaseData()
            self.normalData[key].data = values
        elif type == self.DATA_TYPE_TIMING:
            if key not in self.timingData:
                self.timingKeys.append(key)
                self.timingData[key] = CaseData()
            self.timingData[key].data = values
        self.lock.release()

    def addExtra(self, key, value):
        self.lock.acquire()
        if key not in self.extra:
            self.extra[key] = value
        self.lock.release()

    def addTimingExtra(self, key, extra, value):
        self.lock.acquire()
        if key in self.timingData:
            self.timingData[key].extra[extra] = value
        self.lock.release()
        pass

    def addNormalExtra(self, key, extra, value):
        self.lock.acquire()
        if key in self.normalData:
            self.normalData[key].extra[extra] = value
        self.lock.release()
        pass

    def addDataExtra(self, type, key, extra, value):
        self.lock.acquire()
        if type == self.DATA_TYPE_NORMAL:
            if key in self.normalData:
                self.normalData[key].extra[extra] = value
        elif type == self.DATA_TYPE_TIMING:
            if key in self.timingData:
                self.timingData[key].extra[extra] = value
        self.lock.release()

    def setTitle(self, title):
        self.title = str(title)

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
            print('CASE: %s, VALUE: %s' % (key, self.normalData[key].data))

            for extra in caseData.extra:
                print('EXTRA: %s, VALUE: %s' % extra, caseData.extra[extra])

        # timing data
        TaskLogger.infoLog('TIMING DATA')
        for key in self.timingData:
            caseData = self.timingData[key]
            print('CASE: %s, VALUE: %s' % (key, self.timingData[key].data))

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
