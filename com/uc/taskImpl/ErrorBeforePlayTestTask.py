# encoding: utf-8

from time import sleep
import os

from com.uc.conf import Conf
from com.uc.html.AverageTemplate import AverageTemplate
from com.uc.html.ScaleTemplate import ScaleTemplate
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.html.DataStruct import DataStruct
from com.uc.utils.BrowserUtils import setCDParams
from com.uc.utils.BrowserUtils import readExcelToUrlist

class ErrorBeforePlayTestTask(AbstractVideoTask):
    repeatCount = 2
    file_path = Conf.URLLIST_PATH + os.sep + "urllist.xls"
    urlList = readExcelToUrlist(file_path)
#     urlList = {
#         'g1':"http://10.1.35.173:8080/t1_50k/test_video_long.html",
#         'b1':"http://uctest.ucweb.com:81/dengzd/video/bad_format.html",
#         'g2':"http://www.baidu.com" 
#                }
    def __init__(self):
        super(ErrorBeforePlayTestTask, self).__init__()
        #设置过滤器
        self.setTemplate(ScaleTemplate())
        self.setValueCount(1)
        self.setTitle("播放前出错数据")
        
    def doTest(self):

        setCDParams(self.cdkey,self.cdvalue)
        
        print u"打开浏览器"
        BrowserUtils.launchBrowser()
        
        sleep(Conf.WAIT_TIME)
        
        print u"清空历史"
        BrowserUtils.clearVideoCache()
        
        print u"打开视频"
        BrowserUtils.openURI(self.urlList[self.currentCategory])
        
        #等待视频播起来
        myloop = 0
        while True:
            sleep(1)
            if self.hasStartPlay is True:
                break
            elif myloop > 40 :
                self.onPlayResult(2)
                break
            myloop += 1
         
        BrowserUtils.openURIInCurrentWindow("http://www.baidu.com")
        
        sleep(Conf.WAIT_TIME)
        
        print u"关闭浏览器"
        BrowserUtils.closeBrowser()
        
    def onPlayResult(self, retcode):
        if retcode < 0:
            return
        self.getCurrentReultList().append(DataStruct(1,retcode))
