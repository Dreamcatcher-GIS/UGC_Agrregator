# -*- coding:utf-8 -*-
__author__ = 'DreamCathcer'
from Service.MapService.BaiduMap.APIService import BaiduMapAPIService
from DAO.BaiduMap.BaiduMapDAO import BaiduMapDAO


class BaiduMapSnatcherService(object):
    def __init__(self):
        self.baiduMapDAO = BaiduMapDAO()
        self.baiduAPIService = BaiduMapAPIService("DW2CwL3B3271CiVyw7GdBsfR")

    def getPoi(self,lng0,lat0,lng1,lat1,query):
        # 使用矩形范围初始栈
        queue = [[lng0,lat0,lng1,lat1]]
        while len(queue)!=0:
            # 取出一个查询范围
            range = queue.pop()
            # 根据范围进行查询
            data = self.baiduAPIService.placeSearch(query=query,bounds="%lf,%lf,%lf,%lf"%(range[1],range[0],range[3],range[2]))
            if data.has_key('results'):
                # 如果范围的poi等于20,就切割该范围,并将切割后的子范围置入栈中
                if len(data['results'])==20:
                    splitX = (range[0]+range[2])/2
                    splitY = (range[1]+range[3])/2
                    if (range[2]-range[0])<0.001 or (range[3]-range[1])<0.001:
                        continue
                    queue.append([range[0],splitY,splitX,range[3]])
                    queue.append([splitX,splitY,range[2],range[3]])
                    queue.append([range[0],range[1],splitX,splitY])
                    queue.append([splitX,range[1],range[2],splitY])
                    continue
                # 如果查询结果小于20则存储
                else:
                    self.baiduMapDAO.savePOIData(data)
