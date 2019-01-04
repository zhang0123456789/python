#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/4 6:25
'''最简单的形式 test_api1.html'''
# import unittest
# from lesson.class_1203_do_execl.http_request import Http_request
# COOKIES=None
# class TestHttpRequest(unittest.TestCase):
#     def test_login(self):#登录
#         login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
#         login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
#         res=Http_request().http_request(login,login_data,'get')
#         print('登录请求结果：',res.json())
#         global COOKIES#声明全局变量
#         if res.cookies:#非空非0数据为真
#             COOKIES=res.cookies#只有当cookies不为空的时候，就去修改全局变量
#     def test_recharge(self):#充值
#         recharge = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
#         recharge_data = {'mobilephone': 18688773467, 'amount': '1000'}
#         res=Http_request().http_request(recharge,recharge_data,'post',COOKIES)
#         print('充值的结果是：',res.json())


'''参数化登录 test_api2.html'''
# import unittest
# from lesson.class_1203_do_execl.http_request import Http_request
# COOKIES=None
# class TestHttpRequest(unittest.TestCase):
#     def setUp(self):
#         self.url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
#     def __init__(self,param,http_method,methodName):
#         self.param=param
#         self.http_method=http_method
#         super(TestHttpRequest,self).__init__(methodName)
#     def test_login(self):#登录
#         res=Http_request().http_request(self.url,self.param,self.http_method)
#         print('登录请求结果：',res.json())

'''参数化登录 test_api6.html'''
# import unittest
# from lesson.class_1203_do_execl.http_request import Http_request
# COOKIES=None
# class TestHttpRequest(unittest.TestCase):
#     def setUp(self):
#         self.url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
#     def __init__(self,param,http_method,methodName):
#         self.param=param
#         self.http_method=http_method
#         super(TestHttpRequest,self).__init__(methodName)
#     def test_login(self):#登录
#         res=Http_request().http_request(self.url,self.param,self.http_method)
#         print('登录请求结果：',res.json())

'''登录充值    test_api9.html'''
# import unittest
# from lesson.class_1203_do_execl.http_request import Http_request
# COOKIES=None
# class TestHttpRequest(unittest.TestCase):
#     def setUp(self):
#        pass
#     def __init__(self,url,param,http_method,methodName):
#         self.url=url
#         self.param=param
#         self.http_method=http_method
#         super(TestHttpRequest,self).__init__(methodName)
#     def test_api(self):#登录
#         global COOKIES
#         res=Http_request().http_request(self.url,self.param,self.http_method,COOKIES)
#         print('登录请求结果：',res.json())
#         if res.cookies:
#             COOKIES=res.cookies

'''断言正确  study-api10.thml'''
# import unittest
# from lesson.class_1203_do_execl.http_request import Http_request
# COOKIES=None
# class TestHttpRequest(unittest.TestCase):
#     def setUp(self):
#        pass
#     def __init__(self,url,param,http_method,expected,methodName):
#         self.url=url
#         self.param=param
#         self.http_method=http_method
#         self.expected=expected
#         super(TestHttpRequest,self).__init__(methodName)
#     def test_api(self):#登录
#         global COOKIES#全局变量
#         res=Http_request().http_request(self.url,self.param,self.http_method,COOKIES)
#         print('登录请求结果：',res.json())
#         if res.cookies:
#             COOKIES=res.cookies
#         self.assertEqual(self.expected,res.json()['code'])

'''断言错误  study-api11.thml'''
# import unittest
# from lesson.class_1203_do_execl.http_request import Http_request
# COOKIES=None
# class TestHttpRequest(unittest.TestCase):
#     def setUp(self):
#        pass
#     def __init__(self,url,param,http_method,expected,methodName):
#         self.url=url
#         self.param=param
#         self.http_method=http_method
#         self.expected=expected
#         super(TestHttpRequest,self).__init__(methodName)
#     def test_api(self):#登录
#         global COOKIES#全局变量
#         res=Http_request().http_request(self.url,self.param,self.http_method,COOKIES)
#         print('登录请求结果：',res.json())
#         if res.cookies:
#             COOKIES=res.cookies
#         self.assertEqual(self.expected,res.json()['code'])

'''断言异常处理  test_api12.html'''
# import unittest
# from lesson.class_1203_do_execl.http_request import Http_request
# COOKIES=None
# class TestHttpRequest(unittest.TestCase):
#     def setUp(self):
#        pass
#     def __init__(self,url,param,http_method,expected,methodName):
#         self.url=url
#         self.param=param
#         self.http_method=http_method
#         self.expected=expected
#         super(TestHttpRequest,self).__init__(methodName)
#     def test_api(self):#登录
#         global COOKIES#全局变量
#         res=Http_request().http_request(self.url,self.param,self.http_method,COOKIES)
#         print('登录请求结果：',res.json())
#         if res.cookies:
#             COOKIES=res.cookies
#         try:
#             self.assertEqual(self.expected,res.json()['code'])
#         except AssertionError as e:
#             print('断言出错：{}'.format(e))
#             raise e
