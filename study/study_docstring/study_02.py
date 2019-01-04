#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: study_02.py 
#@time: 2018/12/26 
#@email:1402686685@qq.com

# '''可以先不在函数里面加内容，直接给函数.__doc__赋值'''
# c = "这里是变量内容"
# def hello():
#     print("hello world!")
# # 用hello.__doc__方法添加注释内容
# hello.__doc__ = """添加的注释部分，%s"""%c
# a = hello.__doc__
# print(a)#运行结果：添加的注释部分，这里是变量内容


def docstring_parameter(*sub):
    """写一个可以添加变量注释的装饰器"""
    def dec(obj):
       obj.__doc__ = obj.__doc__.format(*sub)
       return obj
    return dec
# 案例1-添加一个参数
@docstring_parameter("打印hello world")
def hello():
    """ 实现功能：{0}"""
    print("hello world!")
a = hello.__doc__
print(a)

# 案例2-添加2个参数
@docstring_parameter("打印hello", "打印world")
def world():
    """ 实现功能：{0}, {1}"""
    print("hello world!")
b = world.__doc__
print(b)#运行结果：
#实现功能：打印hello world
#实现功能：打印hello, 打印world