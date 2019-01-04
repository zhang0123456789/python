#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/7 21:22
'''1：一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。'''
# sum=0
# for i in range(1,11):
#     sex=input("请问你的性别：")
#     age=int(input("请问你的年龄："))
#     if sex=='f'and 10<=age<=12:
#         print("恭喜你可以加入足球队")
#         sum+=1
#     else:
#         print("很遗憾，你不可以加入球队")
# print("满足条件的人数：{}".format(sum))

# count=1
# sum=0
# while 1:
#     sex=input("请问你的性别：")
#     age=int(input("请问你的年龄："))
#     if sex=='f'and 10<=age<=12:
#         print("恭喜你可以加入足球队")
#         sum+=1
#     else:
#         print("很遗憾，你不可以加入球队")
#     count+=1
#     if count>10:
#         break
# print("满足条件的人数：{}".format(sum))

# sum=0
# count=0
# while count<10:
#     sex = input("请问你的性别：")
#     age=int(input("请问你的年龄："))
#     if sex=='f'and 10<=age<=12:
#          print("恭喜你可以加入足球队")
#          sum+=1
#     else:
#         print("很遗憾，你不可以加入球队")
#     count+=1
# print("满足条件的人数：{}".format(sum))

'''3： 万科笔试题：
有一组用户的登录信息存储在字典 login_ifno 里面，字典格式如下：
login_info={"admin":"root","user_1":"123456"}
key表示用户名，value表示密码，请编写函数满足如下条件：
1）设计1个登陆的程序， 不同的用户名和对成密码存在个字典里面， 输入正确的用户名和密码去登陆，
2）首先输入用户名，如果用户名不存在或者为空，则一直提示输入正 确的用户名
3)当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应， 则提示密码错误请重新输入。
4)如果密码输入错误超过三次，中断程序运行。
5)当输入密码错误时，提示还有几次机会
6)用户名和密码都输入正确的时候，提示登陆成功!'''

# login_info={"admin":"root","user_1":"123456"}
# while True:
#     name=input("请输入你的用户名：")
#     if name not in  login_info.keys():
#         print("请输入正确的用户名!")
#     else:#用户名正确  继续输入密码
#         count=0
#         while True:
#             pwd=input("请输入密码：")
#             if pwd ==login_info[name]:
#                 print("登录成功")
#                 break
#             else:
#                 count+=1
#                 print("密码错误，还剩{}次机会".format((3-count)))
#                 if count==3:
#                     break
#
#         break




#函数 ：可以实现某个功能的一段代码

'''append  pop insert len range print input str list replace strip find split内置函数'''
# s='Python12期的A组精灵同学 表现非常不错'
# print(len(s))

# sum_1=0
# for i in range(1,101):
#     sum_1+=i
# print("1-100求和是{}：".format(sum_1))

#语法：你必须要记的东西
#关键字  def  define定义
'''def 函数名(参数1、参数2、参数3):
    #代码块
    :return 遍历的个数'''
#1、参数列表  可以有0个参数、可以有多个参数  参数还分为位置参数 默认参数、动态参数  关键字参数
#2、return变量的个数  变量的个数可以是0个 也可以是多个
#3、return的作用 ：当你调用函数的时候，返回一个结果给函数  函数终止


#问候1次
# def greet_user():
#     print("niko同学晚上好呀！")
#     return
# greet_user()

#问候50次  0个参数
# def greet_user():
#     for i in range(1,51):
#         print("niko同学晚上好呀！")
#     return
# greet_user()

#问候50次  0个参数
# def greet_user():
#     print("niko同学晚上好呀！")
#     return
#
# for i in range(1,51):
#     greet_user()


#问候50次  0个参数
# def greet_user():
#     print("niko同学晚上好呀！")
#     return
#
# for i in range(1,51):
#     greet_user()

'''必须要传1个参数'''
# def greet_user(name):#形参、位置参数
#     print("niko同学晚上好呀！")
#     return
# greet_user(1)

'''实现多个人问候'''
# def greet_user(name):
#     print("{}同学晚上好呀！！!!".format(name))
#     return
# greet_user('sunny')
# greet_user('篮子')
# greet_user('hester')

'''传多个参数，'''
# def greet_user(name,content):
#     print("{}同学{}呀！！!!".format(name,content))
#     return
# greet_user('sunny','你好棒')
# greet_user('篮子',"上课很活跃哟")
# greet_user('hester','暂时没有看到你跳出来说话')

# def greet_user(name,content='在柠檬班学习还习惯吗'):
#     print("{}同学{}呀！！!!".format(name,content))
#     return
# greet_user('sunny','你好棒')
# greet_user('篮子',"上课很活跃哟")
# greet_user('hester','暂时没有看到你跳出来说话')
# greet_user("菜鸟")  #取默认值，默认值必须放在位置参数后面

# def greet_user(name='雄姐',content='在柠檬班学习还习惯吗'):
#     print("{}同学{}呀！！!!".format(name,content))
#     return
# greet_user('sunny','你好棒')
# greet_user('篮子',"上课很活跃哟")
# greet_user('hester','暂时没有看到你跳出来说话')
# greet_user("菜鸟")  #取默认值，默认值必须放在位置参数后面
# greet_user()

'''参数  按顺序赋值
#  如果不想按顺序赋值，可以指定关键字  但是关键字与参数保持一致'''
# def greet_user(name='雄姐',content='在柠檬班学习还习惯吗'):
#     print("{}同学{}呀！！!!".format(name,content))
#     return
# greet_user(content='sunny',name='你好棒')
# greet_user('篮子',"上课很活跃哟")
# greet_user('hester','暂时没有看到你跳出来说话')
# greet_user("菜鸟")  #取默认值，默认值必须放在位置参数后面
# greet_user()

# def greet_user(name='雄姐',content='在柠檬班学习还习惯吗'):
#     print("{}同学{}呀！！!!".format(name,content))
#     return 7
# t=greet_user()
# print("greet_user返回的值是：{}".format(t))
#
# def greet_user(name='雄姐',content='在柠檬班学习还习惯吗'):
#     print("{}同学{}呀！！!!".format(name,content))
#     return 7,8
# t=greet_user()
# print("greet_user返回的值是：{}".format(t))

''''''
# def greet_user(name='雄姐',content='在柠檬班学习还习惯吗'):
#     print("{}同学{}呀！！!!".format(name,content))
#     return
# t=greet_user()
# print("greet_user返回的值是：{}".format(t))
#
# def greet_user(name='雄姐',content='在柠檬班学习还习惯吗'):
#     print("{}同学{}呀！！!!".format(name,content))
#     return 5
# t=greet_user()
# print("greet_user返回的值是：{}".format(t))


#写一个函数 计算1-100的和 要求返回最后的结果
# def add():
#     sum=0
#     for i in range(1,101):
#         sum+=i
#     print("1-100的和:{}".format(sum))
#     return sum
# add()


# def add():
#     sum=0
#     for i in range(1,101):
#         sum+=i
#     print("1-100的和:{}".format(sum))
#     return sum
#
# t=add()
# print("1-100的和：{}".format(t))

# def add(a,b):
#     sum=0
#     for i in range(a,b):
#         sum+=i
#     print("1-100的和:{}".format(sum))
#     return sum
# add(1,101)

# def add(a,b): #参数化的过程  怎么样才能提高函数服用性
#     sum=0
#     for i in range(a,b):
#         sum+=i
#     print("1-100的和:{}".format(sum))
#     return  sum
# t=add(1,101)
# print("1-100能返回的值：{}".format(t))

'''疑问：什么时候用return返回结果？？
#当你要利用返回结果时 ，要用return'''

# def add(a,b): #参数化的过程  怎么样才能提高函数服用性
#     sum=0
#     for i in range(a,b):
#         sum+=i
#     print("1-100的和:{}".format(sum))
#     return sum
# t=add(1,101)+100
# print("1-100能返回的值：{}".format(t))


#怎么写一个函数
#先用代码写功能 甚至可以用一组数据替代进去  写代码
#def 函数名  变函数
#想办法提高复用性

#动态参数 关键参数
# s=[1,3,4]
# s.pop() #会删除最后一个元素 然后返回这个被删除的值
# print(s)  #返回[1,3]

# s=[1,3,4]
# print(s.pop()) #打印被删除的值  返回4

# s='hello'
# s.replace('h','@')
# print(s)  #打印hello

# s='hello'
# new_s=s.replace('h','@')
# print(new_s)  #打印@ello

#动态参数=不定长参数=不定个数===你想输多少个就多少个
#动态参数 *变量名  args=arguments
# def coding(*a):
#     '''这是一个现实所用编程语言的函数'''
#     print(a)
# coding()

# def coding(*a):
#     '''这是一个现实所用编程语言的函数'''
#     print(a)  #不定长参数变成了元组
# coding('python','java','shell')

# def coding(*args):
#     '''这是一个现实所用编程语言的函数'''
#     print(args)  #不定长参数变成了元组
#     return   #在函数里面
# coding('python','java','shell','ruby','go')

# def coding(*args):
#     '''这是一个现实所用编程语言的函数'''
#     print(args)  #不定长参数变成了元组
#     return args
# t=coding('python','java','shell','ruby','go')
# print(t)

'''关键字参数  **kwargs key word arguments
**a  可以接受任意多个   键值对'''
# def student_info(**a):
#     print(a)
# student_info(name='ss',age='18',id='python12')


#混合使用 要注意顺序
# def print_msg(a,b=10,*args):
#     print('a',a)
#     print("b",b)
#     print("args",args)
'''默认值参数必须放在位置参数后面'''
# print_msg(1,2,3,4,5,6)

#强制b=10
'''遵守这个规则   位置、默认、动态、 关键字
# #默认值参数必须放在位置参数后面'''
# def print_msg(a,*args,b=10):
#     print('a',a)
#     print("b",b)
#     print("args",args)
# print_msg(1,2,3,4,5,6)

# def print_msg(*args,a,b=10):
#     print('a',a)
#     print("b",b)
#     print("args",args)
# #默认值参数必须放在位置参数后面
# print_msg(2,3,4,5,6,a=1)

#遵守这个规则   位置、动态、默认、 关键字
# def print_msg(a,*args,b=10,**kwargs):
#     print('a',a)
#     print("b",b)
#     print("args",args)
#     print("kwargs", kwargs)
# #默认值参数必须放在位置参数后面
# print_msg(1,2,3,4,5,6,)

'''默认参数必须放在位置参数后面'''
# def add (a,b=4,c=5,*args,**kwargs):
#     print('a+b+c的结果是：',a+b+c)
#     sum=0
#     for item in args:
#         sum+=item
#         print('动态参数的累加结果是：',sum)
#         print('关键字动态参数是：',kwargs)
#
# '''调用函数'''
# add(1,2,3,4,5,6,x=1,y=2)


def add(a,b=3,c=5):
    result=a+b+c
    return  result
res=add(1,2,3)
print(res)