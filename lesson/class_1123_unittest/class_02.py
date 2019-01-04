#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/24 14:16
'''unittest python自带的'''
import unittest
from lesson.class_1123_unittest.sai import Sai
'''unittest四大类
TestCase：写测试用例
TestLoader：加载测试用例
TestSuite: 测试集，存放用例的地方  容器
TextTestRunner：执行用例的---包含输出报告'''


'''不以test开头，就不会执行  这里只执行5条用例'''
# class  TestKerry(unittest.TestCase):#继承TestCase  测试类
#     '''1、用例是一个一个的对象方法2、用例以test_开头3、用例里面不能传参数，除了self'''
#     def runing(self):#这是 kerry的跑步体能
#         expetecd=1000
#         actual=500
#         print('kerry期望跑{}'.format(expetecd,actual))
#         #对比结果---断言
#
#     def test_cooking(self):
#         expetecd='满汉全席'
#         actual='煮方便面'
#         print("kerry期望做{}，实际做{}".format(expetecd,actual))


# class TestSai(unittest.TestCase):#继承  #测试Sai类
#     def test_001(self):#测试俩个正数相加
#         Sai().add(5,4)
#     def test_add_two_positive(self):#测试俩个正数相加
#         Sai().add(5,6)
#
#     def test_add_two_zero(self):#测试俩个0相加
#         Sai().add(0,0)
#
#     def test_add_two_negative(self):#测试俩个负数相加
#         Sai().add(-1,-2)






'''用例以test开头   这里的用例都会执行，这里执行了6条用例'''
# class  TestKerry(unittest.TestCase):#继承TestCase  测试类
#     #1、用例是一个一个的对象方法2、用例以test_开头3、用例里面不能传参数，除了self
#     def test_run(self):#zhes ces kerry的跑步体能
#         expetecd=1000
#         actual=500
#         print('kerry期望跑:{}'.format(expetecd,actual))
#         #对比结果---断言
#
#     def test_cooking(self):
#         expetecd='满汉全席'
#         actual='煮方便面'
#         print("kerry期望做{}，实际做{}".format(expetecd,actual))


# class TestSai(unittest.TestCase):#继承  #测试Sai类
#     def test_001(self):#测试俩个正数相加
#         Sai().add(5,4)
#     def test_add_two_positive(self):#测试俩个正数相加
#         Sai().add(5,6)
#
#     def test_add_two_zero(self):#测试俩个0相加
#         Sai().add(0,0)
#
#     def test_add_two_negative(self):#测试俩个负数相加
#         Sai().add(-1,-2)



'''利用断言比对结果'''
# class  TestKerry(unittest.TestCase):#继承TestCase  测试类
#     #1、用例是一个一个的对象方法2、用例以test_开头3、用例里面不能传参数，除了self
#     def test_run(self):#zhes ces kerry的跑步体能
#         expetecd=1000
#         actual=500
#         print('kerry期望跑{}'.format(expetecd,actual))
#         #对比结果---利用断言
#         self.assertEqual(expetecd,actual)
#
#
#     def test_cooking(self):
#         expetecd='满汉全席'
#         actual='煮方便面'
#         print("kerry期望做{}，实际做{}".format(expetecd,actual))
#         # 对比结果---利用断言
#         self.assertEqual(expetecd, actual)

''' setUp  tearDown的位置无论放哪  都是在测试用例前后出现，与位置无关'''
class TestSai(unittest.TestCase):#继承  #测试Sai类
    def setUp(self): #重写，用例执行之前准备的数据或其他
        print("python12期sai测试用例")

    def test_001(self):#测试俩个正数相加
        actual=Sai().add(5,4)
        expected=9
        #利用断言比较结果
        self.assertEqual(expected,actual)

    def test_add_two_positive(self):#测试俩个正数相加
        actual=Sai().add(5,6)
        expected =11
        # 利用断言比较结果
        self.assertEqual(expected, actual)

    def test_add_two_zero(self):#测试俩个0相加
        actual=Sai().add(0,0)
        expected = 0
        # 利用断言比较结果
        self.assertEqual(expected, actual)

    def test_add_two_negative(self):#测试俩个负数相加
        actual=Sai().add(-1,-2)
        expected = -3
        # 利用断言比较结果
        self.assertEqual(expected, actual)
    def tearDown(self): #测试用例执行完毕后执行的操作
        print("我已经结束测试")


'''在setUp中传参'''
# class TestSai_1(unittest.TestCase):#继承  #测试Sai类
#     def setUp(self):
#         print("python12期sai测试用例")
#         self.a=10
#         self.b=5
#
#     def tearDown(self):
#         print("我已经结束测试")
#
#     def test_001(self):#测试俩个正数相加
#         actual=Sai().add(self.a,self.b)
#         expected=15
#         #利用断言比较结果
#         self.assertEqual(expected,actual)
#
#     def test_add_two_positive(self):#测试俩个正数相加
#         actual=Sai().add(5,6)
#         expected =11
#         # 利用断言比较结果
#         self.assertEqual(expected, actual)
#
#     def test_add_two_zero(self):#测试俩个0相加
#         actual=Sai().add(0,0)
#         expected = 0
#         # 利用断言比较结果
#         self.assertEqual(expected, actual)
#
#     def test_add_two_negative(self):#测试俩个负数相加
#         actual=Sai().add(-1,-2)
#         expected = -3
#         # 利用断言比较结果
#         self.assertEqual(expected, actual)
