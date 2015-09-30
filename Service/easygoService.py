# -*- coding:utf-8 -*-
__author__ = 'DreamCatcher'
from easygo import EasygoClient
from DAO.easygoDAO import EasygoDAO
import time

class EasygoService(object):
    def __init__(self):
        self.easygoClient = EasygoClient('ot5aas1gv5RQ1dOFrlqBp4HcvKqM')
        self.easygoDAO = EasygoDAO()
    def saveDataViaTree(self,lng0,lat0,lng1,lat1,description):
        queue = [[lng0,lat0,lng1,lat1]]
        while len(queue)!=0:
            range = queue.pop()
            try:
                data = self.easygoClient.get_heatmap_data.get(lng0=range[0],lat0=range[1],lng1=range[2],lat1=range[3])
            except:
                splitX = (range[0]+range[2])/2
                splitY = (range[1]+range[3])/2
                if (range[2]-range[0])<0.004 or (range[3]-range[1])<0.004:
                    continue
                queue.append([range[0],splitY,splitX,range[3]])
                queue.append([splitX,splitY,range[2],range[3]])
                queue.append([range[0],range[1],splitX,splitY])
                queue.append([splitX,range[1],range[2],splitY])
                continue
            self.easygoDAO.saveData(data,description)
