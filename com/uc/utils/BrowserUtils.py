# encoding: utf-8

'''启动浏览器'''


import os

from com.uc.conf import Conf
import xlrd


def launchBrowser():
    launchCmd = "adb shell am start -a android.intent.action.VIEW -n {}/{} -d {} -e policy UCM_ONE_WINDOW".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME, "http://www.baidu.com")
    mySystem(launchCmd)

'''设置本地参数'''
def setCDParams( key=None, value=None):
    if (not key) or (not value):
        return
    
    extToolsPath = Conf.EXTTOOLS_PATH
    confPath = os.path.abspath("./confg.ini")
    jarPath = os.path.abspath(extToolsPath + "/editCDout.jar")
    paramStr = key+'='+value
    print '设置本地参数: ' + paramStr
    f1 = open(confPath,'w')
    f1.write(paramStr)
    f1.close()
    
    mvOutCmd = "adb shell su -c \"cat data/data/{}/user/us/zh-cn/ucparam.ucmd2 > sdcard/UCDownloads/ucparam.ucmd2\"".format(Conf.PACKAGE_NAME)
    pullOutCmd = "adb pull sdcard/UCDownloads/ucparam.ucmd2"
    execCmd = "java -jar {}".format(jarPath)
    pushInCmd = "adb push ucparam.ucmd2 sdcard/UCDownloads/"
    mvInCmd = "adb shell su -c \"cat sdcard/UCDownloads/ucparam.ucmd2 > data/data/{}/user/us/zh-cn/ucparam.ucmd2\"".format(Conf.PACKAGE_NAME)
    powerCmd = "adb shell su -c \"chmod 777 data/data/com.UCMobile/user/us/zh-cn/ucparam.ucmd2\""
    os.system(mvOutCmd)
    os.system(pullOutCmd)
    os.system(execCmd)
    os.system(pushInCmd)
    os.system(mvInCmd)
    os.system(powerCmd)

'''清理视频缓存'''
def clearVideoCache():
    clearCmd = "adb shell am start -n {}/{} -e clear_video_cache 1".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME)
    mySystem(clearCmd)

'''清理浏览器所有缓存'''
def clearBrowserCache():
    clearCmd = "adb shell su -c \"pm clear {}\"".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME)
    mySystem(clearCmd)

'''打开页面'''
def openURI(url):
    launchCmd = "adb shell am start -a android.intent.action.VIEW -n {}/{} -d {}".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME, url)
    mySystem(launchCmd)

'''打开页面'''
def openURIInCurrentWindow(url):
    cmd = "adb shell am start -n {}/{} -e open_url_in_current_window {}".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME,url)
    mySystem(cmd)

'''打开页面'''
def fresh():
    refreshCmd = "adb shell am start -n {}/{} -e refresh_current_page 1".format(Conf.PACKAGE_NAME, Conf.ACTIVITE_NAME)
    mySystem(refreshCmd)
    
def goback():
    backCmd = "adb shell input keyevent 4"
    mySystem(backCmd)

'''关闭浏览器'''
def closeBrowser():
    exitCmd = "adb shell am force-stop {}".format(Conf.PACKAGE_NAME)
    print exitCmd
    mySystem(exitCmd)
    
    
def mySystem(command):
    while True:
        result = timeout_command(command,2)
        print result
        if 'Activity not started' in result :
            pass
        else:
            break
     
def timeout_command(command, timeout):
    """call shell-command and either return its output or kill it
    if it doesn't normally exit within timeout seconds and return None"""
    import subprocess, datetime, time
    start = datetime.datetime.now()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=False)
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds> timeout:
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
