#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: study_01.py 
#@time: 2018/12/26 
#@email:1402686685@qq.com
# '''python里面添加字符串注释非常简单，
# 如何将变量放入 python 的函数注释里面呢？
# docstring也就是给代码加注释的内容了，
# python可以给函数，类、方法，模块添加注释内容，
# 注释标准格式一般是三个双引号'''


# '''在函数里面添加注释内容，函数下方三个双引号里面
# 就可以写该函数的注释文档了，如果需要调用此函数的注释内容'''

# def yoyo():
#     """函数功能：打印hello world!"""
#     print("hello world!")
# a = yoyo.__doc__
# print(a)  #运行结果       函数功能：打印hello world!



# '''类、方法和模块也能添加注释内容'''


# """
# 这个是该模块的注释内容：hello.py
# """
# class Hello():
#     """hello类，实现xx功能"""
#     def world(self):
#         """world方法，打印world"""
#         print("world")
# a = __doc__  # 获取模块的docstring内容,这个是该模块的注释内容：hello.py
# print(a)
# b = Hello.__doc__   # 获取类的docstring内容,hello类，实现xx功能
# print(b)
# c = Hello.world.__doc__  # 获取方法的docstring内容,world方法，打印world
# print(c)


# '''如果函数里面带有参数，也能给参数添加注释'''
# def login(user, psw):
#     """
#     登录函数-连着输入三个双引号后回车，自动出来格式
#     :param user: 用户名，str
#     :param psw: 密码, str
#     :return: resut是登录结果， True or False
#     """
#     print(user)
#     print(psw)
#     resut = "登录结果"
#     return resut
# print(login.__doc__)#运行结果：
#     #登录函数-连着输入三个双引号后回车，自动出来格式
#     #:param user: 用户名，str
#     #:param psw: 密码, str
#     #:return: resut是登录结果， True or False