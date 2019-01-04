#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/1 8:26
'''unittest核心'''
'''unittest最核心的四个概念是：study case ,study suite,study runner,study fixture '''
'''TestCase:一个testcase的实例就是一个测试用例'''
'''Testsuite:多个测试用例合在一起'''
'''Testloader:是用来加载TestCase到TestSuite'''
'''TextTestRunner:是用来执行测试用例的，其中的run(study)会执行TestSuite/TestCase中的run(result)'''
'''TextTestResult:保存TextTestRunner执行的测试结果'''
'''fixture:测试用例环境的搭建和销毁，测试前准备环境的搭建（setUp）,执行代码（run)
以及测试后环境的还原（tearDown）'''
