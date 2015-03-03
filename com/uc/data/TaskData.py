
import thread
from com.uc.utils.TaskLogger import TaskLogger


class TaskData():

    def __init__(self):
        self.data = {}
        self.extra = {}
        self.cases = []
        self.lock = thread.allocate_lock()
        self.caseExtra = {}
        self.ceExist = False
        self.title = ''

    def getData(self, case):
        if case in self.data:
            return self.data[case]

    def getAllExtra(self):
        return self.extra

    def getExtra(self, key):
        return self.extra[key]

    def getCaseExtra(self, case):
        return self.caseExtra[case]

    def getCase(self):
        return self.cases

    def ceExist(self):
        return self.ceExist

    def addData(self, case, value):
        self.lock.acquire()
        if case not in self.data:
            self.cases.append(case)
            self.data[case] = []
        self.data[case].append(value)
        self.lock.release()
        pass

    def addExtra(self, key, value):
        self.lock.acquire()
        if key not in self.extra:
            self.extra[key] = value
        self.lock.release()

    def addCaseExtra(self, case, key, value):
        self.lock.acquire()
        if not self.ceExist:
            self.ceExist = True
        if case not in self.caseExtra:
            self.caseExtra[case] = {}
        self.caseExtra[case][key] = value
        self.lock.release()
        pass

    def setData(self, case, values):
        self.lock.acquire()
        if case not in self.data:
            self.cases.append(case)
        self.data[case] = values
        self.lock.release()

    def setTitle(self, title):
        self.title = title

    def printData(self):
        print('')
        TaskLogger.infoLog('=====TASK DATA:=====')
        print(self.title)
        TaskLogger.infoLog('CASE')
        for case in self.data:
            print('CASE: %s, VALUE: %s' % (case, self.data[case]))
        TaskLogger.infoLog('EXTRA')
        for extra in self.extra:
            print('KEY: %s, VALUE: %s' % (extra, self.extra[extra]))
        if self.ceExist:
            TaskLogger.infoLog('CASE EXTRA')
            for case in self.cases:
                ceStr = 'CASE: %s' % case
                for extra in self.caseExtra[case]:
                    ceStr = '%s, KEY: %s, VALUE: %s' % \
                        (ceStr, extra, self.caseExtra[case][extra])
                print(ceStr)
        TaskLogger.infoLog('===================')
        print('')

    def __str__(self):
        return self.title
