# -*- coding:utf-8 -*-
__author__ = 'DreamCathcer'

from Service.MapService.BaiduMap.SnatcherService import BaiduMapSnatcherService

class SnatcherServiceTest(object):

    def __init__(self):
        self.snatcherService = BaiduMapSnatcherService()

    def getPoiTest(self):
        self.snatcherService.getPoi(115.601314,30.612053,117.073098,34.063061,"酒店")


if __name__=="__main__":
    snatcherServiceTest = SnatcherServiceTest()
    snatcherServiceTest.getPoiTest()
