#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/4 6:25
'''断言异常处理  读取表格数据 生成测试报告test_api12.html'''
import unittest
from lesson.class_1205_api.http_request import Http_request

COOKIES=None

class TestHttpRequest(unittest.TestCase):
    def setUp(self):
       pass
    def __init__(self,url,param,http_method,expected,methodName):
        self.url=url
        self.param=param
        self.http_method=http_method
        self.expected=expected
        super(TestHttpRequest,self).__init__(methodName)

    def test_api(self):#登录
        global COOKIES#全局变量
        res=Http_request().http_request(self.url,self.param,self.http_method,COOKIES)
        print('登录请求结果：',res.json())
        if res.cookies:
            COOKIES=res.cookies

        try:
            self.assertEqual(self.expected,res.json()['code'])
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            raise e
