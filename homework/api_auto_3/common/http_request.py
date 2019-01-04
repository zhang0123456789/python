# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 20:06
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_01.py

#1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
#2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
#温馨提示：可以用到全局变量，global

import requests

class Http_request:

    def http_request(self,url,param,method,cookies=None):
        if method=='get':
          res=requests.get(url,param,cookies=cookies)
        else:
          res=requests.post(url,param,cookies=cookies)
        return res


