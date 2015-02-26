
import thread


class TaskData():

    def __init__(self):
        self.data = {}
        self.extra = {}
        self.cases = []
        self.lock = thread.allocate_lock()

    def getData(self, case):
        if case in self.data:
            return self.data[case]

    def getAllExtra(self):
        return self.extra

    def getExtra(self, key):
        return self.extra[key]

    def getCase(self):
        return self.cases

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

    def setData(self, case, values):
        self.lock.acquire()
        if case not in self.data:
            self.cases.append(case)
        self.data[case] = values
        self.lock.release()

    def printData(self):
        print ''
        print '=====TASK DATA====='
        print 'CASE:'
        for case in self.data:
            print 'NAME: %s, VALUE: %s' % (case, self.data[case])
        print 'EXTRA:'
        for extra in self.extra:
            print 'KEY: %s, VALUE: %s' % (extra, self.extra[extra])
        print '==================='
        print ''

    def __str__(self):
        return str(self.cases)
