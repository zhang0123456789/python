#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/2 23:07
#1、input是从控制台获取一个数据 但是这个数据都是字符串类型的
# data=input("请你输入一个数据:")
# print(data)
# print("类型：",type(data))

# 作业讲解   从控制台输入格式如：20181031   获取年月日
# date=input("请你输入一个日期，格式如：20181031")
# print("{}年{}月{}日".format(date[0:4],date[4:6],date[6:]))

'''字典 无序  dict  ditcionary
#1、空字典 d={}
#2、z字典里面的值 key:value的形式存在 键值对
#3、value 可以是任意类型  key是不可变的 就不支持列表、字典——因为列表、字典都是可变的
#4、支持数字、字符串、元组、浮点数、因为他们的类型都是不可变的
#5、一般我们的key都字符串90%
#6、不同的键值对之间用逗号隔开
#7、可变的 支持增删改查'''
# d={"class_id":"pyrhon12","age":18,"num":104,"grade":[99,98,100,4,66],"cousre":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d)

'''查询  根据key查询  字典.[key]'''
 #查询键值
# d={"class_id":"python12","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d['course'])       #查询course{'en': 100, 'ch': 120, 'math': 99}

#查询值
# d={"class_id":"pyrhon12","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d['course']['math'])    #查询course里面的math

#查询值
# d={"class_id":"pyrhon12","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d['grade'][2])            #查询grade里面的100


'''key必须是唯一的  不重复的，重复了会将前面相同的key覆盖掉'''
# d={"class_id":"pyrhon12","class_id":"pyrhon777","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d)

'''查询所有的key  字典名.keys()'''
# d={"class_id":"pyrhon12","class_id":"pyrhon777","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d.keys())   #获取所有的ksy   dict_keys(['class_id', 'age', 'num', 'grade', 'course', (1, 2)])

'''查询所有的value  字典名.value()'''
# d={"class_id":"pyrhon12","class_id":"pyrhon777","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d.values())  #获取所有的value  dict_values(['pyrhon777', 18, 104, [99, 98, 100, 4, 66], {'en': 100, 'ch': 120, 'math': 99}, 9])

'''查询所有的键值对  字典名.item()'''
# d={"class_id":"pyrhon12","class_id":"pyrhon777","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d.items())   #获取所有的键值对  dict_items([('class_id', 'pyrhon777'), ('age', 18), ('num', 104), ('grade', [99, 98, 100, 4, 66]), ('course', {'en': 100, 'ch': 120, 'math': 99}), ((1, 2), 9)])

'''删除  字典名.pop()'''
# d={"class_id":"pyrhon12","class_id":"pyrhon777","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# d.pop('course')
# print (d)             #删除course  打印出{'class_id': 'pyrhon777', 'age': 18, 'num': 104, 'grade': [99, 98, 100, 4, 66], (1, 2): 9}

# d={"class_id":"pyrhon12","class_id":"pyrhon777","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d.pop('course'))     #删除course  涉及函数返回值  直接打印被删除的内容 {'en': 100, 'ch': 120, 'math': 99}


'''随机删除  d.popitem()'''
# d={"class_id":"pyrhon12","class_id":"pyrhon777","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# d.popitem()
# print(d)     #随机删除 打印的结果{'class_id': 'pyrhon777', 'age': 18, 'num': 104, 'grade': [99, 98, 100, 4, 66], 'course': {'en': 100, 'ch': 120, 'math': 99}}

# d={"class_id":"pyrhon12","class_id":"pyrhon777","age":18,"num":104,"grade":[99,98,100,4,66],"course":{"en":100,"ch":120,"math":99},(1,2):9}
# print(d.popitem())

'''修改和新增  都是 字典名.[key]=value'''
d={"class_id":"python777","sex":'boy',"num":104}
d['class_id']='python888'
d['age']=18
print(d)

# t=(1,3,'sunflower')
# print(1 not in t)


# t=(1,3,'sunflower')
# print('s' in t)
# print('s'in t[2])


# L=[1,0.02,[4,5]]
# print([4,5] in L )

# d={"name":'gxq','age':22}
# print('gxq' in d.values())  #查找value

# d={"name":'gxq','age':22}
# print('name'in d)  #根据Key取找值
# print('age'in d.keys())    #根据Key取找值
# print('age'in d)   #默认是查找key值

'''控制语句：条件语句  循环语句
#条件语句：根据不同的条件对不同的情况作出不同的处理
#if   条件表达式  ：  条件表达式的值都是布尔值
#if  后面的表达式我True  才会执行if下面的子代码
# 基础的 必须掌握的python的特点：要换行要缩进用TAB键'''

#比较运算符
# score=80
# if score>=80:   #看到冒号:要换行要缩进
#     print("考试及格")

#成员运算符
# s='ks/share'
# if 'k'in s:
#     print("k在字符串s里面")

# #逻辑运算符
# a=10
# b=20
# if a>0 and b>0:
#     print("a和b都是正数")

'''所有为0的数据，放在if后面  就会判断为false'''
# a=0
# if a:
#     print('666666666')

'''所有为空的数据，放在if后面  就会判断为false'''
# a=[]
# if a:
#     print('666666666')
#
# a={}
# if a:
#     print('666666666')
#
# a=()
# if a:
#     print('666666666')

'''所有为非空的数据，放在if后面  就会判断为True'''
# a={"a":10}
# if a:
#     print('666666666')

# grade=60
# if grade>=80:
#     print("比较满意，学习的不错")
# else:        #else后面是不能加任何值，在一个语句里面只能有一个else
#     print("算了！破罐子破摔跟不上")

# grade=int(input("请你最近输入对之间的打分（0-100分）："))
# if 80>grade>=60:
#     print("比较满意，学习的不错")
# elif grade >=80:   #else if   可以有多个elif  elif后面必须要有条件表达式
#     print("非常优秀")
# else:
#     print("算了！破罐子破摔跟不上")


# total=float(input("请输入弄的购买总金额:"))
# if 50<=total<=100:
#     print("你可以享受的折扣是10%")
#     print("你需要付款{}元，优惠{}元，最后需要支付{}元".format(total,total*0.1,total-total*0.1))
# elif total>100:
#     print("你可以享受的折扣是20%")
#     print("你需要付款{}元，优惠{}元，最后需要支付{}元".format(total,total*0.2,total-total*0.2))
# else:
#     print("不好意思，你不可以享受折扣")
#     print("你需要付款{}元，优惠{}元，最后需要支付{}元".format(total,0,total))



