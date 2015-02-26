#!/usr/bin/python
# coding=utf-8

'''
Created on 2015年1月22日

@author: Administrator
'''
import os

PACKAGE_NAME = 'com.UCMobile'
ACTIVITE_NAME = PACKAGE_NAME + '.main.UCMobile'
WAIT_TIME = 3
EXTTOOLS_PATH = os.getcwd() + os.sep + 'ext_tools'
SEVER_ADDRESS = "http://100.84.35.173:8080/"
URLLIST_PATH = os.getcwd() + os.sep + 'com' + os.sep + 'uc' + os.sep + 'conf'

REPORT_DIR = os.environ['HOME'] + os.sep + 'work' + os.sep + 'vr' + os.sep
LOOP_TIME = 50
PLAYER_COUNT = 2
PLAYER_LIB = ['/home/tangjp/work/vr/apolloso/2.8.8.888/',
				#'/home/tangjp/work/vr/apolloso/2.9.9.999/',
				#'/home/tangjp/work/vr/apolloso/2.8.8.888/',
				#'/home/tangjp/work/vr/apolloso/2.9.9.999/',
				'/home/tangjp/work/vr/apolloso/2.25/',
				]
DEBUG_LOG = 'true'
T1_FILTER = ['CutPeak', 'Average']
