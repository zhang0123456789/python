#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/11 12:59

'''定义一个函数    你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。'''


'''语法
Python 定义函数使用 def 关键字，一般格式如下：
def 函数名（参数列表）:
    函数体'''

'''默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。'''
#让我们使用函数来输出"Hello World！"：
# def hello():
#     print("Hello World!")
# hello()


#更复杂点的应用，函数中带上参数变量:
# 计算面积函数
# def area(width, height):
#     return width * height
# def print_welcome(name):
#     print("Welcome", name)
# print_welcome("Runoob")
# w = 4
# h = 5
# print("width =", w, " height =", h, " area =", area(w, h))


'''函数调用
定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。'''
# 定义函数
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
# # 调用函数
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")


'''默认参数
调用函数时，如果没有传递参数，则会使用默认参数。'''
#以下实例中如果没有传入 age 参数，则使用默认值：
# 可写函数说明
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo(name="runoob")

'''不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。
这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]'''

'''加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。'''
# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
# # 调用printinfo 函数
# printinfo(70, 60, 50)

'''如果在函数调用时没有指定参数，它就是一个空元组。
我们也可以不向函数传递未命名的变量。'''
#如下实例：
# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)

'''还有一种就是参数带两个星号 **基本语法如下：
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]'''

#加了两个星号 ** 的参数会以字典的形式导入。
# 可写函数说明
# def printinfo(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
# # 调用printinfo 函数
# printinfo(1, a=2, b=3)

'''return语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，
以下实例演示了 return 语句的用法：'''
# 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2
#     print("函数内 : ", total)
#     return total
# # 调用sum函数
# total = sum(10, 20)
# print("函数外 : ", total)

'''global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，
就要用到global和nonlocal关键字了。'''
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)


