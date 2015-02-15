# encoding: utf-8
from os.path import sys
import thread
import threading

from com.uc.html.HtmlBuilder import HtmlBuilder
from com.uc.log.LogcatMonitor import LogcatMonitor


__author__ = 'Administrator'
class TaskManager:
    taskList = []
    builder = HtmlBuilder()
    monitorThread = LogcatMonitor()
    htmlBuilder = HtmlBuilder()
    
    def __init__(self):
        self.monitorThread.start()
        pass
    def addTask(self,task):
        self.taskList.append(task)
        self.htmlBuilder.addNode(task)
        pass
    
    def startTest(self):
        try:
            print u"环境初始化..."

            print u"执行测试案例..."
            for task in self.taskList:
                self.monitorThread.setLogListener(task)
                self.monitorThread.setLogEventListener(task)
                task.run()
                
            print u"生成报表..."
            htmlcode = self.htmlBuilder.generatingRepors()
            
            f1 = open('C:\\Users\\Administrator\\Desktop\\report.html','w')
            f1.write(htmlcode)
            f1.close()
                
            return 0
        except:
            print "Unexpected error:", sys.exc_info()
            return -1
    def stopTest(self):
        self.monitorThread.stop()
        self.monitorThread.join()
