#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/8 19:46
'''1：一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，
询问用户的性别（m表示男性，f表示女性）
和年龄，然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。'''
def printinfo(mix,max,sex_1):
    count=0
    for i in range(1,(k+1)):
        sex=("请输入您的性别:")
        age=int("请输入您的年龄:")
        if sex==sex_1 and min<=int(age)<=max:
            print("这个人可以加入球队")
            count+=1
            print("满足条件的人数为{}人".format(count))
            return
        else:
            print("这个人不可以加入球队")

printinfo(x,y,f)

'''2：写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5'''
# def a(n):
#     if len(n)>5:
#         return True
#     else:
#         return False
#
# t=input("请输入对象：")
# print(a(t))

'''写函数，检查传入列表的长度，如果大于2，
 那么仅仅保留前两个长度的内容， 并将新内容返回'''
# def a(m):
#     if len(m)>2:
#         m_1=m[0:2]
#         return m_1
#
# p=a([11,22,33,44])
# print(p)

'''3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
如果字符串不在字典中，则添加到字典中，并返回新的字典。'''
# def add_str_to_dict(dict_1,str_1):
#     if str_1 in dict_1.values():
#         print("已存在")
#     else:
#         print("字符串不在字典中")
#         dict_1[str_1]=str_1
#         print(dict_1)
# add_str_to_dict({'age':12,'sex':'hello'},'hello')
