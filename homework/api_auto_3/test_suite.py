# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 20:22
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_suite.py
import unittest
import HTMLTestRunnerNew
from homework.api_auto_3.common import project_path
from homework.api_auto_3.common.test_http_request import TestHttpRequest


suite=unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_api'))#创建对象的形式来添加用例
#ddt loader---加载用例   discover---web
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))


with open(project_path.report_path,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)

