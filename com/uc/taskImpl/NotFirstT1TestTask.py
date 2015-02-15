# encoding: utf-8
from time import sleep

from com.uc.conf import Conf
from com.uc.html.AverageTemplate import AverageTemplate
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.html.DataStruct import DataStruct
from com.uc.utils.BrowserUtils import setCDParams


class NotFirstT1TestTask(AbstractVideoTask):
    repeatCount = 20
    urlList={
        '100_s':Conf.SEVER_ADDRESS + "t1_100k/test_NF_t1_short.html",
        '100_l':Conf.SEVER_ADDRESS + "t1_100k/test_NF_t1_long.html",
        '50_s':Conf.SEVER_ADDRESS  + "t1_100k/test_NF_t1_short.html",
        '50_l':Conf.SEVER_ADDRESS + "t1_50k/test_NF_t1_long.html"
         }
    def __init__(self):
        super(NotFirstT1TestTask, self).__init__()
        self.setTemplate(AverageTemplate())
        self.setValueCount(1)
        self.setTitle("非首次T1测试数据")
    
    def onVideoNotFirstT1(self, t1):
        if t1 <= 0:
            return
        self.getCurrentReultList().append(DataStruct(1,t1))
    
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
        while True:
            sleep(1)
            if self.hasComplatePlay is True:#视频播放完成之后，sleep60s，记录数据
                sleep(10)
                break
        
        BrowserUtils.openURIInCurrentWindow("http://www.baidu.com")
        
        sleep(Conf.WAIT_TIME)
        
        print u"关闭浏览器"
        BrowserUtils.closeBrowser()

