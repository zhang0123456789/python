#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/1 16:45
'''1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
温馨提示：可以用到全部变量，global'''
import unittest
import requests
from homework.homework_20181130.homework_01 import HttpRequest
login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
login_data={'mobilephone':18688773467,'pwd':'123456'}
recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
recharge_data={'mobilephone':18688773467,'amount':'1000'}
class TestHttpRequest(unittest.TestCase):
    def __init__(self,url,param,method):
        super(TestHttpRequest,self).__init__(method)
        self.request=HttpRequest()
        self.url=url
        self.param=param
        self.method=method
    def test_01(self):
        res_request=self.request.http_request(self.url,self.param,self.method)
        print("第一条get请求登录测试用例执行结果是：{}".format(res_request.json()['登录成功']))
        global cookies
        actual=res_request
        ecpected='登录成功'
        self.assertEqual(ecpected,actual)
    def test_02(self):
        res_charge = self.request.http_request(self.url, self.param,self.method,cookies=cookies)
        print("第一条get请求充值测试用例执行结果是：{}".format(res_charge.json()['msg']))
        actual=res_charge.json()['msg']
        ecpected='充值成功'
        self.assertEqual(ecpected,actual)
