#coding:utf-8
import urlparse
import httplib
parsedurl = urlparse.urlparse('https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1457758644&di=a35a020cb3e5da7c2c179da3f18b6ad5&src=http://img.hb.aicdn.com/d2024a8a998c8d3e4ba842e40223c23dfe1026c8bbf3-OudiPA_fw580')

print parsedurl[1]
print parsedurl[2]
httpConn = httplib.HTTPConnection(parsedurl[1])
httpConn.request('GET', parsedurl[2])
response = httpConn.getresponse()
if response.status == 200:
    size = response.getheader('Content-Length')
    size = int(size) / 1024
    print 'Size: %s KB,Content-Type: %s, Last-Modified: %s'%(size,response.getheader('Content-Type'),response.getheader('Last-Modified'))
else:
    print response.status,response.reason
httpConn.close()
