# encoding: utf-8
'''
Created on 2015年1月27日

@author: Administrator
'''

class DataStruct(object):
    '''
    classdocs
    '''
    dataCount = 0
    datalist = []
    
    def __init__(self, dataCount,dataDefoutValue=0):
        '''
        Constructor
        '''
        self.dataCount = dataCount
        self.datalist = [dataDefoutValue] *  dataCount
    
    def getDataCount(self):
        return self.dataCount;
    
    def get(self,index):
        if index >= 0 and index <  self.dataCount:
            return self.datalist[index]
    
    def set(self,index,value):
        if index >= 0 and index <  self.dataCount:
            self.datalist[index] = value
            
    def append(self,*value):
        index = 0
        for i in value:
            self.set(index, self.get(index) + i)
            index += 1
            
    