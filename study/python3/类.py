#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/19 22:12

'''==============第一个例子==================='''
class MyClass:
    """一个简单的类实例"""
    i = 12345   #属性
    def f(self):   #对象方法
        return 'hello world'
# 实例化类
x = MyClass()
print("MyClass 类的属性 i 为：", x.i)   # 访问类的属性
print("MyClass 类的方法 f 输出为：", x.f())#访问类的方法


'''===========第二个例子=============='''
class Complex:
    def __init__(self, realpart, imagpart):   #初始化函数
        self.realpart = realpart              #给对象本身传入个参数
        self.imagpart = imagpart              #给对象本身传入个参数
x = Complex(3.0, -4.5)
print(x.realpart)   # 输出结果：3.0
print(x.imagpart)   # 输出结果：-4.5