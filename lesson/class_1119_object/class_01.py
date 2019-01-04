#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/20 21:14
'''对象==实例'''

'''写一个机器人  类  具有的属性 制造年月   名字'''
'''第一代机器人 简单的交流  直线行走遇到障碍物  就会报警  停止行走'''
'''听歌名到音乐库里面找音乐  黑你播放'''


'''对象方法'''
# class Robotone:
#     #属性
#     birthday='20181119'
#     name='小麦'
#
#     def talk(self):  #对象方法
#         print("可以跟你简单的交流'")
#     def walk(self):
#         print("会直线行走")
#     def sing(self):
#         print("会播放音乐")

'''类外边调用对象方法--创建对象  调用对象方法
创建对象  类名()
对象可以调用类里面的所有方法和属性，可以随时调用'''

# r1=Robotone()
# r1.sing()
# r1.talk()
# r1.walk()
# print(r1.name) #调用属性，应该用print
#
#
# print("========这是分割线==========")
# r2=Robotone()
# r2.sing()
# print(r2.birthday)  #调用属性


'''类方法'''
# class Robotone:
#     #属性
#     birthday='20181119'
#     name='小麦'
#
#     def talk(self):  #对象方法,需要self占坑，self就是对象本身
#         '''可以跟你简单的交流'''
#         print("可以跟你简单的交流'")
#
#     @classmethod
#     def walk(cls):#类方法，装饰@classmethod  cls占坑  cls就是累本身
#         print("会直线行走")
#
#     def sing(self):
#         print("会播放音乐")
#
# '''类外边调用类方法   1、对象调用   2、类.(函数名)直接调用'''
# r3=Robotone()
# r3.walk()
#
# print("==================这是分割线==================")
# Robotone.walk()

'''静态方法    当你的方法里面不需要用到类的属性时，写成静态方法'''
# class Robotone:
#     #属性
#     birthday='20181119'
#     name='小麦'
#
#     def talk(self):  #对象方法,需要self占坑，self就是对象本身
#         '''可以跟你简单的交流'''
#         print("可以跟你简单的交流'")
#
#     @classmethod
#     def walk(cls):#类方法，装饰@classmethod  cls占坑  cls就是类本身
#         print("会直线行走")
#
#     @staticmethod
#     def sing():#静态方法  装饰@staticmethod装饰  跟普通函数一模一样
#         print("会播放音乐")

'''类外面调用静态方法    1、对象调用   2、类.(函数名)直接调用'''
# r4=Robotone()
# r4.sing()
# print("=======这是分割线===========")
# Robotone.sing()
# print(Robotone.birthday) #类调用属性   类和对象都可以调用属性
# print(Robotone.name)   #类调用属性     类和对象都可以调用属性


'''=========================类和对象都可以对属性调用========================'''
# class Robotone:
#     #属性
#     birthday='20181119'
#     name='小麦'
#
#     def talk(self):  #对象方法,需要self占坑，self就是对象本身
#         '''可以跟你简单的交流'''
#         print(self.name+"可以跟你简单的交流")
#         print(Robotone.name+"可以跟你简单的交流")
#
#     @classmethod
#     def walk(cls):#类方法，装饰@classmethod  cls占坑  cls就是累本身
#         print("会直线行走")
#
#     @staticmethod
#     def sing():#静态方法  装饰@staticmethod装饰  跟普通函数一模一样
#         print("会播放音乐")
#
#     @staticmethod
#     def math_method(a,b):
#         print(a+b)
# '''类和对象都可以对属性调用'''
# r5=Robotone()
# r5.talk()


'''=====================初始化函数    初始化和普通函数一样  但没有return========================'''
# class Robotone:
#     def __init__(self,birthday,name):#初始化函数  创建对象的时候去传值
#         self.birthday=birthday    #把属性传给对象
#         self.name=name             #把属性传给对象
#         Robotone.birthday=birthday #把属性传给类
#         Robotone.name=name          #把属性传给类  #对象可以调用类里面所有属性和方法
#
#     def talk(self):  #对象方法,需要self占坑，self就是对象本身
#         '''可以跟你简单的交流'''
#         print(self.name+"可以跟你简单的交流")
#         print(Robotone.name+"可以跟你简单的交流")
#
#     @classmethod
#     def walk(cls):#类方法，装饰@classmethod  cls占坑  cls就是累本身
#         print("会直线行走")
#
#     @staticmethod
#     def sing():#静态方法  装饰@staticmethod装饰  跟普通函数一模一样
#         print("会播放音乐")
#
#     @staticmethod
#     def math_method(a,b):
#         print(a+b)
# r1=Robotone(20181119,'小麦')
# r1.talk()

'''传入动态参数  关键字参数'''
# class Robotone:
#     def __init__(self,birthday,name,*args,**kwargs):#初始化函数  创建对象的时候去传值
#         self.birthday=birthday    #把属性传给对象
#         self.name=name             #把属性传给对象
#         self.hobby=args
#         self.kwargs=kwargs
#         Robotone.birthday=birthday #把属性传给类
#         Robotone.name=name          #把属性传给类
#
#     def talk(self,content):  #对象方法,需要self占坑，self就是对象本身
#         '''可以跟你简单的交流'''
#         print(self.name+"可以跟你简单的交流"+content)
#         print(Robotone.name+"可以跟你简单的交流")
#         print(self.name,'业余爱好是：',self.hobby)
#         print(self.name, '业余爱好是：', self.kwargs)
#     @classmethod
#     def walk(cls):#类方法，装饰@classmethod  cls占坑  cls就是类本身
#         print("会直线行走")
#
#     @staticmethod
#     def sing(music='听妈妈的话'):#静态方法  装饰@staticmethod装饰  跟普通函数一模一样
#         print("会播放音乐："+music)
#
#     @staticmethod
#     def math_method(a,b):
#         print(a+b)
# r1=Robotone('20181119','33','羽毛球','爬山',x='a',y='b')
# r1.talk('英语')
# Robotone.sing()


class Robotone:
    '''机器人   类    具有题目里面的所有属性和行为'''
    def __init__(self,birthday,name):#初始化函数  创建对象的时候去传值
        self.birthday=birthday    #把属性传给对象
        self.name=name             #把属性传给对象


    def talk(self,content):  #对象方法,需要self占坑，self就是对象本身
        '''可以跟你简单的交流'''
        print(self.name+"可以跟你简单的交流，说指定的内容"+content)


    def walk(self):
        print("会直线行走")

    @staticmethod
    def sing(music='听妈妈的话'):#静态方法  装饰@staticmethod装饰  跟普通函数一模一样
        print("会播放音乐："+music)
t1=Robotone(20181208,'mimi')
t1.sing()
