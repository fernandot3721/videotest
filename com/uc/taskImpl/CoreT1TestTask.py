# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.html.AverageTemplate import AverageTemplate
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.html.DataStruct import DataStruct
from com.uc.utils.BrowserUtils import setCDParams


class CoreT1TestTask(AbstractVideoTask):
    urlList={
        '50_l':Conf.SEVER_ADDRESS + "t1_50k/test_video_long.html",
        '50_s':Conf.SEVER_ADDRESS + "t1_50k/test_video_short.html",
        '100_l':Conf.SEVER_ADDRESS + "t1_100k/test_video_long.html",
        '100_s':Conf.SEVER_ADDRESS + "t1_100k/test_video_short.html",
        '200_l':Conf.SEVER_ADDRESS + "t1_200k/test_video_long.html",
        '200_s':Conf.SEVER_ADDRESS + "t1_200k/test_video_short.html",
    }
    def __init__(self):
        super(CoreT1TestTask, self).__init__()
        #设置过滤器
        self.setTemplate(AverageTemplate())
        self.setValueCount(1)
        self.setTitle("内核T1测试数据")
        
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
            if self.hasStartPlay is True or myloop > 15:
                break
            myloop += 1
            
        BrowserUtils.openURIInCurrentWindow("http://www.baidu.com")
        
        sleep(Conf.WAIT_TIME)
        
        print u"关闭浏览器"
        BrowserUtils.closeBrowser()
        
    def onVideoFirstCoreT1(self, t1):
        if t1 <= 0:
            return
        self.getCurrentReultList().append(DataStruct(1,t1))
