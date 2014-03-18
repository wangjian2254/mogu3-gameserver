#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
from tools.page import Page

__author__ = u'王健'


class UploadPoint(Page):
    def get(self):
        username = self.request.get('username','')
        appcode = self.request.get('appcode','')
        spaceid = self.request.get('spaceid','')

