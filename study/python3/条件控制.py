#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/11 12:23

'''if 语句   Python中if语句的一般形式如下所示：'''

'''if condition_1:
      statement_block_1
   elif condition_2:
       statement_block_2
   else:
      statement_block_3
如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
如果 "condition_1" 为False，将判断 "condition_2"
如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
如果 "condition_2" 为False，将执行"statement_block_3"块语句
Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。'''

'''注意：
1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。'''
# var1 = 100
# if var1:
#     print("1 - if 表达式条件为 true")
#     print(var1)
#
# var2 = 0
# if var2:
#     print("2 - if 表达式条件为 true")
#     print(var2)
# print("Good bye!")  #从结果可以看到由于变量 var2 为 0，所以对应的 if 内的语句没有执行。

'''狗的年龄计算判断：'''
# age = int(input("请输入你家狗狗的年龄: "))
# print("")    #空行
# if age < 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)

# print(5 == 6)
# # 使用变量
# x = 5
# y = 8
# print(x == y)

'''该实例演示了数字猜谜游戏'''
# number = 7
# guess = -1
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")

'''if 嵌套   在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句'''

# num=int(input("输入一个数字："))
# if num%2==0:
#     if num%3==0:
#         print ("你输入的数字可以整除 2 和 3")
#     else:
#         print ("你输入的数字可以整除 2，但不能整除 3")
# else:
#     if num%3==0:
#         print ("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print  ("你输入的数字不能整除 2 和 3")