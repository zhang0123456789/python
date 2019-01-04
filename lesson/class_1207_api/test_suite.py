#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/12/4 6:44
'''用了ddt装饰，只能用loader---加载用例  discover---web'''
'''用ddt装饰了，   生成测试报告 test_api1.html'''
import unittest
import HTMLTestRunnerNew
from lesson.class_1207_api.test_http_request import TestHttpRequest
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
with open('test_api.html','wb+')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)