#!/usr/bin/python
# coding=utf-8

'''
Created on 2015年1月22日

@author: Administrator
''' 
import os

PACKAGE_NAME = 'com.UCMobile'
ACTIVITE_NAME = PACKAGE_NAME +'.main.UCMobile'
WAIT_TIME = 3
EXTTOOLS_PATH = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "/ext_tools")
SEVER_ADDRESS = "http://100.84.35.173:8080/"
#"http://10.1.93.169/"
URLLIST_PATH = os.path.dirname(os.path.dirname(__file__) + "/conf")

LOOP_TIME = 5