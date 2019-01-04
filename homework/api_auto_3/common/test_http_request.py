# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 20:12
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_http_request.py

import unittest
import time
from homework.api_auto_3.common.http_request import Http_request
from ddt import ddt,data
from homework.api_auto_3.common.read_config import ReadConfig
from homework.api_auto_3.common.do_excel import DoExcel
from homework.api_auto_3.common.my_log import MyLog
from homework.api_auto_3.common import project_path

COOKIES=None

#利用我们写的配置类 从配置文件case.conf里面的section: Case   option：button的 value
button=ReadConfig().read_config(project_path.config_path,'CASE','button')

#调用do_excel这个模块里面的DoExcel类里面的get_data方法  方法需要几个参数
#文件名   表单名   配置的值
test_data=DoExcel().get_data(project_path.case_path,'test_data',button)

#日志类 可以用它来收集日志
my_logger=MyLog()

@ddt
class TestHttpRequest(unittest.TestCase):#测试类的类名

    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self,item):#登录
        global COOKIES#声明全局变量
        my_logger.info('目前正在执行第{}条用例：{}'.format(item['case_id'],item['title']))
        my_logger.info('----------------开检查我们的URL地址-------------')
        my_logger.info('url:{}'.format(item['url']))

        my_logger.info('----------------开检查我们的param参数-------------')
        my_logger.info('param：{}'.format(item['param']))

        my_logger.info('----------------开始http请求-------------')
        res=Http_request().http_request(item['url'],eval(item['param']),item['http_method'],COOKIES)
        my_logger.info('----------------结束http请求-------------')

        my_logger.info("登录请求结果:{0}".format(res.json()))
        if res.cookies:
            COOKIES=res.cookies

        #断言
        try:
            self.assertEqual(str(item['expected']),res.json()['code'])
            TestResult='Pass'
        except AssertionError as e:
            TestResult='Failed'#本次测试结果
            my_logger.error('断言出错了：{0}'.format(e))
            raise e
        finally:
            my_logger.info('本条用例的测试结论是:{0}'.format(TestResult))
            my_logger.info('我在这里要看看TestResult的值')

