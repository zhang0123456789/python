#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2018/12/15 0015 上午 11:29
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : readcfg.py
'''读取配置文件'''
import configparser
import os

# cur_path=os.path.dirname(os.path.realpath(__file__))
# cfg_path=os.path.join(cur_path,'cfg.ini')
# print(cfg_path)#cfg.ini的路径
# conf=configparser.ConfigParser()#创建管理对象
# conf.read(cfg_path,encoding='utf-8')#读取ini文件
# sections=conf.sections()#获取所有的section
# print(sections)
# item=conf.items('email_163')
# print(item)



'''remove'''
# import configparser
# import os
# cur_path=os.path.dirname(os.path.realpath(__file__))
# cfg_path=os.path.join(cur_path,'cfg.ini')
# print(cfg_path)
# conf=configparser.ConfigParser()#创建管理对象
# conf.remove_option('email_163','port')
#
# item=conf.items('email_163')
# print(item)  #list里面的对象都是元组
#
#
# # 删除一个 section
# conf.remove_section('email_163')
# sects = conf.sections()
# print(sects)  # list里面对象是元祖



'''set修改ini文件'''
# curpath = os.path.dirname(os.path.realpath(__file__))
# cfgpath = os.path.join(curpath, "cfg.ini")
#
# conf = configparser.ConfigParser()# 创建管理对象
# conf.read(cfgpath, encoding="utf-8")# 先读出来
#
# conf.set("email_163", "port", "蜜蜜")  # # 修改section里面的值
# conf.write(open(cfgpath, "r+", encoding="utf-8"))  # r+模式
