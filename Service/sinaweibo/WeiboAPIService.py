# -*- coding: utf-8 -*-
__author__ = 'kaipeng'

from weibo import APIClient


class WeiboAPIService(object):

    def __init__(self,appKey="1268278335",appSecret = "204dfdc6e50ea33fe282445f4f0a3b0e",token = "2.005jCfXFLIZp4Bd42d17a3dbC3fmaB"):
        self.appKey = appKey
        self.appSecret = appSecret
        self.token = token
        self.client = APIClient(self.appKey,self.appSecret, redirect_uri='')
        self.client.set_access_token(self.token,0)

    def getUserInfo(self,screen_name):
        return self.client.users.show.get(screen_name = screen_name)
