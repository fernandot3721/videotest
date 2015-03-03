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
SEVER_ADDRESS = "http://100.84.44.238/videocase/"
URLLIST_PATH = os.getcwd() + os.sep + 'com' + os.sep + 'uc' + os.sep + 'conf'

# REPORT_DIR = os.environ['HOME'] + os.sep + 'work' + os.sep + 'vr' + os.sep
DATA_DIR = '/opt/lampp/htdocs/videotest/origin/'
REPORT_DIR = '/opt/lampp/htdocs/videotest/'
HTML_TEMPLATE = os.getcwd() + os.sep + 'template' + os.sep + 'tableTemplate.html'
LOOP_TIME = 1
PLAYER_COUNT = 1
PLAYER_LIB = [
                '/home/tangjp/work/vr/apolloso/2.2.0/',
                '/home/tangjp/work/vr/apolloso/2.8.8.888/',
                '/home/tangjp/work/vr/apolloso/2.25/',
                ]
CD_COUNT = 3
CD_PARAM = [
#'mov_seg_dur=0',
#'mov_seg_dur=10',
#'mov_seg_dur=20',
#'mov_seg_dur=30',
            'mov_seg_dur=40',
            'mov_seg_dur=60',
            'mov_seg_dur=80',
            ]
DEBUG_LOG = 'true'
INFO_LOG = 'true'
DETAIL_LOG = 'true'
ERROR_LOG = 'true'
NORMAL_LOG = 'true'
TASK_LOG_PATH = '/opt/lampp/htdocs/videotest/log/'
# LOGGER_LEVEL = DEBUG_LOG
TASK_TYPE = ['CORE-T1']
FILTERS = {'CORE-T1': ['Count', 'CutPeak', 'Average']}

CORE_T1_URL= {#'50_l': SEVER_ADDRESS + "t1_50k/test_video_long.html",
        # '50_s': SEVER_ADDRESS + "t1_50k/test_video_short.html",
        '100_l': SEVER_ADDRESS + "t1_100k/test_video_long.html",
        '100_s': SEVER_ADDRESS + "t1_100k/test_video_short.html",
        # '200_l': SEVER_ADDRESS + "t1_200k/test_video_long.html",
        # '200_s': SEVER_ADDRESS + "t1_200k/test_video_short.html",
    }

APOLLO_T1_URL= {
        'movie': SEVER_ADDRESS + "t1Test/mp4/t1Test_2577Kbps.html",
        'tv': SEVER_ADDRESS + "t1Test/mp4/t1Test_1203Kbps.html",
        'movie_200': SEVER_ADDRESS + "t1Test_200k/mp4/t1Test_2577Kbps.html",
        'tv_200': SEVER_ADDRESS + "t1Test_200k/mp4/t1Test_1203Kbps.html",
        'movie_new': SEVER_ADDRESS + 't1Test/mp4/t1Test_850_480_720Kbps.html'
        'movie_new_200': SEVER_ADDRESS + 't1Test_200k/mp4/t1Test_850_480_720Kbps.html'
    }
