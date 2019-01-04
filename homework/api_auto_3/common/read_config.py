# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 20:33
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : read_config.py

#配置文件相关的知识
#.ini .properties .conf 等等 都是配置文件
# section  片段[片段名]  option 选项
#存在配置文件里面的数据 读取出来后 全部是字符串类型

#怎么读取呢？？
import configparser
#
# cf=configparser.ConfigParser()#创建对象  可以读取配置文件信息的对象
#
# cf.read('case.conf',encoding='utf-8')#open  当你的配置文件里面有中文的时候 记得加encoding='utf-8'
#
# print(cf.sections())
# print(cf.options('Teacher'))
# #section和option的组合 可以帮我们确定一个想要的值
# print(cf.get('Student','name'))
# print(type(cf.get('Student','score')))
# print(type(cf.get('Student','age')))
# print(type(cf.get('Student','height')))
# print(cf['Student']['height'])

#写成一个类
class ReadConfig:

    @staticmethod
    def read_config(file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        value=cf.get(section,option)
        return value

if __name__ == '__main__':
    from homework.api_auto_3 import project_path
    value=ReadConfig().read_config(project_path.config_path,'LOGS','formatter')
    print(value)