#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/5 7:21
'''1:根据老师上课讲解的测试用例参数化，去写单元测试用例以及用到超继承
2：把所有的测试用例数据存到Excel中，然后写一个类do_excel，完成测试数据的读取
3：利用do_excel类读取到的测试数据 传给1203课堂上讲解的test_suite，完成测试用例的加载。
4：要求：登录3条用例 充值3条用例
5：请给用例加上断言 以及异常处理，断言可以用code 也可以用msg或者是用整段信息都OK，最后要有测试报告出具'''
import unittest
from homework.homework20181203.hm_01 import Http_request

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
