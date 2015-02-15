# encoding: utf-8
'''
Created on 2015-1-21

@author: Administrator
'''
from os.path import os, sys
from signal import SIGTERM
import subprocess
import thread
import threading
from time import sleep

from com.uc.log.LogListener import LogListener
from com.uc.utils import BrowserUtils


class  LogcatMonitor (threading.Thread):
    isStop = False
    logListener = LogListener()
    
    def __init__(self, threadID=1, name="logcat", counter=1):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def setLogListener(self,listener):
        self.logListener = listener
           
    def run(self):
        try:
            print u"开启监听器"
            print BrowserUtils.timeout_command("adb logcat -c", 3)
            popen = subprocess.Popen(args="adb shell su -c \"logcat\"", stdout=subprocess.PIPE, shell=False)
            while popen != None and popen.stdout is not None and popen.poll() == None:
                try:
                    line = popen.stdout.readline()
                    if self.logListener is not None:
                        self.logListener.onRead(line)
                    else:
                        print u"没有正确设置logcat监听器，程序退出"
                        isStop = true
                    if self.isStop:
                        popen.terminate()
                except Exception as e:
                    print e
        finally:
            print 'logcat 线程退出!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
            thread.exit_thread()
    
    def stop(self):
        self.isStop = True
