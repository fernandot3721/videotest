# encoding: utf-8
'''
Created on 2015年1月22日

@author: Administrator
'''
from abc import abstractmethod

from com.uc.log.LogListener import LogListener
from com.uc.task.Filter import Filter


t1Keyword = "shell_t1="
coreT1KeyWorld="`tl="
t2Keyword = "shell_t2="
NFt1Keyword = "shell_nf_t1="
endKeyword = "shell_end_play"
playResultword = "ac_pl_re"
retcodeword = "retcode="

class VideoEventLogListener(LogListener):
    '''
    classdocs
    '''
    myfilter = Filter()
    
    def setFilter(self,myfilter):
        self.myfilter = myfilter
    
    def __init__(self):pass
    
    def onRead(self, lineStr):
        if t1Keyword in lineStr:
            t1Time = parseLog(lineStr, t1Keyword)#t1Keyword
            print "tl = ", t1Time
            self.onVideoStartPlay()
            self.onVideoFirstT1(t1Time)
            
        if coreT1KeyWorld in lineStr:
            t1Time = parseLog(lineStr, coreT1KeyWorld)#t1Keyword
            print "内核tl = ", t1Time
            self.onVideoFirstCoreT1(t1Time)
        
        if t2Keyword in lineStr:
            t2Time = parseLog(lineStr, t2Keyword)
            self.onVideoT2(t2Time)
            
        if NFt1Keyword in lineStr:
            NFt1Time =  parseLog(lineStr, NFt1Keyword)
            print u"非首次t1 = ", NFt1Time
            self.onVideoNotFirstT1(NFt1Time)
            
        if playResultword in lineStr:
            isSuccessful = parseLog(lineStr,retcodeword)
            print u"播放结果返回码=", isSuccessful
            self.onPlayResult(isSuccessful)
        
        if endKeyword in lineStr:
            self.onVideoEndPlay()
        
        
        if self.myfilter:
            if self.myfilter.match(lineStr):
                self.onInterested(lineStr);
            
    @abstractmethod
    def onVideoStartPlay(self):
        pass
    
    @abstractmethod
    def onVideoEndPlay(self):
        pass
    
    @abstractmethod
    def onVideoFirstCoreT1(self,t1):
        pass
    
    @abstractmethod
    def onVideoFirstT1(self,t1):
        pass
    
    @abstractmethod
    def onVideoNotFirstT1(self,t1):
        pass
    
    @abstractmethod
    def onVideoT2(self,t2):
        pass
    
    @abstractmethod
    def onPlayResult(self,retcode):
        pass
    
    @abstractmethod
    def onInterested(self,lineStr):
        pass

def parseLog(lineStr,prefix,suffix='`'):
    start = lineStr.find(prefix)
    if start >= 0:
        if len(suffix) > 0:
            end = lineStr.find(suffix,start + len(prefix))
        else:
            end = len(lineStr)
        result = float(lineStr[start + len(prefix):end].strip())
        return result
