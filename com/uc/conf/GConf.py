#!/usr/bin/python
# coding=utf-8

import os
import sys
sys.path.append(os.getcwd())
import ConfigParser
import traceback


GLOBAL = None
CASE = None
URL = None


def inred(s):
    return"%s[1;31;40m%s%s[0m" % (chr(27), s, chr(27))


def initConfig():
    print('init config============')
    globalConfig()
    caseConfig()
    urlConfig()


def globalConfig(path=None):
    global GLOBAL
    if GLOBAL is None:
        GLOBAL = ConfigParser.ConfigParser()
        print('init GLOBAL')
    if path is None:
        path = 'confg.ini'  # default config
    print('globalConfig: %s' % path)
    GLOBAL.read(path)


def caseConfig(path=None):
    global CASE
    if CASE is None:
        CASE = ConfigParser.ConfigParser()
        print('init CASE')
    if path is None:
        path = 'confg.ini'  # default config
    print('globalConfig: %s' % path)
    CASE.read(path)


def urlConfig(path=None):
    global URL
    if URL is None:
        URL = ConfigParser.ConfigParser()
        print('init URL')
    if path is None:
        path = 'confg.ini'  # default config
    print('globalConfig: %s' % path)
    URL.read(path)


def getGlobal(conf):
    global GLOBAL
    if GLOBAL is None:
        print('GLOBAL not init, reutrn None')
        return None
    ret = None
    try:
        ret = GLOBAL.get('global', conf)
    except:
        print(inred('@@@@getGlobal %s failed' % conf))
    finally:
        return ret


def getGlobalInt(conf):
    global GLOBAL
    if GLOBAL is None:
        print('GLOBAL not init, reutrn None')
        return None
    ret = None
    try:
        ret = GLOBAL.getint('global', conf)
    except:
        print(inred('@@@@getGlobalInt %s failed' % conf))
    finally:
        return ret


def getCase(conf):
    if CASE is None:
        print('CASE not init, reutrn None')
        return None
    ret = None
    try:
        ret = CASE.get('case', conf)
    except:
        print(inred('@@@@get case %s failed' % conf))
    finally:
        return ret


def getCaseInt(conf):
    if CASE is None:
        print('CASE not init, reutrn None')
        return None
    ret = None
    try:
        ret = CASE.getint('case', conf)
    except:
        print(inred('@@@@getCaseInt %s failed' % conf))
    finally:
        return ret


def getUrl(conf):
    if URL is None:
        print('URL not init, reutrn None')
        return None
    ret = None
    try:
        ret = URL.get('url', conf)
    except:
        print(inred('@@@@getUrl %s failed' % conf))
    finally:
        return ret


def getUrlList():
    if URL is None:
        print(inred('@@@@URL not init, reutrn None'))
        return None
    ret = None
    try:
        ret = URL.options('url')
    except:
        print(inred('@@@@get url list failed'))
    finally:
        return ret


def getTaskList():
    if GLOBAL is None:
        print(inred('@@@@GLOBAL not init, return None'))
        return None
    ret = None
    try:
        ret = GLOBAL.options('task')
    except:
        print(inred('@@@@get task list failed'))
    finally:
        return ret


def getTaskConfig(conf):
    if GLOBAL is None:
        print(inred('@@@@GLOBAL not init, return None'))
        return None
    ret = None
    try:
        ret = GLOBAL.get('config', conf)
    except:
        print(inred('@@@@getTaskConf %s failed' % conf))
    finally:
        return ret
