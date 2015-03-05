from com.uc.utils.TaskLogger import TaskLogger
from com.uc.log.LogMonitor import LogMonitor
from com.uc.conf import Conf

import shlex
import subprocess


class AndroidLogcat(LogMonitor):

    def __init__(self):
        super(AndroidLogcat, self).__init__()
        self.keywords = ''
        self.startPlayKey = ''
        self.playerVerKey = ''
        pass

    def doMonitor(self):
        self.setName('AndroidLogcat')
        TaskLogger.\
            infoLog("===========THREAD %s start===========" % self.getName())
        command = "adb shell su -c \"logcat\""
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
        self.startPlayKey = Conf.START_PLAY_TAG
        self.playerVerKey = Conf.PLAYER_VERSION_TAG
        pass

    def onRead(self, line):
        if len(self.startPlayKey) > 0:
            for key in self.startPlayKey:
                if key in line:
                    self.handler.onVideoStartPlay()
        if len(self.playerVerKey) > 0:
            for key in self.playerVerKey:
                if key in line:
                    version = \
                        self.parseLogStr(line, key, self.playerVerKey[key])
                    self.handler.onPlayerVersion(version)
        for key in self.keywords:
            if key in line:
                value = self.parseLog(line, key, self.keywords[key])
                self.handler.onKeywordDetected(key, value)
        pass

    def parseLog(self, lineStr, prefix, suffix):
        start = lineStr.find(prefix)
        if start >= 0:
            if len(suffix) > 0:
                end = lineStr.find(suffix, start + len(prefix))
            else:
                end = len(lineStr)
            result = float(lineStr[start + len(prefix):end].strip())
            return result

    def parseLogStr(self, lineStr, prefix, suffix):
        start = lineStr.find(prefix)
        if start >= 0:
            if len(suffix) > 0:
                end = lineStr.find(suffix, start + len(prefix))
            else:
                end = len(lineStr)
            result = lineStr[start + len(prefix):end].strip()
            return result
