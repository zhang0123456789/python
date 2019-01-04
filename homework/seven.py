#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/20 19:52


'''初始化函数，  创建对象的时候传参'''
class MyInfo:
    def __init__(self,name,height,weight,age,*args,**kwargs):#初始化函数
        self.name=name
        self.height=height                       #把属性传给对象   对象拥有类的所有方法和属性
        self.weight=weight                       #把属性传给对象   对象拥有类的所有方法和属性
        self.age=age                             #把属性传给对象   对象拥有类的所有方法和属性
        self.MyInfo=height                     #把属性传给类
        self.args=args
        self.kwargs=kwargs
    def my_height(self):       #对象方法  self就是对象本身
        print(self.name+'买的东西是：',self.kwargs)
        print(self.name+'爱好是：',self.args)
    def my_weight(self):       #对象方法 self就是对象本身
        print(self.name+"好苗条啊")
    def my_age(self):          #对象方法 self就是对象本身
        print(self.name+"年龄好小好年轻啊")


'''类外面调用对象方法---创建对象   调用对象方法'''
p1=MyInfo('蜜蜜',168,90,18,('sing','dance','hike'),a='电脑',b='手机',c='衣服')      #初始化函数，创建对象的时候记得要传参数
p1.my_height()                                     #调用对象方法
p1.my_weight()                                      #调用对象方法
p1.my_age()                                         #调用对象方法









'''对象方法调用静态方法'''
class MyInfo:
    def __init__(self,name,height,weight,age,*args,**kwargs):
        self.name=name
        self.height=height
        self.weight=weight
        self.age=age
        self.args = args
        self.kwargs=kwargs
    def my_height(self):       #对象方法
        print(self.name+"好高啊")
        print(self.name + '买的东西是：', self.kwargs)
        self.my_mes(1234567890)  #调用静态方法，此时要给静态方法的参数传入值

    @staticmethod
    def my_mes(phonenumber):       #静态方法    一般不需要用到类的属性时，可以考虑用静态方法，静态方法与普通的函数没有区别
        print("蜜蜜的手机号是：{}".format(phonenumber))

    def my_age(self):          #对象方法
        print(self.name+"年龄好小好年轻啊")

'''对象方法调用静态方法'''
p1=MyInfo('蜜蜜',168,90,18,('sing','dance','hike'),a='电脑',b='手机',c='衣服')      #初始化函数，创建对象的时候记得要传参数
p1.my_height()                                     #调用对象方法




'''对象方法调用静态方法、类方法'''
class MyInfo:
    def __init__(self,height,weight,age,hobbies):
        self.height=height
        self.weight=weight
        self.age=age
        self.hobbies=hobbies
    def my_height(self):       #对象方法
        print("蜜蜜好高啊")
        self.my_mes(1234567890)  #调用静态方法，此时要给静态方法的参数传入值
        self.my_age(18)          #调用类方法，此时要给类方法的参数传入值

    @staticmethod
    def my_mes(phonenumber):       #静态方法    一般不需要用到类的属性时，可以考虑用静态方法，静态方法与普通的函数没有区别
        print("蜜蜜的手机号是：{}".format(phonenumber))

    @classmethod
    def my_age(cls,age):          #类方法用@classmethod 装饰，cls就是类本身 即此处的MyInfo
        print("蜜蜜才{}岁，好小好年轻啊".format(age))

    def my_hobbies(self):       #对象方法
        print("蜜蜜的爱好好广泛啊")

'''类外面调用对象方法---创建对象   调用对象方法'''
p1=MyInfo(168,90,18,('sing','dance','hike'))      #初始化函数，创建对象的时候记得要传参数
p1.my_height()                                     #调用对象方法
