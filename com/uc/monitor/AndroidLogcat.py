from com.uc.utils.TaskLogger import TaskLogger
from com.uc.monitor.LogMonitor import LogMonitor
from com.uc.conf import Conf

import shlex
import subprocess


class AndroidLogcat(LogMonitor):

    def __init__(self):
        super(AndroidLogcat, self).__init__()
        self.keywords = []
        self.keyevents = []
        self.startPlayKey = ''
        self.playerVerKey = ''
        pass

    def doMonitor(self):
        self.setName('AndroidLogcat')
        TaskLogger.\
            infoLog("===========THREAD %s start===========" % self.getName())
        command = "adb shell \"logcat\" -v time"
        popen = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, shell=False)
        while popen is not None and popen.stdout is not None and popen.poll() is None:
            try:
                line = popen.stdout.readline()
                self.onRead(line)
                if self.isStop:
                    popen.terminate()
            except Exception as e:
                TaskLogger.errorLog(e)
        pass

    def init(self):
        self.keywords = self.handler.getKeywords()
        self.keyevents = self.handler.getKeyevents()
        self.startPlayKey = Conf.START_PLAY_TAG
        self.playerVerKey = Conf.PLAYER_VERSION_TAG
        pass

    def onRead(self, line):
        if self.startPlayKey in line:
            self.handler.onVideoStartPlay()

        if self.playerVerKey[0] in line:
            version = self.\
                parseLogStr(line, self.playerVerKey[0], self.playerVerKey[1])
            self.handler.onPlayerVersion(version)

        for key in self.keywords:
            if key in line:
                value = self.parseLog(line, key, self.keywords[key])
                self.handler.onKeywordDetected(key, value)
                return

        for event in self.keyevents:
            if event in line:
                # parse time and key
                time = self.parseTime(line)
                self.handler.onEventDetected(event, time)
                return
        pass
