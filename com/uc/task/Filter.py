'''
Created on 2015-1-22

@author: Administrator
'''

class Filter(object):
    '''
    classdocs
    '''
    keyword = ""
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def match(self,lineStr):
        if self.keyword in lineStr:
            return True
        else:
            return False
        
    def setKeyWorld(self,keyword):
        self.keyword = keyword