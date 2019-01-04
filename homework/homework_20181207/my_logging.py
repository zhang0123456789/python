#!/usr/bin/env python 
# encoding: utf-8
# time: 2018/12/9 9:18
# author: 蜜蜜
# file: my_logging.py
'''1：结合1207上课讲的日志知识，以及配置文件知识点编写一个属于自己的可控制的日志类，要求如下：
1）日志输出的渠道 可以通过配置文件指定输出到指定文件或者是指定渠道
2）通过配置文件 可以指定输出日志的格式 formatter
3）通过配置文件 可以指定我们日志收集器收集日志的级别 以及 输出渠道输出日志的级别
4）把这个日志类 结合我们test_http_requst这个测试类来做
print的信息用 info级别日志信息来代替
异常信息用error级别的日志信息来代替'''
import logging
from homework.homework_20181207.read_config import ReadConfig

logging_file=ReadConfig().read_config('case.conf','log','logger_name')
formatter_1=ReadConfig().read_config('case.conf','log','formatter')
handlers_option=ReadConfig().read_config('case.conf','log','console_handle')
file_handle_1=ReadConfig().read_config('case.conf','log','file_handle')
level=ReadConfig().read_config('case.conf','log','log_level')

class MyLog:
    def mylog(self,level,msg):
        my_logger=logging.getLogger(logging_file)#建立收集器
        my_logger.setLevel(level)#设置

        formatter=logging.Formatter(formatter_1)#设置输出格式

        #输出到本地文件
        fh=logging.FileHandler('python',encoding='utf-8')
        fh.setLevel(file_handle_1)
        fh.setFormatter(formatter)
        #输出到控制台
        sh=logging.StreamHandler()
        sh.setLevel(handlers_option)
        sh.setFormatter(formatter)

        #对接
        my_logger.addHandler(fh)
        my_logger.addHandler(sh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

            # 移除掉
        my_logger.removeHandler(sh)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.mylog('DEBUG', msg)

    def info(self, msg):
        self.mylog('INFO', msg)

    def warning(self, msg):
        self.mylog('WARNING', msg)

    def error(self, msg):
        self.mylog('ERROR', msg)

    def critical(self, msg):
        self.mylog('CRITICAL', msg)


if __name__ == '__main__':
    my_logger = MyLog()
    my_logger.debug('66666')
    my_logger.info('7777')
    my_logger.error('8888')
    my_logger.critical('99999')








