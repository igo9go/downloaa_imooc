#coding:utf-8
import urllib2,cookielib
import bs4

# url = "http://www.imooc.com/learn/615"
#
#
# print '第一种方法'
#
# response1 = urllib2.urlopen(url)
#
# print response1.getcode()
# print response1.read()
#
# print '第二种方法'
#
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#    'Referer':'http://www.kuaidaili.com/',
# 'Cookie':'Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1466940405,1466944441; _ga=GA1.2.172144337.1466940406; _gat=1'
#           '; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1466944441',
# 'Connection':'keep-alive'
# }

# request = urllib2.Request("http://www.kuaidaili.com/free/inha/2")
# request.add_header('user-agent','Mozilla-Firefox-Spider(Wenanry)')
# request.add_header('Referer','http://www.kuaidaili.com/')
# request.add_header('Cookie','Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1466953979; _ga=GA1.2.555532848.1466953979; _gat=1'
#           '; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1466953979',)
#
# try:
#     response2= urllib2.urlopen(request)
# except urllib2.HTTPError,e:
#     # print response2
#     # print response2.getcode()
#     # print response2.read()
#     print e.getcode()
#     print e.read(),e.info()


from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')

# import requests
#
# loginUrl = 'http://www.kuaidaili.com/free/'
# s = requests.Session()
# # r = s.get(loginUrl,proxies=proxies,allow_redirects=True)
# r = s.get(loginUrl,allow_redirects=True)
#
# response= r.text
# r = s.get(loginUrl,allow_redirects=False)
#
# response= r.text
# print response

#
# print '第三种方法'
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#
# urllib2.install_opener(opener)
#
# response3 = urllib2.urlopen(url)
#
# print response3.getcode()
# print cj
# print len(response3.read())


# freader = urllib2.urlopen(self.__fileInfor.url[conf.STATE])
# filepath = self.filedir+os.sep+self.__fileInfor.filename+'.mp4'
# with open(filepath, "wb") as fwriter:
#     fwriter.write(freader.read())
#     fwriter.flush()
# fwriter.close()
# import urllib
# #下载文件
# def callbackfunc(blocknum, blocksize, totalsize):
#     '''回调函数
#     @blocknum: 已经下载的数据块
#     @blocksize: 数据块的大小
#     @totalsize: 远程文件的大小
#     '''
#     percent = 100.0 * blocknum * blocksize / totalsize
#     if percent > 100:
#         percent = 100
#     print "%.2f%%"% percent
# url = 'http://www.sina.com.cn'
# local = 'd:\\sina.html'
# urllib.urlretrieve(url, local, callbackfunc)
