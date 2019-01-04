#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/4 6:44
'''最简单的形式 test_api1.html'''
# import unittest
# import HTMLTestRunnerNew
# from lesson.class_1203_do_execl.test_http_request import TestHttpRequest
# suite=unittest.TestSuite()
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
# with open('test_api1.html','wb+')as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(file)
#     runner.run(suite)

'''参数化登录 test_api2.html'''
# import unittest
# import HTMLTestRunnerNew
# login_data_1 = {'mobilephone': 18688773467, 'pwd': '123456'}
# login_data_2 = {'mobilephone': 18688773467, 'pwd': '12345678'}
# login_data_3 = {'mobilephone': 11868877346347, 'pwd': '123456'}
# from lesson.class_1203_do_execl.test_http_request import TestHttpRequest
# suite=unittest.TestSuite()
# suite.addTest(TestHttpRequest(login_data_1,'post','test_login'))#创建实例的方法
# suite.addTest(TestHttpRequest(login_data_2,'get','test_login'))
# suite.addTest(TestHttpRequest(login_data_3,'post','test_login'))
# with open('test_api2.html','wb+')as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(file)
#     runner.run(suite)

'''参数化登录 test_api6.html'''
# import unittest
# import HTMLTestRunnerNew
# test_data=[ {'param':{'mobilephone': 18688773467, 'pwd': '123456'},'http_method':'get'},
#             {'param':{'mobilephone': 18688773467, 'pwd': '12345678'},'http_method':'post'},
#             {'param':{'mobilephone': 11868877346347, 'pwd': '123456'},'http_method':'get'}]
#
# from lesson.class_1203_do_execl.test_http_request import TestHttpRequest
# suite=unittest.TestSuite()
# for item in test_data:
#     suite.addTest(TestHttpRequest(item['param'],item['http_method'],'test_login'))
# with open('test_api6.html','wb+')as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(file)
#     runner.run(suite)

'''登录充值  test_api9.html'''
# import unittest
# import HTMLTestRunnerNew
# test_data=[ {'param':{'mobilephone': 18688773467, 'pwd': '123456'},'http_method':'get',
#              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},
#
#             {'param':{'mobilephone': 18688773467, 'pwd': '12345678'},'http_method':'post',
#              'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},
#
#             {'param':{'mobilephone': 11868877346347, 'pwd': '123456'},'http_method':'get',
#              'url' :'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},
#
#             {'param':{'mobilephone': 18688773467, 'amount': '1000'},'http_method':'post',
#              'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'}]
#
# from lesson.class_1203_do_execl.test_http_request import TestHttpRequest
# suite=unittest.TestSuite()
# for item in test_data:
#     suite.addTest(TestHttpRequest(item['url'],item['param'],item['http_method'],'test_api'))
# with open('test_api9.html','wb+')as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(file)
#     runner.run(suite)

'''断言正确  test_api10.html'''
# import unittest
# import HTMLTestRunnerNew
# test_data=[ {'param':{'mobilephone': 18688773467, 'pwd': '123456'},'http_method':'get',
#              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'10001'},
#
#             {'param':{'mobilephone': 18688773467, 'pwd': '12345678'},'http_method':'post',
#              'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'20111'},
#
#             {'param':{'mobilephone': 11868877346347, 'pwd': '123456'},'http_method':'get',
#              'url' :'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'20111'},
#
#             {'param':{'mobilephone': 18688773467, 'amount': '1000'},'http_method':'post',
#              'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','expected':'10001'}]
#
# from lesson.class_1203_do_execl.test_http_request import TestHttpRequest
# suite=unittest.TestSuite()
# for item in test_data:
#     suite.addTest(TestHttpRequest(item['url'],
#                                   item['param'],
#                                   item['http_method'],
#                                   item['expected'],
#                                   'test_api'))
# with open('test_api10.html','wb+')as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(file)
#     runner.run(suite)

'''断言错误  test_api11.html'''
# import unittest
# import HTMLTestRunnerNew
# test_data=[ {'param':{'mobilephone': 18688773467, 'pwd': '123456'},'http_method':'get',
#              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'10001'},
#
#             {'param':{'mobilephone': 18688773467, 'pwd': '12345678'},'http_method':'post',
#              'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'20111'},
#
#             {'param':{'mobilephone': 11868877346347, 'pwd': '123456'},'http_method':'get',
#              'url' :'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'20112'},
#
#             {'param':{'mobilephone': 18688773467, 'amount': '1000'},'http_method':'post',
#              'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','expected':'10001'}]
#
# from lesson.class_1203_do_execl.test_http_request import TestHttpRequest
# suite=unittest.TestSuite()
# for item in test_data:
#     suite.addTest(TestHttpRequest(item['url'],
#                                   item['param'],
#                                   item['http_method'],
#                                   item['expected'],
#                                   'test_api'))
# with open('test_api11.html','wb+')as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(file)
#     runner.run(suite)

# '''断言异常处理  test_api12.html'''
# import unittest
# import HTMLTestRunnerNew
# test_data=[ {'param':{'mobilephone': 18688773467, 'pwd': '123456'},'http_method':'get',
#              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'10001'},
#
#             {'param':{'mobilephone': 18688773467, 'pwd': '12345678'},'http_method':'post',
#              'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'20111'},
#
#             {'param':{'mobilephone': 11868877346347, 'pwd': '123456'},'http_method':'get',
#              'url' :'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'20112'},
#
#             {'param':{'mobilephone': 18688773467, 'amount': '1000'},'http_method':'post',
#              'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','expected':'10001'}]
#
# from lesson.class_1203_do_execl.test_http_request import TestHttpRequest
# suite=unittest.TestSuite()
# for item in test_data:
#     suite.addTest(TestHttpRequest(item['url'],
#                                   item['param'],
#                                   item['http_method'],
#                                   item['expected'],
#                                   'test_api'))
# with open('test_api12.html','wb+')as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(file)
#     runner.run(suite)