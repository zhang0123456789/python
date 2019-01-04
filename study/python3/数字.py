#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/10 21:24
'''Python 数字数据类型用于存储数值。
数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，
将重新分配内存空间。'''
# 以下实例在变量赋值时 Number 对象将被创建：
# var1 = 1
# var2 = 10

'''您也可以使用del语句删除一些数字对象的引用。
del语句的语法是：del var1[,var2[,var3[....,varN]]]]'''

'''我们可以使用十六进制和八进制来代表整数：'''
# number = 0xA0F # 十六进制
# print(number)
# number=0o37 # 八进制
# print(number)

'''有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
int(x) 将x转换为一个整数。
float(x) 将x转换到一个浮点数。
complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。'''


'''注意：// 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。'''
# a=7//2
# print(a)
# b=7.0//2
# print(b)
# c=7//2.0
# print(c)


'''Python 可以使用 ** 操作来进行幂运算：'''
# a=5 ** 2  # 5 的平方
# print(a)
# b=2 ** 7  # 2的7次方
# print(b)

'''pow() 方法返回 xy（x的y次方） 的值。
以下是 math 模块 pow() 方法的语法:
import math
math.pow( x, y );'''
'''内置的 pow() 方法:pow(x, y[, z])'''



'''pow() 通过内置的方法直接调用，内置方法会把参数作为整型，
而 math 模块则会把参数转换为 float。'''
#以下展示了使用 pow() 方法的实例：
# import math   # 导入 math 模块
#
# print ("math.pow(100, 2) : ", math.pow(100, 2))
# # 使用内置，查看输出结果区别
# print ("pow(100, 2) : ", pow(100, 2))
# print ("math.pow(100, -2) : ", math.pow(100, -2))
# print ("math.pow(2, 4) : ", math.pow(2, 4))
# print ("math.pow(3, 0) : ", math.pow(3, 0))

'''random() 方法返回随机生成的一个实数，它在[0,1)范围内。'''
'''以下是 random() 方法的语法:
import random
random.random()
random()是不能直接访问的，需要导入 random 模块，
然后通过 random 静态对象调用该方法'''


'''返回值     返回随机生成的一个实数，它在[0,1)范围内。'''

# import random
# # 第一个随机数
# print ("random() : ", random.random())
# # 第二个随机数
# print ("random() : ", random.random())

'''choice() 方法返回一个列表，元组或字符串的随机项。返回值:返回随机项。
以下是 choice() 方法的语法:
import random
random.choice( seq  )   seq -- 可以是一个列表，元组或字符串。
注意：choice()是不能直接访问的，需要导入 random 模块，
然后通过 random 静态对象调用该方法'''

import random
print ("从 range(100) 返回一个随机数 : ",random.choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))