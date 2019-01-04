#!/usr/bin/env python 
# encoding: utf-8
# time: 2018/12/8 22:49
# author: 蜜蜜
# file: learn_logging.py
'''日志  ：定义  作业    log  记录代码执行的过程'''
'''一旦记录下来  就可以跟进日志去定位排查问题'''
'''日志的级别  debug  info  waring error critical'''
'''为何不用print'''


'''默认收集输出warning以及以上的信息 
 root logger是习题自定义的收集日志的收集器'''
#handles 输出渠道  默认是console控制台'''


# import logging
# logging.debug('JiangM同学，你这个是一个debug信息')
# logging.info('蛋蛋菌同学，你这个是一个info信息')
# logging.warning('33同学，你这个是一个warning信息')
# logging.error('David zhang同学，你这个是一个error信息')
# logging.critical('路人甲同学，你这个是一个critical信息')



# import logging
# qq_logger=logging.getLogger('qianqian')#getlogger 创建一个日志收集器
# qq_logger.setLevel('DEBUG')#设置级别
#
# #指定自己的渠道
# ch=logging.StreamHandler()#输出到控制台
# ch.setLevel('DEBUG')#设置好自己输出渠道的级别
# #对接
# qq_logger.addHandler(ch)
#
# qq_logger.debug('JiangM同学，你这个是一个debug信息')
# qq_logger.info('蛋蛋菌同学，你这个是一个info信息')
# qq_logger.warning('33同学，你这个是一个warning信息')
# qq_logger.error('David zhang同学，你这个是一个error信息')
# qq_logger.critical('路人甲同学，你这个是一个critical信息')#控制输出5条信息

# '''收集器和渠道取交集'''
# import logging
# qq_logger=logging.getLogger('qianqian')#getlogger 创建一个日志收集器
# qq_logger.setLevel('INFO')#设置级别
#
# #指定自己的渠道
# ch=logging.StreamHandler()#输出到控制台
# ch.setLevel('DEBUG')#设置好自己输出渠道的级别
# #对接
# qq_logger.addHandler(ch)
#
# qq_logger.debug('JiangM同学，你这个是一个debug信息')
# qq_logger.info('蛋蛋菌同学，你这个是一个info信息')
# qq_logger.warning('33同学，你这个是一个warning信息')
# qq_logger.error('David zhang同学，你这个是一个error信息')
# qq_logger.critical('路人甲同学，你这个是一个critical信息')#控制台输出4条信息



'''收集器和渠道取交集'''
import logging
qq_logger=logging.getLogger('qianqian')#getlogger 创建一个日志收集器
qq_logger.setLevel('DEBUG')#设置级别

#指定输出格式
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')

#指定自己的渠道
ch=logging.StreamHandler()#输出到控制台
ch.setLevel('ERROR')#设置好自己输出渠道的级别
ch.setFormatter(formatter)#规定日志输出的时候，按照指定的formatter格式
#本地文件
fh=logging.FileHandler('python12.txt',encoding='UTF-8')
fh.setLevel('ERROR')
fh.setFormatter(formatter)

#对接
qq_logger.addHandler(ch)
qq_logger.addHandler(fh)


qq_logger.debug('JiangM同学，你这个是一个debug信息')
qq_logger.info('蛋蛋菌同学，你这个是一个info信息')
qq_logger.warning('33同学，你这个是一个warning信息')
qq_logger.error('David zhang同学，你这个是一个error信息')
qq_logger.critical('路人甲同学，你这个是一个critical信息')#输出2条信息