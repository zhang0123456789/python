#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/24 17:59
import unittest
from study.unittest.class_001 import Practice
class Practice_1(unittest.TestCase):
    def test_choice(self):
        Practice(5,5).Method()
    def test_choice_1(self):
        Practice(5,1).Method()
if __name__=='__main__':
    unittest.main()