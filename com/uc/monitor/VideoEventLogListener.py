# encoding: utf-8
'''
Created on 2015年1月22日

@author: Administrator
'''
from abc import abstractmethod

from com.uc.monitor.LogListener import LogListener
from com.uc.task.Filter import Filter
from com.uc.utils.TaskLogger import TaskLogger


t1Keyword = "shell_t1="
coreT1KeyWorld = "`tl="
apolloT1KeyWorld = "mov_seg_dur T1 "
t2Keyword = "shell_t2="
NFt1Keyword = "shell_nf_t1="
endKeyword = "shell_end_play"
playResultword = "ac_pl_re"
retcodeword = "retcode="
apolloVersion = "[apollo"


class VideoEventLogListener(LogListener):
    '''
    classdocs
    '''
    myfilter = Filter()

    def setFilter(self, myfilter):
        self.myfilter = myfilter

    def onRead(self, lineStr):
        if t1Keyword in lineStr:
            t1Time = parseLog(lineStr, t1Keyword)
            TaskLogger.detailLog("tl = %s" % t1Time)
            self.onVideoStartPlay()
            self.onVideoFirstT1(t1Time)

        if coreT1KeyWorld in lineStr:
            t1Time = parseLog(lineStr, coreT1KeyWorld)
            TaskLogger.detailLog("CORE T1 = {}".format(t1Time))
            self.onVideoFirstCoreT1(t1Time)

        if apolloT1KeyWorld in lineStr:
            t1Time = parseLog(lineStr, apolloT1KeyWorld, 'ms')
            TaskLogger.detailLog("APOLLO T1 = {}".format(t1Time))
            self.onVideoStartPlay()
            self.onVideoFirstApolloT1(t1Time)

        if t2Keyword in lineStr:
            t2Time = parseLog(lineStr, t2Keyword)
            self.onVideoT2(t2Time)

        if NFt1Keyword in lineStr:
            NFt1Time = parseLog(lineStr, NFt1Keyword)
            TaskLogger.normalLog("NOT FIRST T1 = %s" % NFt1Time)
            self.onVideoNotFirstT1(NFt1Time)

        if playResultword in lineStr:
            isSuccessful = parseLog(lineStr, retcodeword)
            # TaskLogger.detailLog("播放结果返回码=" + str(isSuccessful))
            self.onPlayResult(isSuccessful)

        if endKeyword in lineStr:
            self.onVideoEndPlay()

        if apolloVersion in lineStr:
            version = parseLogStr(lineStr, apolloVersion, ']')
            self.onPlayerVersion(version)

        if self.myfilter:
            if self.myfilter.match(lineStr):
                self.onInterested(lineStr)

    @abstractmethod
    def onVideoStartPlay(self):
        pass

    @abstractmethod
    def onVideoEndPlay(self):
        pass

    @abstractmethod
    def onVideoFirstCoreT1(self, t1):
        pass

    @abstractmethod
    def onVideoFirstApolloT1(self, t1):
        pass

    @abstractmethod
    def onVideoFirstT1(self, t1):
        pass

    @abstractmethod
    def onVideoNotFirstT1(self, t1):
        pass

    @abstractmethod
    def onVideoT2(self, t2):
        pass

    @abstractmethod
    def onPlayResult(self, retcode):
        pass

    @abstractmethod
    def onPlayerVersion(self, version):
        pass

    @abstractmethod
    def onInterested(self, lineStr):
        pass

def parseLogStr(lineStr,prefix,suffix='`'):
    start = lineStr.find(prefix)
    if start >= 0:
        if len(suffix) > 0:
            end = lineStr.find(suffix,start + len(prefix))
        else:
            end = len(lineStr)
        result = lineStr[start + len(prefix):end].strip()
        return result

def parseLog(lineStr,prefix,suffix='`'):
    start = lineStr.find(prefix)
    if start >= 0:
        if len(suffix) > 0:
            end = lineStr.find(suffix,start + len(prefix))
        else:
            end = len(lineStr)
        result = float(lineStr[start + len(prefix):end].strip())
        return result