#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/21 7:46
'''不继承初始化函数，根据父类的初始化参数个数传参'''
# from lesson.class_1119_object.robot_one import RobotOne
# '''继承'''
# class RobotTwo(RobotOne):  #RobotOne是RobotTwo的父类
#     def jump(self):   #拓展  只有子类里面有的函数叫拓展
#         print("遇到障碍物，可以双脚蹦跳，蹦过障碍物")
#     def walk(self):   #子类跟父类函数重名的叫重写  跟函数的内容以及参数无关
#         print("会直线行走6666666")
# r1=RobotTwo('20111121','幸福')
# r1.jump()
# r1.sing('七里香')
# r1.walk()


'''继承初始化函数，初始化函数重写，调用的时候根据子类的初始化参数传个参数个数'''
# from lesson.class_1119_object.robot_one import RobotOne
# '''继承'''
# class RobotTwo(RobotOne):  #RobotOne是RobotTwo的父类
#     def __init__(self,name,birthday,sex):
#         self.name=name
#         self.birthday=birthday
#         self.sex=sex
#     def jump(self):   #拓展  只有子类里面有的函数叫拓展
#         print("遇到障碍物，可以双脚蹦跳，蹦过障碍物")
#     def walk(self):   #子类跟父类函数重名的叫重写  跟函数的内容以及参数无关
#         print("会直线行走6666666")
# r1=RobotTwo('幸福','20111121','boy')
# r1.jump()
# r1.sing('你还好吗')
# r1.walk()


from lesson.class_1119_object.robot_one import RobotOne
'''继承'''
class RobotTwo(RobotOne):  #RobotOne是RobotTwo的父类

    def jump(self):   #拓展  只有子类里面有的函数叫拓展
        print("遇到障碍物，可以双脚蹦跳，蹦过障碍物")
    def walk(self):   #子类跟父类函数重名的叫重写  跟函数的内容以及参数无关
        print("会直线行走6666666")
r1=RobotTwo(20181208,'boy')
r1.jump()
r1.talk('高一同学 今天真是棒棒滴')
r1.sing('七里香')
r1.walk()
