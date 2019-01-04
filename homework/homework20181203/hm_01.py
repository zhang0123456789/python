#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/5 7:19
'''1:根据老师上课讲解的测试用例参数化，去写单元测试用例以及用到超继承
2：把所有的测试用例数据存到Excel中，然后写一个类do_excel，完成测试数据的读取
3：利用do_excel类读取到的测试数据 传给1203课堂上讲解的test_suite，完成测试用例的加载。
4：要求：登录3条用例 充值3条用例
5：请给用例加上断言 以及异常处理，断言可以用code 也可以用msg或者是用整段信息都OK，最后要有测试报告出具'''
import  requests
class Http_request:
    def http_request(self,url,param,method,cookie=None):
        if method == 'get':
            res = requests.get(url, param, cookies=cookie)
        else:
            res = requests.post(url, param, cookies=cookie)
        return res