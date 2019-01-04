#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/4 6:22
import  requests
class Http_request:
    def http_request(self,url,param,method,cookie=None):
        if method == 'get':
            res = requests.get(url, param, cookies=cookie)
        else:
            res = requests.post(url, param, cookies=cookie)
        return res