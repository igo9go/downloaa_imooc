#coding:utf-8
#全局变量
import threading

DOWNLOAD_URL = 'http://www.imooc.com/course/ajaxmediainfo/?mid={}&mode=flash'#下载链接
COURSEURL = "http://www.imooc.com/learn/"#课程链接
#COURSEURL = "http://coding.imooc.com/learn/list/74.html"

CHOOSE=['H','M','L']#视频品质

STATE='L'#视频默认品质

LOCK = threading.Lock()#线程锁

INFOR = {'L':u'普清','M':u'高清','H':u'超清'}#视频品质描述

PERSUM=0.0#用于描述总进度

PERLIST=[]#记录每个线程的进度