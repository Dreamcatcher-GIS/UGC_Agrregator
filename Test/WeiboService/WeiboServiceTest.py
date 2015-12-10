# -*- coding:utf-8 -*-
__author__ = 'DreamCathcer'

from Service.WeiboService.WeiboService import WeiboService


class WeiboServiceTest(object):

    def __init__(self):
        self.weiboService = WeiboService()

    def saveWeibo_byCycleTest(self):
        self.weiboService.saveWeibo_byCycle(31.40456,118.39862,1420045261,1444233600)



if __name__=="__main__":
    weiboServiceTest = WeiboServiceTest()

    weiboServiceTest.saveWeibo_byCycleTest()