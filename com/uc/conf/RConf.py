# import ConfigParser

# config = ConfigParser.ConfigParser()
# cfile = open('com/uc/conf/default.ini', 'rb')

# config.readfp(cfile)
# packageName = config.get("event", "play")
# print packageName

# testlist = config.get('list', 'tl')
# print testlist

# ret = testlist.splitlines()
# print ret

# from com.uc.conf import GConf
import os
import sys
sys.path.append(os.getcwd())
import GConf

# config = ConfigParser.ConfigParser()
# config.read('com/uc/conf/default.ini')
# print config.sections()
# print config.items('list')
# print config.options('list')
# hello1 = config.get('global', 'REPORT_DIR')
# print hello1

# GConf.globalConfig('com/uc/conf/default.ini')
# hello = GConf.getGlobal('REPORT_DIR')
# print hello


import importlib

# from com.uc.utils.TaskLogger import TaskLogger

GConf.initConfig()
key = GConf.getCase('TASK_NAME')
module = importlib.import_module("com.uc.taskImpl.%s" % key)
filterClass = getattr(module, key)
filterObject = filterClass()

print(filterObject)
