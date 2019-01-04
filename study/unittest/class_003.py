#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/24 18:07
'''根据类来加载单独的一条用例'''
# import unittest
# from study.unittest.class_002 import Practice_1
# suit=unittest.TestSuite()
# suit.addTest(Practice_1('test_choice'))
# a=unittest.TextTestRunner()
# a.run(suit)


'''根据测试类加载用例'''
# import unittest
# from study.unittest.class_002 import Practice_1
# suit=unittest.TestSuite()
# loader=unittest.TestLoader()
# suit.addTest(loader.loadTestsFromTestCase(Practice_1))
# a=unittest.TextTestRunner()
# a.run(suit)

'''根据测试类所在模块来加载用例'''
import unittest
from study.unittest import class_002
suit=unittest.TestSuite()
loader=unittest.TestLoader()
suit.addTest(loader.loadTestsFromModule(class_002))
a=unittest.TextTestRunner()
a.run(suit)
