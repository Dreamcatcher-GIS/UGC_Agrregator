# -*- coding:utf-8 -*-
__author__ = 'DreamCatcher'

import MySQLdb
from datetime import datetime
import uuid

class EasygoDAO(object):
    def __init__(self,host= 'localhost',db='easygodb',user='root',password='1234'):
        self.host = host
        self.db = db
        self.user=user
        self.password =password
    #将从接口中获取到的数据持久化到easygodata表中
    def saveData(self,data,description=''):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,charset='utf8')
        id = uuid.uuid1()
        currentTime = datetime.now()
        strCurrentTime = currentTime.strftime('%Y-%m-%d %H:%M:00').encode('utf-8')
        cursor = db.cursor()
        try:
            print len(data['body']['grid_result'])
        except:
            return
        for point in data['body']['grid_result']:
            count = point['count']
            if count==0:
                continue
            x = (point['grid_x']*250+125)*0.000001
            y = (point['grid_y']*250+125)*0.000001
            cursor.execute("insert into easygodata(guid,count,x,y,time,description)values(%s,%s,%s,%s,%s,%s)" ,(id,count,x,y,strCurrentTime,description))
            db.commit()
        cursor.close()
        db.close()