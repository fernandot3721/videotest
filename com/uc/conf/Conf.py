#!/usr/bin/python
# coding=utf-8

'''
Created on 2015年1月22日

@author: Administrator
'''
import os

PACKAGE_NAME = 'com.UCMobile.apollo'
ACTIVITE_NAME = 'com.UCMobile.main.UCMobile'
WAIT_TIME = 15
EXTTOOLS_PATH = os.getcwd() + os.sep + 'ext_tools'
# SEVER_ADDRESS = "http://100.84.35.173:8080/"
SEVER_ADDRESS = "http://192.168.0.4/"
URLLIST_PATH = os.getcwd() + os.sep + 'com' + os.sep + 'uc' + os.sep + 'conf'

# REPORT_DIR = os.environ['HOME'] + os.sep + 'work' + os.sep + 'vr' + os.sep
DATA_DIR = '/opt/lampp/htdocs/videotest/origin/'
REPORT_DIR = '/opt/lampp/htdocs/videotest/'
HTML_TEMPLATE = os.getcwd() + os.sep + 'template' + os.sep + 'tableTemplate.html'
LOOP_TIME = 1
LOOP_TIME_T1 = 50
LOOP_TIME_T2 = 1
LOOP_TIME_T2_M = 1
PLAYER_COUNT = 2
PLAYER_LIB = [
                '/home/tangjp/work/vr/apolloso/3.3.3.333/',
                '/home/tangjp/work/vr/apolloso/2.2.1.137/',
                '/home/tangjp/work/vr/apolloso/2.2.0.129/',
                '/home/tangjp/work/vr/apolloso/2.2.0.128/',
                '/home/tangjp/work/vr/apolloso/2.0.0.122/',
                '/home/tangjp/work/vr/apolloso/1.0.0.117/',
                '/home/tangjp/work/vr/apolloso/2.8.8.888/',
                '/home/tangjp/work/vr/apolloso/2.25/',
                ]
CD_COUNT = 1
CD_PARAM = [
            'mov_seg_dur=0',
            # 'mov_seg_dur=10',
            # 'mov_seg_dur=20',
            # 'mov_seg_dur=30',
            # 'mov_seg_dur=40',
            # 'mov_seg_dur=60',
            # 'mov_seg_dur=80',
            ]
DEBUG_LOG = True
INFO_LOG = True
DETAIL_LOG = True
ERROR_LOG = True
NORMAL_LOG = True
FILE_LOG = True
HARDCODE_APOLLO = True
TASK_LOG_PATH = '/opt/lampp/htdocs/videotest/log/'
# LOGGER_LEVEL = DEBUG_LOG
TASK_TYPE = ['CORE-T1', 'APOLLO_T1', 'MEMEROY', 'APOLLO_T2', 'APOLLO_T2_MEM']
FILTERS = {
    'CORE-T1': ['Count', 'CutPeak', 'Average'],
    'APOLLO_T1': ['Count', 'Normalize'],
    'MEMEROY': ['Average'],
    'APOLLO_T2': ['Count', 'Average'],
    'APOLLO_T2_MEM': ['Count'], 
    }

CORE_T1_URL= {#'50_l': SEVER_ADDRESS + "t1_50k/test_video_long.html",
        # '50_s': SEVER_ADDRESS + "t1_50k/test_video_short.html",
        '100_l': SEVER_ADDRESS + "t1_100k/test_video_long.html",
        '100_s': SEVER_ADDRESS + "t1_100k/test_video_short.html",
        # '200_l': SEVER_ADDRESS + "t1_200k/test_video_long.html",
        # '200_s': SEVER_ADDRESS + "t1_200k/test_video_short.html",
    }

APOLLO_T1_URL= {
        'ol-mp4-normal': SEVER_ADDRESS + "t1Test/mp4/t1Test_normal.html",
        'ol-mp4-normal-200': SEVER_ADDRESS + "t1Test_200k/mp4/t1Test_normal.html",
        'ol-mp4-hd-smoov': SEVER_ADDRESS + "t1Test/mp4/t1Test_1203Kbps.html",
        'ol-mp4-hd-smoov-200': SEVER_ADDRESS + "t1Test_200k/mp4/t1Test_1203Kbps.html",
        'ol-mp4-hd-bmoov': SEVER_ADDRESS + 't1Test/mp4/1280_720_1019Kbps_4053979.html',
        'ol-mp4-hd-bmoov-200': SEVER_ADDRESS + 't1Test_200k/mp4/1280_720_1019Kbps_4053979.html',
        'ol-m3u8-hd': SEVER_ADDRESS + 't1Test/m3u8/m3u8_super.html',
        'ol-m3u8-hd-200': SEVER_ADDRESS + 't1Test_200k/m3u8/m3u8_super.html',
    }

APOLLO_T2_URL= {
        # 'movie': SEVER_ADDRESS + "t1Test/mp4/t1Test_2577Kbps.html",
        # 'tv': SEVER_ADDRESS + "t1Test/mp4/t1Test_1203Kbps.html",
        'hd_online_': SEVER_ADDRESS + "/t1Test/m3u8/m3u8_high.html",
        'movie_200': SEVER_ADDRESS + "t1Test_200k/mp4/t1Test_2577Kbps.html",
        'tv_200': SEVER_ADDRESS + "t1Test_200k/mp4/t1Test_1203Kbps.html",
        # 'movie_new': SEVER_ADDRESS + 't1Test/mp4/t1Test_850_480_720Kbps.html',
        # 'movie_new_200': SEVER_ADDRESS + 't1Test_200k/mp4/t1Test_850_480_720Kbps.html',
    }

APOLLO_T2_M_URL= {
        'ol-mp4-normal': SEVER_ADDRESS + "t1Test_200k/mp4/t1Test_normal.html",
        'ol-mp4-hd': SEVER_ADDRESS + "t1Test/mp4/t1Test_2577Kbps.html",
        'ol-mp4-hd-200': SEVER_ADDRESS + "t1Test_200k/mp4/t1Test_2577Kbps.html",
        'ol-m3u8-hd': SEVER_ADDRESS + "t1Test/m3u8/m3u8_super.html",
        'ol-m3u8-hd-200': SEVER_ADDRESS + "t1Test_200k/m3u8/m3u8_super.html",
        'movie_new': SEVER_ADDRESS + 't1Test/mp4/t1Test_850_480_720Kbps.html',
        'movie_new_200': SEVER_ADDRESS + 't1Test_200k/mp4/t1Test_850_480_720Kbps.html',
    }

MEMEROY_URL= {
        # 'normal': SEVER_ADDRESS + "t1Test/mp4/t1Test_2577Kbps.html",
        'hd_online_': "http://192.168.0.4/t1Test/m3u8/m3u8_high.html",
        'hd_local_': "file:///sdcard/test.mp4",
        'st_online_': "http://192.168.0.4/t1Test/mp4/t1Test_normal.html",
    }

START_PLAY_TAG = 'mov_seg_dur T1'
PLAYER_VERSION_TAG = ('[apollo', ']')
CORE_T1_KEYWORD = {
        '`tl=': 'ms',
        }
APOLLO_T1_KEYWORD = {
        'mov_seg_dur T1 ': 'ms',
        }
MEMORY_KEYWORD = {
        'MemFree:': 'kB',
        }
APOLLO_T2_KEYEVENT = {
        't1': '>>> nativeCreateInstance',
        'seek': 'jni nativeSeekTo',
        't2': 'MediaPlayerInstance::onBufferingStateUpdate() 1',
        'play': 'play(). isPlaying = 0',
        }
