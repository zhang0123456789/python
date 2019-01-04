#!/usr/bin/env python 
# encoding: utf-8
# time: 2018/12/11 6:43
# author: 蜜蜜
# file: class_01.py
'''笨人三步走
1、先用代码写出来
2、加def
3、想办法提升复用性'''
'''1：一个足球队在寻找年龄在x岁到y岁的小女孩（
包括x岁和y岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。'''
# def football_team(x,y,k):
#     count=0
#     for i in range(k):
#         sex=input("请输入你的性别：")
#         age=int(input("请输入你的年龄："))
#         if x<=age<=y and sex=='f':
#             print("恭喜你，可以加入球队")
#             count+=1
#         else:
#             print("很遗憾，你不能参加我们的球队")
#     print("满足条件的总人数是{}".format(count))
# football_team(10,12,10)

'''2：写函数，判断用户传入的对象（字符串、列表、元组）
长度是否大于5'''
# def jude(a):
#     if len(a)>5:
#         print(True)
#     else:
#         print(False)
# jude([1,2,3,4,5,6])
'''3、写函数，检查传入列表的长度，如果大于2，
那么仅仅保留前两个长度的内容，并将新内容返回 '''

# def check_list(L):
#     if len(L)>2:
#         new_L=L[0:2]
#         print(new_L)
#         return
# check_list([1,2,3])

'''3、定义一个函数，传入一个字典和字符串，
判断字符串是否为字典中的值，如果字符串不在字典中，
则添加到字典中，并返回新的字典。'''
# def jude_dict(d,s):
#     if s not in d.values():
#         if s not in d.keys():
#             d[s]=s
#         else:
#             d[s+"_1"]=s
#     return d
# res=jude_dict({"name":"rui"},"name")
# print(res)