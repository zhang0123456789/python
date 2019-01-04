#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/1 16:45
import unittest
import HTMLTestRunnerNew
from homework.homework_20181130.homework_02 import *
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
with open('homework.html','wb+')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title="20181202",description="request测试",tester="蜜蜜")
    runner.run(suite)
