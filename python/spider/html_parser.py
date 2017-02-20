#coding:utf-8
import re
import urlparse
from bs4 import BeautifulSoup
from conf import DOWNLOAD_URL
from entity.fileinfor import FileInfor
from spider.html_downloader import Html_Downloader


class Html_Parser(object):
    '''
    html解析器:从中提取出视频信息
    '''
    def __init__(self):
        self.res_data=[]#用来存放视频信息


    def parser(self, html_cont):
        '''

        :param html_cont: html内容
        :return:
        '''
        if html_cont is None:
            return
        # 使用BeautifulSoup模块对html进行解析
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')#str ='<div class="hd"><h2 class="l">Hibernate注解</h2></div>'
        subject = soup.find('div',class_ = "hd").get_text()
        links = soup.find_all('a',class_='J-media-item')
        html_down = Html_Downloader()#这个主要是请求视频的真实链接,抓包的时候你就会明白

        #下面的代码是将视频信息封装成对象添加到res_data列表中
        for link in links:
            fileinfor = FileInfor()
            fileinfor.subject = subject.strip()
            fileinfor.filename= link.get_text().strip().replace(':','_').replace("\r\n","").replace(u'开始学习',"").replace(' ', '')
            fileinfor.mid = link['href'].split('/')[2]
            json = html_down.download(DOWNLOAD_URL.replace('{}',fileinfor.mid)).replace('\/','/').encode('utf-8')
            # print json
            dic_json=eval(json)
            # print dic_json['data']['result']['mpath'][0]
            fileinfor.url['L']=dic_json['data']['result']['mpath'][0]
            fileinfor.url['M']=dic_json['data']['result']['mpath'][1]
            fileinfor.url['H']=dic_json['data']['result']['mpath'][2]
            self.res_data.append(fileinfor)
        print self.res_data
        return self.res_data





