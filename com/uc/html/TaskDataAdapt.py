# encoding: utf-8
'''
Created on 2015-1-21

@author: Administrator
'''
from abc import abstractmethod

class TaskDataAdapt(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    @abstractmethod    
    def getKeys(self):
        pass
    @abstractmethod    
    def getDatas(self,key):
        pass
    @abstractmethod    
    def getCount(self):
        pass
    @abstractmethod    
    def getTitle(self):
        pass