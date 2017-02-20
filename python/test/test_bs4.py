#coding:utf-8
#pip install beautifulsoup
from bs4 import BeautifulSoup
import re

# soup = BeautifulSoup('123','html.parser',from_encoding='utf-8')
# #查找所有标签为a的节点
# soup.find_all('a')
# #查找所有标签为a,链接符合/view/123.html形式的节点
# soup.find_all('a',href='/view/123.html')
#
# soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
#
# #查找所有标签为div,class为abc,文字为python的节点
# soup.find_all('div',class_='abc',string='python')

# #获取查找到的节点的标签名称
# node.name
# #获取查找到的按节点的href属性
# node['href']
#
# #获取查找到的a节点的链接文字
# node.get_text()

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc)
# links = soup.find_all('a')
#
# for link in links:
#     print link.name,link['href'],link.get_text()
#
# p_node = soup.find('p',class_ = "title")
# print p_node.name,p_node.get_text()

# str = '<a target="_self" href="http://pic.yesky.com/146/101110646.shtml"><img alt="星女郎林允清纯活泼 当街开吃抬腿跳跃_街拍" ' \
# 'src="http://image.tianjimedia.com/uploadImages/2016/071/44/6Q13W9S85S75_113.jpg"></a>'
#
# soup = BeautifulSoup(str,'html.parser',from_encoding='utf-8')
# links = soup.find_all('img')
# for link in links:
#     print link['src']
# str = '<a class="J-media-item studyvideo" href="/video/11304" target="_blank">1-1 项目介绍 (02:14)<i class="study-state done"></i></a>'
# soup = BeautifulSoup(str,'html.parser',from_encoding='utf-8')
# links = soup.find_all('a',class_='J-media-item studyvideo')
#
# for link in links:
#     print link.get_text().strip(),int(link['href'].split('/')[2])

str ='<div class="hd"><h2 class="l">Hibernate注解</h2></div>'
soup = BeautifulSoup(str,'html.parser',from_encoding='utf-8')
p_node = soup.find('div',class_ = "hd")

print p_node.get_text()
