#!/usr/bin/env python 
# encoding: utf-8
# time: 2018/12/11 6:43
# author: 蜜蜜
# file: class_02.py
#语法 怎么取定义一个函数 参数的类型/参数的位置 return


'''函数的调用'''
# def print_msg(content):
#     print("我想说：{}".format(content))
# def learn_language(name):
#     print("我正在学{}语言".format(name))
#     print_msg("很难")  #函数的调用
# learn_language("pyhton")

# def print_msg(content):
#     print("我想说：{}".format(content))
# def learn_language(name,content):
#     print("我正在学{}语言".format(name))
#     print_msg(content)
# learn_language("pyhton",'so easy')


# def print_msg(content):
#     print("我想说：{}".format(content))
#     learn_language("java")
#
# def learn_language(name):
#     print("我正在学{}语言".format(name))
# print_msg("好容易")

#局部变量  全局变量
#作用域
# a=5   #a在函数外，全部变量  在该模块里面生效
# def add(b):
#     '''加法'''
#     a=6  #a在函数里面 称为就不变量 他只能作用域函数内部
#     print(a+b)
# def sub(b):
#     '''减法'''
#     print(a-b)
# add(10)  #打印16
# sub(5)   #打印0
# print(a)  #打印5
'''1、当全局变量与局部变量相同时，函数内部优先使用自己的局部变量
2、如果函数内部，没有这个变量，就会使用全局变量
3、如果在函数内部声明了全局变量，那么我们可以在函数内部改变全局变量  全局生效'''

# a=5   #a在函数外，全部变量  在该模块里面生效
# def add(b):
#     '''加法'''
#     global a  #globals()声明是全局变量，我可以在函数内部改变他的值
#     a=6  #a在函数里面 称为就不变量 他只能作用域函数内部
#     print(a+b)
# def sub(b):
#     '''减法'''
#     print(a-b)
# add(10)  #打印16
# sub(5)   #打印1
# print(a)  #打印6

# a=5   #a在函数外，全部变量  在该模块里面生效
# def add(b):
#     '''加法'''
#     global a  #globals()声明是全局变量，我可以在函数内部改变他的值
#                #a在函数里面 称为就不变量 他只能作用域函数内部
#     a=a+b
# def sub(b):
#     '''减法'''
#     print(a-b)
# add(10)  #没有打印
# sub(5)   #打印10
# print(a)  #打印15
