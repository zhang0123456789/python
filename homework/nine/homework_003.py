#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/11/27 20:25
import  unittest
import HTMLTestRunnerNew
from homework.nine.homework_002 import *
suit=unittest.TestSuite()
loader=unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(Homework))
with open('homework_1.html','wb+')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suit)

