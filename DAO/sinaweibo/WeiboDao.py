# -*- coding: utf-8 -*-
__author__ = 'kaipeng'

import MySQLdb
import uuid

class WeiboDao(object):
    def __init__(self,host= 'localhost',db='ugc',user='root',password='1234'):
        self.host = host
        self.db = db
        self.user=user
        self.password =password

    def saveWeiboID(self,weiboIDSet,userID,pageNum):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,charset='utf8')
        cursor = db.cursor()
        for weiboID in weiboIDSet:
            cursor.execute("insert into weiboID(guid,userID,weiboID,pageNum)values(%s,%s,%s,%s)" ,(uuid.uuid1(),userID,weiboID,pageNum))
            db.commit()
        cursor.close()
        db.close()

    def saveWeiboComment(self,items):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,charset='utf8')
        cursor = db.cursor()
        for item in items:
            try:
                cursor.execute("insert into commentData(guid,userID,weiboID,pageNum,commPeople,commentText,commentTime,crawlTime,likeNum)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,(uuid.uuid1(),item["userID"],item["weiboID"],item["pageNum"],item["commPeople"],item["commentText"],item["commentTime"],item["crawlTime"],item["likeNum"]))
            except:
                continue
            db.commit()
        cursor.close()
        db.close()