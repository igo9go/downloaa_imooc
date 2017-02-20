# -*- coding: utf-8 -*-

import os
from conf import COURSEURL, CHOOSE
import conf
from filedeal import file_downloader
from spider import html_parser
from spider import html_downloader

'''

这个类是爬虫的主逻辑
'''

class SpiderMan(object):

    def __init__(self):
        self.downloader = html_downloader.Html_Downloader()#html下载器
        self.parser = html_parser.Html_Parser()#html解析器



    def crawl(self,url):
        '''

        :param url: 需要爬取的url
        :return:
        '''
        #下载好的html
        html_cont = self.downloader.download(url)
        #爬取到的视频数据信息
        self.res_datas = self.parser.parser(html_cont)



    def download(self,res_datas):
        '''

        :param res_datas: 视频数据信息列表
        :return:
        '''
        id = 0 #设置线程的id号，只是为了进度条显示的时候进行分类信息
        for res_data in res_datas:
            downloader = file_downloader.File_Downloader(res_data,id)#视频文件下载线程，给每个文件分配一个线程(有点偷懒了)
            id += 1
            conf.PERLIST.append(0)#百分比列表
            downloader.start()

    def cmdshow_gbk(self):
        print u'#####################################################################'
        print u"#慕课网视频抓取器"
        print u"author:七夜"
        print u"博客：http://blog.csdn.net/qiye_/和http://www.cnblogs.com/qiyeboy/ 同步更新 "
        print u"微信公众号:qiye_python"
        print u"github:https://github.com/qiyeboy/"
        print u"#到慕课网官网打开想要下载的课程的章节列表页面，查看当前url链接"
        print u"#例如http://www.imooc.com/learn/615，则课程编号为615"
        print u"#####################################################################"
        try:
            ID = raw_input(u'输入要下载的课程编号：'.encode('utf-8'))
            url = COURSEURL+str(ID)
            print u"将要下载的课程链接为:",url
            print u'开始解析视频,请稍后:'
            self.crawl(url)
            conf.PERSUM = len(self.res_datas)*100.0#总的进度
            print u'共有%d条视频'% len(self.res_datas)
            print u"课程名称:%s" % self.res_datas[0].subject
            for res_data in self.res_datas:
                print u"----->%s" % res_data.filename

            state = input(u'选择清晰度（1：超清UHD，2：高清HD，3：普清SD）：'.encode('utf-8'))
            if state not in [1,2,3]:
                print u'输入有误'
                return
            conf.STATE = CHOOSE[state-1]
            self.download(self.res_datas)

        except Exception ,e:
            print u'程序炸了',e
            return

    def prn_obj(obj):
        print '\n'.join(['%s:%s' % item for item in obj.__dict__.items()])




