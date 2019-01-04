#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/21 7:29
'''新功能：双肩蹦   绕开障碍物'''
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
