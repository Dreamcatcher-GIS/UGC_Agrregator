# -*- coding: utf-8 -*-
__author__ = 'lizhen'
import time

from Model import jsonToMysql
from Service.MapService.BaiduMap.SnatcherService import BaiduMapSnatcherService

if __name__=="__main__":
    while True:
        # word_keywords.keywords()
        # word_keywords.keywords()
        # jsonToMysql.dzdpbusinessreviewsToSql()

        #获取新浪微博数据测试
        jsonToMysql.weibojsontomysql()

        #获取大众点评数据测试
        #jsonToMysql.dzdptosql()

        #获取大众点评商户id
        # jsonToMysql.dzdpbusinessidjsontosql()

        #获取滁州的旅行社数据
        baiduMapService = BaiduMapSnatcherService()
        baiduMapService.getPoi(118.243339,32.195425,118.500901,32.496076,'旅行社')
        #
        # #暂停600秒后再进行爬取
        print 'ok'
        time.sleep(600)