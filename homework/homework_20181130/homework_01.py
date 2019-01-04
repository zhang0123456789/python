#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/1 16:44
'''1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
温馨提示：可以用到全部变量，global'''
import requests
class HttpRequest:
    def http_request(self,url,param,method,cookies=None):
        if method=='get':
            try:
                res=requests.get(url,param,cookies=cookies)
            except Exception as e:
                print("执行的get请求报错：{}".format(e))
                res='Error:get请求报错{}'.format(e)
        elif method=='post':
            try:
                res=requests.post(url,param,cookies=cookies)
            except Exception as e:
                print("执行的post请求报错：{}".format(e))
                res='Error:post请求报错{}'.format(e)
        else:
            print("你请求的方式不对！")
            res='Error:请求的方法不对 报错{}'.format(method)
        return res







