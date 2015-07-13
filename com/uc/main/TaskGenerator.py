# encoding: utf-8
from os.path import sys
from com.uc.monitor.AndroidLogcat import AndroidLogcat
from com.uc.monitor.AdbTimingMonitor import AdbTimingMonitor
from com.uc.utils.TaskLogger import TaskLogger
import traceback
import os
from com.uc.conf import GConf
from time import sleep
from com.uc.task.TaskManager import TaskManager
import importlib


class TaskGenerator:

    def __init__(self):
        self.taskList = GConf.getTaskList()
        self.taskObject = {}
        self.manager = None
        self.cdkeyList = []
        self.playerlibList = []
        pass

    def initConfig(self, path):
        GConf.initConfig()
        GConf.caseConfig(path)
        GConf.urlConfig(path)

    def configTask(self):
        for task in self.taskList:
            confPath = GConf.getTaskConfig(task)

            module = importlib.import_module("com.uc.taskImpl.%s" % key)
            taskClass = getattr(module, task)
            taskObject = taskClass()



