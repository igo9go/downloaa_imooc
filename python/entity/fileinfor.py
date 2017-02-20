#coding:utf-8
'''
这个类用于描述文件信息的模型，将文件的所有信息封装成一个类，便于管理
'''
class FileInfor(object):
    def __init__(self):
        self.__subject=''#教程名称
        self.__filename=''#课程名称(也是下载的每个文件名称)
        self.__mid= ''#课程的ID号
        self.__url={}#下载链接(分高中低,H M L)
    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self,value):
        self.__subject = value

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self,value):
        self.__filename = value

    @property
    def mid(self):
        return self.__mid

    @mid.setter
    def mid(self,value):
        self.__mid = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self,value):
        self.__url = value