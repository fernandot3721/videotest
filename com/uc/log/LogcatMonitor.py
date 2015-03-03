# encoding: utf-8
'''
Created on 2015-1-21

@author: Administrator
'''
import subprocess
import thread
import threading
import shlex
from com.uc.log.LogListener import LogListener
from com.uc.utils.TaskLogger import TaskLogger


class LogcatMonitor(threading.Thread):
    isStop = False
    logListener = LogListener()

    def __init__(self, threadID=1, name="logcat", counter=1):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.isRunning = True

    def isRunning(self):
        return self.isRunning

    def setLogListener(self, listener):
        self.logListener = listener

    def run(self):
        self.isRunning = True
        try:
            TaskLogger.infoLog("===========THREAD logcat start===========")
            # BrowserUtils.timeout_command("adb logcat -c", 10)
            # It won't work to clean log in the subprocess
            command = "adb shell su -c \"logcat\""
            popen = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, shell=False)
            while popen != None and popen.stdout is not None and popen.poll() == None:
                try:
                    line = popen.stdout.readline()
                    if self.logListener is not None:
                        self.logListener.onRead(line)
                    else:
                        TaskLogger.errorLog("ERROR: logcat monitor empty")
                        self.isStop = True
                    if self.isStop:
                        popen.terminate()
                except Exception as e:
                    TaskLogger.errorLog(e)
        except Exception as e1:
            TaskLogger.errorLog(e1)
        finally:
            TaskLogger.errorLog('===========THREAD logcat end===========')
            self.isRunning = False
            thread.exit_thread()

    def stop(self):
        self.isStop = True
