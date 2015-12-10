# -*- coding:utf-8 -*-
__author__ = 'DreamCathcer'

from Service.WeiboService.APIService import WeiboAPIService
from DAO.Weibo.WeiboDAO import WeiboDAO


class WeiboService(object):

    def __init__(self):
        self.weiboDAO = WeiboDAO()
        self.apiService = WeiboAPIService()

    def saveWeibo_byCycle(self,lat,lon,starttime,endtime,radius=3000,count=50,offset=0):
        data = self.apiService.getWeibo_nearbyline(lat=lat, lon=lon,starttime=starttime,endtime=endtime,range=radius,count=count,offset=offset)
        weibonumber = len(data["statuses"])
        for i in range(0,weibonumber):
            # 取微博ID
            weiboid=data["statuses"][i]["id"].encode('utf-8')
            #取text
            try:
                if text.startswith('http'):
                    text=''
                else:
                    text = data["statuses"][i]["text"].encode('utf-8')
            except:
                text = "unknown"
            #取经纬度
            # try:
            if "annotations" in data["statuses"][i]:
                if "place" in data["statuses"][i]["annotations"]:
                    lat = data["statuses"][i]["annotations"]["place"]["lat"]
                    lon = data["statuses"][i]["annotations"]["place"]["lon"]
                else:
                    lat=data["statuses"][i]["geo"]["coordinates"][0]
                    lon=data["statuses"][i]["geo"]["coordinates"][1]
            else:
                lat=data["statuses"][i]["geo"]["coordinates"][0]
                lon=data["statuses"][i]["geo"]["coordinates"][1]

            #取title
            if "annotations" in data["statuses"][i]:
                if "title" in data["statuses"][i]["annotations"]:
                    title = data["statuses"][i]["annotations"]["place"]["title"]
                else:
                    title='unknow'.encode('utf-8')
            else:
                title='unknow'.encode('utf-8')

            # 取userid
            userid=data["statuses"][i]["user"]["id"].encode('utf-8')
            #取location
            location = data["statuses"][i]["user"]["location"]
            #取userdescription
            decription = data["statuses"][i]["user"]["description"].encode('utf-8')
            #取gender

            gender = data["statuses"][i]["user"]["gender"]

            #取时间
            created_at=data["statuses"][i]["user"]["created_at"]
            monthdict = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
            timelist = created_at.split()
            timestrnew = '%s-%s-%s %s' %(timelist[-1] ,monthdict[timelist[1]], timelist[2] ,timelist[3])
            timestrnew = timestrnew.encode('utf-8')
            #取地点类型
            try:
                if "object" in data["statuses"][i]["url_objects"][i]:
                    if "object" in data["statuses"][i]["url_objects"][i]["object"]:
                        if "address" in data["statuses"][i]["url_objects"][i]["object"]["object"]:
                            if "fax" in data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]:
                                fax = data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]["fax"]
                else:
                    fax='unknow'.encode('utf-8')
            except IndexError:
                fax='unknow'.encode('utf-8')
            #取城市名
            try:
                if "object" in data["statuses"][i]["url_objects"][i]:
                    if "object" in data["statuses"][i]["url_objects"][i]["object"]:
                        if "address" in data["statuses"][i]["url_objects"][i]["object"]["object"]:
                            if "locality" in data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]:
                                locality = data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]["locality"]
                else:
                    locality='unknow'
            except IndexError:
                locality='unknow'.encode('utf-8')

            #取街道名
            try:
                if "object" in data["statuses"][i]["url_objects"][i]:
                    if "object" in data["statuses"][i]["url_objects"][i]["object"]:
                        if "address" in data["statuses"][i]["url_objects"][i]["object"]["object"]:
                            if "formatted" in data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]:
                                formatted = data["statuses"][i]["url_objects"][i]["object"]["object"]["address"]["formatted"]
                else:
                    formatted='unknow'.encode('utf-8')
            except IndexError:
                formatted='unknow'.encode('utf-8')

            #写入mysql,因特殊字符写入问题，将text和description中含有特殊字符按unknown处理
            try:
                self.weiboDAO.saveWeibo_ByAPI(weiboid,text,lat,lon,title,userid,location,decription,gender,timestrnew,fax,locality,formatted)
            except Exception:
                decription="unknown"
                text = "unknown"
                self.weiboDAO.saveWeibo_ByAPI(weiboid,text,lat,lon,title,userid,location,decription,gender,timestrnew,fax,locality,formatted)
