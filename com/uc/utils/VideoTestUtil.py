# encoding: utf-8

from com.uc.conf import GConf
import shlex
from com.uc.utils.TaskLogger import TaskLogger
import subprocess
import datetime
import time


def launchBrowser():
    launchCmd = "adb shell am start -n com.example.videoviewtest/.MainActivity"
    mySystem(launchCmd)


def clearBrowserCache():
    '''清理浏览器所有缓存'''
    clearCmd = "adb shell \"pm clear com.example.videoviewtest\""
    mySystem(clearCmd)


def openURI(url):
    '''打开页面'''
    launchCmd = "adb shell am start -n com.example.videoviewtest/.MainActivity -d %s" % url
    mySystem(launchCmd)


def closeBrowser():
    '''关闭浏览器'''
    exitCmd = "adb shell am force-stop com.example.videoviewtest"
    mySystem(exitCmd)


def mySystem(command):
    while True:
        result = timeout_command(command, 2)
        TaskLogger.normalLog(result)
        if 'Activity not started' in result:
            pass
        else:
            break


def timeout_command(command, timeout):
    """call shell-command and either return its output or kill it
    if it doesn't normally exit within timeout seconds and return None"""

    start = datetime.datetime.now()
    process = \
        subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=False)
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            process.terminate()
    return process.stdout.read()
