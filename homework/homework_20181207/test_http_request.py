#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/4 6:25
'''ddt装饰    test_api.html'''
import unittest
import time
from homework.homework_20181207.http_request import Http_request
from ddt import ddt,data
from homework.homework_20181207.read_config import ReadConfig
from homework.homework_20181207.do_execl import DoExecl
from homework.homework_20181207.my_logging import MyLog
my_logger=MyLog()

button=ReadConfig().read_config('case.conf','CASE','button')
COOKIES=None
test_data=DoExecl().get_data('test_cases.xlsx','test_data',button)

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
       print('开始执行测试用例')
    @data(*test_data)
    def test_api(self,item):#登录
        global COOKIES#全局变量

        my_logger.info('目前正在执行第{}条用例：{}'.format(item['case_id'], item['title']))
        my_logger.info('------------开始请求，检查我们的URL地址----------')
        my_logger.info('url:{}'.format(item['url']))

        my_logger.info('------------开始请求，检查我们的param参数----------')
        my_logger.info('param:{}'.format(item['param']))

        my_logger.info('-------------------开始http请求-------------------------------')
        res=Http_request().http_request(item['url'],eval(item['param']),item['http_method'],COOKIES)
        my_logger.info('-----------------------结束http请求--------------------------')

        my_logger.info('登录请求结果：{}'.format(res.json()))
        if res.cookies:
            COOKIES=res.cookies

        try:
            self.assertEqual(str(item['expected']),res.json()['code'])
            TestResult='PASS'#本次测试结果
        except AssertionError as e:
            TestResult='Failed'
            my_logger.error('断言出错：{}'.format(e))
            raise e
        finally:
            my_logger.info('断言结果是{}'.format(TestResult))
            my_logger.info('----------------断言结束-----------------')
        time.sleep(1)

    def tearDown(self):
        print('测试用例执行结束')
