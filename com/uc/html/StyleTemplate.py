'''
Created on 2015-1-21

@author: Administrator
'''
from abc import ABCMeta, abstractmethod
from com.uc.html.TaskDataAdapt import TaskDataAdapt

class StyleTemplate(object):
    '''
    classdocs
    '''
    taskDataAdapt = TaskDataAdapt
    
    def __init__(self):
        '''
        Constructor
        '''
    def setTaskDataAdapter(self,taskDataAdapt):
        self.taskDataAdapt = taskDataAdapt
        pass
    
    @abstractmethod
    def createReportb(self):
        return ""