#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/5 7:31
import unittest
import HTMLTestRunnerNew
from homework.homework20181203.hm_04 import DoExecl
from homework.homework20181203.hm_02 import TestHttpRequest

test_data=DoExecl().get_data('test_cases.xlsx','test_data')
suite=unittest.TestSuite()
for item in test_data:
    suite.addTest(TestHttpRequest(item['url'],
                                  eval(item['param']),
                                  item['http_method'],
                                  str(item['expected']),
                                  'test_api'))
with open('test_api.html','wb+')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)