#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/24 12:55
'''超继承'''
# from lesson.class_1119_object.robot_one import RobotOne
# class RobotThree(RobotOne):
#     def walk(self):   #对象方法  self占坑 self就是对象本身  只能由对象调用
#         super(RobotThree,self).walk('1000')   #根据子类名找到父类，调用父类里面的方法  超继承的时候传参
#         print("第三代机器人：可以避开障碍物")
# RobotThree("20181121",'HUAHUA').walk()


# from lesson.class_1119_object.robot_one import RobotOne
# class RobotThree(RobotOne):
#     def walk(self,a):   #对象方法  self占坑 self就是对象本身  只能由对象调用
#         super(RobotThree,self).walk(a)   #根据子类名找到父类，调用父类里面的方法
#         print("第三代机器人：可以避开障碍物")
# RobotThree("20181121",'HUAHUA').walk(666)



'''超继承初始化函数，初始化函数重写，调用的时候根据子类的初始化参数传个参数个数'''
from lesson.class_1119_object.robot_one import RobotOne
class RobotThree(RobotOne):
    def __init__(self,birthday,name,sex):
        super(RobotThree,self).__init__(birthday,name)
        self.sex=sex

    def walk(self,a):   #对象方法  self占坑 self就是对象本身  只能由对象调用
        super(RobotThree,self).walk(a)   #根据子类名找到父类，调用父类里面的方法
        print("第三代机器人：可以避开障碍物")
RobotThree("20181121",'HUAHUA','boy').walk(666)