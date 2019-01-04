#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/12/4 6:44

'''断言异常处理  读取表格数据 生成测试报告test_api12.html'''
# import unittest
# import HTMLTestRunnerNew
# from lesson.class_1205_api.do_execl import DoExecl
# from lesson.class_1205_api.test_http_request import TestHttpRequest
#
#
# test_data=DoExecl().get_data('test_cases.xlsx','test_data')
#
# suite=unittest.TestSuite()
# for item in test_data:
#     suite.addTest(TestHttpRequest(item['url'],
#                                  eval(item['param']),#转回它原本python可以识别的数据类型
#                                   item['http_method'],
#                                   str(item['expected']),
#                                   'test_api'))
# with open('test_api12.html','wb+')as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(file)
#     runner.run(suite)




'''断言异常处理 根据配置文件  读取表格数据 生成测试报告 test_api13.html'''
import unittest
import HTMLTestRunnerNew
from lesson.class_1205_api.do_execl import DoExecl
from lesson.class_1205_api.test_http_request import TestHttpRequest
from lesson.class_1205_api.read_config import ReadConfig

#利用我们写的配置类，从配置文件case.conf里面的section:case
button=ReadConfig().read_config('case.conf','CASE','button')
#调用do_execl这个模块里面的DoExcel类里面的get_data方法，方法需要几个参数
#文件名   表单名    配置的值
test_data=DoExecl().get_data('test_cases.xlsx','test_data',button)
suite=unittest.TestSuite()
for item in test_data:
    suite.addTest(TestHttpRequest(item['url'],
                                 eval(item['param']),#转回它原本python可以识别的数据类型
                                  item['http_method'],
                                  str(item['expected']),
                                  'test_api'))#创建实例的方法
with open('test_api13.html','wb+')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)