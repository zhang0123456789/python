# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 21:22
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_logging.py

import logging
from homework.api_auto_3.common import project_path
from homework.api_auto_3.common.read_config import ReadConfig
#写成一个可配置的日志类
class MyLog:

    def my_log(self,level,msg):
        my_logger=logging.getLogger(ReadConfig.read_config(project_path.config_path,'LOGS','logger_name'))#getLogger 创建一个日志收集器
        my_logger.setLevel(ReadConfig.read_config(project_path.config_path,'LOGS','log_level'))#设置级别

        #指定输出格式：
        formatter = logging.Formatter(ReadConfig.read_config(project_path.config_path,'LOGS','formatter'))

        #指定自己的渠道
        ch=logging.StreamHandler()#输出到控制台
        ch.setLevel(ReadConfig.read_config(project_path.config_path,'LOGS','console_handle'))#设置好自己输出渠道的级别
        ch.setFormatter(formatter)#规定日志输出的时候 按照指定的formatter格式

        #本地文件
        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')#日志有中文 要设置一个编码
        fh.setLevel(ReadConfig.read_config(project_path.config_path,'LOGS','file_handle'))
        fh.setFormatter(formatter)

        #对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)

        #移除掉
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log('DEBUG',msg)

    def info(self,msg):
        self.my_log('INFO',msg)

    def warning(self,msg):
        self.my_log('WARNING',msg)

    def error(self,msg):
        self.my_log('ERROR',msg)

    def critical(self,msg):
        self.my_log('CRITICAL',msg)

if __name__ == '__main__':
    my_logger=MyLog()
    my_logger.debug('66666')
    my_logger.info('yuxuan')
    my_logger.error('gaoyi')
    my_logger.critical('yuexiaqignfeng')