__author__ = 'Xaxdus'
str='''{"result":0,"data":{"result":{"mid":11305,"mpath":["http:\/\/v2.mukewang.com\/b0e670ef-7695-4ded-b5d8-3f78d221413d\/L.mp4?auth_key=1457620869-0-0-688a98b2f90af6006b38ddf89b750ad1","http:\/\/v2.mukewang.com\/b0e670ef-7695-4ded-b5d8-3f78d221413d\/M.mp4?auth_key=1457620869-0-0-2c0f5e8ca614ce7fd2a4e2b1ef844074","http:\/\/v2.mukewang.com\/b0e670ef-7695-4ded-b5d8-3f78d221413d\/H.mp4?auth_key=1457620869-0-0-7287a7bc3fd090f504d592117600d4cf"],"cpid":"3019","name":"\u8bbe\u7f6e\u5e03\u5c40","time":"59","practise":[]}},"msg":"\u6210\u529f"}'''.replace('\/','/')

dict = eval(str)

print dict['data']['result']['mpath'][1]