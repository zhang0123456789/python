#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/24 15:34
'''unittest四大类
TestCase：写测试用例
TestLoader：加载测试用例
TestSuite: 测试集，存放用例的地方  容器
TextTestRunner：执行用例的---包含输出报告'''

'''方法一   生成测试集'''
# import unittest
# from lesson.class_1123_unittest.class_02 import TestKerry
# suite=unittest.TestSuite()#装用例的地方
# '''方法一   addTest()专门加载用例的方法   测试类的对象形式来添加用例'''
# suite.addTest(TestKerry('test_run'))
# suite.addTest(TestKerry('test_cooking'))
# '''执行用例'''
# Kerry=unittest.TextTestRunner()#执行用例的执行者
# Kerry.run(suite)

'''方法二  通过loader从指定的测试类里面添加测试用例'''
# import unittest
# from lesson.class_1123_unittest.class_02 import TestKerry
# suite=unittest.TestSuite()#装用例的地方
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestKerry))
# '''执行用例'''
# Kerry=unittest.TextTestRunner()#执行用例的执行者
# Kerry.run(suite)

'''方法二  通过loader从指定的测试类里面添加测试用例  verbosity=1 用unittest生成测试报告'''
# import unittest
# from lesson.class_1123_unittest.class_02 import *
# suite=unittest.TestSuite()#装用例的地方
# loader=unittest.TestLoader()
# # suite.addTest(loader.loadTestsFromTestCase(TestKerry))
# suite.addTest(loader.loadTestsFromTestCase(TestSai))
# '''执行用例'''
# with open('test_api.txt','w+') as file:
#     Kerry=unittest.TextTestRunner(stream=file,verbosity=1)#执行用例的执行者
#     Kerry.run(suite)

'''方法二  通过loader从指定的测试类里面添加测试用例  verbosity=2  用unittest生成测试报告'''
# import unittest
# from lesson.class_1123_unittest.class_02 import *
# suite=unittest.TestSuite()#装用例的地方
# loader=unittest.TestLoader()
# # suite.addTest(loader.loadTestsFromTestCase(TestKerry))
# suite.addTest(loader.loadTestsFromTestCase(TestSai))
# '''执行用例'''
# with open('test_api_2.txt','w+') as file:
#     Kerry=unittest.TextTestRunner(stream=file,verbosity=2)#执行用例的执行者
#     Kerry.run(suite)




'''方法二  通过loader从指定的测试类里面添加测试用例  verbosity=0  用unittest生成测试报告'''
# import unittest
# from lesson.class_1123_unittest.class_02 import *
# suite=unittest.TestSuite()#装用例的地方
# loader=unittest.TestLoader()
# # suite.addTest(loader.loadTestsFromTestCase(TestKerry))
# suite.addTest(loader.loadTestsFromTestCase(TestSai))
# '''执行用例'''
# with open('test_api_3.txt','w+') as file:
#     Kerry=unittest.TextTestRunner(stream=file,verbosity=0)#执行用例的执行者
#     Kerry.run(suite)


'''方法二  通过loader从指定的测试类里面添加测试用例  verbosity=0  用html生成测试报告'''
import unittest
import HTMLTestRunnerNew
from lesson.class_1123_unittest.class_02 import *
suite=unittest.TestSuite()#装用例的地方
loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestKerry))
suite.addTest(loader.loadTestsFromTestCase(TestSai))
'''执行用例'''
with open('test_api_4.html','wb+') as file:
    Kerry=HTMLTestRunnerNew.HTMLTestRunner(file)
    Kerry.run(suite)

'''方法三  通过loader总指定放模块里面添加用例'''
# import unittest
# from lesson.class_1123_unittest import class_02
# suite=unittest.TestSuite()#装用例的地方
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(class_02))
# Kerry=unittest.TextTestRunner()#执行用例的执行者
# Kerry.run(suite)
