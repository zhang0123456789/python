#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/6 20:27
'''ddt  data drive  study   数据驱动测试'''
'''1、结合我们的单元测试区执行用例'''
'''2、装饰器'''
'''3、安装pip install ddt'''
# def print_msg(*args):#动态参数
#     print(args) #*args  到了函数内部，就会变成一个元组
#     print('参数的个数：',len(args))
# print_msg(1,2,3,4,5,'hello')   #函数调用  打印出一个元组(1,2,3,4,5,'hello')


# def print_msg(*args):#动态参数
#     print(args)
#     print('参数的个数：', len(args))
# a=(1,2,3,4,5,'hello')
# print_msg(a)  #打印一个元组


# def print_msg(*args):#动态参数
#     print(args)
#     print('参数的个数：', len(args))
# a=(1,2,3,4,5,'hello')
# print_msg(*a)  #*理解为脱外套  返回6个参数

# def print_msg(*args):#动态参数
#     print(args)
#     print('参数的个数：', len(args))
# a=[1,2,3,4,5,'hello']
# print_msg(*a)  #*理解为脱外套  返回6个参数

# def print_msg(*args):#动态参数
#     print(args)
#     print('参数的个数：', len(args))
# a=[[1,2,3,4],[5,'hello']]
# print_msg(*a)  #*理解为脱外套  返回2个参数

'''不带*   执行一条用例'''
# import unittest
# from ddt import ddt,data
# test_data=(1,2,3)#元组
# @ddt
# class TestMath(unittest.TestCase):
#     @data(test_data)
#     def test_001(self,item):
#         print('--------我是用例001————-')
#         print('----------item——-——--:',item)

'''带*   执行三条用例'''
import unittest
# from ddt import ddt,data
# test_data=(1,2,3)#元组
# @ddt
# class TestMath(unittest.TestCase):
#     @data(*test_data)
#     def test_001(self,item):
#         print('--------我是用例001————-')
#         print('----------item——-——--:',item)
#         print()

'''带*   执行俩条用例'''
# import unittest
# from ddt import ddt,data
# test_data=(1,2,3),(5,6,7)#元组
# @ddt
# class TestMath(unittest.TestCase):
#     @data(*test_data)
#     def test_001(self,item):
#         print('--------我是用例001————-')
#         print('----------item——-——--:',item)
#         print()

'''不带*  执行一条用例       '''
# import unittest
# from ddt import ddt,data
# test_data=(1,2,3),(5,6,7)#元组
# @ddt
# class TestMath(unittest.TestCase):
#     @data(test_data)
#     def test_001(self,item):
#         print('--------我是用例001————-')
#         print('----------item——-——--:',item)
#         print()


'''不带*  执行一条用例       '''
# import unittest
# from ddt import ddt,data
# test_data=[(1,2,3),(5,6,7)]#元组
# @ddt
# class TestMath(unittest.TestCase):
#     @data(test_data)
#     def test_001(self,item):
#         print('--------我是用例001————-')
#         print('----------item——-——--:',item)
#         print()

# '''带*  执行俩条用例'''
# import unittest
# from ddt import ddt,data
# test_data=[(1,2,3),(5,6,7)]#元组
# @ddt
# class TestMath(unittest.TestCase):
#     @data(*test_data)
#     def test_001(self,item):
#         print('--------我是用例001————-')
#         print('----------item——-——--:',item)
#         print()

'''带*  执行俩条用例'''
# import unittest
# from ddt import ddt,data
# test_data=[[1,2,3],[5,6,7]]#元组
# @ddt
# class TestMath(unittest.TestCase):
#     @data(*test_data)
#     def test_001(self,item):
#         print('--------我是用例001————-')
#         print('----------item——-——--:',item)
#         print()


# import unittest
# from ddt import ddt,data
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
# @ddt
# class TestMath(unittest.TestCase):
#     @data(*test_data)
#     def test_001(self,item):
#         print('--------param————-'.format(item['param']))
#         print('--------url————-'.format(item['param']))
#         print('--------http_method————-'.format(item['param']))
#         print('--------expected————-'.format(item['param']))
#         print('-----------我是分隔符---------------')
#         print()


# import unittest
# from ddt import ddt,data
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
# @ddt
# class TestMath(unittest.TestCase):
#     @data(*test_data)
#     def test_001(self,item):
#         print('param:',item['param'])
#         print('url:',item['url'])
#         print('http_method:',item['http_method'])
#         print('expected',item['expected'])
#         print('-----------我是分隔符---------------')
#         print()


'''折叠'''
import unittest
from ddt import ddt,data,unpack
test_data=[ {'param':{'mobilephone': 18688773467, 'pwd': '123456'},'http_method':'get',
             'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'10001'},

            {'param':{'mobilephone': 18688773467, 'pwd': '12345678'},'http_method':'post',
             'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'20111'},

            {'param':{'mobilephone': 11868877346347, 'pwd': '123456'},'http_method':'get',
             'url' :'http://47.107.168.87:8080/futureloan/mvc/api/member/login','expected':'20112'},

            {'param':{'mobilephone': 18688773467, 'amount': '1000'},'http_method':'post',
             'url' : 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','expected':'10001'}]

@ddt
class TestMath(unittest.TestCase):
    @data(*test_data)
    @unpack

    def test_001(self,param,url,http_method,expected):
        print('param:',param)
        print('url',url)
        print('http_method',http_method)
        print('expected',expected)
        print('-----------我是分隔符---------------')
        print()
