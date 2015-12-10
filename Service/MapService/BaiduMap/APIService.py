# -*- coding:utf-8 -*-
__author__ = 'DreamCathcer'

from Service.UniversalSDK import APIClient


class BaiduMapAPIService(object):

    def __init__(self,ak):
        self.baiduClient = APIClient("http://api.map.baidu.com")
        self.__ak = ak

    #地理编码
    #地址：http://api.map.baidu.com/geocoder/v2/
    #类型：get
    def doGeocoding(self,addressText):
        data = self.baiduClient.geocoder.v2.addtrail("/").get(ak=self.__ak,output="json",address=addressText)
        return data

    #poi查询
    #地址：http://api.map.baidu.com/place/v2/search
    #类型：get
    def placeSearch(self,query,bounds,output="json",page_size="20",scope=2):
        data = self.baiduMapClient.place.v2.search.get(ak=self.__ak,query=query,bounds=bounds,output=output,page_size=page_size,scope=scope)
        return data
