# encoding: utf-8

'''启动浏览器'''


import os

from com.uc.conf import Conf
import xlrd
import shlex
from com.uc.utils.TaskLogger import TaskLogger
import subprocess
import datetime
import time


def launchBrowser():
    # launchCmd = "adb shell am start -a android.intent.action.VIEW -n {}/{} -d {} -e policy UCM_ONE_WINDOW".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME, "http://www.baidu.com")
    launchCmd = "adb shell am start -n {}/{}".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME)
    # TaskLogger.errorLog(launchCmd)
    mySystem(launchCmd)


def setCDParams(key=None, value=None):
    '''设置本地参数'''
    if (not key) or (not value):
        return

    extToolsPath = Conf.EXTTOOLS_PATH
    confPath = os.path.abspath("./confg.ini")
    jarPath = os.path.abspath(extToolsPath + "/editCDout.jar")
    paramStr = key+'='+value
    TaskLogger.normalLog('SET CDPARAM: %s' % paramStr)
    f1 = open(confPath, 'w')
    f1.write(paramStr)
    f1.close()

    mvOutCmd = "adb shell su -c \"cat /data/data/{}/user/us/zh-cn/ucparam.ucmd2 > sdcard/UCDownloads/ucparam.ucmd2\"".format(Conf.PACKAGE_NAME)
    pullOutCmd = "adb pull sdcard/UCDownloads/ucparam.ucmd2"
    execCmd = "java -jar {}".format(jarPath)
    pushInCmd = "adb push ucparam.ucmd2 sdcard/UCDownloads/"
    mvInCmd = "adb shell su -c \"cat sdcard/UCDownloads/ucparam.ucmd2 > /data/data/{}/user/us/zh-cn/ucparam.ucmd2\"".format(Conf.PACKAGE_NAME)
    powerCmd = "adb shell su -c \"chmod 777 /data/data/com.UCMobile/user/us/zh-cn/ucparam.ucmd2\""
    os.system(mvOutCmd)
    os.system(pullOutCmd)
    os.system(execCmd)
    os.system(pushInCmd)
    os.system(mvInCmd)
    os.system(powerCmd)


def clearVideoCache():
    '''清理视频缓存'''
    clearCmd = "adb shell am start -n {}/{} -e clear_video_cache 1".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME)
    mySystem(clearCmd)


def clearBrowserCache():
    '''清理浏览器所有缓存'''
    clearCmd = "adb shell \"pm clear {}\"".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME)
    mySystem(clearCmd)


def openURI(url):
    '''打开页面'''
    launchCmd = "adb shell am start -a android.intent.action.VIEW -n {}/{} -d {}".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME, url)
    mySystem(launchCmd)


def openURIInCurrentWindow(url):
    '''打开页面'''
    cmd = "adb shell am start -n {}/{} -e open_url_in_current_window {}".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME,url)
    mySystem(cmd)


def fresh():
    '''打开页面'''
    refreshCmd = "adb shell am start -n {}/{} -e click refresh".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME)
    mySystem(refreshCmd)


def goback():
    backCmd = "adb shell input keyevent 4"
    mySystem(backCmd)


def closeBrowser():
    '''关闭浏览器'''
    exitCmd = "adb shell am force-stop {}".format(Conf.PACKAGE_NAME)
    # TaskLogger.normalLog(exitCmd)
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
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=False)
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            process.terminate()
    return process.stdout.read()


def readExcelToUrlist(file_path):
    urllist = {}
    key = ""
    value = ""
    data = xlrd.open_workbook(file_path)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    for i in range(nrows):
        """adb 对&会特殊处理，需要转义"""
        key = str(table.row_values(i)[0]).replace("&", "\&")
        value = str(table.row_values(i)[1]).replace("&", "\&")
        urllist[key] = value
    return urllist
