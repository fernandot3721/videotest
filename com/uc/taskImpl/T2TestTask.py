# encoding: utf-8
from time import sleep

from com.uc.conf import Conf
from com.uc.html.AverageTemplate import AverageTemplate
from com.uc.log import VideoEventLogListener
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.task.Filter import Filter
from com.uc.utils import BrowserUtils
from com.uc.html.DataStruct import DataStruct
from com.uc.utils.BrowserUtils import setCDParams

class T2TestTask(AbstractVideoTask):
    urlList={
        '100_s':Conf.SEVER_ADDRESS + "t1_100k/test_video_short_h.html",
        '100_l':Conf.SEVER_ADDRESS + "t1_100k/test_video_short_h.html",
        '50_s':Conf.SEVER_ADDRESS + "t1_50k/test_video_short_h.html",
        '50_l':Conf.SEVER_ADDRESS + "t1_50k/test_video_long_h.html"
    }
    def __init__(self):
        super(T2TestTask, self).__init__()
        self.setTemplate(AverageTemplate())
        self.setValueCount(2)
        self.setTitle("T2测试数据")
        myfilter = Filter()
        myfilter.setKeyWorld('dl_spd=')
        
        self.setFilter(myfilter)
    
    def onVideoT2(self,t2):
        if t2 <= 0:
            return
        
        datas = self.getCurrentReultList()
        if self.getCurrentLoopIndex() >=  len(datas):
            data = DataStruct(2,0)
            datas.append(data)
        else:
            data = datas[self.getCurrentLoopIndex()]
        
        data.append(1,t2)
        
        print u'出现一次loading'
        print't2=',t2
    
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
        i = 0
        while True:
            sleep(1)
            i += 1
            if self.hasComplatePlay is True:
                break
        
        BrowserUtils.openURIInCurrentWindow("http://www.baidu.com")
        
        sleep(Conf.WAIT_TIME)
        
        print u"关闭浏览器"
        BrowserUtils.closeBrowser()
        
    def onInterested(self, lineStr):
        print '网速是',int(VideoEventLogListener.parseLog(lineStr,'dl_spd=')/1024)
