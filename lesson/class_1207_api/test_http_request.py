#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/4 6:25
'''ddt装饰    test_api.html'''
import unittest
import time
from lesson.class_1207_api.http_request import Http_request
from ddt import ddt,data
from lesson.class_1207_api.read_config import ReadConfig
from lesson.class_1207_api.do_execl import DoExecl
COOKIES=None
#利用我们写的配置类，从配置文件case.conf里面的section:case
button=ReadConfig().read_config('case.conf','CASE','button')
#调用do_execl这个模块里面的DoExcel类里面的get_data方法，方法需要几个参数
#文件名   表单名    配置的值
test_data=DoExecl().get_data('test_cases.xlsx','test_data',button)

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
       pass
    @data(*test_data)
    def test_api(self,item):#登录
        global COOKIES#全局变量
        print('目前正在执行第{}用例'.format(item['case_id'],item['title']))
        print('------------开始请求，检查我们的URL地址----------')
        print('url:{}'.format(item['url']))

        print('------------开始请求，检查我们的param参数----------')
        print('param:{}'.format(item['param']))

        print('-------------------开始http请求-------------------------------')
        res=Http_request().http_request(item['url'],eval(item['param']),item['http_method'],COOKIES)
        print('-----------------------结束http请求--------------------------')

        print('登录请求结果：',res.json())
        if res.cookies:
            COOKIES=res.cookies

        try:
            self.assertEqual(str(item['expected']),res.json()['code'])
        except AssertionError as e:
            print('断言出错：{}'.format(e))
            raise e
        time.sleep(1)
