# -*- coding: utf-8 -*-
__author__ = 'lizhen'
from weibo import APIClient
import json
from DAO import conMySql
def nearbytline():
    db = conMySql.openSQL()
    #微博账号获取
    weiboacount = conMySql.getweiboacount(db)
    app_key=weiboacount[1]
    app_secret=weiboacount[2]
    token=weiboacount[3]
    #poiinfo获取
    poiinfo = conMySql.getPoiInfo(db)
    lat = poiinfo[2]
    lon = poiinfo[3]

    client = APIClient(app_key, app_secret, redirect_uri='')
    client.set_access_token(token, 0)

    data =client.place.nearby_timeline.get(lat=lat,long=lon,starttime='1422720000',range=3000,count=50)
    # print data["statuses"][0]["url_objects"][0]["object"]["object"]["address"]["fax"]
    # print data
    return data

def userShow(userName):
    db = conMySql.openSQL()
    #微博账号获取
    weiboacount = conMySql.getweiboacount(db)
    app_key=weiboacount[1]
    app_secret=weiboacount[2]
    token=weiboacount[3]

    client = APIClient(app_key, app_secret, redirect_uri='')
    client.set_access_token(token, 0)

    data=client.users.show.get(screen_name=userName)
    return data
def searchTopics(topics):
    db = conMySql.openSQL()
    #微博账号获取
    weiboacount = conMySql.getweiboacount(db)
    app_key=weiboacount[1]
    app_secret=weiboacount[2]
    token=weiboacount[3]

    client = APIClient(app_key, app_secret, redirect_uri='')
    client.set_access_token(token, 0)

    data = client.search.topics.get(q=topics,count=50)
    return data
def userMessage(status,data,client,mid,userName):
    if status == 1:
        return data
    else:
        messageData = client.statuses.user_timeline.get(screen_name=userName,mix_id=mid,count=100)
        length = len(messageData['statuses'])
        if length == 1:
            data.append(messageData['statuses'][0])
            status = 1
        else:
            i = 0
            while i<length:
                data.append(messageData['statuses'][i])
                i+=1
                if i == length-1:
                    mid = messageData['statuses'][i]['mid']
                    status = 0
                    break
    return  userMessage(status,data,client,mid,userName)


if __name__ =='__main__':
    data = searchTopics(u"滁州1912")
    print len(data["statuses"])
    pass