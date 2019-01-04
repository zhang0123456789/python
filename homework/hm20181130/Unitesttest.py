#encoding=utf-8
__author__ = 'Administrator'
'''
@Time:2018-12-2 16:37
'''
import unittest
from python12_HomeWork_1130.Requests import HttpRequests
class UnitestTest(unittest.TestCase):
    def __init__(self,url,param,http_method,methodName):
        super(UnitestTest,self).__init__(methodName)
        self.request=HttpRequests()
        self.url=url
        self.param=param
        self.http_method=http_method
    def test_login(self):
        login_res=self.request.httprequests(self.url,self.param,self.http_method)
        expected_result="登录成功"
        global cookie
        cookie=login_res.cookies
        try:
            self.assertEqual(login_res.json()["msg"],expected_result)
            print(login_res.json())
        except AssertionError as e:
            print("登录的结果是{0}".format(login_res.json()["msg"]))
            raise e
    def test_recharge(self):
        recharge_res=self.request.httprequests(self.url,self.param,self.http_method,cookie)
        expected_result="充值成功"
        try:
            self.assertEqual(recharge_res.json()["msg"],expected_result)
            print(recharge_res.json())
        except AssertionError as e:
            print("充值的结果是{0}".format(recharge_res.json()["msg"]))
            raise e