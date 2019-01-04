#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/27 20:02
import unittest
from homework.nine.homework_001 import Tool
class Homework(unittest.TestCase):
    def setUp(self):
        print("============开始对Tool类进行测试==================")
    def tearDown(self):
        print("@@@@已经结束测试工作@@@")
    def test_add_two_positive(self):
        actual=Tool().add(4,5)
        expected=9
        try:
            self.assertEqual(expected,actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

    def test_add_two_negative(self):
        actual=Tool().add(-1,-2)
        expected=-3
        try:
            self.assertEqual(expected, actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

    def test_sub_two_positive(self):
        actual=Tool().sub(5,4)
        expected=1
        try:
            self.assertEqual(expected, actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

    def test_sub_two_negative(self):
        actual=Tool().sub(-5,-4)
        expected=-1
        try:
            self.assertEqual(expected, actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

    def test_multi_two_positive(self):
        actual=Tool().multi(5,4)
        expected=20
        try:
            self.assertEqual(expected, actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

    def test_multi_two_negative(self):
        actual=Tool().multi(-5,-4)
        expected=20
        try:
            self.assertEqual(expected, actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

    def test_division_two_positive(self):
        actual=Tool().division(10,5)
        expected=2.0
        try:
            self.assertEqual(expected, actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

    def test_divisiong_two_negative(self):
        actual=Tool().division(-10,-5)
        expected=2.0
        try:
            self.assertEqual(expected, actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

    def test_square_integrable_function_two_positive(self):
        actual=Tool().square_integrable_function(10,5)
        expected=2500
        try:
            self.assertEqual(expected, actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

    def test_square_integrable_function_two_negative(self):
        actual=Tool().square_integrable_function(-1,-2)
        expected=4
        try:
            self.assertEqual(expected, actual)
            print('测试通过')
        except AssertionError as e:
            print("报错的是{}".format(e))

