# -*- coding:utf-8 -*-
__author__ = 'DreamCathcer'

from Service.WeiboService.APIService import WeiboAPIService


class APIServiceTest(object):

    def __init__(self):
        self.weiboAPIService = WeiboAPIService()

    def getUserInfoTest(self):
        print self.weiboAPIService.getUserInfo("DreamCatcher-GIS")

    def getWeibo_nearbylineTest(self):
        print self.weiboAPIService.getWeibo_nearbyline(31.40456,118.39862,1420045261,1444233600)


if __name__=="__main__":
    weiboAPIServiceTest = APIServiceTest()
    # 测试:获取用户信息
    weiboAPIServiceTest.getUserInfoTest()
    # 测试:获取周边地区微博
    weiboAPIServiceTest.getWeibo_nearbylineTest()

