
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

    def getExtra(self, case):
        if case in self.extra:
            return self.extra[case]

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

    def addExtra(self, case, key, value):
        self.lock.acquire()
        if case not in self.extra:
            self.extra[case] = []
        self.extra[case][key] = value
        self.lock.release()
