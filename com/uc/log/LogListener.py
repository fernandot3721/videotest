'''
Created on 2015-1-21

@author: Administrator
'''
from abc import ABCMeta, abstractmethod

class  LogListener(object):
    @abstractmethod
    def onRead(self,lineStr):
        pass