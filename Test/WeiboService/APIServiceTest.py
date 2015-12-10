# -*- coding:utf-8 -*-
__author__ = 'DreamCathcer'

from Service.WeiboService.APIService import WeiboAPIService


class APIServiceTest(object):

    def __init__(self):
        self.weiboAPIService = WeiboAPIService()

    def getUserInfoTest(self):
        print self.weiboAPIService.getUserInfo("DreamCatcher-GIS")


if __name__=="__main__":
    weiboAPIServiceTest = APIServiceTest()

    weiboAPIServiceTest.getUserInfoTest()