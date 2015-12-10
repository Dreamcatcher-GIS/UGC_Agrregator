# -*- coding: utf-8 -*-
__author__ = 'kaipeng'

import MySQLdb
import uuid
import random

class WeiboDAO(object):
    def __init__(self,host= 'localhost',db='weibo',user='root',password='1234'):
        self.host = host
        self.db = db
        self.user=user
        self.password =password

    # 存储微博id
    def saveWeiboID(self,weiboIDSet,userID,pageNum):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,charset='utf8')
        cursor = db.cursor()
        for weiboID in weiboIDSet:
            cursor.execute("insert into weibo_id(guid,userID,weiboID,pageNum)values(%s,%s,%s,%s)" ,(uuid.uuid1(),userID,weiboID,pageNum))
            db.commit()
        cursor.close()
        db.close()

    # 存储微博评论
    def saveWeiboComment(self,items):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,charset='utf8')
        cursor = db.cursor()
        for item in items:
            try:
                cursor.execute("insert into weibo_comment(guid,userID,weiboID,pageNum,commPeople,commentText,commentTime,crawlTime,likeNum)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,(uuid.uuid1(),item["userID"],item["weiboID"],item["pageNum"],item["commPeople"],item["commentText"],item["commentTime"],item["crawlTime"],item["likeNum"]))
            except:
                continue
            db.commit()
        cursor.close()
        db.close()

    # 获取api账号数量
    def countweiboaccountnumber(self):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,charset='utf8')
        cursor = db.cursor()
        cursor.execute("select count(*) from api_account")
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data

    #从mysql中获取微博账号,随机获取微博账号
    def getweiboacount(self,db):
        weiboacount = []
        accountnumber = self.countweiboaccountnumber()[0]
        i = random.randint(0,accountnumber-1)
        cursor = db.cursor()
        cursor.execute("select * from api_account where ID=%s"%i)
        data = cursor.fetchone()
        weiboacount.extend(data)
        cursor.close()
        db.close()
        return weiboacount

    def saveWeibo_ByAPI(self,weiboid,text,lat,lon,title,userid,location,userdecription,gender,created_at,fax,localcity,formatted):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,charset='utf8')
        cursor = db.cursor()
        cursor.execute("insert into weibo_content(weiboid,text,lat,lon,title,userid,location,userdescription,gender,created_at,fax,locality,formatted)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                   ,(weiboid,text,lat,lon,title,userid,location,userdecription,gender,created_at,fax,localcity,formatted))
        db.commit()
        cursor.close()
        db.close()
