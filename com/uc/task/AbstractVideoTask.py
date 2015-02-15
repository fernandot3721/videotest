# encoding: utf-8
from abc import ABCMeta, abstractmethod

from com.uc.conf import Conf
from com.uc.html.DataStruct import DataStruct
from com.uc.html.HtmlNode import HtmlNode
from com.uc.html.StyleTemplate import StyleTemplate
from com.uc.html.TaskDataAdapt import TaskDataAdapt
from com.uc.log.VideoEventLogListener import VideoEventLogListener


__author__ = 'Administrator'

class AbstractVideoTask(HtmlNode,TaskDataAdapt,VideoEventLogListener):
    
    def setValueCount(self,count):
        self.valueCount = count
    
    def getCurrentReultList(self):
        return self.keyValue.get(self.currentCategory)
    
    def setTitle(self,titleStr):
        self.title = titleStr
        
    def __init__(self):
        self.template = StyleTemplate()
        self.loopCount = Conf.LOOP_TIME
        self.currentLoopIndex = 0
        self.hasComplatePlay = False
        self.hasStartPlay = False
        self.valueCount = 0
        self.currentCategory = ""
        self.currentCategoryIndex = 0
        self.title = ""
        self.keyValue = {}
        self.cdkey = ""
        self.cdvalue = ""
        
    def setTemplate(self,template):
        self.template = template
        self.template.setTaskDataAdapter(self)
        
    def initTest(self,i):
        ##每次测试之前做一下初始化
        self.hasComplatePlay = False
        self.hasStartPlay = False
        self.currentCategoryIndex = i
        self.currentCategory = self.urlList.keys()[i] 
         
    def dataInit(self):
        for key in self.urlList.keys():
            self.keyValue[key] = []
                
    def run(self):
        self.dataInit()
        print self.getTitle(),u"测试开始"
        for i in range(0,self.loopCount):
            self.currentLoopIndex = i
            for j in range(0,len(self.urlList)):
                print "loopIndex:"+str(i)
                print "case"+str(j)+" is running"
                self.initTest(j)
                self.doTest()
                
    @abstractmethod
    def doTest(self):
        pass
    
    def createHtmlCode(self):
        if self.template:
            return self.template.createReportb()
        
    def setLoopCount(self,loopCount):
        self.loopCount = loopCount
        
    def getCurrentLoopIndex(self):
        return self.currentLoopIndex
    
    def onVideoEndPlay(self):
        self.hasComplatePlay = True
    
    def onVideoStartPlay(self): 
        self.hasStartPlay = True
    
    def getDatas(self,key):
        return self.keyValue.get(key)
    
    def getCount(self):
        return len(self.keyValue)
    
    def getKeys(self):
        return self.keyValue.keys()
    
    def getTitle(self):
        return self.title
    
    def setCD(self,key,value):
        self.cdkey = key
        self.cdvalue = value
    