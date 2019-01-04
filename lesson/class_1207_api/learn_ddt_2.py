#!/usr/bin/env python 
# encoding: utf-8
# time: 2018/12/8 20:28
# author: 蜜蜜
# file: learn_ddt_2.py

'''不带*      加载出来的是一条测试用例'''
# import unittest
# from ddt import ddt,data
#
# test_data=(1,2)
#
# @ddt#装饰测试类
# class TestMath(unittest.TestCase):
#
#     @data(test_data)#装饰测试方法
#     def test_001(self,item):#item只是一个变量名
#         print('item',item)

'''带*     加载出来的是俩条测试用例'''
# import unittest
# from ddt import ddt,data,unpack
#
#
# test_data=(1,2)
#
# @ddt#装饰测试类
# class TestMath(unittest.TestCase):
#     @data(*test_data)#装饰测试方法
#     def test_001(self,item):#item只是一个变量名
#         print('item',item)
#         print('-'*100)

'''不带*     加载出来的是一条测试用例'''
# import unittest
# from ddt import ddt,data,unpack
# test_data=((1,2),(3,4))
# @ddt#装饰测试类
# class TestMath(unittest.TestCase):
#     @data(test_data)#装饰测试方法
#     def test_001(self,item):#item只是一个变量名
#         print('item',item)
#         print('-'*100)


'''带*     加载出来的是俩条测试用例'''
# import unittest
# from ddt import ddt,data,unpack
# test_data=((1,2),(3,4))
# @ddt#装饰测试类
# class TestMath(unittest.TestCase):
#     @data(*test_data)#装饰测试方法
#     def test_001(self,item):#item只是一个变量名
#         print('item',item)
#         print('-'*100)

'''带*    用了Unpack,对data拆分出来的数据，再次进行拆分，
要用等量的接收，不然会报错， 加载出来的是俩条测试用例'''
# import unittest
# from ddt import ddt,data,unpack
# test_data=((1,2),(3,4))
# @ddt#装饰测试类
# class TestMath(unittest.TestCase):
#     @data(*test_data)#装饰测试方法
#     @unpack
#     def test_001(self,a,b):#item只是一个变量名
#         print('item-a',a)
#         print('item-b',b)
#         print('-'*100)

'''带*    用了Unpack,对data拆分出来的数据，再次进行拆分，
要用等量的接收，不然会报错， 加载出来的是俩条测试用例'''
# import unittest
# from ddt import ddt,data,unpack
# test_data=((1,(2,6)),(3,(4,9)))
# @ddt       #装饰测试类
# class TestMath(unittest.TestCase):
#     @data(*test_data)#装饰测试方法
#     @unpack
#     def test_001(self,a,b):#item只是一个变量名
#         print('item-a',a)
#         print('item-b',b)
#         print('-'*10)

'''test_data是字典'''
# import unittest
# from ddt import ddt,data,unpack
# test_data=[{'a':1,'b':18},{'a':6,'b':12}]
# @ddt       #装饰测试类
# class TestMath(unittest.TestCase):
#     @data(*test_data)#装饰测试方法
#     def test_001(self,item):#item只是一个变量名
#         print('item',item)
#         print('-'*20)

'''字典值相加'''
# import unittest
# from ddt import ddt,data,unpack
# test_data=[{'a':1,'b':18},{'a':6,'b':12}]
# @ddt       #装饰测试类
# class TestMath(unittest.TestCase):
#     @data(*test_data)#装饰测试方法
#     def test_001(self,item):#item只是一个变量名
#         print('item',item)
#         print('a+b={}'.format(item['a']+item['b']))
#         print('-'*20)


'''拆分的对象是字典，那么用来接收数据的变量名必须要和Key值一致，  以下代码报错'''
# import unittest
# from ddt import ddt,data,unpack
# test_data=[{'x':1,'y':18},{'x':6,'y':12}]
# @ddt
# class TestMath(unittest.TestCase):
#     @data(*test_data)
#     @unpack
#     def test_002(self,a,b):
#         print('item-a', a)
#         print('item-b', b)
#         print('a+b={}'.format(a+b))
#         print('-'*20)

import unittest
from ddt import ddt,data,unpack
test_data=[{'x':1,'y':18},{'x':6,'y':12}]
@ddt
class TestMath(unittest.TestCase):
    @data(*test_data)
    @unpack
    def test_002(self,x,y):
        print('item-a:', x)
        print('item-b:', y)
        print('a+b={}'.format(x+y))
        print('-' * 20)

