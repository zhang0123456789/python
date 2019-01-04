#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/11/24 13:54

'''语法  def(self)  def(cls)@classmethod   def()@staticmethod
对象可以调用类里面的任意方法
类名只能调用类方法以及静态方法'''

'''单元测试  ：unittest接口测试     pytest自动化测试  叫法不同而已
pytest更好用是第三方安装              unittest是基础，是python自带的'''

'''单元测试谁做？-----开发
单元测试是干嘛？------对单个模块进行的测试  知道没有问题为止'''

'''为什么学习单元测试？
1、对自己的代码进行测试
2、利用单元测试完成功能模块的测试---数据驱动测试
3、测试的时候，一般怎么测试-----测试的内容是类
4、测试手段：调用里面的方法
5、调用方法---数据驱动测试---不同的场景需要不同的数据
6、测试用例---完成这个模块的测试'''


'''TestCase:一个testcase的十六就是一个测试用例
TsetSuite：多个测试用例合在一起
TestLoader:是用来加载TestCase到TestSuite中
TextTestRunner:是用来执行测试用例的，其中的run(study)会执行TestSuite/TestCase中的run(result)方法
TextTestResult:保存TextTestRunner执行的测试结果
fxture：测试用例环境的搭建和销毁。测试前环境的准备和搭建setUp、 执行测试的代码run.
以及测试后环境的还原（tearDown）'''