#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/6 7:19
'''配置文件相关知识'''
'''ini,properties,conf结尾的  都是配置文件
section：片段   option：选项
存在配置文件里面的数据都是字符串类型'''

'''怎么读取'''
import configparser  #读取配置文件
# cf=configparser.ConfigParser()#创建对象，可以读取配置文件信息的对象
# cf.read('case.conf',encoding='utf-8')  #类型于Open函数  配置文件有中文的时候，要加编码encoding=utf-8
# print(cf.sections())  #读取section
# print(cf.options('Teacher'))#读取option

'''section 和option的组合，可以帮我们确定一个想要的值'''

'''存在配置文件里面的数据都是字符串类型'''
# print(cf.get('Student','name'))
# print(type(cf.get('Student','name')))
# print(cf.get('Student','score'))
# print(type(cf.get('Student','score')))
#
#
# print(cf.get('Student','height'))
# print(cf['Student']['height'])
# print(type(cf.get('Student','height')))

'''写成一个类'''
class ReadConfig:
    def read_config(self,file_name,section,option):
        cf = configparser.ConfigParser()
        cf.read('case.conf',encoding='utf-8')
        value=cf.get(section,option)
        return value
if __name__ == '__main__':
    value=ReadConfig().read_config('case.conf','Teacher','hobby')
    print(value)

